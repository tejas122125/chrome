import os
import requests 
from bs4 import BeautifulSoup
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from dotenv import load_dotenv
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.question_answering import load_qa_chain



load_dotenv()
openaikey = os.environ.get("OPENAI_API_KEY")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",api_key=openaikey)



def get_all_links (url):
    link_collection = []

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all anchor tags (links) in the parsed HTML
        links = soup.find_all('a')

        # Extract the href attribute (URL) from each link
        for link in links:
            href = link.get('href')
            if href:
                link_collection.append(href)
                print(href)
    else:
        print("Failed to fetch the webpage. Status code:", response.status_code)

def data_loader(urls):
    for url in urls :
        loader = UnstructuredURLLoader(urls=url)



        
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(api_key=openaikey)
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore        

def conversational_chain(vectorestore):
    llm = ChatOpenAI(temperature=0.2,api_key=openaikey)
    
    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorestore.as_retriever())
    return chain 
    
    



def main():
    links = get_all_links("https://python.langchain.com/docs/modules/chains") 
    # here we have to change the dynamic routes manually
       
    text_chunks = get_text_chunks(links)
    vectore_store = get_vectorstore(text_chunks) 
    conversation_chain = get_conversational_chain(vectore_store)   

if __name__ == '__main__':
    
    main()    