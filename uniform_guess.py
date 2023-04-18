import os
import random
os.environ['OPENAI_API_KEY'] = open("api_key").read()

from chatgpt_wrapper import OpenAIAPI
from chatgpt_wrapper.core.config import Config

config = Config()
config.set('chat.model', 'gpt4')
bot = OpenAIAPI(config, default_user_id=1)

from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

user_input = "Let's play a game, you choose a number between 1 and 100 and I guess it. Don't give me any hint at all. Just answer with Yes or No."
print(user_input)
success, response, message = bot.ask(user_input)

l = list(range(1, 101))
random.shuffle(l)

for i, number in enumerate(l):
    if success:
        print(response)
        if sentiment_pipeline(response)[0]['label']=='POSITIVE' and i!=0:
            print("success")
            print(i)
            break
        current_user_input = f"Is it {number}?"
        print(current_user_input)
        success, response, message = bot.ask(current_user_input)
    else:
        raise RuntimeError(message)