# Third Party
from aws_cdk import Stack
from constructs import Construct

# My Libraries
from cdk import enums, constructs


class MyDNSSECStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str = "my-dnsssec-stack",
        *,
        stack_name: str = "my-dnsssec-stack",
        **kwargs,
    ) -> None:
        env = constructs.MyEnvironment()

        super().__init__(scope, id, env=env, stack_name=stack_name, **kwargs)

        # Add DNSSEC signing to my hosted zone
        constructs.MyDNSSECSigning(
            self, "my-dnssec-signing", hosted_zone_id=enums.HOSTED_ZONE_ID
        )


# class MyApiSubdomainStack(Stack):
#     def __init__(
#         self,
#         scope: Construct,
#         id: str = "my-api-subdomain-stack",
#         *,
#         stack_name: str = "my-api-subdomain-stack",
#         **kwargs,
#     ) -> None:
#         env = constructs.MyEnvironment()

#         super().__init__(scope, id, env=env, stack_name=stack_name, **kwargs)

#         # TODO: do stuff
