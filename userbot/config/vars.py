# Configs imports from here

import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from .Config import Config
else:
    if os.path.exists("Config.py"):
        from .Config import Development as Config

# legendbot
