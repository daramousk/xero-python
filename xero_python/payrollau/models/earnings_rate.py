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


class EarningsRate(BaseModel):
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
        "name": "str",
        "account_code": "str",
        "type_of_units": "str",
        "is_exempt_from_tax": "bool",
        "is_exempt_from_super": "bool",
        "is_reportable_as_w1": "bool",
        "earnings_type": "EarningsType",
        "earnings_rate_id": "str",
        "rate_type": "RateType",
        "rate_per_unit": "str",
        "multiplier": "float",
        "accrue_leave": "bool",
        "amount": "float",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "updated_date_utc": "datetime[ms-format]",
        "current_record": "bool",
        "allowance_type": "AllowanceType",
    }

    attribute_map = {
        "name": "Name",
        "account_code": "AccountCode",
        "type_of_units": "TypeOfUnits",
        "is_exempt_from_tax": "IsExemptFromTax",
        "is_exempt_from_super": "IsExemptFromSuper",
        "is_reportable_as_w1": "IsReportableAsW1",
        "earnings_type": "EarningsType",
        "earnings_rate_id": "EarningsRateID",
        "rate_type": "RateType",
        "rate_per_unit": "RatePerUnit",
        "multiplier": "Multiplier",
        "accrue_leave": "AccrueLeave",
        "amount": "Amount",
        "employment_termination_payment_type": "EmploymentTerminationPaymentType",
        "updated_date_utc": "UpdatedDateUTC",
        "current_record": "CurrentRecord",
        "allowance_type": "AllowanceType",
    }

    def __init__(
        self,
        name=None,
        account_code=None,
        type_of_units=None,
        is_exempt_from_tax=None,
        is_exempt_from_super=None,
        is_reportable_as_w1=None,
        earnings_type=None,
        earnings_rate_id=None,
        rate_type=None,
        rate_per_unit=None,
        multiplier=None,
        accrue_leave=None,
        amount=None,
        employment_termination_payment_type=None,
        updated_date_utc=None,
        current_record=None,
        allowance_type=None,
    ):  # noqa: E501
        """EarningsRate - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._account_code = None
        self._type_of_units = None
        self._is_exempt_from_tax = None
        self._is_exempt_from_super = None
        self._is_reportable_as_w1 = None
        self._earnings_type = None
        self._earnings_rate_id = None
        self._rate_type = None
        self._rate_per_unit = None
        self._multiplier = None
        self._accrue_leave = None
        self._amount = None
        self._employment_termination_payment_type = None
        self._updated_date_utc = None
        self._current_record = None
        self._allowance_type = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if type_of_units is not None:
            self.type_of_units = type_of_units
        if is_exempt_from_tax is not None:
            self.is_exempt_from_tax = is_exempt_from_tax
        if is_exempt_from_super is not None:
            self.is_exempt_from_super = is_exempt_from_super
        if is_reportable_as_w1 is not None:
            self.is_reportable_as_w1 = is_reportable_as_w1
        if earnings_type is not None:
            self.earnings_type = earnings_type
        if earnings_rate_id is not None:
            self.earnings_rate_id = earnings_rate_id
        if rate_type is not None:
            self.rate_type = rate_type
        if rate_per_unit is not None:
            self.rate_per_unit = rate_per_unit
        if multiplier is not None:
            self.multiplier = multiplier
        if accrue_leave is not None:
            self.accrue_leave = accrue_leave
        if amount is not None:
            self.amount = amount
        if employment_termination_payment_type is not None:
            self.employment_termination_payment_type = (
                employment_termination_payment_type
            )
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if current_record is not None:
            self.current_record = current_record
        if allowance_type is not None:
            self.allowance_type = allowance_type

    @property
    def name(self):
        """Gets the name of this EarningsRate.  # noqa: E501

        Name of the earnings rate (max length = 100)  # noqa: E501

        :return: The name of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EarningsRate.

        Name of the earnings rate (max length = 100)  # noqa: E501

        :param name: The name of this EarningsRate.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError(
                "Invalid value for `name`, "
                "length must be less than or equal to `100`"
            )  # noqa: E501

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this EarningsRate.  # noqa: E501

        See Accounts  # noqa: E501

        :return: The account_code of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this EarningsRate.

        See Accounts  # noqa: E501

        :param account_code: The account_code of this EarningsRate.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def type_of_units(self):
        """Gets the type_of_units of this EarningsRate.  # noqa: E501

        Type of units used to record earnings (max length = 50). Only When RateType is RATEPERUNIT  # noqa: E501

        :return: The type_of_units of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._type_of_units

    @type_of_units.setter
    def type_of_units(self, type_of_units):
        """Sets the type_of_units of this EarningsRate.

        Type of units used to record earnings (max length = 50). Only When RateType is RATEPERUNIT  # noqa: E501

        :param type_of_units: The type_of_units of this EarningsRate.  # noqa: E501
        :type: str
        """
        if type_of_units is not None and len(type_of_units) > 50:
            raise ValueError(
                "Invalid value for `type_of_units`, "
                "length must be less than or equal to `50`"
            )  # noqa: E501

        self._type_of_units = type_of_units

    @property
    def is_exempt_from_tax(self):
        """Gets the is_exempt_from_tax of this EarningsRate.  # noqa: E501

        Most payments are subject to tax, so you should only set this value if you are sure that a payment is exempt from PAYG withholding  # noqa: E501

        :return: The is_exempt_from_tax of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_exempt_from_tax

    @is_exempt_from_tax.setter
    def is_exempt_from_tax(self, is_exempt_from_tax):
        """Sets the is_exempt_from_tax of this EarningsRate.

        Most payments are subject to tax, so you should only set this value if you are sure that a payment is exempt from PAYG withholding  # noqa: E501

        :param is_exempt_from_tax: The is_exempt_from_tax of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._is_exempt_from_tax = is_exempt_from_tax

    @property
    def is_exempt_from_super(self):
        """Gets the is_exempt_from_super of this EarningsRate.  # noqa: E501

        See the ATO website for details of which payments are exempt from SGC  # noqa: E501

        :return: The is_exempt_from_super of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_exempt_from_super

    @is_exempt_from_super.setter
    def is_exempt_from_super(self, is_exempt_from_super):
        """Sets the is_exempt_from_super of this EarningsRate.

        See the ATO website for details of which payments are exempt from SGC  # noqa: E501

        :param is_exempt_from_super: The is_exempt_from_super of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._is_exempt_from_super = is_exempt_from_super

    @property
    def is_reportable_as_w1(self):
        """Gets the is_reportable_as_w1 of this EarningsRate.  # noqa: E501

        Boolean to determine if the earnings rate is reportable or exempt from W1  # noqa: E501

        :return: The is_reportable_as_w1 of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._is_reportable_as_w1

    @is_reportable_as_w1.setter
    def is_reportable_as_w1(self, is_reportable_as_w1):
        """Sets the is_reportable_as_w1 of this EarningsRate.

        Boolean to determine if the earnings rate is reportable or exempt from W1  # noqa: E501

        :param is_reportable_as_w1: The is_reportable_as_w1 of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._is_reportable_as_w1 = is_reportable_as_w1

    @property
    def earnings_type(self):
        """Gets the earnings_type of this EarningsRate.  # noqa: E501


        :return: The earnings_type of this EarningsRate.  # noqa: E501
        :rtype: EarningsType
        """
        return self._earnings_type

    @earnings_type.setter
    def earnings_type(self, earnings_type):
        """Sets the earnings_type of this EarningsRate.


        :param earnings_type: The earnings_type of this EarningsRate.  # noqa: E501
        :type: EarningsType
        """

        self._earnings_type = earnings_type

    @property
    def earnings_rate_id(self):
        """Gets the earnings_rate_id of this EarningsRate.  # noqa: E501

        Xero identifier  # noqa: E501

        :return: The earnings_rate_id of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._earnings_rate_id

    @earnings_rate_id.setter
    def earnings_rate_id(self, earnings_rate_id):
        """Sets the earnings_rate_id of this EarningsRate.

        Xero identifier  # noqa: E501

        :param earnings_rate_id: The earnings_rate_id of this EarningsRate.  # noqa: E501
        :type: str
        """

        self._earnings_rate_id = earnings_rate_id

    @property
    def rate_type(self):
        """Gets the rate_type of this EarningsRate.  # noqa: E501


        :return: The rate_type of this EarningsRate.  # noqa: E501
        :rtype: RateType
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this EarningsRate.


        :param rate_type: The rate_type of this EarningsRate.  # noqa: E501
        :type: RateType
        """

        self._rate_type = rate_type

    @property
    def rate_per_unit(self):
        """Gets the rate_per_unit of this EarningsRate.  # noqa: E501

        Default rate per unit (optional). Only applicable if RateType is RATEPERUNIT.  # noqa: E501

        :return: The rate_per_unit of this EarningsRate.  # noqa: E501
        :rtype: str
        """
        return self._rate_per_unit

    @rate_per_unit.setter
    def rate_per_unit(self, rate_per_unit):
        """Sets the rate_per_unit of this EarningsRate.

        Default rate per unit (optional). Only applicable if RateType is RATEPERUNIT.  # noqa: E501

        :param rate_per_unit: The rate_per_unit of this EarningsRate.  # noqa: E501
        :type: str
        """

        self._rate_per_unit = rate_per_unit

    @property
    def multiplier(self):
        """Gets the multiplier of this EarningsRate.  # noqa: E501

        This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MULTIPLE  # noqa: E501

        :return: The multiplier of this EarningsRate.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this EarningsRate.

        This is the multiplier used to calculate the rate per unit, based on the employee’s ordinary earnings rate. For example, for time and a half enter 1.5. Only applicable if RateType is MULTIPLE  # noqa: E501

        :param multiplier: The multiplier of this EarningsRate.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def accrue_leave(self):
        """Gets the accrue_leave of this EarningsRate.  # noqa: E501

        Indicates that this earnings rate should accrue leave. Only applicable if RateType is MULTIPLE  # noqa: E501

        :return: The accrue_leave of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._accrue_leave

    @accrue_leave.setter
    def accrue_leave(self, accrue_leave):
        """Sets the accrue_leave of this EarningsRate.

        Indicates that this earnings rate should accrue leave. Only applicable if RateType is MULTIPLE  # noqa: E501

        :param accrue_leave: The accrue_leave of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._accrue_leave = accrue_leave

    @property
    def amount(self):
        """Gets the amount of this EarningsRate.  # noqa: E501

        Optional Amount for FIXEDAMOUNT RateType EarningsRate  # noqa: E501

        :return: The amount of this EarningsRate.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EarningsRate.

        Optional Amount for FIXEDAMOUNT RateType EarningsRate  # noqa: E501

        :param amount: The amount of this EarningsRate.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def employment_termination_payment_type(self):
        """Gets the employment_termination_payment_type of this EarningsRate.  # noqa: E501


        :return: The employment_termination_payment_type of this EarningsRate.  # noqa: E501
        :rtype: EmploymentTerminationPaymentType
        """
        return self._employment_termination_payment_type

    @employment_termination_payment_type.setter
    def employment_termination_payment_type(self, employment_termination_payment_type):
        """Sets the employment_termination_payment_type of this EarningsRate.


        :param employment_termination_payment_type: The employment_termination_payment_type of this EarningsRate.  # noqa: E501
        :type: EmploymentTerminationPaymentType
        """

        self._employment_termination_payment_type = employment_termination_payment_type

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this EarningsRate.  # noqa: E501

        Last modified timestamp  # noqa: E501

        :return: The updated_date_utc of this EarningsRate.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this EarningsRate.

        Last modified timestamp  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this EarningsRate.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def current_record(self):
        """Gets the current_record of this EarningsRate.  # noqa: E501

        Is the current record  # noqa: E501

        :return: The current_record of this EarningsRate.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this EarningsRate.

        Is the current record  # noqa: E501

        :param current_record: The current_record of this EarningsRate.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record

    @property
    def allowance_type(self):
        """Gets the allowance_type of this EarningsRate.  # noqa: E501


        :return: The allowance_type of this EarningsRate.  # noqa: E501
        :rtype: AllowanceType
        """
        return self._allowance_type

    @allowance_type.setter
    def allowance_type(self, allowance_type):
        """Sets the allowance_type of this EarningsRate.


        :param allowance_type: The allowance_type of this EarningsRate.  # noqa: E501
        :type: AllowanceType
        """

        self._allowance_type = allowance_type
