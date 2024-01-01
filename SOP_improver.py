import json
import google.generativeai as genai

# Import SOP examples and initial student SOP
from sop_examples_module import (
    example_sop1,
    example_sop2,
    example_sop3,
    initial_student_sop,
)


class SOPImprover:
    """
    A class to handle SOP feedback generation and improvement using an AI model.
    """

    def __init__(self, api_key: str):
        """
        Initializes the SOPImprover with an API key for the AI model.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def generate_feedback(self, student_sop: str) -> str:
        """
        Generates feedback for a given student's SOP.
        """
        feedback_prompt = (
            f"You are provided with some sample SOP's and feedback, and a student's SOP. "
            "Provide comments/useful feedback for the student's SOP. The comments should be brief and should be presented in the following format "
            "[.. snippet of the text where comment most applies], Comment \n\n"
            "Examples and guidance: \n"
            f"[Example SOP 1: {example_sop1}]\n"
            f"[Example SOP 2: {example_sop2}]\n"
            f"[Example SOP 3: {example_sop3}]\n"
            f"[Student's actual SOP: {student_sop}] for analysis and feedback."
        )
        feedback = self.model.generate_content(feedback_prompt)
        return feedback.text

    def improve_sop(self, student_sop: str, feedback: str) -> str:
        """
        Improves the SOP based on the given feedback.
        """
        improvement_prompt = (
            f"Based on the following feedback, improve the student's SOP. "
            f"Feedback: {feedback}\n"
            f"Student's initial SOP: {student_sop}\n"
            "Provide a revised version of the SOP."
        )
        improved_sop = self.model.generate_content(improvement_prompt)
        return improved_sop.text


def read_api_key(file_path: str) -> str:
    """
    Reads API key from a specified file.
    """
    with open(file_path) as f:
        api_keys = json.load(f)
    return api_keys["GEMINI_API_KEY"]


def main(api_key_file: str):
    """
    Main function demonstrating the use of SOPImprover.
    """
    try:
        GEMINI_API_KEY = read_api_key(api_key_file)

        sop_improver = SOPImprover(GEMINI_API_KEY)

        # Generate feedback for the initial SOP
        feedback = sop_improver.generate_feedback(initial_student_sop)
        print("Feedback:\n", feedback)

        # Generate an improved version of the SOP based on feedback
        improved_sop = sop_improver.improve_sop(initial_student_sop, feedback)
        print("Improved SOP:\n", improved_sop)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main(
        r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"
    )
