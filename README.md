# personal-chatgpt
Personal ChatGPT Allow you to enhance the Power of ChatGPT with your PERSONAL DATA using LangChain

Here's the [YouTube Video](https://youtu.be/ROsb_73EpzE).

<a href="https://www.buymeacoffee.com/scaleupsaas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=scaleupsaas&button_colour=BD5FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>


## Installation

Follow next steps in order to obtain the power of Personal-ChatGPT

### Step 1 - Git clone

```
git clone https://github.com/saasscaleup/personal-chatgpt.git
```

### Step 2 - Install required packages.

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip3 install langchain openai chromadb tiktoken unstructured requests duckduckgo-search google-search-results
```

### Step 3 - Update OpenAI API Key


Modify `env.py.copy` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `env.py`.

### Step 4 - Place your own personal DATA

Place your own data into `data/data.txt` or `data/`.


## Example usage

### Example of personal-gpt
Test reading `data/My Youtube tutorials.pdf` file.

```
> python personal-gpt.py "Which youtube video will help me to learn how to develop telegram bot with laravel"
The YouTube video titled "Let’s Build a Telegram Bot AI with Laravel 10 and AWS Lambda | Laravel Tutorial"
will help you learn how to develop a Telegram bot with Laravel. Here is the video link: https://youtu.be/4KKAX8ZYTbk
```

Test reading `data/data.txt` file.

```
> python chatgpt.py "what plans I have for 25 to October?"
Your plan for October 25th is to upload a new YouTube video.
```

### Example of research-agent

Test Researching "Research about the top 5 stock to invest now." 

```
> python research-agent.py "Research about the top 5 stock to invest now."

According to Bank of America's list of best stocks to buy now, the top 5 stocks to invest in are
Boeing (BA), CSX (CSX), Five Below (FIVE), Kraft Heinz (KHC), and Occidental Petroleum (OXY). 
These stocks have been selected based on their potential for growth and positive catalysts. 
However, it is important to conduct further research and analysis before making any investment decisions.
```


## Support 🙏😃
  
 If you Like the tutorial and you want to support my channel so I will keep releasing amzing content that will turn you to a desirable Developer with Amazing Cloud skills... I will realy appricite if you:
 
 1. Subscribe to My youtube channel and leave a comment: http://www.youtube.com/@ScaleUpSaaS?sub_confirmation=1
 2. Buy me A coffee ❤️ : https://www.buymeacoffee.com/scaleupsaas

Thanks for your support :)

<a href="https://www.buymeacoffee.com/scaleupsaas"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=scaleupsaas&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>

