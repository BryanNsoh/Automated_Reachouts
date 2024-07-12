from typing import Dict
import json
from prompts import (
    student_email_advice,
    professor_email_advice,
    subject_line_advice,
    criteria_craft_email,
    criteria_insightful_story,
)


class EmailCrafter:
    """
    Crafts an email based on the search results and student preferences.
    """

    def __init__(self, llm_handler):
        self.llm_handler = llm_handler

    def generate_text(self, prompt: str, model_choice: str) -> str:
        # Generating the email using the chosen model via LLM_APIHandler
        response = self.llm_handler.generate_content(prompt, model_choice)
        return response

    def generate_and_evaluate(
        self, prompt: str, criteria: str, model_choice: str
    ) -> str:
        # Three responses are generated and evaluated based on the criteria
        response = self.llm_handler.generate_and_evaluate(
            prompt, criteria, model_choice
        )
        return response

    def create_insightful_story(
        self, student_info: Dict, professor_info: Dict, model_choice: str
    ) -> str:
        insightful_story_prompt = (
            f"You are Mary Mambo, an anglophone educator and econimist from Cameroon reflecting on your life story and your motivation to pursue a second master's degree in {professor_info.get('Department', 'N/A')}. "
            f"Consider the cultural and linguistic dynamics you navigated, both personally and professionally. "
            f"Using the information: {json.dumps(student_info)} and {json.dumps(professor_info)}, "
            f"link your experiences to a deep interest in {professor_info.get('Department', 'N/A')}. "
            f"Particularly focus on how the socio-political climate of Cameroon, your educational background, the specifics of your upbringing and your specific teaching experiences "
            f"have uniquely positioned you to contribute to and benefit from working with {professor_info.get('Employee', 'N/A')}, "
            f"known for their work in {professor_info.get('Department', 'N/A')}. "
            f"Provide the details of your life that highlight these connections, ensuring it resonates authentically with both your and the professor's profiles."
            f"You are liscensed to be creative and imaginative. Create specific events that reference real places and events in cameroon within the bounds of plausibility.\n"
        )
        story = self.generate_and_evaluate(
            insightful_story_prompt, criteria_insightful_story, model_choice
        )
        print("\nStory:", story)
        return story

    def generate_subject_line(
        self,
        email_body: str,
        student_info: Dict,
        professor_info: Dict,
        model_choice: str,
    ) -> str:
        # Craft a subject line based on email content and other information
        subject_prompt = (
            f"You are the student Mary Mambo. Craft five alternative concise and relevant email subject lines based on the following email body, your information, and professor's information. **Clearly and explicitly emphasize** the your intent to pursue a Master's in summer '24 for enhanced research experience in [specific field].\n"
            f"Email Body: {email_body}\n"
            f"Your Information: {json.dumps(student_info)}\n"
            f"Professor Information: {json.dumps(professor_info)}\n"
            f"Guidelines for subject line: {subject_line_advice}\n"
        )

        subject_lines = self.generate_text(subject_prompt, model_choice)

        selection_prompt = (
            f"Return the single best subject line verbatim for the email body from the following options. \n"
            f"Email Body: {email_body}\n"
            f"Subject Lines: {subject_lines}\n"
        )
        subject_line = self.generate_text(selection_prompt, model_choice)

        print("Subject line:", subject_line)

        return subject_line

    def craft_email(
        self, student_info: Dict, professor_info: Dict, model_choice: str
    ) -> Dict:
        # Generate the student's insightful story
        story = self.create_insightful_story(student_info, professor_info, model_choice)

        # Prompt 1: Student generates the initial email draft
        prompt_1 = (
            f"You are the student, Mary Mambo, reaching out to a professor for an opportunity in Summer 2024. \n"
            f"Your Information: {json.dumps(student_info)}\n"
            f"Professor Contact: {professor_info.get('Employee', 'N/A')}, {professor_info.get('Position', 'N/A')}, {professor_info.get('Department', 'N/A')}\n"
            f"Key Reason for Second Master's: {story}\n"
            f"Professor Information: {professor_info.get('Result_1', 'N/A')}, {professor_info.get('Result_2', 'N/A')}, {professor_info.get('Result_3', 'N/A')}\n"
            f"Important Advice: {student_email_advice}\n"
            f"Email (formatted in HTML. Do not include any placeholders or urls.):\n"
        )

        initial_draft = self.generate_and_evaluate(
            prompt_1, criteria_craft_email, model_choice
        )
        print("Initial draft:", initial_draft)

        # Prompt 2: Professor reviews the draft and provides feedback
        prompt_2 = f"{professor_email_advice} \n\n{initial_draft}\n"
        professor_feedback = self.generate_text(prompt_2, model_choice)
        print("Professor feedback:", professor_feedback)

        prompt_3 = (
            f"You are the student, Mary Mambo, Refine the following email draft based on an expert reviewer's feedback and the provided advice. Focus on enhancing your reasons for choosing the professor's department, {professor_info.get('Department', 'N/A')}, and how it aligns with your academic goals and interests. \n"
            f"Expert reviewer's Feedback: {professor_feedback}\n"
            f"Important advice: {student_email_advice}\n"
            f"Your first draft Email:{initial_draft}\n"
            f"Professor Information: {professor_info.get('Result_1', 'N/A')}, {professor_info.get('Result_2', 'N/A')}, {professor_info.get('Result_3', 'N/A')}\n"
            "NB: This is the final email that will be sent to the professor. Be concise and specific in your reasons for choosing the department and how it aligns with your academic journey. **Do not include any comments, placeholders or notes.** \n"
            "Final refined Email (formatted in HTML. Do not include any placeholders or urls. MAKE IT CONCISE.):"
        )

        refined_email = self.generate_and_evaluate(
            prompt_3, criteria_craft_email, model_choice
        )
        print("Refined email:", refined_email)

        # Generate subject line for the email
        subject_line = self.generate_subject_line(
            refined_email, student_info, professor_info, model_choice
        )

        # Return both the email body and subject line
        return {"body": refined_email, "subject": subject_line}
