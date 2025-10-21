import nltk
from transformers import pipeline
from bs4 import BeautifulSoup
import requests

# Download NLTK data (only need to do this once)
# You can run this file directly once to download: python summarizer.py
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("NLTK 'punkt' tokenizer not found. Downloading...")
    nltk.download('punkt')
    print("Download complete.")

def scrape_text_from_url(url):
    """Pulls the main text content from a given URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all paragraph tags
        paragraphs = soup.find_all('p')
        
        # Join them into a single block of text
        article_text = ' '.join([p.get_text() for p in paragraphs])
        return article_text
    except Exception as e:
        print(f"Error scraping URL: {e}")
        return None

def get_extractive_summary(text, percentage=30):
    """
    Generates an extractive summary using NLTK.
    TODO: Implement the NLTK frequency-based algorithm here.
    """
    print("Extractive summary logic goes here...")
    # For now, just return the first few sentences as a placeholder
    sentences = nltk.sent_tokenize(text)
    num_sentences = max(1, int(len(sentences) * (percentage / 100)))
    return ' '.join(sentences[:num_sentences])

def get_abstractive_summary(text):
    """
    Generates an abstractive summary using Hugging Face Transformers.
    """
    print("Loading abstractive model...")
    # Using 't5-small' is a good balance of performance and size
    summarizer_pipeline = pipeline("summarization", model="t5-small")
    
    # T5 has a max length, so we may need to truncate
    max_chunk_length = 512 
    
    # Simple chunking (a more advanced way would be to split by sentences)
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    
    summary_text = ""
    for chunk in chunks:
        summary = summarizer_pipeline(chunk, max_length=150, min_length=30, do_sample=False)
        summary_text += summary[0]['summary_text'] + " "
        
    return summary_text.strip()

if __name__ == '__main__':
    # This block runs if you execute 'python summarizer.py'
    # Useful for downloading NLTK data
    print("NLTK data checked/downloaded.")