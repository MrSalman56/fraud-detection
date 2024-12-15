import pandas as pd

def analyze_link(url):
    # Normalize the URL by removing http:// and https://
    normalized_url = url.replace('http://', '').replace('https://', '')

    # Load your phishing links dataset
    dataset = pd.read_csv('./datasets/phishing_links_dataset.csv')

    # Debugging: Print the normalized URL and dataset for verification
    print(f"Normalized URL: {normalized_url}")
    print("Dataset URLs:", dataset['urls'].tolist())  # Print all URLs in the dataset

    # Check if the provided normalized URL is in the dataset's malicious URLs
    if normalized_url in dataset['urls'].values:
        # Find the corresponding label for the matched URL
        matched_row = dataset[dataset['urls'] == normalized_url]
        return {"result": matched_row['label'].values[0]}  # Return the label directly
    
    # If no match is found, return a custom message
    return {"result": "No match found. The URL appears to be safe."}  # Default to safe if no match
