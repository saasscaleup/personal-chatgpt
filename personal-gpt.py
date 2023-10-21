import os
import sys

import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader, WebBaseLoader
from langchain.indexes import VectorstoreIndexCreator

import env

os.environ["OPENAI_API_KEY"] = env.APIKEY

query = None

if len(sys.argv) > 1:
  query = sys.argv[1]

#loader = TextLoader("data/data.txt") # Use this line if you only need data.txt
loader_dic = DirectoryLoader("data/")
#loader_web = WebBaseLoader(["https://aws.amazon.com/getting-started/hands-on/setting-up-a-redis-cluster-with-amazon-elasticache/?ref=gsrchandson"])

index = VectorstoreIndexCreator().from_loaders([loader_dic])

chain = ConversationalRetrievalChain.from_llm(
  llm=ChatOpenAI(model="gpt-3.5-turbo"),
  retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

chat_history = []

while True:
  if not query:
    query = input("\033[31m\r\nPrompt: \033[0m")
  if query in ['quit', 'q', 'exit']:
    sys.exit()
  result = chain({"question": query, "chat_history": chat_history})
  print("\033[32m"+result['answer']+"\033[0m")


  chat_history.append((query, result['answer']))
  query = None
