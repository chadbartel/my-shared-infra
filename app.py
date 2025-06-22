#!/usr/bin/env python
# Standard Library
from os import getenv

# Third Party
from aws_cdk import App

if getenv("IS_LOCAL") == "true":
    # Try to load .env
    try:
        # Third Party
        from dotenv import load_dotenv

        load_dotenv()
    except ImportError as e:
        print("Error -> ", e)

# My Libraries
from cdk import stacks

# Initialize application
app = App()

# Create stacks
stacks.MyDNSSECStack(app)

# Synthesize application stack
app.synth()
