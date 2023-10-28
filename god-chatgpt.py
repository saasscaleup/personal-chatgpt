# used to load text
from langchain.vectorstores import Chroma

# used to create the retriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.utilities import SerpAPIWrapper
from langchain.text_splitter import RecursiveCharacterTextSplitter

# used to create the retrieval tool
from langchain.tools import Tool

from langchain.document_loaders import DirectoryLoader, TextLoader

# used to create the memory
from langchain.memory import ConversationBufferMemory

# used to create the prompt template
from langchain.agents.openai_functions_agent.base import OpenAIFunctionsAgent
from langchain.schema import SystemMessage
from langchain.prompts import MessagesPlaceholder

# used to create the agent executor
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor

from langchain.chains import RetrievalQA


import env
import os
import sys

os.environ["OPENAI_API_KEY"] = env.OPENAI_APIKEY
os.environ["SERPAPI_API_KEY"] = env.SERPAPI_APIKEY


"""
In this section, we're setting up our personal data Database 
by using OpenAIEmbeddings, ChromaDB and Langcahin Tool
"""

# Use this line if you want to load all data under data/ dir
loader_dic = DirectoryLoader("data/")
#loader_dic = TextLoader("data/data.txt")
data = loader_dic.load()

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
splits = text_splitter.split_documents(data)

# VectorDB
embedding = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
vectordb = Chroma.from_documents(
    documents=splits, embedding=embedding, collection_name="personal-data"
)

llm = ChatOpenAI(temperature=0, openai_api_key=os.environ["OPENAI_API_KEY"])

personal_data = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=vectordb.as_retriever()
)

personal_data_tool = Tool(
    name="PersoanlData",
    func=personal_data.run,
    description="useful for when you need to answer questions about personal-data. Input should be a fully formed question.",
)

"""
In this section, we're setting up our Google search agent SerpAPI
So we gonna have access to the Internet
"""

search = SerpAPIWrapper()

serpapi_tool = Tool(
    name="Search",
    func=search.run,
    description="useful for when you need to answer questions about current events",
)


"""
In this section, we're setting up our Agent Memory and defined 
our agent default prompt.
"""

# setting up memory 
memory_key = "history"
memory = ConversationBufferMemory(memory_key=memory_key, return_messages=True)

# setting default promp
system_message = SystemMessage(
    content=(
        "Do your best to answer the questions. "
        "Feel free to use any tools available to look up "
        "relevant information, only if neccessary"
    )
)

prompt = OpenAIFunctionsAgent.create_prompt(
    system_message=system_message,
    extra_prompt_messages=[MessagesPlaceholder(variable_name=memory_key)]
)

"""
In this section, we're initiating our agent and agent_executor
the combine all of our tools, momery, agent, llm etc...
"""

tools = [serpapi_tool, personal_data_tool]

agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)


# agent = initialize_agent(
#     tools=tools,
#     agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
#     llm=llm,
#     verbose=True,
#     handle_parsing_errors=True
# )


agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    memory=memory, 
    verbose=True, 
    handle_parsing_errors=True
)

# Run first encounter with our agent
result = agent_executor({"input": "Hey, Are you ready for work?"})

prompt = None

if len(sys.argv) > 1:
    prompt = sys.argv[1]

while True:
    if not prompt:
        prompt = input("\033[31m\r\nPrompt: \033[0m")
    if prompt in ['quit', 'q', 'exit']:
        sys.exit()

    #print(agent.run(prompt))
    agent_executor({"input": prompt})
    #print(result["output"])
    prompt = None
