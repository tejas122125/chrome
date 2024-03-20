from langchain.agents.agent_types import AgentType
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import create_openai_functions_agent
import pandas as pd
from langchain_openai import OpenAI
pythontools = [PythonREPLTool()]

instructions = """You are an agent designed to write and execute python code to answer questions.
You have access to a python REPL, which you can use to execute python code.
If you get an error, debug your code and try again.
Only use the output of your code to answer the question. 
You might know the answer without running any code, but you should still run the code to get the answer.
If it does not seem like you can write code to answer the question, just return "I don't know" as the answer.
"""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)

# agent_python = create_openai_functions_agent(ChatOpenAI(temperature=0,api_key="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"), tools, prompt)


llm = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0,api_key="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")

# agent = create_openai_tools_agent(llm, pythontools, prompt)

df = pd.read_csv("Player.csv")
agent_pandas = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    extra_tools=[pythontools]
)

# agent_executor = AgentExecutor(agent=agent_pandas,tools=pythontools, verbose=True)
agent_pandas.run("make changes and save in the original file by deleting all the values from Bowling_Skill column that have null value you can use any tool ")