import tkinter as tk
from tkinter import messagebox

# Questions and answers
quiz = [
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["list", "dictionary", "tuple", "set"],
        "answer": "tuple"
    },
    {
        "question": "What does 'len()' do in Python?",
        "options": ["Calculates length", "Adds numbers", "Subtracts numbers", "None of the above"],
        "answer": "Calculates length"
    }
]

# Initialize quiz variables
current_question = 0
score = 0

def submit_answer():
    global current_question, score
    
    # Get the selected answer
    selected = answer_var.get()
    if selected == "":
        messagebox.showwarning("Warning", "Please select an answer!")
        return
    
    # Check if the answer is correct
    if selected == quiz[current_question]["answer"]:
        score += 1
        messagebox.showinfo("Correct!", "Good job, that's the correct answer!")
    else:
        messagebox.showerror("Incorrect", f"Oops! The correct answer is '{quiz[current_question]['answer']}'.")

    # Move to the next question
    current_question += 1
    if current_question < len(quiz):
        load_question()
    else:
        messagebox.showinfo("Quiz Completed", f"Your score is {score}/{len(quiz)}.")
        root.quit()

def load_question():
    question_label.config(text=quiz[current_question]["question"])
    for i, option in enumerate(quiz[current_question]["options"]):
        option_buttons[i].config(text=option, value=option)
    answer_var.set("")  # Reset answer selection

# Setup the main Tkinter window
root = tk.Tk()
root.title("Python Quiz App")

# Quiz Frame
quiz_frame = tk.Frame(root, padx=20, pady=20)
quiz_frame.pack()

# Question Label
question_label = tk.Label(quiz_frame, text="", font=("Arial", 14), wraplength=400, justify="left")
question_label.pack(pady=10)

# Answer Variable and Option Buttons
answer_var = tk.StringVar()
option_buttons = []
for _ in range(4):
    btn = tk.Radiobutton(quiz_frame, text="", variable=answer_var, font=("Arial", 12), anchor="w", value="")
    btn.pack(fill="x", pady=2)
    option_buttons.append(btn)

# Submit Button
submit_btn = tk.Button(quiz_frame, text="Submit Answer", font=("Arial", 12), bg="blue", fg="white", command=submit_answer)
submit_btn.pack(pady=10)

# Load the first question
load_question()

# Start the app
root.mainloop()
