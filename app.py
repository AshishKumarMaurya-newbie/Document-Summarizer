import streamlit as st
from summarizer import get_extractive_summary, get_abstractive_summary, scrape_text_from_url

# Set up the page title and icon
st.set_page_config(page_title="Text Summarizer", page_icon="📝")

st.title("AI Document Summarizer 📝")
st.subheader("Summarize text, articles, or web pages with a single click.")

# Input choice: Text Area or URL
input_option = st.radio("Choose input type:", ("Paste Text", "From URL"))

# Model choice
model_option = st.selectbox("Choose summarization model:", ("Extractive (Fast)", "Abstractive (AI-Powered)"))

if input_option == "Paste Text":
    user_text = st.text_area("Paste your text here:", height=250)
else:
    user_text = st.text_input("Enter the URL:")

if st.button("Summarize"):
    if not user_text:
        st.warning("Please enter some text or a URL to summarize.")
    else:
        # Get the text (either from text area or by scraping URL)
        final_text = user_text
        if input_option == "From URL":
            with st.spinner("Scraping text from URL..."):
                final_text = scrape_text_from_url(user_text)
                if not final_text:
                    st.error("Could not scrape text from the URL. Please try another one.")
                    final_text = None # Stop processing

        if final_text:
            with st.spinner("Summarizing your text... This might take a moment."):
                if model_option == "Extractive (Fast)":
                    summary = get_extractive_summary(final_text)
                else:
                    # Abstractive (AI)
                    summary = get_abstractive_summary(final_text)

            st.subheader("Your Summary:")
            st.success(summary)