# Standard Library
from os import getenv

# Third Party
from aws_cdk import Environment, RemovalPolicy, aws_route53 as route53
from constructs import Construct


class MyEnvironment(Environment):
    def __init__(self, *, account: str = None, region: str = None) -> None:
        account = getenv("AWS_ACCOUNT_ID") if not account else account
        region = getenv("AWS_DEFAULT_REGION") if not region else region
        super().__init__(account=account, region=region)


class MyHostedZone:
    @classmethod
    def make(
        cls, scope: Construct, id: str, hosted_zone_id: str, zone_name: str
    ) -> route53.HostedZone:
        return route53.HostedZone.from_hosted_zone_attributes(
            scope, id, hosted_zone_id=hosted_zone_id, zone_name=zone_name
        )


class MyDNSSECSigning(route53.CfnDNSSEC):
    def __init__(
        self,
        scope: Construct,
        id: str,
        hosted_zone_id: str,
    ) -> None:
        super().__init__(scope, id, hosted_zone_id=hosted_zone_id)
        self.apply_removal_policy(RemovalPolicy.DESTROY)
