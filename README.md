📝 AI Document Summarizer

An interactive web app built with Python, Streamlit, and Hugging Face. This tool automatically generates concise summaries from long text documents — including PDF, Word (.docx), and plain text files.

🚀 Features

   • Multi-Input: Supports summarizing text directly pasted by the user.

   • Web Scraping: Can fetch and summarize articles directly from a URL.

   • Dual Models:

      • Abstractive (AI): Uses Hugging Face T5-Small to generate new, human-like summaries.

      • Extractive (Fast): Uses NLTK to find and present the most important sentences.

   • Simple UI: A clean and simple web interface built with Streamlit.
 
   • Live Demo: Deployed and accessible online via Streamlit Community Cloud.

🧩 Tech Stack

   • Python 3.10+

   • Streamlit: For the web app UI

   • Hugging Face transformers: For abstractive summarization

   • NLTK (Natural Language Toolkit): For extractive summarization

   • Requests: For fetching web content

   • BeautifulSoup4: For parsing HTML and extracting text

🧠 How It Works

   1. The user visits the Streamlit web app.

   2. They choose an input type (Paste Text or From URL) and a model (Abstractive or Extractive).

   3. Text is either read from the text box or scraped from the provided URL.

   4. The selected model processes the text.

   5. The final, concise summary is displayed to the user on the page.
