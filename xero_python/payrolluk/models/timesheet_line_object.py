# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class TimesheetLineObject(BaseModel):
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
        "timesheet_line": "TimesheetLine",
    }

    attribute_map = {
        "pagination": "pagination",
        "problem": "problem",
        "timesheet_line": "timesheetLine",
    }

    def __init__(
        self, pagination=None, problem=None, timesheet_line=None
    ):  # noqa: E501
        """TimesheetLineObject - a model defined in OpenAPI"""  # noqa: E501

        self._pagination = None
        self._problem = None
        self._timesheet_line = None
        self.discriminator = None

        if pagination is not None:
            self.pagination = pagination
        if problem is not None:
            self.problem = problem
        if timesheet_line is not None:
            self.timesheet_line = timesheet_line

    @property
    def pagination(self):
        """Gets the pagination of this TimesheetLineObject.  # noqa: E501


        :return: The pagination of this TimesheetLineObject.  # noqa: E501
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """Sets the pagination of this TimesheetLineObject.


        :param pagination: The pagination of this TimesheetLineObject.  # noqa: E501
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def problem(self):
        """Gets the problem of this TimesheetLineObject.  # noqa: E501


        :return: The problem of this TimesheetLineObject.  # noqa: E501
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this TimesheetLineObject.


        :param problem: The problem of this TimesheetLineObject.  # noqa: E501
        :type: Problem
        """

        self._problem = problem

    @property
    def timesheet_line(self):
        """Gets the timesheet_line of this TimesheetLineObject.  # noqa: E501


        :return: The timesheet_line of this TimesheetLineObject.  # noqa: E501
        :rtype: TimesheetLine
        """
        return self._timesheet_line

    @timesheet_line.setter
    def timesheet_line(self, timesheet_line):
        """Sets the timesheet_line of this TimesheetLineObject.


        :param timesheet_line: The timesheet_line of this TimesheetLineObject.  # noqa: E501
        :type: TimesheetLine
        """

        self._timesheet_line = timesheet_line
