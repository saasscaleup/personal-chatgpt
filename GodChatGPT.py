import sys

# streamlit special fix
try:
    import pysqlite3
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except:
    print("Can't import pysqlite3")


# used to save information
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

import os

class GodChatGPT():

    def __init__(self,openai_apikey,serpapi_apikey):

        self.openai_apikey  = openai_apikey
        self.serpapi_apikey  = serpapi_apikey
        self.setEnvirmentKeys()

        self.llm            = ChatOpenAI(temperature=0, openai_api_key=self.openai_apikey)

        # setting up memory 
        self.memory_key     = "history"
        self.memory         = ConversationBufferMemory(memory_key=self.memory_key, return_messages=True)

        self.personal_data_tool = self.setPersonalDataTool()
        self.google_search_tool = self.setGoogleSearchTool()

        self.tools = [self.google_search_tool, self.personal_data_tool]

        self.agent = self.setAgent();

        self.agent_executor = self.setAgentExecuter()


    def setEnvirmentKeys(self):
        
        os.environ["OPENAI_API_KEY"] = self.openai_apikey
        os.environ["SERPAPI_API_KEY"] = self.serpapi_apikey

    def setPersonalDataTool(self):

        """
        In this section, we're setting up our personal data Database 
        by using OpenAIEmbeddings, ChromaDB and Langchain Tool
        """
                
        # Use this line if you want to load all data under data/ dir
        loader_dic = DirectoryLoader("data/")
        #loader_dic = TextLoader("data/data.txt")
        data = loader_dic.load()

        # Split
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=10)
        splits = text_splitter.split_documents(data)

        # VectorDB
        embedding = OpenAIEmbeddings(openai_api_key=self.openai_apikey)
        vectordb = Chroma.from_documents(
            documents=splits, embedding=embedding, collection_name="personal-data"
        )

        personal_data = RetrievalQA.from_chain_type(
            llm=self.llm, chain_type="stuff", retriever=vectordb.as_retriever(search_kwargs={"k": 1})
        )

        personal_data_tool = Tool(
            name="PersoanlData",
            func=personal_data.run,
            description="useful for when you need to answer questions about personal-data. Input should be a fully formed question.",
        )

        return personal_data_tool

    def setGoogleSearchTool(self):
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

        return serpapi_tool

    def setAgent(self):

        """
        our agent default prompt.
        """
        # setting default promp
        system_message = SystemMessage(
            content=(
                "Do your best to answer the questions. "
                "Feel free to use any tools available to look up "
                "relevant information and personal data. "
                "Use Personal Data tool when asked personal questions. "
                "Use search tool when asking questions about current event or when you don't have answer. "
                "Use Your memory when needed."
            )
        )

        prompt = OpenAIFunctionsAgent.create_prompt(
            system_message=system_message,
            extra_prompt_messages=[MessagesPlaceholder(variable_name=self.memory_key)]
        )

        agent = OpenAIFunctionsAgent(llm=self.llm, tools=self.tools, prompt=prompt)

        return agent

    def setAgentExecuter(self):
        
        agent_executor = AgentExecutor(
            agent=self.agent, 
            tools=self.tools, 
            memory=ConversationBufferMemory(memory_key=self.memory_key, return_messages=True), 
            verbose=True, 
            handle_parsing_errors=True
        )

        return agent_executor

