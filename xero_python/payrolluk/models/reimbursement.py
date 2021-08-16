# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Reimbursement(BaseModel):
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
        "reimbursement_id": "str",
        "name": "str",
        "account_id": "str",
        "current_record": "bool",
    }

    attribute_map = {
        "reimbursement_id": "reimbursementID",
        "name": "name",
        "account_id": "accountID",
        "current_record": "currentRecord",
    }

    def __init__(
        self, reimbursement_id=None, name=None, account_id=None, current_record=None
    ):  # noqa: E501
        """Reimbursement - a model defined in OpenAPI"""  # noqa: E501

        self._reimbursement_id = None
        self._name = None
        self._account_id = None
        self._current_record = None
        self.discriminator = None

        if reimbursement_id is not None:
            self.reimbursement_id = reimbursement_id
        self.name = name
        self.account_id = account_id
        if current_record is not None:
            self.current_record = current_record

    @property
    def reimbursement_id(self):
        """Gets the reimbursement_id of this Reimbursement.  # noqa: E501

        Xero unique identifier for a reimbursement  # noqa: E501

        :return: The reimbursement_id of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._reimbursement_id

    @reimbursement_id.setter
    def reimbursement_id(self, reimbursement_id):
        """Sets the reimbursement_id of this Reimbursement.

        Xero unique identifier for a reimbursement  # noqa: E501

        :param reimbursement_id: The reimbursement_id of this Reimbursement.  # noqa: E501
        :type: str
        """

        self._reimbursement_id = reimbursement_id

    @property
    def name(self):
        """Gets the name of this Reimbursement.  # noqa: E501

        Name of the reimbursement  # noqa: E501

        :return: The name of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Reimbursement.

        Name of the reimbursement  # noqa: E501

        :param name: The name of this Reimbursement.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def account_id(self):
        """Gets the account_id of this Reimbursement.  # noqa: E501

        Xero unique identifier for the account used for the reimbursement  # noqa: E501

        :return: The account_id of this Reimbursement.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Reimbursement.

        Xero unique identifier for the account used for the reimbursement  # noqa: E501

        :param account_id: The account_id of this Reimbursement.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError(
                "Invalid value for `account_id`, must not be `None`"
            )  # noqa: E501

        self._account_id = account_id

    @property
    def current_record(self):
        """Gets the current_record of this Reimbursement.  # noqa: E501

        Indicates that whether the reimbursement is active  # noqa: E501

        :return: The current_record of this Reimbursement.  # noqa: E501
        :rtype: bool
        """
        return self._current_record

    @current_record.setter
    def current_record(self, current_record):
        """Sets the current_record of this Reimbursement.

        Indicates that whether the reimbursement is active  # noqa: E501

        :param current_record: The current_record of this Reimbursement.  # noqa: E501
        :type: bool
        """

        self._current_record = current_record
