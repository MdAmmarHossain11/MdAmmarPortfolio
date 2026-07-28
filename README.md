# Md. Ammar Hossain Portfolio

A modern personal portfolio website for Md. Ammar Hossain, built with plain HTML, Tailwind CSS, Font Awesome, and a lightweight Python server for handling contact form submissions.

## Overview
This portfolio showcases:
- A professional landing page and introduction
- About me section with education, experience, and achievements
- Projects section highlighting key technical work
- Skills section covering programming and development capabilities
- Contact page with contact details and a working contact form
- A dedicated CV page for visitors to request a copy or preview

## Project Structure
- index.html — Home page with hero section and introduction
- about.html — Personal background, experience, achievements, and education
- projects.html — Featured projects and project details
- skills.html — Technical and professional skill highlights
- contact.html — Contact information and message form
- cv.html — CV page with request-based download/preview actions
- server.py — Python server for processing contact form submissions
- assets/ — CV download assets

## Features
- Responsive layout for desktop and mobile
- Light/dark theme toggle
- Smooth navigation between portfolio pages
- Professional styling using Tailwind CSS
- Contact form integration with email sending support
- CV page with message-based request actions

## How to View the Portfolio
You can open the website directly by launching the HTML files in a browser. A simple local preview option is:

```bash
python -m http.server 8000
```

Then visit:

```text
http://localhost:8000/
```

## Contact Form Setup
The contact form is supported by the Python server in server.py. To use it locally:

```bash
python server.py
```

Then open the contact page and submit a message. If needed, update the SMTP credentials in server.py for your own email provider.

## Customization
- Update profile content directly inside the HTML pages
- Replace the CV files in the assets folder with your real PDF/DOCX files
- Adjust colors and visual styling through the Tailwind configuration in the HTML files

## Contact
For inquiries, collaboration, or CV requests, use the contact page or reach out through the listed social and contact details.
