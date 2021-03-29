# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import opensilexClientTools
from opensilexClientTools.api.authentication_api import AuthenticationApi  # noqa: E501
from opensilexClientTools.rest import ApiException


class TestAuthenticationApi(unittest.TestCase):
    """AuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientTools.api.authentication_api.AuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate(self):
        """Test case for authenticate

        Authenticate a user and return an access token  # noqa: E501
        """
        pass

    def test_authenticate_open_id(self):
        """Test case for authenticate_open_id

        Authenticate a user and return an access token  # noqa: E501
        """
        pass

    def test_get_credentials_groups(self):
        """Test case for get_credentials_groups

        Get list of existing credentials indexed by Swagger @API concepts in the application  # noqa: E501
        """
        pass

    def test_logout(self):
        """Test case for logout

        Logout by discarding a user token  # noqa: E501
        """
        pass

    def test_renew_token(self):
        """Test case for renew_token

        Send back a new token if the provided one is still valid  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
