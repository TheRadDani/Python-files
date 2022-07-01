from instabot import Bot
bot = Bot()
bot.login(username="ldaniel_ferreto",password="Humanoide2000!")
#bot.upload_photo("luna.jpg",caption="cute baby <3")
# bot.follow("elonmuskk")
followers = bot.get_user_followers("dhavalsays")
for follower in followers:
    print(bot.get_user_info(follower))