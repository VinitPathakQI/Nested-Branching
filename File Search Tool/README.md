# Gemini File Search Tool 📄

A Streamlit application that leverages **Gemini File Search** for end-to-end document ingestion, indexing, and retrieval, allowing users to upload .txt or .pdf files and run natural-language queries that are answered using content retrieved from the underlying File Search Store.

---

## Features

- **File Upload:** Supports `.txt` and `.pdf` files.
- **Automatic Indexing:** Uploaded files are stored and indexed in a Gemini File Search Store.
- **Document-Aware Q&A:** Ask questions like  _“Summarise the document”_ and get answers grounded in the file.
- **Store Management:** Create a new File Search Store and delete it from within the UI.

---

## Tech Stack

- **Streamlit** – UI
- **Google Gemini API (google-genai)** – File Search + text generation
- **Gemini File Search Store** – Managed document indexing and retrieval
- **python-dotenv** – Environment variable management
- **tempfile / os** – Temporary file handling for uploads

---

## Quick Start

### 1. Install Dependencies

Create a virtual environment and install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Add Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY="your_google_gemini_api_key"
```

### 3. Run the App

```bash
streamlit run app.py
```

Your browser will open at:

**<http://localhost:8501>**

---

## Project Structure

```bash
gemini-file-search-tool/
├── app.py              # Main Streamlit app
├── requirements.txt    # Required Python packages
├── .env                # Add your API keys here
└── README.md           # Project documentation
```

---

## How It Works

1. Upload a `.txt` or `.pdf` file from the sidebar.
2. The app creates a **File Search Store** in Gemini with the given display name.
3. The uploaded file is saved temporarily, uploaded to the store, and indexed.
4. Once indexing is complete, you can type a question in the main page input box.
5. The app calls `gemini-2.5-flash` (or your chosen model) with the **File Search tool** enabled.
6. Gemini retrieves relevant content from the indexed file and generates a grounded answer.

---

Made with using Google Gemini File Search Tool and Streamlit!
