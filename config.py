from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25405777")
    API_HASH = environ.get("API_HASH", "6bff46327fffc7e03fa30a1ed19c5ce0")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7660152059:AAG8QTAtSdMEQ6QRiTkuK2VRFHs0XLlconM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://fibegi:8oV4fjNNVasSfcoY@cluster0.jp8thup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '8007695130').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
