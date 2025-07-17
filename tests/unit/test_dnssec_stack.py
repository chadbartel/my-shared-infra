# Third Party
import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk import aws_kms as kms

# My Libraries
from cdk import enums
from cdk.stacks import MyDNSSECStack as MyStack


def test_dnssec_service_created():
    app = core.App()
    stack = MyStack(app)
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::Route53::DNSSEC",
        assertions.Match.object_like(
            {
                "HostedZoneId": enums.HOSTED_ZONE_ID,
            },
        ),
    )


def test_kms_key_created():
    app = core.App()
    stack = MyStack(app)
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::KMS::Key",
        assertions.Match.object_like(
            {
                "EnableKeyRotation": False,
                "KeySpec": kms.KeySpec.ECC_NIST_P256,
                "KeyUsage": kms.KeyUsage.SIGN_VERIFY,
            }
        ),
    )


def test_key_alias_created():
    app = core.App()
    stack = MyStack(app)
    template = assertions.Template.from_stack(stack)
    template.has_resource_properties(
        "AWS::KMS::Alias",
        assertions.Match.object_like(
            {
                "AliasName": "alias/chadbartel-dnssec-signing-key",
            }
        ),
    )


def test_signing_key_created():
    app = core.App()
    stack = MyStack(app)
    template = assertions.Template.from_stack(stack)
    template.has_resource(
        "AWS::Route53::KeySigningKey",
        assertions.Match.object_like(
            {
                "Properties": {
                    "Name": "chadbartelDNSSECKSK",
                    "HostedZoneId": enums.HOSTED_ZONE_ID,
                    "Status": "ACTIVE",
                    "KeyManagementServiceArn": assertions.Match.any_value(),
                }
            }
        ),
    )


def test_ds_record_created():
    app = core.App()
    stack = MyStack(app)
    template = assertions.Template.from_stack(stack)
    template.has_resource(
        "AWS::Route53::RecordSet",
        assertions.Match.object_like(
            {
                "Properties": {
                    "HostedZoneId": enums.HOSTED_ZONE_ID,
                    "Name": "*.chadbartel.com.",
                    "TTL": "3600",
                    "Type": "DS",
                }
            }
        )
    )
