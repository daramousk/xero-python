# coding: utf-8

"""
    Xero Payroll AU

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayrollCalendars(BaseModel):
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
    openapi_types = {"payroll_calendars": "list[PayrollCalendar]"}

    attribute_map = {"payroll_calendars": "PayrollCalendars"}

    def __init__(self, payroll_calendars=None):  # noqa: E501
        """PayrollCalendars - a model defined in OpenAPI"""  # noqa: E501

        self._payroll_calendars = None
        self.discriminator = None

        if payroll_calendars is not None:
            self.payroll_calendars = payroll_calendars

    @property
    def payroll_calendars(self):
        """Gets the payroll_calendars of this PayrollCalendars.  # noqa: E501


        :return: The payroll_calendars of this PayrollCalendars.  # noqa: E501
        :rtype: list[PayrollCalendar]
        """
        return self._payroll_calendars

    @payroll_calendars.setter
    def payroll_calendars(self, payroll_calendars):
        """Sets the payroll_calendars of this PayrollCalendars.


        :param payroll_calendars: The payroll_calendars of this PayrollCalendars.  # noqa: E501
        :type: list[PayrollCalendar]
        """

        self._payroll_calendars = payroll_calendars
