#!/usr/bin/env python
# Standard Library
from os import getenv

# Third Party
from aws_cdk import App, Environment

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

# Define the AWS environment for the certificate stack
cert_env = Environment(
    account=getenv("CDK_DEFAULT_ACCOUNT"),
    region="us-east-1",  # ACM certificates must be in us-east-1 for CloudFront
)

# Determine stack suffix from context variable (passed by CI/CD or default to 'Dev')
# This allows for unique stack names per feature branch
stack_suffix = app.node.try_get_context("stack-suffix")
formatted_stack_suffix = f"-{stack_suffix}" if stack_suffix else ""

# Create stacks
stacks.MyDNSSECStack(app)

# Create certificate stack
stacks.MyDnsCertificateStack(
    app,
    "MyDnsCertificateStack",
    domain_name=app.node.try_get_context("domain-name"),
    env=cert_env,
    stack_suffix=formatted_stack_suffix,
    cross_region_references=True,  # Allow cross-region references for the certificate
)

# Synthesize application stack
app.synth()
