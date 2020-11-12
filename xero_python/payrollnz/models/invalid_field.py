# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class InvalidField(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"name": "str", "reason": "str"}

    attribute_map = {"name": "name", "reason": "reason"}

    def __init__(self, name=None, reason=None):  # noqa: E501
        """InvalidField - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._reason = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if reason is not None:
            self.reason = reason

    @property
    def name(self):
        """Gets the name of this InvalidField.  # noqa: E501

        The name of the field that caused the error  # noqa: E501

        :return: The name of this InvalidField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvalidField.

        The name of the field that caused the error  # noqa: E501

        :param name: The name of this InvalidField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def reason(self):
        """Gets the reason of this InvalidField.  # noqa: E501

        The reason the error occurred  # noqa: E501

        :return: The reason of this InvalidField.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InvalidField.

        The reason the error occurred  # noqa: E501

        :param reason: The reason of this InvalidField.  # noqa: E501
        :type: str
        """

        self._reason = reason
