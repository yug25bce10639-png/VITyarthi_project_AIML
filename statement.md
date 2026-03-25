# Project Statement

## Problem Statement
In shared living situations, group trips, or collaborative events, managing finances is often a source of friction. The manual process of tracking who paid for what, categorizing those expenses, and calculating who owes whom is prone to human error and complexity.

Traditional spreadsheets or basic calculator apps require users to manually categorize every item and often present confusing negative balances without a clear way to settle them. There is a need for a system that can understand natural language input and intelligently automate the settlement process.

## Scope of the Project
The scope of this project is to develop a **Hybrid AI Application** that streamlines expense splitting. The system integrates two distinct branches of Artificial Intelligence:
1.  **Machine Learning (Statistical AI):** To automate the categorization of expenses based on text descriptions (e.g., inferring that "latte" falls under "Food").
2.  **Logic Programming (Symbolic AI):** To define strict rules for debt relationships using Prolog, ensuring the financial logic is sound and verifiable.

The application operates as a Command Line Interface (CLI) tool that takes raw user input, processes it through an NLP model, and outputs a minimized transaction list to settle all debts.

## Target Users
* **Roommates:** Individuals sharing rent, utilities, and grocery costs in shared apartments.
* **Travelers:** Groups of friends on vacation needing to track shared costs like taxis, hotels, and meals.
* **Students:** Project groups splitting costs for materials or event organizers managing shared budgets.
* **Families:** Households managing shared expenses among members.

## High-Level Features
* **AI-Powered Categorization:** Utilizes a Naive Bayes classifier to automatically predict expense categories (e.g., Food, Travel, Utilities) from simple text descriptions, reducing manual data entry.
* **Logical Debt Resolution:** Integrates a Prolog engine to strictly define and validate "Debtor" and "Creditor" relationships based on calculated balances.
* **Smart Settlement Algorithm:** Implements a "Min-Match" algorithm that simplifies complex debt networks into a concise list of direct transfers (e.g., "User A pays User B"), minimizing the total number of transactions required.
* **Dynamic Knowledge Base:** Automatically generates a Prolog knowledge base representing the current financial state of the group for logical querying.
