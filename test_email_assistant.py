import pandas as pd
from transformers import pipeline

# Load your real dataset
df = pd.read_csv("data/Sample_Support_Emails_Dataset.csv")

# Keep only support-related emails (filter by subject keywords)
keywords = ["support", "query", "request", "help"]
df = df[df["subject"].str.lower().str.contains("|".join(keywords))]

# Sentiment analysis
sentiment_analyzer = pipeline("sentiment-analysis")
df["sentiment"] = df["body"].apply(lambda x: sentiment_analyzer(x)[0]["label"])

# Priority classification (simple keyword-based)
def classify_priority(text):
    urgent_keywords = ["immediately", "urgent", "cannot access", "critical", "asap", "blocked"]
    if any(word in str(text).lower() for word in urgent_keywords):
        return "Urgent"
    return "Not Urgent"

df["priority"] = df["body"].apply(classify_priority)

# Show results
print(df[["sender", "subject", "sent_date", "sentiment", "priority"]])

# Save results to a CSV file
df.to_csv("classified_emails.csv", index=False)
print("\n✅ Results saved to classified_emails.csv")

