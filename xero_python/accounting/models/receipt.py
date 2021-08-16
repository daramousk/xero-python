# coding: utf-8

"""
    Xero Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Receipt(BaseModel):
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
        "date": "date[ms-format]",
        "contact": "Contact",
        "line_items": "list[LineItem]",
        "user": "User",
        "reference": "str",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "float",
        "total_tax": "float",
        "total": "float",
        "receipt_id": "str",
        "status": "str",
        "receipt_number": "str",
        "updated_date_utc": "datetime[ms-format]",
        "has_attachments": "bool",
        "url": "str",
        "validation_errors": "list[ValidationError]",
        "warnings": "list[ValidationError]",
        "attachments": "list[Attachment]",
    }

    attribute_map = {
        "date": "Date",
        "contact": "Contact",
        "line_items": "LineItems",
        "user": "User",
        "reference": "Reference",
        "line_amount_types": "LineAmountTypes",
        "sub_total": "SubTotal",
        "total_tax": "TotalTax",
        "total": "Total",
        "receipt_id": "ReceiptID",
        "status": "Status",
        "receipt_number": "ReceiptNumber",
        "updated_date_utc": "UpdatedDateUTC",
        "has_attachments": "HasAttachments",
        "url": "Url",
        "validation_errors": "ValidationErrors",
        "warnings": "Warnings",
        "attachments": "Attachments",
    }

    def __init__(
        self,
        date=None,
        contact=None,
        line_items=None,
        user=None,
        reference=None,
        line_amount_types=None,
        sub_total=None,
        total_tax=None,
        total=None,
        receipt_id=None,
        status=None,
        receipt_number=None,
        updated_date_utc=None,
        has_attachments=False,
        url=None,
        validation_errors=None,
        warnings=None,
        attachments=None,
    ):  # noqa: E501
        """Receipt - a model defined in OpenAPI"""  # noqa: E501

        self._date = None
        self._contact = None
        self._line_items = None
        self._user = None
        self._reference = None
        self._line_amount_types = None
        self._sub_total = None
        self._total_tax = None
        self._total = None
        self._receipt_id = None
        self._status = None
        self._receipt_number = None
        self._updated_date_utc = None
        self._has_attachments = None
        self._url = None
        self._validation_errors = None
        self._warnings = None
        self._attachments = None
        self.discriminator = None

        if date is not None:
            self.date = date
        if contact is not None:
            self.contact = contact
        if line_items is not None:
            self.line_items = line_items
        if user is not None:
            self.user = user
        if reference is not None:
            self.reference = reference
        if line_amount_types is not None:
            self.line_amount_types = line_amount_types
        if sub_total is not None:
            self.sub_total = sub_total
        if total_tax is not None:
            self.total_tax = total_tax
        if total is not None:
            self.total = total
        if receipt_id is not None:
            self.receipt_id = receipt_id
        if status is not None:
            self.status = status
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if updated_date_utc is not None:
            self.updated_date_utc = updated_date_utc
        if has_attachments is not None:
            self.has_attachments = has_attachments
        if url is not None:
            self.url = url
        if validation_errors is not None:
            self.validation_errors = validation_errors
        if warnings is not None:
            self.warnings = warnings
        if attachments is not None:
            self.attachments = attachments

    @property
    def date(self):
        """Gets the date of this Receipt.  # noqa: E501

        Date of receipt – YYYY-MM-DD  # noqa: E501

        :return: The date of this Receipt.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Receipt.

        Date of receipt – YYYY-MM-DD  # noqa: E501

        :param date: The date of this Receipt.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def contact(self):
        """Gets the contact of this Receipt.  # noqa: E501


        :return: The contact of this Receipt.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Receipt.


        :param contact: The contact of this Receipt.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def line_items(self):
        """Gets the line_items of this Receipt.  # noqa: E501


        :return: The line_items of this Receipt.  # noqa: E501
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Receipt.


        :param line_items: The line_items of this Receipt.  # noqa: E501
        :type: list[LineItem]
        """

        self._line_items = line_items

    @property
    def user(self):
        """Gets the user of this Receipt.  # noqa: E501


        :return: The user of this Receipt.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Receipt.


        :param user: The user of this Receipt.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def reference(self):
        """Gets the reference of this Receipt.  # noqa: E501

        Additional reference number  # noqa: E501

        :return: The reference of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Receipt.

        Additional reference number  # noqa: E501

        :param reference: The reference of this Receipt.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def line_amount_types(self):
        """Gets the line_amount_types of this Receipt.  # noqa: E501


        :return: The line_amount_types of this Receipt.  # noqa: E501
        :rtype: LineAmountTypes
        """
        return self._line_amount_types

    @line_amount_types.setter
    def line_amount_types(self, line_amount_types):
        """Sets the line_amount_types of this Receipt.


        :param line_amount_types: The line_amount_types of this Receipt.  # noqa: E501
        :type: LineAmountTypes
        """

        self._line_amount_types = line_amount_types

    @property
    def sub_total(self):
        """Gets the sub_total of this Receipt.  # noqa: E501

        Total of receipt excluding taxes  # noqa: E501

        :return: The sub_total of this Receipt.  # noqa: E501
        :rtype: float
        """
        return self._sub_total

    @sub_total.setter
    def sub_total(self, sub_total):
        """Sets the sub_total of this Receipt.

        Total of receipt excluding taxes  # noqa: E501

        :param sub_total: The sub_total of this Receipt.  # noqa: E501
        :type: float
        """

        self._sub_total = sub_total

    @property
    def total_tax(self):
        """Gets the total_tax of this Receipt.  # noqa: E501

        Total tax on receipt  # noqa: E501

        :return: The total_tax of this Receipt.  # noqa: E501
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """Sets the total_tax of this Receipt.

        Total tax on receipt  # noqa: E501

        :param total_tax: The total_tax of this Receipt.  # noqa: E501
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total(self):
        """Gets the total of this Receipt.  # noqa: E501

        Total of receipt tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :return: The total of this Receipt.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Receipt.

        Total of receipt tax inclusive (i.e. SubTotal + TotalTax)  # noqa: E501

        :param total: The total of this Receipt.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def receipt_id(self):
        """Gets the receipt_id of this Receipt.  # noqa: E501

        Xero generated unique identifier for receipt  # noqa: E501

        :return: The receipt_id of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._receipt_id

    @receipt_id.setter
    def receipt_id(self, receipt_id):
        """Sets the receipt_id of this Receipt.

        Xero generated unique identifier for receipt  # noqa: E501

        :param receipt_id: The receipt_id of this Receipt.  # noqa: E501
        :type: str
        """

        self._receipt_id = receipt_id

    @property
    def status(self):
        """Gets the status of this Receipt.  # noqa: E501

        Current status of receipt – see status types  # noqa: E501

        :return: The status of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Receipt.

        Current status of receipt – see status types  # noqa: E501

        :param status: The status of this Receipt.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "DRAFT",
            "SUBMITTED",
            "AUTHORISED",
            "DECLINED",
            "VOIDED",
            "None",
        ]  # noqa: E501

        if status:
            if status not in allowed_values:
                raise ValueError(
                    "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                        status, allowed_values
                    )
                )

        self._status = status

    @property
    def receipt_number(self):
        """Gets the receipt_number of this Receipt.  # noqa: E501

        Xero generated sequence number for receipt in current claim for a given user  # noqa: E501

        :return: The receipt_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        """Sets the receipt_number of this Receipt.

        Xero generated sequence number for receipt in current claim for a given user  # noqa: E501

        :param receipt_number: The receipt_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._receipt_number = receipt_number

    @property
    def updated_date_utc(self):
        """Gets the updated_date_utc of this Receipt.  # noqa: E501

        Last modified date UTC format  # noqa: E501

        :return: The updated_date_utc of this Receipt.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date_utc

    @updated_date_utc.setter
    def updated_date_utc(self, updated_date_utc):
        """Sets the updated_date_utc of this Receipt.

        Last modified date UTC format  # noqa: E501

        :param updated_date_utc: The updated_date_utc of this Receipt.  # noqa: E501
        :type: datetime
        """

        self._updated_date_utc = updated_date_utc

    @property
    def has_attachments(self):
        """Gets the has_attachments of this Receipt.  # noqa: E501

        boolean to indicate if a receipt has an attachment  # noqa: E501

        :return: The has_attachments of this Receipt.  # noqa: E501
        :rtype: bool
        """
        return self._has_attachments

    @has_attachments.setter
    def has_attachments(self, has_attachments):
        """Sets the has_attachments of this Receipt.

        boolean to indicate if a receipt has an attachment  # noqa: E501

        :param has_attachments: The has_attachments of this Receipt.  # noqa: E501
        :type: bool
        """

        self._has_attachments = has_attachments

    @property
    def url(self):
        """Gets the url of this Receipt.  # noqa: E501

        URL link to a source document – shown as “Go to [appName]” in the Xero app  # noqa: E501

        :return: The url of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Receipt.

        URL link to a source document – shown as “Go to [appName]” in the Xero app  # noqa: E501

        :param url: The url of this Receipt.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def validation_errors(self):
        """Gets the validation_errors of this Receipt.  # noqa: E501

        Displays array of validation error messages from the API  # noqa: E501

        :return: The validation_errors of this Receipt.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """Sets the validation_errors of this Receipt.

        Displays array of validation error messages from the API  # noqa: E501

        :param validation_errors: The validation_errors of this Receipt.  # noqa: E501
        :type: list[ValidationError]
        """

        self._validation_errors = validation_errors

    @property
    def warnings(self):
        """Gets the warnings of this Receipt.  # noqa: E501

        Displays array of warning messages from the API  # noqa: E501

        :return: The warnings of this Receipt.  # noqa: E501
        :rtype: list[ValidationError]
        """
        return self._warnings

    @warnings.setter
    def warnings(self, warnings):
        """Sets the warnings of this Receipt.

        Displays array of warning messages from the API  # noqa: E501

        :param warnings: The warnings of this Receipt.  # noqa: E501
        :type: list[ValidationError]
        """

        self._warnings = warnings

    @property
    def attachments(self):
        """Gets the attachments of this Receipt.  # noqa: E501

        Displays array of attachments from the API  # noqa: E501

        :return: The attachments of this Receipt.  # noqa: E501
        :rtype: list[Attachment]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Receipt.

        Displays array of attachments from the API  # noqa: E501

        :param attachments: The attachments of this Receipt.  # noqa: E501
        :type: list[Attachment]
        """

        self._attachments = attachments
