# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OntologyReference(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'documentation_links': 'list[DocumentationLink]',
        'ontology_db_id': 'str',
        'ontology_name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'documentation_links': 'documentationLinks',
        'ontology_db_id': 'ontologyDbId',
        'ontology_name': 'ontologyName',
        'version': 'version'
    }

    def __init__(self, documentation_links=None, ontology_db_id=None, ontology_name=None, version=None):  # noqa: E501
        """OntologyReference - a model defined in Swagger"""  # noqa: E501

        self._documentation_links = None
        self._ontology_db_id = None
        self._ontology_name = None
        self._version = None
        self.discriminator = None

        if documentation_links is not None:
            self.documentation_links = documentation_links
        if ontology_db_id is not None:
            self.ontology_db_id = ontology_db_id
        if ontology_name is not None:
            self.ontology_name = ontology_name
        if version is not None:
            self.version = version

    @property
    def documentation_links(self):
        """Gets the documentation_links of this OntologyReference.  # noqa: E501


        :return: The documentation_links of this OntologyReference.  # noqa: E501
        :rtype: list[DocumentationLink]
        """
        return self._documentation_links

    @documentation_links.setter
    def documentation_links(self, documentation_links):
        """Sets the documentation_links of this OntologyReference.


        :param documentation_links: The documentation_links of this OntologyReference.  # noqa: E501
        :type: list[DocumentationLink]
        """

        self._documentation_links = documentation_links

    @property
    def ontology_db_id(self):
        """Gets the ontology_db_id of this OntologyReference.  # noqa: E501


        :return: The ontology_db_id of this OntologyReference.  # noqa: E501
        :rtype: str
        """
        return self._ontology_db_id

    @ontology_db_id.setter
    def ontology_db_id(self, ontology_db_id):
        """Sets the ontology_db_id of this OntologyReference.


        :param ontology_db_id: The ontology_db_id of this OntologyReference.  # noqa: E501
        :type: str
        """

        self._ontology_db_id = ontology_db_id

    @property
    def ontology_name(self):
        """Gets the ontology_name of this OntologyReference.  # noqa: E501


        :return: The ontology_name of this OntologyReference.  # noqa: E501
        :rtype: str
        """
        return self._ontology_name

    @ontology_name.setter
    def ontology_name(self, ontology_name):
        """Sets the ontology_name of this OntologyReference.


        :param ontology_name: The ontology_name of this OntologyReference.  # noqa: E501
        :type: str
        """

        self._ontology_name = ontology_name

    @property
    def version(self):
        """Gets the version of this OntologyReference.  # noqa: E501


        :return: The version of this OntologyReference.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OntologyReference.


        :param version: The version of this OntologyReference.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OntologyReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OntologyReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
