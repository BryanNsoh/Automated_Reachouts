from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import json
import base64

# Read API keys
key_path = r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"
with open(key_path) as f:
    api_keys = json.load(f)
    BREVO_API_KEY = api_keys["BREVO_API_KEY"]


class BrevoEmailSender:
    def __init__(self, api_key):
        configuration = sib_api_v3_sdk.Configuration()
        configuration.api_key["api-key"] = api_key
        self.api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
            sib_api_v3_sdk.ApiClient(configuration)
        )

    def send_email(self, html_data):
        for item in html_data:
            if item.get("Sent", 0) == 0:
                contact = item.get("Contact")
                html_content = item.get("Email_To_Send", "")
                subject = item.get("Subject", "")
                sender = {"email": "mamboanye6@gmail.com"}
                to = [{"email": contact}]
                attachments = []

                # Check for attachment
                if "Attachment_Path" in item:
                    with open(item["Attachment_Path"], "rb") as file:
                        encoded_string = base64.b64encode(file.read()).decode("utf-8")
                        attachments.append(
                            {
                                "content": encoded_string,
                                "name": "Mambo-Mary-Resume.pdf",
                            }
                        )

                send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                    to=to,
                    html_content=html_content,
                    sender=sender,
                    subject=subject,
                    attachment=attachments,
                )

                try:
                    api_response = self.api_instance.send_transac_email(send_smtp_email)
                    print("Email sent successfully: ", api_response)
                    item["Sent"] = 1  # Update 'Sent' status on success
                except ApiException as e:
                    print(
                        "Exception when calling SMTPApi->send_transac_email: %s\n" % e
                    )


if __name__ == "__main__":
    brevo_email_sender = BrevoEmailSender(BREVO_API_KEY)

    html_email = [
        # Sample data structure
        {
            "Contact": "bryan.anye.5@gmail.com",
            "Email_To_Send": """
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
                <p>Dear Professor XXXX,</p>

                <p>My name is Raman Dutt, a graduate of XXXX University <a href="http://www.example.com">insert URL</a>. <strong>I am currently working</strong> as a research associate at HITI Lab <a href="http://www.example.com">insert URL</a> at Emory University with Professor A <a href="http://www.example.com">insert URL</a> and Professor B <a href="http://www.example.com">insert URL</a>. <strong>My research includes applications of deep learning for medical image analysis, with a special focus on domain adaptation and transfer learning</strong> . I have read your <strong>intriguing work</strong> on medical image analysis (such as <a href="http://www.example.com">URL</a> and <a href="http://www.example.com">URL</a>) and <strong>I am highly motivated to pursue</strong> an MS/ PhD in Artificial Intelligence. Here are a few questions -</p>
                
                <ul>
                    <li>Are you looking for new graduate students for Fall'21?</li>
                    <li>Which department should I apply to be able to best work in your lab?</li>
                    <li>What qualities/ skills do you prefer in a student?</li>
                </ul>

                <p><strong>I've attached my resume</strong> to give you more information about my background.</p>

                <p>Thank you for your consideration!</p>

                <p>Sincerely,<br>Raman Dutt <a href="http://www.example.com">URL to personal website/ Google scholar/ Github/ etc</a></p>
            </body>
            </html>

            """,
            "Subject": "Inquiry: Leveraging AI for Medical Imaging Breakthroughs - Fall 2023",
            "Sent": 0,
            "Attachment_Path": r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\Coding Projects\Automated_Reachouts\Mambo_resume.pdf",
        }
    ]

    brevo_email_sender.send_email(html_email)

    # Print updated html_smail to check 'Sent' status
    print("Updated Data: ", html_email)
