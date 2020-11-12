# coding: utf-8

"""
    Xero Projects API

    This is the Xero Projects API  # noqa: E501

    OpenAPI spec version: 2.4.4
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class ProjectUser(BaseModel):
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
    openapi_types = {"user_id": "str", "name": "str", "email": "str"}

    attribute_map = {"user_id": "userId", "name": "name", "email": "email"}

    def __init__(self, user_id=None, name=None, email=None):  # noqa: E501
        """ProjectUser - a model defined in OpenAPI"""  # noqa: E501

        self._user_id = None
        self._name = None
        self._email = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email

    @property
    def user_id(self):
        """Gets the user_id of this ProjectUser.  # noqa: E501

        Identifier of the user of the project.  # noqa: E501

        :return: The user_id of this ProjectUser.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ProjectUser.

        Identifier of the user of the project.  # noqa: E501

        :param user_id: The user_id of this ProjectUser.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def name(self):
        """Gets the name of this ProjectUser.  # noqa: E501

        Full name of the user.  # noqa: E501

        :return: The name of this ProjectUser.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectUser.

        Full name of the user.  # noqa: E501

        :param name: The name of this ProjectUser.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this ProjectUser.  # noqa: E501

        Email address of the user.  # noqa: E501

        :return: The email of this ProjectUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ProjectUser.

        Email address of the user.  # noqa: E501

        :param email: The email of this ProjectUser.  # noqa: E501
        :type: str
        """

        self._email = email
