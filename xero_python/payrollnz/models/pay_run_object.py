# coding: utf-8

"""
    Xero Payroll NZ

    This is the Xero Payroll API for orgs in the NZ region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayRunObject(BaseModel):
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
    openapi_types = {
        "pagination": "Pagination",
        "problem": "Problem",
        "pay_run": "PayRun",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "pay_run": "payRun",
    }

    def __init__(self, pagination=None, problem=None, pay_run=None):  # noqa: E501
        """PayRunObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._pay_run = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if pay_run is not None:
            self.pay_run = pay_run

    @property
    def pagination(self):
        """Gets the pagination of this PayRunObject.  # noqa: E501


        :return: The pagination of this PayRunObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this PayRunObject.


        :param pagination: The pagination of this PayRunObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this PayRunObject.  # noqa: E501


        :return: The problem of this PayRunObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this PayRunObject.


        :param problem: The problem of this PayRunObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def pay_run(self):
        """Gets the pay_run of this PayRunObject.  # noqa: E501


        :return: The pay_run of this PayRunObject.  # noqa: E501
        :rtype: PayRun
        """
        return self._pay_run

    @pay_run.setter
    def pay_run(self, pay_run):
        """Sets the pay_run of this PayRunObject.


        :param pay_run: The pay_run of this PayRunObject.  # noqa: E501
        :type: PayRun
        """

        self._pay_run = pay_run
