import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "28620686"))
    API_HASH = os.environ.get("API_HASH", "684bafe87b27ac3723884d2bb6ea03e0")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7731194758:AAE-Ft35AwRz3u351SF7Llar2BZOf5OmlOo")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "mahi_1357_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
