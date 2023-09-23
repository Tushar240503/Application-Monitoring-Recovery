# Application-Monitoring-Recovery
An automated script in Python for monitoring a web application. Notifying about the status and recovering the application if not accessible.
Project Description:

The Automated Website Monitoring and Recovery System is a Python script designed to continuously monitor the availability of a specified website and take automated actions in case of downtime. This project combines web monitoring, email notifications, and server recovery using SSH to ensure the seamless operation of a web service hosted on a remote server.

Features:

Website Availability Monitoring:

The script sends HTTP requests to a specified website (http://68.183.84.39:8080/) at regular intervals to check its availability.
If the website responds with a status code of 200, it is considered "up," and a notification is logged.
If the website is down (any other status code), an email notification is triggered to alert the administrator.
Email Notifications:

The script uses SMTP to send email notifications in case of website downtime.
It utilizes the provided email address and password (from environment variables) to send notifications.
Two types of email notifications are sent:
"SITE DOWN" notification when the website is unreachable.
"Server not running" notification in case of a connection error.
Server Recovery:

If the website is down, the script attempts to recover the server automatically.
It establishes an SSH connection to a DigitalOcean droplet using SSH key authentication.
The SSH connection is configured to handle missing host keys automatically.
The script then executes a Docker command to restart the web server (NGINX in this case) on the remote server.
The command and its output are logged for reference.
Exception Handling:

The script provides robust exception handling to manage potential errors.
It logs authentication errors, SSH errors, and general exceptions with descriptive error messages.
Requirements:

Python 3.x
Required Python packages: requests, smtplib, paramiko
A DigitalOcean droplet for server hosting
SSH private key for authentication
Usage:

Set up environment variables for your email address (email) and password (pwd) to enable email notifications.
Ensure that your SSH private key path and other SSH configuration details are correctly specified.
Run the script, which will continuously monitor the website and take actions as necessary.
This project provides an automated solution for monitoring and managing the availability of a web service, reducing downtime and ensuring a reliable user experience. It can be further extended and customized for specific web services and server configurations.
