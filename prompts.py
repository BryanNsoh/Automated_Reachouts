# Information about the student
student_info = {
    "Name": "Nkem Afolayan",
    "Nationality": "Cameroonian",
    "Age": 28,
    "Education": {
        "Undergraduate": {
            "Degree": "BSc in Agricultural Science",
            "University": "University of Yaoundé I",
            "Year Graduated": 2017,
        },
        "Postgraduate": {
            "Degree": "Masters in Sustainable Development",
            "University": "University of Dschang",
            "Year Graduated": 2019,
        },
    },
    "Work Experience": [
        {
            "Role": "Agricultural Extension Officer",
            "Organization": "Green Cameroon",
            "Duration": "2017-2018",
            "Responsibilities": [
                "Implemented sustainable farming practices in rural communities",
                "Organized workshops for local farmers on crop diversification",
            ],
        },
        {
            "Role": "Project Coordinator",
            "Organization": "Farmers Without Borders",
            "Duration": "2019-2020",
            "Responsibilities": [
                "Led a team on agricultural development projects",
                "Managed partnerships with local NGOs and government bodies",
            ],
        },
    ],
    "Teaching Experience": {
        "Role": "Science Teacher",
        "School": "Yaoundé High School",
        "Duration": "2020-2021",
        "Subjects": ["Biology", "Environmental Science"],
        "Achievements": [
            "Developed a new environmental science curriculum",
            "Organized student-led sustainability projects",
        ],
    },
    "Skills": [
        "Project Management",
        "Community Outreach",
        "Sustainable Agriculture",
        "Educational Leadership",
    ],
    "Languages": ["English", "French", "Bamun"],
    "Interests": [
        "Sustainable Development",
        "Education Reform",
        "Agricultural Technology",
    ],
}

perplexity_system_msg = "Provide a thorough, highly detailed, nuanced and comprehensive response to the following question:"

student_email_advice = """Email Template for Reaching Out to Professors

                            Subject: Inquiry Regarding Research Opportunities in [Your Area of Interest]

                            Dear Professor XXXX,

                            [Your Introduction]
                            - Briefly introduce yourself, including your current academic or professional status. 

                            [Your current position and prior work]
                            - Mention your current role and highlight 1-2 key achievements or experiences, particularly those where you demonstrated skills in writing scientific manuscripts and proposing creative, logical research ideas.

                            [Connection to the Professor’s Work]
                            - Explain what led you to the professor's research and their group. Articulate how your research ideas link to their work, showing an understanding of relevant literature and hypotheses. Mention specific works or projects (with URLs if available) that align with your interests.

                            [Questions for the Professor]
                            - Pose 2-3 well-thought-out questions that indirectly address your real concerns, showcasing your readiness to contribute effectively to their research. For example:
                            1. Are you currently looking for new graduate students for the upcoming academic year?
                            2. Which department or program would be most suitable for someone aiming to work in your lab, considering my background and research interests?
                            3. What qualities or skills do you value most in your students, particularly in terms of research creativity and writing ability?

                            [Attachment of Resume/CV]
                            - Attach your resume or CV for a more detailed background overview, emphasizing experiences where you successfully linked your research topics to existing literature and paradigms.

                            Closing Remarks
                            - Express your understanding of the investment a faculty member makes in a graduate student and your eagerness to justify this through your contributions.

                            Warm Regards,
                            Your Name
                            [Optional: URL to personal website/Google Scholar/GitHub, etc.]

                            --------------------------------------------------------------------------------

                            Example Email

                            Dear Professor XXXX,

                            My name is Raman Dutt, a graduate of XXXX University [insert URL]. I am currently working as a research associate at HITI Lab [insert URL] at Emory University with Professor A [insert URL] and Professor B [insert URL]. My research includes applications of deep learning in medical image analysis, focusing on domain adaptation and transfer learning. I am committed to contributing to the field through innovative research and well-crafted scientific manuscripts. I have read your fascinating work on medical image analysis ([insert URLs]) and am keen to pursue an MS/PhD in Artificial Intelligence, especially in areas where I can apply my experience in linking research with established paradigms. Here are a few questions:

                            1. Are you looking for new graduate students for Fall '21?
                            2. Which department should I apply to best align with your lab's work?
                            3. What qualities/skills do you prefer in a student, especially regarding research creativity and scientific writing?

                            I've attached my resume for more details about my background and how I can contribute to your research group.

                            Thank you for considering my inquiry!

                            Sincerely,
                            Raman Dutt
                            [insert URL to personal website/Google Scholar/GitHub, etc.]
                """

professor_email_advice = """
As an experienced research professor, your task is to provide concise, actionable feedback on a student's email draft. Focus primarily on areas of improvement that can increase the likelihood of a positive response from another professor. Acknowledge the strengths of the email briefly, and then provide specific suggestions on how the student can enhance their message. Your insights should guide the student in refining their approach to be more effective and impactful.

Student's email:
"""
