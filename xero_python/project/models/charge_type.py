# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class ChargeType(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    TIME = "TIME"
    FIXED = "FIXED"
    NON_CHARGEABLE = "NON_CHARGEABLE"
