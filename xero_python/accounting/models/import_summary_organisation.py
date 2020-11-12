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


class ImportSummaryOrganisation(BaseModel):
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
    openapi_types = {"present": "bool"}

    attribute_map = {"present": "Present"}

    def __init__(self, present=None):  # noqa: E501
        """ImportSummaryOrganisation - a model defined in OpenAPI"""  # noqa: E501

        self._present = None
        self.discriminator = None

        if present is not None:
            self.present = present

    @property
    def present(self):
        """Gets the present of this ImportSummaryOrganisation.  # noqa: E501


        :return: The present of this ImportSummaryOrganisation.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this ImportSummaryOrganisation.


        :param present: The present of this ImportSummaryOrganisation.  # noqa: E501
        :type: bool
        """

        self._present = present
