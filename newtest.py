from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain import hub
import os
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import create_openai_functions_agent
import pandas as pd
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory


pythontools = [PythonREPLTool()]
from dotenv import load_dotenv
load_dotenv()

openaikey = os.environ.get("OPENAI_API_KEY")


llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0,api_key=openaikey)

conversation_with_summary = ConversationChain(
    llm=llm,    
    memory=ConversationBufferWindowMemory(k=2),
    verbose=True
)




prompt_template = PromptTemplate.from_template(
    "you are skillfull csv reader using pandas and pythons tools. So answer the question {question} based on the csv file given. If it is a general question just answer donot go for genrating any code or if required generate the necessary python code assuming name of file is {name}. or you can ask necessary question to user for better results"
)


df = pd.read_csv("Player.csv")
agent_pandas = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
   
)
agent = prompt_template  | agent_pandas 
response = agent.invoke({"question":"give the code to do one hot encoding on Bowling_Skill column","name":"Player.csv"})
print (response)