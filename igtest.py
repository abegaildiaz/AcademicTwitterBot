from instabot import Bot
import random 
kphrases = ["Check out our latest paper:", "We just published a new paper, take a look!", 
            "Explore our newest paper!", "Read our newest published paper here: ", 
            "Looking for a new read? We just published a new paper!", "Take a look at our newest published paper!"]
phrase = random.choice(kphrases) 

cap = phrase
bot = Bot()
bot.login(username = "moulegroup", password = "pw")
bot.upload_photo("pic.jpeg", caption = cap)
