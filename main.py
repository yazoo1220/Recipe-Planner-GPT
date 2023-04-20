import streamlit as st
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(temperature=0.5)
tools = load_tools(["serpapi", "requests", "python_repl","wolfram-alpha"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
st.title('Recipe Planner GPT')


query = st.text_input(label="request", value="create menus for one week. Each day the total calory should be 2000. Don't repeat menus. generate the list of menus with the details of the menu's name and ingredients with their weight and calories calculates in Wolfram in json objects and store as menus.json file in the same folder.")
button = st.button('ask')

if query and button:
    with st.spinner('generating menus'):
        prefix = 'return the same Jason strings as stdout'
        json = agent.run(prefix + query)
        st.write('thank you for waiting! Those use the list of menus I came up with')
        import pandas as pd
        df = pd.read_json(json)
        st.dataframe(df)
