Email Assistant - Coding Challenge:

  An AI-powered assistant that filters support emails, classifies sentiment and urgency, and saves the results into a structured CSV file.

Overview:

  This project classifies support emails by sentiment and urgency using a HuggingFace transformer model (distilbert-base-uncased-finetuned-sst-2-english).

Files:

  test_email_assistant.py → main script
  
  classified_emails.csv → output with sentiment + priority
  
  Sample_Support_Emails_Dataset.csv → input dataset (sample)
  
  requirements.txt → Python dependencies

How to Run:

  Create a virtual environment
  
  Install dependencies
  
  pip install -r requirements.txt


Run the script:

  python test_email_assistant.py
  
  
  This will generate classified_emails.csv with sentiment and priority results.


📖 Approach / Architecture:

  The solution is built in a simple pipeline:
  
  Email Filtering – The script reads emails from a dataset and filters only those related to support (keywords like support, query, request, help in the subject).
  
  Sentiment Analysis – Each email body is classified as Positive/Negative/Neutral using a HuggingFace DistilBERT model.
  
  Priority Classification – A rule-based check marks urgent cases if the body contains words like immediately, cannot access, critical, urgent, blocked.
  
  Output – Results with sender, subject, date, sentiment, and priority are saved into classified_emails.csv.




Requirements Checklist:

  Email filtering by keywords – Done
  
  Sentiment classification (DistilBERT) – Done
  
  Urgency detection (rule-based) – Done
  
  Results saved into classified_emails.csv – Done
  
  Dashboard with analytics – Planned
  
  Context-aware auto-replies with RAG – Planned



