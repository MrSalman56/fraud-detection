import pandas as pd

def analyze_email(email_content):
    # Load the email fraud dataset
    dataset = pd.read_csv('./datasets/email_fraud_dataset.csv')
    
    # Check if the email content matches any entry in the dataset
    for index, row in dataset.iterrows():
        if row['content'] in email_content:
            return {"result": row['label']}  # Return the label directly
    
    # Custom message for no match found
    return {"result": "No match found. The email appears to be legitimate."}
