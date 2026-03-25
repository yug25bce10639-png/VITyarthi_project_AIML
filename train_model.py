import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# 1. Dataset: Mappings of descriptions to categories
data = {
    'description': [
        'burger', 'pizza', 'lunch', 'dinner', 'coffee', 'groceries', 'milk', 'snacks',
        'uber', 'taxi', 'bus', 'flight', 'gas', 'fuel', 'train',
        'movie', 'netflix', 'cinema', 'concert', 'bowling',
        'rent', 'electricity', 'water bill', 'wifi',
        'hotel', 'airbnb', 'resort', 'books', 'tuition'
    ],
    'category': [
        'Food', 'Food', 'Food', 'Food', 'Food', 'Groceries', 'Groceries', 'Groceries',
        'Transport', 'Transport', 'Transport', 'Transport', 'Transport', 'Transport', 'Transport',
        'Entertainment', 'Entertainment', 'Entertainment', 'Entertainment', 'Entertainment',
        'Utilities', 'Utilities', 'Utilities', 'Utilities',
        'Travel', 'Travel', 'Travel', 'Education', 'Education'
    ]
}

# 2. Train Model
df = pd.DataFrame(data)
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(df['description'], df['category'])

# 3. Save Model
with open('expense_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'expense_model.pkl'")
