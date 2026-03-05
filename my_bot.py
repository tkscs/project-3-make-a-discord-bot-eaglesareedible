from my_secrets import *
import time
import numpy
import string
import random
"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
results = ["🍒", "7", "🍇", "🍓", "🍊", "🍷"]

def slots():
  slotspot1 = random.choice(results)
  slotspot2 = random.choice(results)
  slotspot3 = random.choice(results)
  return f"{slotspot1}, {slotspot2}, {slotspot3}"

def coinflip():
  headsTails=random.randint(1, 2)
  if headsTails==1:
    return "Heads"
  if headsTails==2:
    return "Tails"
  
currenttime=time.asctime(time.localtime())
userInput=["bad", "no", "hello", "yes", "what is dodos name", "how are you", 'what can you do', 'keo', "what time is it", "coinflip", "slotmachine"]
botResponse=["That's bad!", "Aww, that's a shame", "Hi! I'm here.","Agreed","Dodo's name is Ido Tsoref. Google it!", "I'm good, how are you?","I can say hi when you say my name, or Keo's name, I can let you know how I'm doing, and I can tell you what time it is! And I can flip a coin", "haha, keo", f"{currenttime}", f"{coinflip()}", f"{slots()}"]

ALPA = string.ascii_lowercase + " "

def should_i_respond(user_message, user_name):
  whitelisteed_user_message=""
  editeduser_message=user_message.lower()
  for char in editeduser_message:
    if(char in ALPA):
        whitelisteed_user_message += char
  for i in userInput:
    if f"{i}" in whitelisteed_user_message:
      return True
  return False
 
#Do NOT change the name of this function.


def respond(user_message, user_name):
  currenttime=time.asctime(time.localtime())
  botResponse=["That's bad!", "Aww, that's a shame", "Hi! I'm here.","Agreed","Dodo's name is Ido Tsoref. Google it!", "I'm good, how are you?","I can say hi when you say my name, or Keo's name, I can let you know how I'm doing, and I can tell you what time it is! And I can flip a coin", "haha, keo", f"{currenttime}", f"{coinflip()}"]
  whitelisteed_user_message=""
  editeduser_message=user_message.lower()
  for char in editeduser_message:
    if(char in ALPA):
        whitelisteed_user_message += char
  var = userInput.index(whitelisteed_user_message)
  return f"{botResponse[var]}"""
  {user_message.replace("robot", user_name)}




