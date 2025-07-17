# Standard Library
from os import getenv
from enum import Enum
from typing import List, Optional

# Static
AWS_ACCOUNT_ID = getenv("AWS_ACCOUNT_ID")
AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
HOSTED_ZONE_ID = getenv("HOSTED_ZONE_ID")
CHAINOFTRUST_DS_RECORD = getenv("CHAINOFTRUST_DS_RECORD")


# Enums
class BaseEnum(Enum):
    @classmethod
    def values(cls) -> Optional[List[str]]:
        result = []
        for item in cls:
            result.append(item.value)
        return result


class MyDomainName(Enum):
    domain_name = "chadbartel.com"


class CDKStackRegion(Enum):
    region = getenv("AWS_REGION", "us-west-2")


# Data classes
