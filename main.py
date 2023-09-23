import requests
import smtplib
import paramiko
import os


email = os.environ.get('email')
pwd = os.environ.get('pwd')


try:
    response = requests.get('http://68.183.84.39:8080/')
    if response.status_code == 200:
        print("Website is up")
    else:
        print("Website is down")

        subject = "SITE DOWN"
        body = "The website is down."

        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email, pwd)
            smtp.sendmail(email, email, message)
            print("Email sent: SITE DOWN")
except Exception as ex:
    print(f"connection error happened: {ex}")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email, pwd)
        message1='server not running'
        smtp.sendmail(email, email, message1)
        print("Email sent")

        # Define your DigitalOcean droplet SSH details
        hostname = '68.183.84.39'
        port = 22  # Default SSH port
        username = 'root'
        private_key_path = '/Users/tusharsharma/.ssh/id_rsa'

        # Initialize an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Load your private key
            private_key = paramiko.RSAKey(filename=private_key_path)

            # Connect to the droplet using SSH key authentication
            ssh_client.connect(hostname, port, username, pkey=private_key)

            # Execute a command (e.g., "ls" to list files)
            command = "docker run  -d -p 8080:80 nginx"
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # Read and print the command output
            output = stdout.read().decode()
            print(f"Command Output:\n{output}")

        except paramiko.AuthenticationException:
            print("Authentication failed. Check your SSH key or configuration.")
        except paramiko.SSHException as e:
            print(f"SSH error occurred: {str(e)}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
        finally:
            # Close the SSH connection
            ssh_client.close()

