from my_secrets import *
import time

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "robot" in user_message:
    return True
  else:
    return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  return f"""you said my name!!
  {user_message.replace("robot", user_name)}"""

userInput=["bad", "no", "hello", "yes", "what is dodo's name", "how are you", 'what can you do', 'keo']
botResponse=["That's bad!", "Aww, that's a shame", "Hi! I'm here.","Agreed","Dodo's name is Ido Tsoref. Google it!", "I'm good, how are you?","I can say hi when you say my name, or Keo's name, I can let you know how I'm doing, and I can tell you wha time it is!", "haha, keo"]

