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


class DeductionObject(BaseModel):
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
        "deduction": "Deduction",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "deduction": "deduction",
    }

    def __init__(self, pagination=None, problem=None, deduction=None):  # noqa: E501
        """DeductionObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._deduction = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if deduction is not None:
            self.deduction = deduction

    @property
    def pagination(self):
        """Gets the pagination of this DeductionObject.  # noqa: E501


        :return: The pagination of this DeductionObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this DeductionObject.


        :param pagination: The pagination of this DeductionObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this DeductionObject.  # noqa: E501


        :return: The problem of this DeductionObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this DeductionObject.


        :param problem: The problem of this DeductionObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def deduction(self):
        """Gets the deduction of this DeductionObject.  # noqa: E501


        :return: The deduction of this DeductionObject.  # noqa: E501
        :rtype: Deduction
        """
        return self._deduction

    @deduction.setter
    def deduction(self, deduction):
        """Sets the deduction of this DeductionObject.


        :param deduction: The deduction of this DeductionObject.  # noqa: E501
        :type: Deduction
        """

        self._deduction = deduction
