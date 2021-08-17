import requests
import random
import sys

api_url = "https://api.imgflip.com/get_memes"
get_joke = requests.get(api_url)
joke_obj = get_joke.json()
joke = joke_obj["data"]["memes"]

def select_random_joke(joke):
    return joke[random.randint(0, len(joke)+1)]["url"]

joke_url = select_random_joke(joke)

print("Hey Justin, Check this out ")
print(joke_url)
# 여기에서 output 정하는 것이다 - git hub action docs에 자세히 나와 있음
print(f"::set-output name=joke::{joke_url}")

