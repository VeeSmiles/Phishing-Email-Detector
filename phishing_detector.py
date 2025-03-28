import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import tkinter as tk
from tkinter import messagebox
import nltk
nltk.download('stopwords')

# Kenyan phishing examples + global dataset
data = {
    'email_text': [
        "Urgent M-Pesa Alert! Your account is frozen. Click to verify: http://fake-mpesa.co.ke",
        "KRA TAX REFUND: Claim your 12,560 KSH now!",  # Kenyan-specific
        "Hi team, attached is the Q3 sales report.",  # Legitimate
        "JOB OFFER: Earn 50K/day from home. No experience needed!",  # Common Kenyan scam
        "Meeting reminder: Project discussion at 2 PM."
    ],
    'is_phishing': [1, 1, 0, 1, 0]  # 1=phishing, 0=legitimate
}

# Preprocessing and model training (same as before)
df = pd.DataFrame(data)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['email_text'])
y = df['is_phishing']
model = SVC(kernel='linear')
model.fit(X, y)

# Simple GUI for demo
def check_email():
    email = entry.get()
    prediction = model.predict(vectorizer.transform([email]))[0]
    result = "⚠️ PHISHING" if prediction == 1 else "✅ LEGITIMATE"
    messagebox.showinfo("Result", f"Email: {email}\nClassification: {result}")

root = tk.Tk()
root.title("CA Kenya Phishing Detector")
tk.Label(root, text="Enter email text:").pack()
entry = tk.Entry(root, width=50)
entry.pack()
tk.Button(root, text="Check", command=check_email).pack()
root.mainloop()
