import os

SECRET_KEY = os.environ.get("SECRET_KEY")

# 🔥 CHANGE BOT HERE ONLY (or via Render ENV)
ACTIVE_BOT_URL = os.environ.get(
    "ACTIVE_BOT_URL",
    "https://t.me/YourMainVideoBot"
)
