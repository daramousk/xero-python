# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from enum import Enum


class TaxCode(Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    allowed enum values
    """

    ND = "ND"
    M = "M"
    ME = "ME"
    MSL = "MSL"
    MESL = "MESL"
    SB = "SB"
    S = "S"
    SH = "SH"
    ST = "ST"
    SBSL = "SBSL"
    SSL = "SSL"
    SHSL = "SHSL"
    STSL = "STSL"
    WT = "WT"
    CAE = "CAE"
    EDW = "EDW"
    NSW = "NSW"
    STC = "STC"
    STCSL = "STCSL"
