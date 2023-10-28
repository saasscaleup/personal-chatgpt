import os
import sys
import requests
import env
from bs4 import BeautifulSoup

from langchain.tools import Tool, DuckDuckGoSearchResults
from langchain.utilities import SerpAPIWrapper
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.agents import initialize_agent, AgentType


os.environ["OPENAI_API_KEY"] = env.OPENAI_APIKEY
os.environ["SERPAPI_API_KEY"] = env.SERPAPI_APIKEY

# Setting Up the DuckDuckGo Search Tool
ddg_search = DuckDuckGoSearchResults()

search = SerpAPIWrapper()

serpapi_tool = Tool(
    name="Search",
    func=search.run,
    description="useful for when you need to answer questions about current events",
)

# Defining Headers for Web Requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'
}

"""
In this section, we're setting two functions to fetch and grab any url content 
"""

# Parsing HTML Content
def parse_html(content) -> str:
    soup = BeautifulSoup(content, 'html.parser')
    text_content_with_links = soup.get_text()
    return text_content_with_links

# Fetching Web Page Content
def fetch_web_page(url: str) -> str:
    response = requests.get(url, headers=HEADERS)
    return parse_html(response.content)


"""
In this section, we're generating a new tool utilizing the Tool.from_function approach. 
This particular tool will employ our fetch_web_page function to retrieve and process web pages.
"""

# Creating the Web Fetcher Tool
web_fetch_tool = Tool.from_function(
    func=fetch_web_page,
    name="WebFetcher",
    description="Fetches the content of a web page"
)

# Setting Up the Summarizer
prompt_template = "Summarize the following content: {content}"
llm = ChatOpenAI(model="gpt-3.5-turbo-16k")


"""
This section sets up a summarizer using the ChatOpenAI model from LangChain. 
We define a prompt template for summarization, create a chain using the model and the prompt, 
and then define a tool for summarization. 
We use ChatGPT 3.5 16k context as most web pages will exceed the 4k context of ChatGPT 3.5.
"""

llm_chain = LLMChain(
    llm=llm,
    prompt=PromptTemplate.from_template(prompt_template)
)

summarize_tool = Tool.from_function(
    func=llm_chain.run,
    name="Summarizer",
    description="Summarizes a web page"
)

"""
In this section, we're initiating an agent equipped with the tools we've established. 
This agent will possess the capability to explore the web, retrieve web pages, and generate summaries. 
It's worth noting the versatility in utilizing the LLM from the summarization tool for various tasks.

"""
# Initializing the Agent
tools = [serpapi_tool, web_fetch_tool, summarize_tool]

agent = initialize_agent(
    tools=tools,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    llm=llm,
    verbose=True,
    handle_parsing_errors=True
)

prompt = None
post_prompt = ". Use your tools to search and summarize content"

if len(sys.argv) > 1:
    prompt = sys.argv[1]


"""
Lastly, we formulate a prompt for our agent and set it in motion. 
The agent will conduct a web search for details regarding the Python's Requests Library, 
retrieve a portion of the content, and proceed to generate a summary.
"""

while True:
    if not prompt:
        prompt = input("\033[31m\r\nPrompt: \033[0m")
    if prompt in ['quit', 'q', 'exit']:
        sys.exit()

    prompt = prompt+" "+post_prompt
    print(agent.run(prompt))
    prompt = None

# print(agent.run(prompt))
