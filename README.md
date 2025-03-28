# Phishing Email Detector  
A Python tool to classify phishing emails using machine learning (SVM).  

## Features  
- Preprocesses text (removes stopwords).  
- Uses TF-IDF for feature extraction.  
- Achieves ~85% accuracy on sample data.  

## How to Use  
1. Install dependencies: `pip install pandas scikit-learn nltk`.  
2. Run: `python phishing_detector.py`.  

## Dataset Sources  
- Phishing examples inspired by real scams reported by [Communications Authority of Kenya](https://www.ca.go.ke).  
- Legitimate emails simulated for balance.  
