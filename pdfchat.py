import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from operator import itemgetter
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import conversational_retrieval
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import ConversationChain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.messages import AIMessage, HumanMessage, get_buffer_string
from langchain_core.prompts import format_document
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts.prompt import PromptTemplate

load_dotenv()
openaikey = os.environ.get("OPENAI_API_KEY")
# print("fbvjhvb"+openaikey)

embeddings = OpenAIEmbeddings(model="text-embedding-3-large",api_key=openaikey)
def get_pdf_text(pdf_docs_path):
    loader = PyPDFLoader(pdf_docs_path)
    pages = loader.load_and_split()
    text = ""
    for page in pages:
         text += page.page_content
    return text



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

def get_conversational_chain(vectorstore):
    llm = ChatOpenAI(temperature=0.2,api_key=openaikey)
    # # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    # memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    # conversation_chain = conversational_retrieval(
    #     llm=llm,
    #     retriever=vectorstore.as_retriever(),
    #     memory=memory
    # )
    # return conversation_chain
    
    # retriever = VectorStoreRetriever(vectorstore=FAISS(...))
    # retrievalQA = RetrievalQA.from_llm(llm=OpenAI(), retriever=retriever)

    
    template = """Answer the question based only on the following context:
    {context}   

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    chain = (
    {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
    )
    return chain
    
def question_with_memory(vectorstore):
    retriever = vectorstore.as_retriever()
    
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.

    Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:"""
    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    ANSWER_PROMPT = ChatPromptTemplate.from_template(template)
    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")


    def _combine_documents(
        docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"
    ):
        doc_strings = [format_document(doc, document_prompt) for doc in docs]
        return document_separator.join(doc_strings)    

    _inputs = RunnableParallel(
    standalone_question=RunnablePassthrough.assign(
        chat_history=lambda x: get_buffer_string(x["chat_history"])
    )
    | CONDENSE_QUESTION_PROMPT
    | ChatOpenAI(temperature=0)
    | StrOutputParser(),
    )
    _context = {
    "context": itemgetter("standalone_question") | retriever | _combine_documents,
    "question": lambda x: x["standalone_question"],
    }
    conversational_qa_chain = _inputs | _context | ANSWER_PROMPT | ChatOpenAI()

    
def main():
   
    raw_text = get_pdf_text("monu.pdf")
    text_chunks = get_text_chunks(raw_text)
    vectore_store = get_vectorstore(text_chunks) 
    conversation_chain = get_conversational_chain(vectore_store)   
    response  = conversation_chain.invoke("List out the marketing strategies of Blackberry.")
    print (response)


if __name__ == '__main__':
    
    main()    