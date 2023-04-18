from chatgpt_wrapper.core.config import Config
import random
from chatgpt_wrapper import OpenAIAPI
import os

os.environ['OPENAI_API_KEY'] = open("api_key").read()


def random_guess(start, end):
    l = list(range(start, end + 1))
    random.shuffle(l)
    success = True
    response = ""
    for i, number in enumerate(l):
        if success:
            print(response)
            if "yes" in response or sentiment_pipeline(response)[0]['label'] == 'POSITIVE' and i != 0:
                print("success")
                print(i)
                break
            current_user_input = f"Is it {number}?"
            print(current_user_input)
            success, response, message = bot.ask(current_user_input)
        else:
            raise RuntimeError(message)


config = Config()
config.set('chat.model', 'gpt4')
bot = OpenAIAPI(config, default_user_id=1)

from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

user_input = "Let's play a game, you choose a number between 1 and 100 and I guess it. Don't give me any hint at all. Just answer with Yes or No."

print(user_input)
success, response, message = bot.ask(user_input)
print(response)
current_user_input = "Is it bigger than 50?"
print(current_user_input)
success, response, message = bot.ask(current_user_input)
print(response)
if sentiment_pipeline(response)[0]['label'] == 'POSITIVE':  # bigger than 50
    current_user_input = "Is it smaller than 75?"
    print(current_user_input)
    success, response, message = bot.ask(current_user_input)
    print(response)
    if sentiment_pipeline(response)[0]['label'] == 'POSITIVE':  # bigger than 50 and smaller than 75
        random_guess(51, 74)
    else:
        random_guess(75, 100)

else:  # smaller than 50
    current_user_input = "Is it bigger than 25?"
    print(current_user_input)
    success, response, message = bot.ask(current_user_input)
    print(response)
    if sentiment_pipeline(response)[0]['label'] == 'POSITIVE':  # smaller than 50 and bigger than 25
        random_guess(26, 50)
    else:
        random_guess(1, 25)
