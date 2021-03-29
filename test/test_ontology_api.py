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
from opensilexClientTools.api.ontology_api import OntologyApi  # noqa: E501
from opensilexClientTools.rest import ApiException


class TestOntologyApi(unittest.TestCase):
    """OntologyApi unit test stubs"""

    def setUp(self):
        self.api = opensilexClientTools.api.ontology_api.OntologyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_class_property_restriction(self):
        """Test case for add_class_property_restriction

        Add a rdf type property restriction  # noqa: E501
        """
        pass

    def test_check_ur_is_types(self):
        """Test case for check_ur_is_types

          # noqa: E501
        """
        pass

    def test_create_property(self):
        """Test case for create_property

        Create a RDF property  # noqa: E501
        """
        pass

    def test_delete_class_property_restriction(self):
        """Test case for delete_class_property_restriction

        Delete a rdf type property restriction  # noqa: E501
        """
        pass

    def test_delete_property(self):
        """Test case for delete_property

        Delete a property  # noqa: E501
        """
        pass

    def test_get_classes(self):
        """Test case for get_classes

        Return classes models definitions with properties for a list of rdt types  # noqa: E501
        """
        pass

    def test_get_data_properties(self):
        """Test case for get_data_properties

        Search data properties tree  # noqa: E501
        """
        pass

    def test_get_object_properties(self):
        """Test case for get_object_properties

        Search object properties tree  # noqa: E501
        """
        pass

    def test_get_properties(self):
        """Test case for get_properties

        Search properties tree  # noqa: E501
        """
        pass

    def test_get_property(self):
        """Test case for get_property

        Return property model definition detail  # noqa: E501
        """
        pass

    def test_get_rdf_type(self):
        """Test case for get_rdf_type

        Return class model definition with properties  # noqa: E501
        """
        pass

    def test_get_sub_classes_of(self):
        """Test case for get_sub_classes_of

        Search sub-classes tree of an RDF class  # noqa: E501
        """
        pass

    def test_get_uri_label(self):
        """Test case for get_uri_label

        Return associated rdfs:label of an uri if exists  # noqa: E501
        """
        pass

    def test_update_class_property_restriction(self):
        """Test case for update_class_property_restriction

        Update a rdf type property restriction  # noqa: E501
        """
        pass

    def test_update_property(self):
        """Test case for update_property

        Update a RDF property  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()