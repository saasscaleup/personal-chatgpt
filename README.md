# personal-chatgpt
Personal ChatGPT Allow you to enhance the Power of ChatGPT with your PERSONAL DATA using LangChain

Here's the [YouTube Video](https://youtu.be/).

## Installation

```
git clone (saasscaleup/personal-chatgpt)
```

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```

Modify `env.py.copy` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `env.py`.

Place your own data into `data/data.txt` or `data/`.

## Example usage
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
