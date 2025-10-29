"""Tnc Framework Core - Telegram Bot Utility Package"""

from .constants import *
from .version import __version__
from .logger import LOG

BANNER = """
╭━━━┳━━━┳━╮╭━┳━━━┳━━━┳━━━┳━━━╮
┃╭━╮┃╭━╮┃┃╰╯┃┃╭━━┫╭━━┫╭━╮┃╭━╮┃
┃╰━━┫┃╱┃┃╭╮╭╮┃╰━━┫╰━━┫╰━╯┃╰━━╮
╰━━╮┃╰━╯┃┃┃┃┃┃╭━━┫╭━━┫╭╮╭┻━━╮┃
┃╰━╯┃╭━╮┃┃┃┃┃┃╰━━┫╰━━┫┃┃╰┫╰━╯┃
╰━━━┻╯╱╰┻╯╰╯╰┻━━━┻━━━┻╯╰━┻━━━╯
        Tnc Force Join Bot v5
"""

LOG.info(BANNER)
LOG.info("✅ Tnc Framework initialized successfully.")
