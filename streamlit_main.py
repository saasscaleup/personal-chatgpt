import streamlit as st
from GodChatGPT import GodChatGPT

@st.cache_resource  # 👈 Add the caching decorator
def load_god_chatgpt():
    god_chatgpt = GodChatGPT(st.secrets["openai_apikey"],st.secrets["serpapi_apikey"])
    return god_chatgpt

if 'user_input' not in st.session_state:
    st.session_state.user_input = ''

def submit():
    st.session_state.user_input = st.session_state.query
    st.session_state.query = ''

god_chatgpt = load_god_chatgpt();

# Set page title
st.title("🔥 Wellcome to GOD-ChatGPT 🔥")

st.text_input("Play with me:",key='query', on_change=submit)

user_input = st.session_state.user_input
# Display the user input
st.write("You entered:", user_input)

if user_input:
    result = god_chatgpt.agent_executor({"input": user_input})
    print(result)

    # Additional interaction with the input 
    st.write("🔥 GOD-ChatGPT Answer: ", result['output'])
