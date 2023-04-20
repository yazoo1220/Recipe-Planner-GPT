import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.5)
tools = load_tools(["serpapi", "requests", "python_repl","wolfram-alpha"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

query = st.text_input('create menus for one week. Each day the total calory should be 2000. generate the list of menus with the details of it's ingredients with their weight and calories in json objects and store as menus.json file in the same folder. All the language should be Japanese')

agent.run(query)

import pandas as pd

df = pd.read_json('menus.json')

st.dataframe(df)
