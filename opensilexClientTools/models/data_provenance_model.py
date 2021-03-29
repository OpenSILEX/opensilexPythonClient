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


class DataProvenanceModel(object):
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
        'uri': 'str',
        'prov_used': 'list[ProvEntityModel]',
        'settings': 'dict(str, object)',
        'experiments': 'list[str]'
    }

    attribute_map = {
        'uri': 'uri',
        'prov_used': 'prov_used',
        'settings': 'settings',
        'experiments': 'experiments'
    }

    def __init__(self, uri=None, prov_used=None, settings=None, experiments=None):  # noqa: E501
        """DataProvenanceModel - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self._prov_used = None
        self._settings = None
        self._experiments = None
        self.discriminator = None

        self.uri = uri
        if prov_used is not None:
            self.prov_used = prov_used
        if settings is not None:
            self.settings = settings
        if experiments is not None:
            self.experiments = experiments

    @property
    def uri(self):
        """Gets the uri of this DataProvenanceModel.  # noqa: E501

        provenance uri  # noqa: E501

        :return: The uri of this DataProvenanceModel.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DataProvenanceModel.

        provenance uri  # noqa: E501

        :param uri: The uri of this DataProvenanceModel.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def prov_used(self):
        """Gets the prov_used of this DataProvenanceModel.  # noqa: E501

        list of inputs of the process described in the provenance  # noqa: E501

        :return: The prov_used of this DataProvenanceModel.  # noqa: E501
        :rtype: list[ProvEntityModel]
        """
        return self._prov_used

    @prov_used.setter
    def prov_used(self, prov_used):
        """Sets the prov_used of this DataProvenanceModel.

        list of inputs of the process described in the provenance  # noqa: E501

        :param prov_used: The prov_used of this DataProvenanceModel.  # noqa: E501
        :type: list[ProvEntityModel]
        """

        self._prov_used = prov_used

    @property
    def settings(self):
        """Gets the settings of this DataProvenanceModel.  # noqa: E501

        a key-value system to store specific information  # noqa: E501

        :return: The settings of this DataProvenanceModel.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this DataProvenanceModel.

        a key-value system to store specific information  # noqa: E501

        :param settings: The settings of this DataProvenanceModel.  # noqa: E501
        :type: dict(str, object)
        """

        self._settings = settings

    @property
    def experiments(self):
        """Gets the experiments of this DataProvenanceModel.  # noqa: E501

        experiments uris on which the data has been produced  # noqa: E501

        :return: The experiments of this DataProvenanceModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._experiments

    @experiments.setter
    def experiments(self, experiments):
        """Sets the experiments of this DataProvenanceModel.

        experiments uris on which the data has been produced  # noqa: E501

        :param experiments: The experiments of this DataProvenanceModel.  # noqa: E501
        :type: list[str]
        """

        self._experiments = experiments

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
        if issubclass(DataProvenanceModel, dict):
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
        if not isinstance(other, DataProvenanceModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other