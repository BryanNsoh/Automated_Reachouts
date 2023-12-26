# Information about the student
student_info = {
    "Name": "Mary Mambo",
    "Gender": "Female",
    "Date of Birth": "03/03/1997",
    "Nationality": "Cameroonian",
    "Contact": {"Phone": "+237676292112", "Email": "mambomary33@gmail.com"},
    "Personal Statement": "A result-driven young professional with interest in food and development economics. Motivated by the need to address economic development crises in developing countries by examining cultural and political institutions and their impact on ordinary people worldwide. A development enthusiast focused on bridging the gap between research findings and practical applications.",
    "Education": {
        "Postgraduate": {
            "Degree": "MSc Economics Science",
            "University": "University of Bamenda",
            "Grade": "Very Good",
            "Year Graduated": 2019,
        },
        "Undergraduate": {
            "Degree": "BSc Economics Science",
            "University": "University of Buea",
            "Grade": "Very Good",
            "Year Graduated": 2016,
        },
        "Teacher Diploma": {
            "Degree": "DIPET 1 (Teacher diploma of technical education first degree)",
            "Institution": "Higher Technical Teachers’ Training College Bambili",
            "Grade": "Very Good",
            "Year Completed": 2019,
        },
        "Secondary Education": {
            "Qualification": "General Certificate of Education (Advanced and Ordinary Levels)",
            "School": "Government High School, Bokwaongo-Buea",
            "Year Completed": 2013,
        },
        "Primary Education": {
            "Qualification": "First School Leaving Certificate",
            "School": "Catholic School Buea Station",
            "Year Completed": 2006,
        },
    },
    "Further Education": {
        "Course": "Introduction to Gender Based Violence Eradication Platforms in Schools",
        "Organization": "United Nations for Children Fund (UNICEF)",
        "Year": 2023,
        "Impact": "Specialized in service delivery, enabling environment, and emergency response against gender-based violence in Cameroon.",
    },
    "Work Experience": [
        {
            "Role": "Teacher",
            "Organization": "Government Technical High School, Manengole",
            "Duration": "2019-Present",
            "Responsibilities": [
                "Planned Economics, Mathematics and Management lessons",
                "Adopted various teaching methods for positive learning outcomes",
                "Enhanced social abilities and learning skills among students",
            ],
        },
        {
            "Role": "Livelihood Support Officer",
            "Organization": "Women in Action Against Gender Based Violence",
            "Duration": "2019-2020",
            "Responsibilities": [
                "Technical planning, supervision, and monitoring of public awareness activities",
                "Coordination with municipalities, authorities, and beneficiaries in Nguti community",
            ],
        },
        {
            "Role": "Marketing Intern",
            "Organization": "CAMPOST",
            "Duration": "2017-2019",
            "Responsibilities": [
                "Developing data collection tools such as surveys",
                "Collecting and analyzing data to identify consumer trends",
                "Creating graphic representations of data",
            ],
        },
    ],
    "Skills": {
        "Organizational/Managerial": ["Leadership", "Interpersonal skills"],
        "Digital": ["Office suite", "Statistical software (SPSS, STATA)"],
        "Other": [
            "Graphics design",
            "Team work",
            "Time management",
            "Adaptability",
            "Fashion designing",
        ],
    },
    "Languages": {"English": "Very Good", "French": "Good", "Ngemba": "Native"},
    "Interests": [
        "Development Economics",
        "Educational Economics",
        "Gender Studies",
        "Sustainable Development",
        "Public Policy and Administration",
        "Global Health Economics",
        "Agricultural Economics",
        "Social Research and Statistics",
        "International Relations",
        "Environmental Economics",
        "Urban and Regional Planning",
        "Social Entrepreneurship",
        "Economic Policy",
        "Human Resource Development",
        "Nonprofit Management and Leadership",
    ],
    "Additional Information": {
        "Dissertation": "Role of women empowerment in Economic Development in Cameroon",
        "Seminars": "The Role of educational planning in agricultural development",
        "Memberships": [
            "Cameroon Teachers Trade Union",
            "Youth Development Network Club",
        ],
    },
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
As an experienced research professor, your task is to provide concise, actionable feedback on a student's email draft. Focus primarily on areas of improvement that can increase the likelihood of a positive response from another professor. Acknowledge the strengths of the email briefly, and then provide specific suggestions on how the student can enhance their message. Your insights should guide the student in refining their approach to be more effective and impactful. Be bluntly and brutally honest, as well as constructive.

Student's email:
"""

subject_line_advice = """Be Concise: Keep the subject line short and to the point. Aim for no more than 50 characters to ensure that the entire subject line is visible on mobile devices.

                        Be Specific: Indicate your main purpose or area of interest. Vague subject lines are less likely to capture attention.

                        Personalize: If possible, include the professor's area of expertise or a relevant keyword from their research to show that the email is tailored to them.

                        Convey Urgency or Relevance: Including time-sensitive words like "Inquiry for Fall 2023 Research Position" can prompt quicker opening.

                        Highlight Unique Value or Interest: Mention something that could set you apart, like a particular skill or achievement relevant to the professor's work.

                        Avoid Spam Triggers: Stay away from overly salesy language or all caps, which can make your email seem like spam.

                        Use Proper Formatting: Proper capitalization and grammar show professionalism and respect for the recipient.

                        Test for Clarity: Ensure that someone unfamiliar with your situation would understand the gist of your email from the subject line alone."""
