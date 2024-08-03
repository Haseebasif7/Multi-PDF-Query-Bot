# Chat With Multiple PDFs:

This project is a chatbot application that allows users to interact with multiple PDF documents using Streamlit, LangChain, and open-source LLMs via Groq. The chatbot extracts text from uploaded PDFs, converts the text into embeddings, and provides conversational responses based on the content of the PDFs. It also preserves memory, showing the entire chat history until the session is closed.

**📋 Overview**:

Key Features:
PDF Upload: Users can upload one or more PDF files.
Text Extraction: Text is extracted from the PDFs.
Text Chunking: The extracted text is split into manageable chunks.
Embedding Storage: Chunks are converted into embeddings and stored using FAISS.
Conversational Chain: A conversational model is created to answer user queries based on the content of the PDFs.
Memory Feature: The chatbot maintains a conversation history throughout the session.

**🛠️ Setup and Installation**

1. Clone the Repository
```
git clone <repository-url>
cd <repository-directory>
```
2. Install Dependencies
Make sure you have pip installed, then install the required Python packages:
```
pip install -r requirements.txt
```
3. Configure Environment Variables
Create a .env file in the root directory of the project. Add your Groq API key to this file:
```
GROQ_API_KEY=your_groq_api_key_here
```
4. Run the Application
Start the Streamlit application with the following command:
```
streamlit run pdf-query.py
```

This command launches the Streamlit server and opens the application in your default web browser.

**🧑‍💻 Usage**

Upload PDFs: Click on the "Upload PDF HERE:" button to upload one or more PDF files. The application will extract text from these files.

Ask Questions: Enter your question in the "Enter Question Here:" text area and click "Process." The chatbot will generate a response based on the content of the PDFs.

View Responses: The chatbot will display the response to your query.

Chat History: The chatbot maintains and displays the entire chat history within the session, allowing you to review previous interactions.

**🔧 Project Structure**

pdf-query.py: Main script for the Streamlit application. It handles PDF upload, text extraction, chunking, embedding storage, and conversational querying.

.env: Contains environment variables, such as the API key for Groq.

requirements.txt: Lists all Python packages required for the project.

**📝 Detailed Code Explanation**

The pdf-query.py script is responsible for the following tasks:

**Import Libraries**:

streamlit: For building the web application interface.

PyPDF2: For extracting text from PDF files.

langchain: For processing and managing conversational models.

instructor-embeddings: For generating text embeddings.

faiss-cpu: For storing and retrieving text embeddings.

python-dotenv: For loading environment variables.

**Functions**:

extract(pdf): Extracts text from the provided PDF files.

text_to_chunk(text): Splits extracted text into chunks for processing.

vector_store(chunks): Converts text chunks into embeddings and stores them using FAISS.

conversational_chain(vector): Creates a conversational model using LangChain and Groq.

add_message(sender, text): Adds messages to the chat history.

display_chat(): Displays the chat history in the Streamlit interface.

**Main Function**:

main(): Initializes the Streamlit app, handles PDF uploads, processes user queries, and displays chat history.

**📝 About**
This app leverages:

Streamlit - A framework for creating interactive data applications.

LangChain - A toolkit for building language model applications.

Groq - An API for accessing open-source language models.

**🛠️ Troubleshooting**

Ensure all dependencies are installed correctly.

Verify your API key is valid and correctly placed in the .env file.

Check Streamlit logs for error messages if the app does not run as expected.

Feel free to reach out to me for any inquiries!! 

   

