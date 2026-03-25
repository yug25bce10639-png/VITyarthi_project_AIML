import pickle
import os

# --- 1. AI LOADER ---
def load_ai_model():
    try:
        with open('expense_model.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("⚠️ AI Model not found. Did you run train_model.py?")
        return None

def predict_category(model, description):
    if not model: return "Uncategorized"
    return model.predict([description])[0]

# --- 2. INPUT FUNCTIONS ---
def get_people():
    people_input = input("Enter names (comma separated): ")
    return [p.strip().title() for p in people_input.split(",") if p.strip()]

def record_expenses(people, model):
    expenses = {person: 0.0 for person in people}
    print("\n--- AI Expense Recorder ---")
    
    while True:
        payer = input("\nWho paid? (or 'done'): ").strip().title()
        if payer.lower() == 'done': break
        if payer not in people:
            print("Person not found.")
            continue
            
        desc = input("What was bought? (e.g., pizza, uber): ")
        
        # AI Prediction
        category = predict_category(model, desc)
        print(f"🤖 AI Categorized this as: [{category}]")
        
        try:
            amount = float(input(f"Amount for {desc}: "))
            expenses[payer] += amount
        except ValueError:
            print("Invalid amount.")
            
    return expenses

# --- 3. SETTLEMENT LOGIC ---
def calculate_settlement(expenses):
    total = sum(expenses.values())
    if total == 0: return
    fair_share = total / len(expenses)
    
    # Calculate Balances
    balances = {p: expenses[p] - fair_share for p in expenses}
    
    # Generate Prolog Facts (for your project requirement)
    with open('current_facts.pl', 'w') as f:
        for p, bal in balances.items():
            f.write(f"balance({p.lower()}, {bal}).\n")
            
    print(f"\n--- Summary ---")
    print(f"Total: ${total:.2f} | Fair Share: ${fair_share:.2f}")

    # Who Pays Whom Algorithm
    debtors = sorted([(p, b) for p, b in balances.items() if b < 0], key=lambda x: x[1])
    creditors = sorted([(p, b) for p, b in balances.items() if b > 0], key=lambda x: x[1], reverse=True)
    
    print("\n--- Optimized Settlement ---")
    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor, d_val = debtors[i]
        creditor, c_val = creditors[j]
        
        amount = min(-d_val, c_val)
        d_val += amount
        c_val -= amount
        
        print(f"👉 {debtor} pays {creditor}: ${amount:.2f}")
        
        debtors[i] = (debtor, d_val)
        creditors[j] = (creditor, c_val)
        
        if abs(d_val) < 0.01: i += 1
        if c_val < 0.01: j += 1

def main():
    print("Initializing AI Expense Splitter...")
    model = load_ai_model()
    people = get_people()
    if people:
        expenses = record_expenses(people, model)
        calculate_settlement(expenses)

if __name__ == "__main__":
    main()
