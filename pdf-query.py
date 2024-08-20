import streamlit as st
import pdfplumber 
#from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import CharacterTextSplitter
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Initialize session state for messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

def extract(pdfs):
    text = ''
    for pdf_path in pdfs:
        with pdfplumber.open(pdf_path) as pdf_file:
            for page in pdf_file.pages:
                text += page.extract_text() or ''  # Ensure we don't add 'None' if no text is found
    return text

def text_to_chunk(text):
    text_split = CharacterTextSplitter(
        separator='\n',
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    return text_split.split_text(text)

def vector_store(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    vector = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vector

def conversational_chain(vector):
    llm = ChatGroq(temperature=0.0, model='mixtral-8x7b-32768', api_key=os.getenv('GROQ_API_KEY'))
    memory = ConversationBufferMemory()
    qa_chain = load_qa_chain(llm=llm, chain_type='stuff')
    
    # Create a chain that combines the document retrieval and QA
    chain = RetrievalQA(
        retriever=vector.as_retriever(),
        combine_documents_chain=qa_chain,
        memory=memory
    )
    return chain

def add_message(sender, text):
    label = 'User: ' if sender == 'user' else 'Bot: '
    st.session_state.messages.append({'sender': sender, 'text': f"{label}  {text}"})

def display_chat():  
    for msg in st.session_state.messages:  
        if msg['sender'] == 'user':  
            st.markdown(  
                f"<div style='text-align: left; background-color: #2a2a2a; color: #fff; padding: 10px; border-radius: 10px; margin-bottom: 5px; display: inline-block;'>{msg['text']}</div>",  
                unsafe_allow_html=True  
            )  
        else:  
            st.markdown(  
                f"<div style='text-align: left; background-color: #3e3e3e; color: #fff; padding: 10px; border-radius: 10px; margin-bottom: 5px; display: inline-block;'>{msg['text']}</div>",  
                unsafe_allow_html=True  
            )
            
def main():
    load_dotenv()
    
    st.set_page_config(page_title="Chat With Multiple PDFs", page_icon='📚')
    st.header("Chat With Multiple PDFs 💬")
    
    pdf = st.file_uploader('Upload PDF HERE:', type='pdf', accept_multiple_files=True)
    query = st.text_area('Enter Question Here:',height=105,key='query_input')
    
    if st.button('Process'):
        with st.spinner('Processing'):
            if pdf:
                # Extract text from pdf
                text = extract(pdf)
                # Convert Text to chunks
                chunks = text_to_chunk(text)
                # Convert Chunks to Embeddings and Store in a VectorDB (FAISS)
                vector = vector_store(chunks)
                # Make a Conversational Chain
                chain = conversational_chain(vector)
                
                if query:
                    # Add user's question to the chat
                    add_message('user', query)
                    # Get the response from the chain
                    response = chain.run({'query': query})
                    # Add bot's response to the chat
                    add_message('bot', response)
    
    # Display chat messages
    display_chat()

    with st.sidebar:
        st.title(' 💬 LLM Chat APP')
        add_vertical_space(1)
        st.markdown('''
                    ## About:
        This app is an LLM-powered chatbot built using:
        - [Streamlit](https://streamlit.io/)
        - [Langchain](https://www.langchain.com/)
        - [Groq API For LLM](https://groq.com/)
                    
                    ''')
        add_vertical_space(3)
        st.markdown('''
        Made by Haseeb Asif:
        - [Linkedin](https://www.linkedin.com/in/haseeb-asif-4400212a0?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
        - [Github](https://github.com/Haseebasif7)
        ''')

if __name__ == '__main__':
    main()
