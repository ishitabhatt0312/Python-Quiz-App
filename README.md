# Python-Quiz-App

## Overview of the Python Quiz App
This Python Quiz App is a GUI-based multiple-choice quiz game built with the tkinter library. It allows users to answer a series of Python-related questions, receive immediate feedback on their answers, and view their total score at the end of the quiz.

## **1. App Description**
The app displays one question at a time with four possible answers. The user selects their answer using radio buttons and submits it. Feedback is shown using tkinter message boxes, indicating whether the answer was correct or incorrect. After answering all questions, the app displays the user’s final score.

This app is suitable for beginner-level programming quizzes and can be extended with more questions and features as needed.

## **2. Functionalities**

### **Core Features:**

**1. Question Display:**

Displays one question at a time in a text label.
Provides four answer options using radio buttons.

**2. Answer Selection:**

Allows the user to select one of the four options.

**3. Answer Validation:**

Validates the selected answer when the "Submit Answer" button is pressed.
Provides immediate feedback using message boxes:
Correct Answer: A congratulatory message.
Incorrect Answer: Displays the correct answer.

**4. Progression through Questions:**

Moves to the next question automatically after submission.
Ends the quiz when all questions are answered.

**5. Final Score Display:**

Displays the user’s total score at the end of the quiz in a message box.

### **Additional Features:**

**1. Error Handling:**
Warns the user if no answer is selected before submission.

**2. Replayability:**
Can be restarted by re-running the app.


## **3. How It Works**

### **Setup**

A list of questions, options, and correct answers is pre-defined in a dictionary format (quiz list).

Each question in the quiz contains:

1. The question text.
2. Four options.
3. The correct answer.


### **Question Flow**

**1. Loading a Question:**

The current question is fetched from the quiz list.
The question text and its options are dynamically loaded into the GUI widgets.
The answer selection variable (answer_var) is reset.

**2. Answer Submission:**

The user selects an option using the radio buttons.

**On clicking "Submit Answer":**

The app checks if an answer is selected.
Compares the selected answer with the correct answer in the quiz.

**Feedback is shown using messagebox:**

Correct: Score is incremented.
Incorrect: Correct answer is displayed.

**3. Quiz Completion:**

The app moves to the next question until all questions are answered.
After the last question, the final score is displayed in a message box, and the app closes.

## **4. GUI Layout**

**Title:**
The app window has a title, "Python Quiz App."

**Question Label:**
Displays the current question at the top.

**Options:**
Four radio buttons allow the user to select an answer.

**Submit Button:** 
Below the options, a button labeled "Submit Answer" validates the selection and provides feedback.

## **4. Potential Enhancements**

- Add a restart feature to allow replaying without restarting the program.

- Include a timer to make the quiz time-bound.

- Add categories or difficulty levels for questions.

- Use a scoreboard to track high scores across sessions.

- Provide a review option to revisit incorrect answers after completing the quiz.








![Alt Text](https://github.com/user-attachments/assets/d2f7efb9-5b3b-4db2-b739-0addbdfa0416)









![Alt Text](https://github.com/user-attachments/assets/14f645fe-60a3-4e66-8ad3-387bd0c05d9f)









![Alt Text](https://github.com/user-attachments/assets/c8904b9a-96c6-4c46-9a7e-ba2061767fa1)



