from typing import Dict
import google.generativeai as genai
from prompts import student_email_advice, professor_email_advice
import json


class EmailCrafter:
    """
    Crafts an email based on the search results and student preferences.
    """

    def __init__(self, google_api_key: str):
        self.google_api_key = google_api_key

    def generate_email(self, prompt: str) -> str:
        # Configure the Google Gemini Pro model
        genai.configure(api_key=self.google_api_key)
        self.model = genai.GenerativeModel("gemini-pro")

        # Generating the email using the Gemini Pro model
        return self.model.generate_content(prompt)

    def craft_email(
        self, student_info: Dict, professor_info: Dict, sample_emails: Dict
    ) -> str:
        # Prompt 1: Student generates the initial email draft
        prompt_1 = (
            f"Write an email as a student reaching out to a professor. \n"
            f"Student Information: {json.dumps(student_info)}\n"
            f"Professor Information: {professor_info.get('Employee', 'N/A')}, {professor_info.get('Position', 'N/A')}, {professor_info.get('Department', 'N/A')}\n"
            f"Search Results: {professor_info.get('Result_1', 'N/A')}, {professor_info.get('Result_2', 'N/A')}, {professor_info.get('Result_3', 'N/A')}, {professor_info.get('Result_4', 'N/A')}, {professor_info.get('Result_5', 'N/A')}\n"
            f"Sample Emails for Guidance: {json.dumps(sample_emails)}\n"
            f"Email (formatted in markdown):\n"
        )

        initial_draft = self.generate_email(prompt_1)
        print("Initial draft:", initial_draft.text)

        # Prompt 2: Professor reviews the draft and provides feedback
        prompt_2 = f"{professor_email_advice} \n\n{initial_draft.text}\n"
        professor_feedback = self.generate_email(prompt_2)
        print("Professor feedback:", professor_feedback.text)

        # Prompt 3: Student refines the email based on the professor's feedback
        prompt_3 = (
            f"Refine the following email draft based the professor's feedback and the provided advice. \n"
            f"Professor's Feedback: {professor_feedback.text}\n"
            f"Student advice: {student_email_advice}\n"
            f"Student Email:{initial_draft.text}\n"
            "NB: This is the final email that will be sent to the professor. Do not include any comments, placeholders or notes. Do the best with what you have."
            "Refined Email(formatted in markdown):"
        )
        refined_email = self.generate_email(prompt_3)
        print("Refined email:", refined_email.text)

        return refined_email.text
