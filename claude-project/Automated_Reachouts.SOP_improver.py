import json
import google.generativeai as genai

# Placeholder for importing SOP examples and initial student SOP
from sop_examples_module import example_sop1, example_sop2, example_sop3, student_cv


class SOPImprover:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def initial_feedback(self, student_sop: str) -> str:
        """Step 1: Generate initial feedback on the student's SOP."""
        prompt = (
            f"You are provided with some sample SOP's and feedback, and a student's SOP. "
            f"Provide comments/useful feedback for the student's SOP. The comments should be brief and should be presented in the following format "
            f"[.. snippet of the text where comment most applies], Comment \n\n"
            f"Examples and guidance: \n"
            f"[Example SOP 1: {example_sop1}]\n"
            f"[Example SOP 2: {example_sop2}]\n"
            f"[Example SOP 3: {example_sop3}]\n"
            f"[Student's actual SOP: {student_sop}] for analysis and feedback."
        )
        return self.model.generate_content(prompt).text

    def brutally_honest_feedback(self, student_sop: str) -> str:
        """Step 2: Generate brutally honest feedback."""
        prompt = "Be more brutally honest."
        return self.model.generate_content(prompt).text

    # modify this to use content from the student's CV in addition to the SOP
    def brainstorm_enhancement(self, context: str) -> str:
        """Step 3 & 4: Brainstorming for SOP enhancement."""
        prompt = (
            "Extrapolate from the context given to brainstorm specific facts, narratives, or extra details that would help resolve each of the comments. "
            f"Provide reflection on what to provide and why, then provide the info. You may also use information from the student's cv directly or augmented if it would be helpful. \n\n"
            f"Student CV: {student_cv}\n\n"
            f"Initial and more brutally honest feedback: {context}"
        )
        return self.model.generate_content(prompt).text

    def create_improved_sop(self, context: str) -> str:
        """Step 5: Create an improved SOP."""
        prompt = (
            "You are provided with an SOP some comments on it and some proposed refinements reflect on how all the provided elements can come together to produce an improved SOP for the student that adresses all the provided comments and improves the sop overall:\n\n"
            f"SOP, Comments and proposed refinements: {context}"
        )
        return self.model.generate_content(prompt).text

    def compare_sop_versions(self, sop_version1: str, sop_version2: str) -> str:
        """Step 6: Compare two SOP versions."""
        prompt = (
            "You are provided with two versions of an SOP. Decide which one is better. Output a 1 if version 1 is better and 2 if version 2 is better. Do-not output any other characters\n\n"
            f"Version 1 SOP Content: {sop_version1}\n"
            f"Version 2 SOP Content: {sop_version2}"
        )
        return self.model.generate_content(prompt).text

    def enhance_chosen_sop(self, chosen_sop: str, feedback_points: str) -> str:
        """Step 7: Enhance the chosen SOP."""
        prompt = (
            "Now you are the student. Enhance the chosen SOP according to the 8 points of feedback below. "
            f"Where additional information is needed is needeed such as extra details, goals, personal insight, fabricate it intelligently. cleaving as close to the original content and plausibility as possible. Provide the full modified SOP version 1, minimally altered to completely address all the points below.\n\n"
            f"Chosen SOP: {chosen_sop}\n"
            f"Feedback Points: {feedback_points}"
            "NB: This is the final SOP that will be sent to the professor. Do not include any comments, placeholders or notes. Do the best with what you have."
        )
        return self.model.generate_content(prompt).text

    def final_comparison(self, sop_version1: str, sop_version2: str) -> str:
        """Step 8: Final comparison and conclusion."""
        prompt = (
            "You are provided with two versions of an SOP. Return the one which is better verbatim.\n\n"
            f"Version 1 SOP Content: {sop_version1}\n"
            f"Version 2 SOP Content: {sop_version2}"
            "NB: This is the final SOP that will be sent to the professor. Do not include any comments, placeholders or notes. Do the best with what you have."
        )
        return self.model.generate_content(prompt).text

    def process_sop(self, student_sop: str) -> str:
        """Process the SOP through all the steps."""
        # Step 1: Initial Feedback
        initial_feedback = self.initial_feedback(student_sop)

        # Step 2: Brutally Honest Feedback
        honest_feedback = self.brutally_honest_feedback(student_sop)

        # Step 3 & 4: Brainstorming for Enhancement
        # Consider providing just the honest feedback as context
        brainstorm_context = f"{initial_feedback}\n\n{honest_feedback}"
        brainstormed_ideas = self.brainstorm_enhancement(brainstorm_context)

        # Step 5: Creating an Improved SOP
        improved_sop_context = f"{student_sop}\n\n{brainstormed_ideas}"
        improved_sop = self.create_improved_sop(improved_sop_context)

        # Step 6: Comparison of Two SOP Versions
        comparison_result = self.compare_sop_versions(
            f"Version 1: {student_sop}", f"Version 2: {improved_sop}"
        )

        # Step 7: Enhance Chosen SOP
        # Comparison result will either be 1 or 2. Provide the corresponding SOP version be parsing the comparison result.
        if comparison_result == "1":
            enhanced_sop = self.enhance_chosen_sop(student_sop, comparison_result)
        elif comparison_result == "2":
            enhanced_sop = self.enhance_chosen_sop(improved_sop, comparison_result)

        # Step 8: Final Comparison
        final_comparison = self.final_comparison(enhanced_sop, improved_sop)

        return final_comparison


# Example usage
def main():
    key_path = r"C:\Users\bnsoh2\OneDrive - University of Nebraska-Lincoln\Documents\keys\api_keys.json"
    with open(key_path) as f:
        api_keys = json.load(f)
        GEMINI_API_KEY = api_keys["GEMINI_API_KEY"]

    sop_improver = SOPImprover(GEMINI_API_KEY)

    # Placeholder for Student's Initial SOP
    initial_student_sop = "Placeholder for Student's Initial SOP"

    # Process the SOP through all steps
    final_output = sop_improver.process_sop(initial_student_sop)
    print("Final Output:\n", final_output)


if __name__ == "__main__":
    main()
