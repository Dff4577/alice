import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 19612077
API_HASH = "5b66d8462d913e8427339fbbe1bbd3a7"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7377354798:AAEcvF0XatSHU9ArDxeBmMPdCdbww0V4BT4"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://bheemraoambedkar13:bheemraoambedkar13@cluster0.98n5b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002162515059

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7217885929

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/thanos_pro"
SUPPORT_GROUP = "https://t.me/thanosprosss"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQErQa0Ak6xIzSS-m_ll9NHYxw0q1x6Gfw0PQIhO_Qya2mTWKkfqGit5dX7kjyOiJqeoi6Nw4hPVAeQpaJQwF2A0aFpeyiD7kw54w-Z0Qd_wNuNZXHTrZD24Bv2NQSv9yPaHDUHrulD5kUrvt_wKOiTyMam9e8nTpikEDiy33NzZFUdtBpgAtqHawowAuFnD3ZR0OVB2_vZ2ZEdp8HYnQFe2uma7jDaZRvAwHbG9h8mfEUYR10v2CiLsYRPMcdRV2_s1TVipaj3zwMJQxCixy8KzqfmSsogXmTe04ArVwzl7ZVbjwlu7zcMwVKxEEAPfI-N862DUxXp0V6gKauCrCQd9i7QgAAAAGuODLpAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"

PING_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
STATS_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
STREAM_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/aed6856a68696bd4042eb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("https://t.me/cymusicsupport", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("https://t.me/cymusicchat", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
