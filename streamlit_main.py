import streamlit as st
from GodChatGPT import GodChatGPT

god_chatgpt = GodChatGPT(st.secrets["openai_apikey"],st.secrets["serpapi_apikey"])


# Set page title
st.title("🔥 Wellcome to GOD-ChatGPT 🔥")

# Add an input field
user_input = st.text_input("Play with me:")

# Display the user input
st.write("You entered:", user_input)

result = god_chatgpt.agent_executor({"input": user_input})

print(result)

# Additional interaction with the input (example: converting input to uppercase)
st.write("🔥 GOD-ChatGPT Answer: ", result['output'])