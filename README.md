# MIS203 Basic Programming

**Name:** Esra Kaşık  
**Student Number:** 2404109906  
**Department:** Management Information Systems  
**Course Name:** MIS203 Basic Programming  

---

### AI Tool Usage

* **AI Tool Used:** Gemini
* **Prompt Used:** "Write a simple Python script that asks the user for their Name, Department, Age, and Career Goal using input(), then prints a formatted Student Profile."
* **What did you change?:** I added the `\n` newline character in the print statement to create extra spacing before the profile output. I also customized the user prompt messages to make them clearer.

  ## Week 02

* AI Tool Used: ChatGPT

* Prompt Used: Create a simple Python grade calculator program using a while True loop and break. The program should ask for a student name and score, validate the score between 0 and 100, calculate the letter grade, use continue for invalid scores, and print the total number of students and average score.

* What did you change? I tested the program with different student names and scores. I also checked the invalid score and quit options.

* What does break do in your program? The break statement stops the while loop when the user enters q.

## Week 03

* **AI Tool Used:** ChatGPT
* **Prompt Used:** Help me create a Python cinema ticket office program using input, type conversion, f-strings, loops, conditions (if/elif/else), and input validation. The program should calculate ticket prices based on age, day, and student status, apply the discount rules in the correct order, and print a summary of tickets sold, total revenue, average price, and free tickets.
* **What did you change?** I used the suggested structure and adapted the code to the assignment requirements. I also checked the input validation and ticket discount rules.
* **Tests:**

  1. Input: Age 20, weekday, student yes → `Zeynep: 140.00 TRY (Student)`
  2. Input: Age 5, weekend, student no → `Can: 0.00 TRY (Free)`
  3. Input: Age 12, weekday, student yes → `Deniz: 120.00 TRY (Child)`
* **Why does the order of the rules matter?** The rules must be checked in the given order because one customer can meet more than one condition. For example, a 10-year-old student must be classified as Child because the Child rule comes before the Student rule.


