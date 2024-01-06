from typing import Dict
import json
from prompts import student_email_advice, professor_email_advice, subject_line_advice


class EmailCrafter:
    """
    Crafts an email based on the search results and student preferences.
    """

    def __init__(self, llm_handler):
        self.llm_handler = llm_handler

    def generate_email(self, prompt: str, model_choice: str) -> str:
        # Generating the email using the chosen model via LLM_APIHandler
        response = self.llm_handler.generate_content(prompt, model_choice)
        return response.text

    def generate_subject_line(
        self,
        email_body: str,
        student_info: Dict,
        professor_info: Dict,
        model_choice: str,
    ) -> str:
        # Craft a subject line based on email content and other information
        subject_prompt = (
            f"Craft five alternative concise and relevant email subject lines based on the following email body, student information, and professor information. Emphasize the student's intent to pursue a Master's in summer '24 for enhanced research experience in [specific field].\n"
            f"Email Body: {email_body}\n"
            f"Student Information: {json.dumps(student_info)}\n"
            f"Professor Information: {json.dumps(professor_info)}\n"
            f"Guidelines for subject line: {subject_line_advice}\n"
        )

        subject_lines = self.generate_email(subject_prompt, model_choice)

        selection_prompt = (
            f"Return the single best subject line verbatim for the email body from the following options. \n"
            f"Email Body: {email_body}\n"
            f"Subject Lines: {subject_lines}\n"
        )
        subject_line = self.generate_email(selection_prompt, model_choice)

        print("Subject line:", subject_line)

        return subject_line

    def craft_email(
        self, student_info: Dict, professor_info: Dict, model_choice: str
    ) -> Dict:
        # Prompt 1: Student generates the initial email draft
        prompt_1 = (
            f"You are the student, Mary Mambo, reaching out to a professor. \n"
            f"Student Information: {json.dumps(student_info)}\n"
            f"Professor Information: {professor_info.get('Employee', 'N/A')}, {professor_info.get('Position', 'N/A')}, {professor_info.get('Department', 'N/A')}\n"
            f"Key Reason for Second Master's: To deepen expertise and gain comprehensive research experience in {professor_info.get('Department', 'N/A')}, addressing gaps from previous Master's program and building specific skills relevant to {professor_info.get('Department', 'N/A')}'s field.\n"
            f"Search Results: {professor_info.get('Result_1', 'N/A')}, {professor_info.get('Result_2', 'N/A')}, {professor_info.get('Result_3', 'N/A')}\n"
            f"Student advice: {student_email_advice}\n"
            f"Email (formatted in HTML. Do not include any placeholders or urls.):\n"
        )

        initial_draft = self.generate_email(prompt_1, model_choice)
        print("Initial draft:", initial_draft)

        # Prompt 2: Professor reviews the draft and provides feedback
        prompt_2 = f"{professor_email_advice} \n\n{initial_draft}\n"
        professor_feedback = self.generate_email(prompt_2, model_choice)
        print("Professor feedback:", professor_feedback)

        prompt_3 = (
            f"Refine the following email draft based on the professor's feedback and the provided advice. Focus on enhancing your reasons for choosing the professor's department, {professor_info.get('Department', 'N/A')}, and how it aligns with your academic goals and interests. \n"
            f"Professor's Feedback: {professor_feedback}\n"
            f"Student advice: {student_email_advice}\n"
            f"Original Student Email:{initial_draft}\n"
            f"Searched Results: {professor_info.get('Result_1', 'N/A')}, {professor_info.get('Result_2', 'N/A')}, {professor_info.get('Result_3', 'N/A')}\n"
            "NB: This is the final email that will be sent to the professor. Be concise and specific in your reasons for choosing this department and how it aligns with your academic journey. Do not include any comments, placeholders or notes. \n"
            "Refined Email (formatted in HTML. Do not include any placeholders or urls.):"
        )

        refined_email = self.generate_email(prompt_3, model_choice)
        print("Refined email:", refined_email)

        # Generate subject line for the email
        subject_line = self.generate_subject_line(
            refined_email, student_info, professor_info, model_choice
        )

        # Return both the email body and subject line
        return {"body": refined_email, "subject": subject_line}
