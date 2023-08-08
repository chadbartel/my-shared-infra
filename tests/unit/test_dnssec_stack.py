# Third Party
import aws_cdk as core
import aws_cdk.assertions as assertions

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
        )
    )

# def test_kms_key_created():
#     app = core.App()
#     stack = MyStack(app)
#     template = assertions.Template.from_stack(stack)
#     template.has_resource("AWS::KMS::Key", assertions.Match.any_value())

# def test_resource_policy_created():
#     app = core.App()
#     stack = MyStack(app)
#     template = assertions.Template.from_stack(stack)
#     template.has_resource("AWS::Route53::KeySigningKey", assertions.Match.any_value())
