import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import flight_Intent
import flight_Intent_Response
import random


nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text)
    return[token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
'''
.is_stop gives a boolean value. True if the token is a stop word (all the irrelevant things like: a,an,the,is,were etc
.is_aplha gives boolean too. True is the token contains only alphabet characters.
'''

X_train = []
Y_train = []
for intent,sentences in flight_Intent.INTENT_DATA.items():
    for sentence in sentences:
        X_train.append(sentence)
        Y_train.append(intent)


vectorizer = CountVectorizer(analyzer= preprocess)

X_train_vec = vectorizer.fit_transform(X_train)

clf = MultinomialNB()
clf.fit(X_train_vec, Y_train)



def predict_intent(text, threshold=0.4):
    X_test = vectorizer.transform([text])
    probs = clf.predict_proba(X_test)[0]    #Used [0] just to convert the 'probs' to a string, else it would have been a list.
    best_idx = probs.argmax()       #argmax() will give the position of highest probability.

    if probs[best_idx] < threshold:
        return "I am sorry, I didn't understand. Could you please try reframing your query?", probs[best_idx]

    return clf.classes_[best_idx], probs[best_idx]
        #clf.classes_ stores the unique values of Y_train values in a specific order.






