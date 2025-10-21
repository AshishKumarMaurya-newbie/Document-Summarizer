import nltk
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# ------------------------------
# Download NLTK data if missing
# ------------------------------
nltk_packages = ["punkt", "stopwords"]
for pkg in nltk_packages:
    try:
        nltk.data.find(f"tokenizers/{pkg}") if pkg == "punkt" else nltk.data.find(f"corpora/{pkg}")
    except LookupError:
        print(f"NLTK '{pkg}' not found. Downloading...")
        nltk.download(pkg)
        print(f"{pkg} download complete.")

# ------------------------------
# URL Scraper
# ------------------------------
def scrape_text_from_url(url):
    """Pulls the main text content from a given URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text() for p in paragraphs])
        return article_text
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None

# ------------------------------
# Extractive Summary
# ------------------------------
def get_extractive_summary(text, percentage=30):
    """
    Generates an extractive summary using NLTK.
    Returns the top N sentences based on a simple percentage of the total text.
    """
    sentences = nltk.sent_tokenize(text)
    num_sentences = max(1, int(len(sentences) * (percentage / 100)))
    return ' '.join(sentences[:num_sentences])

# ------------------------------
# Abstractive Summary
# ------------------------------
def get_abstractive_summary(text):
    """
    Generates an abstractive summary using Hugging Face Transformers (T5-small).
    Automatically splits long text into manageable chunks.
    """
    summarizer_pipeline = pipeline("summarization", model="t5-small")
    max_chunk_length = 512  # T5 token limit
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summary_text = ""
    for chunk in chunks:
        summary = summarizer_pipeline(chunk, max_length=150, min_length=30, do_sample=False)
        summary_text += summary[0]['summary_text'] + " "
        
    return summary_text.strip()

# ------------------------------
# Optional: run as script
# ------------------------------
if __name__ == '__main__':
    print("NLTK data checked/downloaded. Summarizer ready to use.")
