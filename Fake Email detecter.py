#


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix


data = {
    'text': [
        "Congratulations! You've won a $1,000 Walmart gift card. Click here to claim.",
        "Hey, are we still meeting for lunch tomorrow?",
        "Earn money fast by working from home. Limited offer!",
        "Your Amazon order has been shipped successfully.",
        "Get cheap meds now! Buy without prescription.",
        "Can you send me the project report by tonight?",
        "You have been selected for a prize, click to verify.",
        "Let's schedule our next meeting for next week."
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}

df = pd.DataFrame(data)


X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.25, random_state=42)


vectorizer = CountVectorizer()
X_train_features = vectorizer.fit_transform(X_train)
X_test_features = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_features, y_train)


y_pred = model.predict(X_test_features)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def check_email(email):
    email_features = vectorizer.transform([email])
    prediction = model.predict(email_features)
    return f"Email is likely: {prediction[0].upper()}"


print(check_email("Claim your free vacation prize now!"))
print(check_email("Let's meet for a project discussion tomorrow."))
