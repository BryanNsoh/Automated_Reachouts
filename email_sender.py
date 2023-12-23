from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from markdown2 import markdown
import json

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

    def send_email(self, markdown_data):
        for item in markdown_data:
            if item.get("Sent", 0) == 0:
                Contact = item.get("Contact")
                markdown_content = self._extract_markdown_content(item)
                html_content = markdown(markdown_content)

                sender = {"email": "info@mamboanye.com"}
                to = [{"email": Contact}]
                subject = "Your Email Subject"
                send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
                    to=to, html_content=html_content, sender=sender, subject=subject
                )

                try:
                    api_response = self.api_instance.send_transac_email(send_smtp_email)
                    print("Email sent successfully: ", api_response)
                    item["Sent"] = 1  # Update 'Sent' status on success
                except ApiException as e:
                    print(
                        "Exception when calling SMTPApi->send_transac_email: %s\n" % e
                    )

    def _extract_markdown_content(self, data_item):
        markdown_content = ""
        # extract markdown content from data_item dictionary with key "Email_To_Send"
        markdown_content = data_item.get("Email_To_Send", None)
        return markdown_content


if __name__ == "__main__":
    brevo_email_sender = BrevoEmailSender(BREVO_API_KEY)

    markdown_data = [
        # Sample data structure
        {
            "Contact": "bnsoh2@huskers.unl.edu",
            "Email_To_Send": """# Sample Markdown

            ## Introduction
            This is a *sample* markdown document to illustrate various markdown features.

            ### Features

            1. **Headers**: Used for structuring content.
            2. **Lists**: Can be ordered (numbered) or unordered (bullets).

            ## Formatting

            - *Italics* are great for emphasis.
            - **Bold** makes your point clear.
            - `Code` format is used for inline code.

            ## Links and Images

            - Visit [OpenAI](https://www.openai.com) for more information.
            - Display images using `![alt text](image_url)` syntax.

            ## Code Blocks

            ```python
            # Python code example
            def hello_world():
                print("Hello, world!")
            """,
            "Result_1": "Content 1",
            "Sent": 0,
        },
        # Add more items as needed...
    ]

    brevo_email_sender.send_email(markdown_data)

    # Print updated markdown_data to check 'Sent' status
    print("Updated Data: ", markdown_data)
