from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from markdown2 import markdown


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
                email = item.get("Email")
                markdown_content = self._extract_markdown_content(item)
                html_content = markdown(markdown_content)

                sender = {"email": "mamboanye6@gmail.com"}
                to = [{"email": email}]
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
        for i in range(1, 6):
            search_key = f"Search_{i}"
            result_key = f"Result_{i}"
            if search_key in data_item and result_key in data_item:
                markdown_content += (
                    f"### {data_item[search_key]}\n{data_item[result_key]}\n\n"
                )
        return markdown_content


if __name__ == "__main__":
    brevo_email_sender = BrevoEmailSender("YOUR_BREVO_API_KEY")

    markdown_data = [
        # Sample data structure
        {
            "Email": "example@example.com",
            "Search_1": "Topic 1",
            "Result_1": "Content 1",
            "Sent": 0,
        },
        # Add more items as needed...
    ]

    brevo_email_sender.send_email(markdown_data)

    # Print updated markdown_data to check 'Sent' status
    print("Updated Data: ", markdown_data)
