class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7147738922"
    sudo_users = "7147738922", "6574393060" , "5607512615"
    GROUP_ID = -1002188991477
    TOKEN = "7411570597:AAFJ33Kh-6xr4_28p8CDz78Nw6GSP7mQlnU"
    mongo_url = "mongodb+srv://bak01072007:bak123456@waifu2.5ahbyyu.mongodb.net/"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "-1002167888245"
    UPDATE_CHAT = ""
    BOT_USERNAME = "Godshiv_bot"
    CHARA_CHANNEL_ID = "-1002133191051"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
