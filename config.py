from os import environ

API_HASH = environ.get("API_HASH", "146fcf83a1670e2e926ce874ce31fcb3")
API_ID = int(environ.get("API_ID", "29762406"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7852033838:AAEjvbXsgvFQHrhZOIz3TEjWqsKr_9MFknI")
BOT_OWNER = int(environ.get("BOT_OWNER", "6670233911"))
BOT_USERNAME = environ.get("BOT_USERNAME", "utmapbot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002465408399"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002271972643"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://nguyenkhactam5:q1231234@kanereaction.zhqqd.mongodb.net/?retryWrites=true&w=majority&appName=kanereaction")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🥇", "🎉", "🕊️", "🆑", "🥳", "🏧", "🚀", "😛", "😻", "🕊️", "🦸", "💫",
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏",
]
