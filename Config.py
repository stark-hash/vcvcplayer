import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18329555"))
    API_HASH = os.environ.get("API_HASH", "7bf83fddf8244fddfb270701e31470a8)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5466262768:AAGoFgMBRYyvetpS6Te65HIwVwx00TMqRRo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKYBux2BKWKgXxcwFeYtJ6GksBE5r978r15tcYvHnvQKmHkcgMA7cBtA2DXC3mzruNjenrW7-9eZjQbSpWO38BgEIw8VOMo4qyYjt56_kHlBX68WARuysXqJFHzTpEYFfhlLYs-pKqi3_KVuFqOPkYVYCX1257gjITDk-lx0_s2qaeP4WHw7cn2C82Xy1mbmKBbxb-dlAltquwmCK66kOMy3ga_x8q3H-RUHOX9Z7SBxITBhLC7tfoB3JuU8bHvKMrkjnpxLHzEJOhAopN6h7hwHVd0RlRqayHeoyg4Yz5yGL2D0EmySD2bye0UrbucbVZxO6f8EVY3geF79r9ZuJUkhOVE=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "FDVCPlayer")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "2114860856"))
