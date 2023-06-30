import ssl
import smtplib
from email.message import EmailMessage

email_sender = "dusach2018@gmail.com"
email_password = "siheqnayysqtlwcj"
email_receiver = email_sender
student_info = {
        'Timestamp': '30/06/2023 10:02:14',
        'name': 'Md. Shahadat Hossain Shakil',
        'collegeName': 'Dhaka Udyan Government College',
        'schoolName': 'Chatkhil P.G. Government High School',
        'sscGroup': 'Science',
        'hscGroup': 'Science',
        'sscResult': '4.78',
        'mobileNumber': '01735632883',
        'email': 'shahadat13456shakil@gmail.com',
        'expect': 'Guideline',
        'question': 'No',
        'hscYear': 'HSC 2023'
    }
def mail(email_receiver, student_info, sit_number):
    # Customize the confirmation message using the student information
    registration_confirmation = f"""
Dear {student_info['name']},

Thank you for registering for the Dhaka University Admission Test Guideline Program! We are excited to have you join us in this program designed to help students like you in their pursuit of higher education and admission to public universities.

Event Details:
Date: 3rd July, 2023
Time: 10:00 AM
Venue: Chatkhil Upazilla Parishad Auditorium, Chatkhil, Noakhali
Sit Number : {sit_number}

During the program, you will have the opportunity to gain a deep understanding of the admission test structure, learn effective study techniques, access recommended resources, get expert tips from DU students, and participate in an interactive Q&A session. By attending this program, you will equip yourself with the necessary tools and knowledge to prepare for the Dhaka University admission tests with confidence.

We admire your dedication and commitment to your education, {student_info['name']}. Your participation in this program demonstrates your strong desire to succeed and secure admission to the program of your choice. We are confident that with the guidance and resources provided in this program, you will enhance your chances of success and achieve your academic goals.

Please find below the details of your registration:
- Name: {student_info['name']}
- College Name: {student_info['collegeName']}
- School Name: {student_info['schoolName']}
- SSC Group: {student_info['sscGroup']}
- HSC Group: {student_info['hscGroup']}
- SSC Result: {student_info['sscResult']}
- Mobile Number: {student_info['mobileNumber']}
- Email: {student_info['email']}
- Expectation from the Program:" {student_info['expect']}"
- Question: "{student_info['question']}"
- HSC Year: {student_info['hscYear']}

If you have any further questions or require additional information, please don't hesitate to contact us. We look forward to seeing you at the event!

Best regards,
Dhaka University Students Association of Chatkhil
    """


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = "Registration Confirmation: Dhaka University Admission Test Guideline Program"
    em.set_content(registration_confirmation)

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls(context=context)
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
if __name__ == "__main__":
    mail(email_receiver, student_info)