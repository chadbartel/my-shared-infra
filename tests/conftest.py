#!/usr/bin/env python
from os import getenv

if getenv("IS_LOCAL") == "true":
    # Try to load .env
    try:
        # Third Party
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError as e:
        print("Error -> ", e)
