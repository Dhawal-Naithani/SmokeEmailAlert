import serial
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

arduino_port = 'COM5'
baud_rate = 9600

sender_email = 'abc@gmail.com'
receiver_email = 'xyz@gmail.com'
email_password = ''
smtp_server = 'smtp.gmail.com'
smtp_port = 587

def send_email(message):
    print("\nSending Email Alert.\n")
    subject = 'Smoke Detected!'
    body = message

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, email_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def main():
    try:
        arduino = serial.Serial(arduino_port, baud_rate, timeout=2)

        while True:
            data = arduino.readline().decode('utf').strip()
            if data:
                smoke_value = int(data)

                if smoke_value == 0:
                    message = f"ALERT!!!\n\nSmoke detected!\nSensor value: {smoke_value}"
                    print(message)
                    send_email(message)
    except serial.SerialException as e:
        print(f"Error: {e}")
    finally:
        if arduino.is_open:
            arduino.close()

main()