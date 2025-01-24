from llms import QwenWrapper
from termcolor import colored
import time

def teacher_print(string: str):
    color = "light_red"
    print(colored("Teacher: ", color))
    print(colored(string, color), "\n")

def student_print(string: str):
    color = "light_blue"
    print(colored("Student: ", color))
    print(colored(string, color), "\n")

student_prompt = f"""
You, the model, are role playing as a student who wants to learn about machine learning.
You, the model, ask questions to follow up on the things that the teacher explains.
Your questions are brief and consist of one sentence maximum.

Inputs will come in the form of replies from a teacher.
"""

teacher_prompt = f"""
You are a teacher who teaches students about machine learning.
Students ask you questions, and you give very concise responses.
"""

student = QwenWrapper(
    system_prompt=student_prompt
)

teacher = QwenWrapper(
    system_prompt=teacher_prompt
)

teacher_response = teacher.query("Introduce yourself.")
teacher_print(teacher_response)

start_time = time.time()
duration = 60. # sec

while time.time() - start_time < duration:
    student_response = student.query(teacher_response)
    student_print(student_response)
    teacher_response = teacher.query(student_response)
    teacher_print(teacher_response)