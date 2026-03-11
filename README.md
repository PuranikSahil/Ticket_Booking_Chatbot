This is a rule based chatbot built using streamlit, Supabase and NLP.
### Tech stack:
    1) Database: Supabase (uses Postgres SQL)
    2) Frontend: Using streamlit (Python)
    3) NLP: spaCy , Scikit-learn (Multinomial Naive Bayes)
### Features:
    1) Intent classification using Naive Bayes
    2) Flight searche and booking by accessing the database
    3) Ticket cancellation
    4) Admin login (just to add a few more flights)
## How to Run
    1) Install dependencies: pip install -r requirements.txt
    2) Add your .env file with SUPABASE_URL and SUPABASE_KEY
    3) Run: streamlit run router.py
