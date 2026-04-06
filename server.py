#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class EmailHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the content length
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            # Parse form data
            data = json.loads(body)
            
            name = data.get('name', '').strip()
            from_email = data.get('from_email', '').strip()
            subject = data.get('subject', '').strip()
            message = data.get('message', '').strip()
            
            # Validate
            if not all([name, from_email, subject, message]):
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Missing required fields'}).encode())
                return
            
            # Send email
            try:
                # Gmail setup (you can use your own email service)
                sender_email = "mdammar10696@gmail.com"
                sender_password = "ftqx ofcj qcgs znll"  # Use App Password if 2FA enabled
                receiver_email = "mdammar10696@gmail.com"
                
                # Create message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = f"Portfolio Contact: {subject}"
                
                body = f"""
New message from your portfolio contact form:

Name: {name}
Email: {from_email}
Subject: {subject}

Message:
{message}

---
Reply to: {from_email}
"""
                msg.attach(MIMEText(body, 'plain'))
                
                # Send email via Gmail
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                server.quit()
                
                # Success response
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success'}).encode())
                print(f"✅ Email sent from {name} ({from_email})")
                
            except Exception as e:
                print(f"❌ Email send error: {e}")
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        
        except Exception as e:
            print(f"❌ Server error: {e}")
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def log_message(self, format, *args):
        """Suppress default logging"""
        pass

if __name__ == '__main__':
    PORT = 8001
    handler = EmailHandler
    server = HTTPServer(('localhost', PORT), handler)
    print(f"📧 Email server running at http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    server.serve_forever()
