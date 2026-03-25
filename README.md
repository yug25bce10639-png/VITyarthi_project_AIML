# AI Expense Splitter

**Project Status: Active**
**Languages: Python, Prolog**

This is a smart tool designed to help groups of friends split bills easily. It uses Artificial Intelligence to figure out what you bought and specific algorithms to calculate the easiest way to pay everyone back.

---

## What does this project do?

1.  **It Understands Context:** You do not need to select categories manually. If you type "burger" or "taxi," the AI knows that implies "Food" or "Travel."
2.  **It Ensures Fairness:** It calculates the total spending, the average cost per person, and identifies who paid too much or too little.
3.  **It Simplifies Payments:** Instead of giving you a confusing list of numbers, it provides a clear plan. For example: "Alice needs to pay Bob $50."

---

## File Description

* **train_model.py:** This is the training script. You run this once to "teach" the AI what different words (like pizza, hotel, gas) mean.
* **main_app.py:** This is the main application. You run this file to enter expenses and get the final settlement plan.
* **settlement.pl:** This is the logic file. It contains the rules that define who counts as a debtor and who counts as a creditor.

---

## How to Run This Project

**Step 1: Install the necessary libraries**
Open your terminal and run the following command to get the required tools:

python -m pip install scikit-learn pandas

**Step 2: Train the AI Model**
Run this command once to generate the AI's "brain" file:

python train_model.py

**Step 3: Start the Application**
Run the main program to start adding expenses:

python main_app.py

---

## Usage Example

**User Input:** "Alice paid for Pizza"
**System Response:** The system automatically marks this as a **Food** expense.

**Final Result:**
At the end of the entry process, the system will output a settlement plan, such as:
"Charlie pays Alice $20 to settle all debts."

---

## Technical Details

* **Python:** The core programming language used.
* **Machine Learning:** Uses a Naive Bayes classifier to predict categories.
* **Prolog:** Used to handle the logic of debt relationships.

**Created by [Yug Parmar]**
