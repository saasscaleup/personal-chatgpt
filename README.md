# personal-chatgpt -> Streamlit Branch
Personal ChatGPT (Streamlit Branch) Allow you to run on your browser the Power of ChatGPT with your PERSONAL DATA, Intenrnet Access and Memory using LangChain and Streamlit

Here's the [YouTube Video](https://youtu.be/us1l14STMX4).

<a href="https://www.buymeacoffee.com/scaleupsaas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=scaleupsaas&button_colour=BD5FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>

## Installation

Follow next steps in order to obtain the power of Personal-ChatGPT - Streamlit branch

### Step 1 - Git clone

```
git clone https://github.com/saasscaleup/personal-chatgpt.git god-chatgpt-streamlit
```

### Step 1 - Git checkout streamlit

```
cd god-chatgpt-streamlit
```
```
git checkout streamlit
```

### Step 2 - Install required packages.

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured requests duckduckgo-search google-search-results
```

Install [Streamlit](https://docs.streamlit.io/) packages.
```
pip install streamlit
```

### Step 3 - Update OpenAI API Key

Modify `/.strreamlit/secrets.toml.copy` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys) and [SerpAPI-Google Search](https://serpapi.com/users/welcome) and 
rename it to `/.strreamlit/secrets.toml`.

```
openai_apikey = ""
serpapi_apikey = ""
```

### Step 4 - Place your own personal DATA

Place your own data into `data/data.txt` or `data/`.


## Run God-ChatGPT Streamlit locally

```
streamlit run streamlit_main.py
```

## Support 🙏😃
  
 If you Like the tutorial and you want to support my channel so I will keep releasing amzing content that will turn you to a desirable Developer with Amazing Cloud skills... I will realy appricite if you:
 
 1. Subscribe to My youtube channel and leave a comment: http://www.youtube.com/@ScaleUpSaaS?sub_confirmation=1
 2. Buy me A coffee ❤️ : https://www.buymeacoffee.com/scaleupsaas

Thanks for your support :)

<a href="https://www.buymeacoffee.com/scaleupsaas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=scaleupsaas&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

