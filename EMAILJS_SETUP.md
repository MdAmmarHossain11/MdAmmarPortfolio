# EmailJS Setup Guide

I've switched your contact form to use **EmailJS**, which is much more reliable for receiving emails. Follow these steps to get it working:

## Step 1: Sign Up on EmailJS
1. Go to https://www.emailjs.com/
2. Click "Sign Up" (top right)
3. Sign up with Google, GitHub, or email
4. Verify your email if needed

## Step 2: Add Your Email Service
1. In the EmailJS dashboard, go to **Email Services** (left sidebar)
2. Click **"Add Service"**
3. Select **Gmail** (or your email provider)
4. Click **"Connect Account"** and authorize EmailJS to access your Gmail
5. Name it something like "Gmail Service"
6. Copy the **Service ID** (looks like: `service_xxxxx`)

## Step 3: Create an Email Template
1. Go to **Email Templates** (left sidebar)
2. Click **"Create New Template"**
3. Use this template:

**Template Name:** `contact_form`

**Template Content:**
```
Subject: {{subject}}

From: {{from_name}} ({{from_email}})
To: {{to_email}}

Message:
{{message}}
```

4. Click **"Save"**
5. Copy the **Template ID** (looks like: `template_xxxxx`)

## Step 4: Get Your Public Key
1. Go to **Account** (left sidebar)
2. Click **"API Keys"** tab
3. Copy your **Public Key** (looks like: `xyz123abcdef...`)

## Step 5: Update Your Portfolio Files
Replace the placeholder values in both files:

**In `index.html` and `contact.html`**, find this line:
```javascript
emailjs.init("YOUR_PUBLIC_KEY");
```
Replace `YOUR_PUBLIC_KEY` with your actual Public Key from EmailJS

Also find:
```javascript
const response = await emailjs.send("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", {
```
Replace:
- `YOUR_SERVICE_ID` with your Service ID
- `YOUR_TEMPLATE_ID` with `contact_form`

## Example (Your values will look different):
```javascript
emailjs.init("k8fj2k3jf923jf923");

const response = await emailjs.send("service_abc123", "contact_form", {
```

## Step 6: Test It!
1. Go to your portfolio website
2. Fill out the contact form and send a test message
3. Check your email inbox (mdammar10696@gmail.com)

✅ **That's it!** Your emails should now come through reliably.

## Troubleshooting
- If you don't receive emails, check your **Spam/Junk folder**
- Make sure Gmail is properly authorized in EmailJS
- Double-check that you copied the IDs correctly
- Check the browser console (F12) for any error messages

## Free Tier Limits
- EmailJS free tier allows **200 emails per month** - plenty for a portfolio!
- Upgrade to Premium if you need more

---

**Need help?** Visit EmailJS docs: https://www.emailjs.com/docs/
