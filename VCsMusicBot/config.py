import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCOu3TV1v3kYsxf60gsGyajwOhQ5-qByTZ92jJCQUr77_riNtzCO6Z2i5bO9t38Ql6xoVJXlAZjjIhXvDmLwCRfaNz_9SVMZYxcdjWmrgq-AaVFxKDrUvYAdF0-HUcFoEqkHNoK5TcYXISaWTa3qEllBR1gk46TX4ceu_JfxBr1MXgPqUgp3pNPc_VtVyO_BTn12Hc-rXqi0w57kp08rzz6YRVsqadGatRJlmP3ckFb-Xk9I6pr6MnbCkEz-178WIGZLENRVSSJlsRVlhq10Qcy4O83SXzyxlW8EVrTM0Nwkgrni6lfauPAHBGyn_QJkYdlnAHTObmu_wxtHXYhlaGAcVyAaQA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GreyWolfXD")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/da1cbc511b2f7237980c5.png")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MirchiAssistant")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "GreyWolfXD")
PROJECT_NAME = getenv("PROJECT_NAME", "MirchiAssiatnt")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/vaibhavchandra13/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
