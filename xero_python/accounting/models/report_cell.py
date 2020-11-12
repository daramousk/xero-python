# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ReportCell(BaseModel):
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
    openapi_types = {"value": "str", "attributes": "list[ReportAttribute]"}

    attribute_map = {"value": "Value", "attributes": "Attributes"}

    def __init__(self, value=None, attributes=None):  # noqa: E501
        """ReportCell - a model defined in OpenAPI"""  # noqa: E501

        self._value = None
        self._attributes = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if attributes is not None:
            self.attributes = attributes

    @property
    def value(self):
        """Gets the value of this ReportCell.  # noqa: E501


        :return: The value of this ReportCell.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ReportCell.


        :param value: The value of this ReportCell.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def attributes(self):
        """Gets the attributes of this ReportCell.  # noqa: E501


        :return: The attributes of this ReportCell.  # noqa: E501
        :rtype: list[ReportAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ReportCell.


        :param attributes: The attributes of this ReportCell.  # noqa: E501
        :type: list[ReportAttribute]
        """

        self._attributes = attributes
