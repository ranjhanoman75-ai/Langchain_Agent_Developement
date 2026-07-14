from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional HR Recruiter, Python Interviewer, Career Counselor, and Linkedln headline optimizer .

Your tasks are:

1. Create a professional ATS-friendly resume.
2. Write a professional career objective.
3. Generate 5 Python interview questions with detailed answers.
4. Give 5 suggestions to improve the candidate's resume.
5. Generate linkedln headline.
6. Generate Top 10 technical skills the candidate should learn next.

Always format your response with proper headings, and follow the following structure for output:
    ============================
        Professional Resume
    ============================


    ...

    =============================
     Career Objectives
    =============================


    ...

    =============================
    Interview Questions
    =============================
    

    ...
    ==============================
    Resume improvements tips
    ==============================

    ....
"""
        ),
        (
            "human",
            """
            
Candidate Information

Name:
{name}

Education:
{education}

Skills:
{skills}

Experience:
{experience}

Projects:
{projects}

Certifications:
{certifications}
"""
        )
    ]
)

parser = StrOutputParser()

chain = prompt | model | parser
print("=" * 60)
print("      PROFESSIONAL AI RESUME GENERATOR")
print("=" * 60)

name = input("Enter your name: ")
education = input("Enter your education: ")
skills = input("Enter your skills (comma separated): ")
experience = input("Enter your experience: ")
projects = input("Enter your projects: ")
certifications = input("Enter your certifications: ")

response = chain.invoke(
    {
        "name": name,
        "education": education,
        "skills": skills,
        "experience": experience,
        "projects": projects,
        "certifications": certifications
    }
)

print("\n")
print("=" * 80)
print("AI GENERATED CAREER REPORT")
print("=" * 80)
print(response)