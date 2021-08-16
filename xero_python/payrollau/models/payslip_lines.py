# coding: utf-8

"""
    Xero Payroll AU API

    This is the Xero Payroll API for orgs in Australia region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class PayslipLines(BaseModel):
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
        "earnings_lines": "list[EarningsLine]",
        "leave_earnings_lines": "list[LeaveEarningsLine]",
        "timesheet_earnings_lines": "list[EarningsLine]",
        "deduction_lines": "list[DeductionLine]",
        "leave_accrual_lines": "list[LeaveAccrualLine]",
        "reimbursement_lines": "list[ReimbursementLine]",
        "superannuation_lines": "list[SuperannuationLine]",
        "tax_lines": "list[TaxLine]",
    }

    attribute_map = {
        "earnings_lines": "EarningsLines",
        "leave_earnings_lines": "LeaveEarningsLines",
        "timesheet_earnings_lines": "TimesheetEarningsLines",
        "deduction_lines": "DeductionLines",
        "leave_accrual_lines": "LeaveAccrualLines",
        "reimbursement_lines": "ReimbursementLines",
        "superannuation_lines": "SuperannuationLines",
        "tax_lines": "TaxLines",
    }

    def __init__(
        self,
        earnings_lines=None,
        leave_earnings_lines=None,
        timesheet_earnings_lines=None,
        deduction_lines=None,
        leave_accrual_lines=None,
        reimbursement_lines=None,
        superannuation_lines=None,
        tax_lines=None,
    ):  # noqa: E501
        """PayslipLines - a model defined in OpenAPI"""  # noqa: E501

        self._earnings_lines = None
        self._leave_earnings_lines = None
        self._timesheet_earnings_lines = None
        self._deduction_lines = None
        self._leave_accrual_lines = None
        self._reimbursement_lines = None
        self._superannuation_lines = None
        self._tax_lines = None
        self.discriminator = None

        if earnings_lines is not None:
            self.earnings_lines = earnings_lines
        if leave_earnings_lines is not None:
            self.leave_earnings_lines = leave_earnings_lines
        if timesheet_earnings_lines is not None:
            self.timesheet_earnings_lines = timesheet_earnings_lines
        if deduction_lines is not None:
            self.deduction_lines = deduction_lines
        if leave_accrual_lines is not None:
            self.leave_accrual_lines = leave_accrual_lines
        if reimbursement_lines is not None:
            self.reimbursement_lines = reimbursement_lines
        if superannuation_lines is not None:
            self.superannuation_lines = superannuation_lines
        if tax_lines is not None:
            self.tax_lines = tax_lines

    @property
    def earnings_lines(self):
        """Gets the earnings_lines of this PayslipLines.  # noqa: E501


        :return: The earnings_lines of this PayslipLines.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._earnings_lines

    @earnings_lines.setter
    def earnings_lines(self, earnings_lines):
        """Sets the earnings_lines of this PayslipLines.


        :param earnings_lines: The earnings_lines of this PayslipLines.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._earnings_lines = earnings_lines

    @property
    def leave_earnings_lines(self):
        """Gets the leave_earnings_lines of this PayslipLines.  # noqa: E501


        :return: The leave_earnings_lines of this PayslipLines.  # noqa: E501
        :rtype: list[LeaveEarningsLine]
        """
        return self._leave_earnings_lines

    @leave_earnings_lines.setter
    def leave_earnings_lines(self, leave_earnings_lines):
        """Sets the leave_earnings_lines of this PayslipLines.


        :param leave_earnings_lines: The leave_earnings_lines of this PayslipLines.  # noqa: E501
        :type: list[LeaveEarningsLine]
        """

        self._leave_earnings_lines = leave_earnings_lines

    @property
    def timesheet_earnings_lines(self):
        """Gets the timesheet_earnings_lines of this PayslipLines.  # noqa: E501


        :return: The timesheet_earnings_lines of this PayslipLines.  # noqa: E501
        :rtype: list[EarningsLine]
        """
        return self._timesheet_earnings_lines

    @timesheet_earnings_lines.setter
    def timesheet_earnings_lines(self, timesheet_earnings_lines):
        """Sets the timesheet_earnings_lines of this PayslipLines.


        :param timesheet_earnings_lines: The timesheet_earnings_lines of this PayslipLines.  # noqa: E501
        :type: list[EarningsLine]
        """

        self._timesheet_earnings_lines = timesheet_earnings_lines

    @property
    def deduction_lines(self):
        """Gets the deduction_lines of this PayslipLines.  # noqa: E501


        :return: The deduction_lines of this PayslipLines.  # noqa: E501
        :rtype: list[DeductionLine]
        """
        return self._deduction_lines

    @deduction_lines.setter
    def deduction_lines(self, deduction_lines):
        """Sets the deduction_lines of this PayslipLines.


        :param deduction_lines: The deduction_lines of this PayslipLines.  # noqa: E501
        :type: list[DeductionLine]
        """

        self._deduction_lines = deduction_lines

    @property
    def leave_accrual_lines(self):
        """Gets the leave_accrual_lines of this PayslipLines.  # noqa: E501


        :return: The leave_accrual_lines of this PayslipLines.  # noqa: E501
        :rtype: list[LeaveAccrualLine]
        """
        return self._leave_accrual_lines

    @leave_accrual_lines.setter
    def leave_accrual_lines(self, leave_accrual_lines):
        """Sets the leave_accrual_lines of this PayslipLines.


        :param leave_accrual_lines: The leave_accrual_lines of this PayslipLines.  # noqa: E501
        :type: list[LeaveAccrualLine]
        """

        self._leave_accrual_lines = leave_accrual_lines

    @property
    def reimbursement_lines(self):
        """Gets the reimbursement_lines of this PayslipLines.  # noqa: E501


        :return: The reimbursement_lines of this PayslipLines.  # noqa: E501
        :rtype: list[ReimbursementLine]
        """
        return self._reimbursement_lines

    @reimbursement_lines.setter
    def reimbursement_lines(self, reimbursement_lines):
        """Sets the reimbursement_lines of this PayslipLines.


        :param reimbursement_lines: The reimbursement_lines of this PayslipLines.  # noqa: E501
        :type: list[ReimbursementLine]
        """

        self._reimbursement_lines = reimbursement_lines

    @property
    def superannuation_lines(self):
        """Gets the superannuation_lines of this PayslipLines.  # noqa: E501


        :return: The superannuation_lines of this PayslipLines.  # noqa: E501
        :rtype: list[SuperannuationLine]
        """
        return self._superannuation_lines

    @superannuation_lines.setter
    def superannuation_lines(self, superannuation_lines):
        """Sets the superannuation_lines of this PayslipLines.


        :param superannuation_lines: The superannuation_lines of this PayslipLines.  # noqa: E501
        :type: list[SuperannuationLine]
        """

        self._superannuation_lines = superannuation_lines

    @property
    def tax_lines(self):
        """Gets the tax_lines of this PayslipLines.  # noqa: E501


        :return: The tax_lines of this PayslipLines.  # noqa: E501
        :rtype: list[TaxLine]
        """
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        """Sets the tax_lines of this PayslipLines.


        :param tax_lines: The tax_lines of this PayslipLines.  # noqa: E501
        :type: list[TaxLine]
        """

        self._tax_lines = tax_lines
