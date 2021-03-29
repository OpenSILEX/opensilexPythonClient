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
from opensilexClientTools.api.devices_api import DevicesApi  # noqa: E501
from opensilexClientTools.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientTools.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device(self):
        """Test case for create_device

        Create a device  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete a device  # noqa: E501
        """
        pass

    def test_export_devices(self):
        """Test case for export_devices

        export devices  # noqa: E501
        """
        pass

    def test_export_list(self):
        """Test case for export_list

        export devices  # noqa: E501
        """
        pass

    def test_get_device(self):
        """Test case for get_device

        Get device detail  # noqa: E501
        """
        pass

    def test_get_device_data_files_provenances(self):
        """Test case for get_device_data_files_provenances

        Get provenances of datafiles linked to this device  # noqa: E501
        """
        pass

    def test_get_device_data_provenances(self):
        """Test case for get_device_data_provenances

        Get provenances of data that have been measured on this device  # noqa: E501
        """
        pass

    def test_get_device_variables(self):
        """Test case for get_device_variables

        Get variables measured by the device  # noqa: E501
        """
        pass

    def test_search_device_data(self):
        """Test case for search_device_data

        Search device data  # noqa: E501
        """
        pass

    def test_search_devices(self):
        """Test case for search_devices

        Search devices  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update a device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()