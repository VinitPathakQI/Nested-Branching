
from google import genai
from google.genai import types
from dotenv import load_dotenv
import time
import os
import streamlit as st
import tempfile


load_dotenv()
client = genai.Client(api_key = os.environ.get("GEMINI_API_KEY"))

st.set_page_config(page_title="Gemini File Search Demo", page_icon="📄")

st.title("📄 Gemini File Search with Streamlit")
st.write(
    "Upload a text file, index it with Gemini File Search, and ask questions about its content."
)

st.sidebar.header("Upload File")
uploaded_file = st.sidebar.file_uploader(
    "Upload a .txt file", type=["txt"], accept_multiple_files=False
)

store_display_name = st.sidebar.text_input(
    "File Search Store Name", value="streamlit-file-search-store"
)
file_display_name = st.sidebar.text_input(
    "File Display Name (for citations)", value="uploaded-text-file"
)

create_store = st.sidebar.button("Create Store & Import File")

if "file_search_store_name" not in st.session_state:
    st.session_state.file_search_store_name = None

if "import_done" not in st.session_state:
    st.session_state.import_done = False

if create_store:
    if not uploaded_file:
        st.error("Please upload a .txt file first.")
    else:
        try:
            with st.spinner("Creating File Search store..."):
                file_search_store = client.file_search_stores.create(
                    config={"display_name": store_display_name}
                )
                st.session_state.file_search_store_name = file_search_store.name

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            st.success(f"Store created: `{file_search_store.name}`")

            with st.spinner("Uploading and importing file into the store..."):
                operation = client.file_search_stores.upload_to_file_search_store(
                    file=tmp_path,
                    file_search_store_name=file_search_store.name,
                    config={
                        "display_name": file_display_name,
                    },
                )

                while not operation.done:
                    time.sleep(2)
                    operation = client.operations.get(operation)

            st.session_state.import_done = True
            st.success("File imported successfully and ready for questions!")

        except Exception as e:
            st.error(f"Error while creating store or importing file: {e}")

st.header("Ask Questions About the File")

if not st.session_state.file_search_store_name:
    st.info("Create a File Search store and import a file first (see sidebar).")
else:
    st.write(f"**Active Store:** `{st.session_state.file_search_store_name}`")

question = st.text_input(
    "Enter your question:",
    value="Who is the author of the book?",
    placeholder="Ask something about your uploaded file...",
)

ask_button = st.button("Ask Gemini")

if ask_button:
    if not st.session_state.import_done:
        st.warning("The file has not finished importing yet. Please try again.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            with st.spinner("Querying Gemini with File Search..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=question,
                    config=types.GenerateContentConfig(
                        tools=[
                            types.Tool(
                                file_search=types.FileSearch(
                                    file_search_store_names=[
                                        st.session_state.file_search_store_name
                                    ]
                                )
                            )
                        ]
                    ),
                )

            st.subheader("🧠 Gemini Answer")
            st.write(response.text)

            with st.expander("Show raw response (debug)"):
                st.json(response.to_dict() if hasattr(response, "to_dict") else str(response))

        except Exception as e:
            st.error(f"Error while generating answer: {e}")

st.sidebar.header("Cleanup")
cleanup = st.sidebar.button("Delete Current Store")

if cleanup and st.session_state.file_search_store_name:
    try:
        client.file_search_stores.delete(
            name=st.session_state.file_search_store_name,
            config={"force": True},
        )
        st.success(f"Deleted store: {st.session_state.file_search_store_name}")
        st.session_state.file_search_store_name = None
        st.session_state.import_done = False
    except Exception as e:
        st.error(f"Error deleting store: {e}")