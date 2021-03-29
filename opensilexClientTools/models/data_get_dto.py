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


class DataGetDTO(object):
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
        '_date': 'str',
        'scientific_objects': 'list[str]',
        'variable': 'str',
        'value': 'object',
        'confidence': 'float',
        'provenance': 'DataProvenanceModel',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'uri': 'uri',
        '_date': 'date',
        'scientific_objects': 'scientific_objects',
        'variable': 'variable',
        'value': 'value',
        'confidence': 'confidence',
        'provenance': 'provenance',
        'metadata': 'metadata'
    }

    def __init__(self, uri=None, _date=None, scientific_objects=None, variable=None, value=None, confidence=None, provenance=None, metadata=None):  # noqa: E501
        """DataGetDTO - a model defined in Swagger"""  # noqa: E501

        self._uri = None
        self.__date = None
        self._scientific_objects = None
        self._variable = None
        self._value = None
        self._confidence = None
        self._provenance = None
        self._metadata = None
        self.discriminator = None

        self.uri = uri
        self._date = _date
        if scientific_objects is not None:
            self.scientific_objects = scientific_objects
        self.variable = variable
        self.value = value
        if confidence is not None:
            self.confidence = confidence
        self.provenance = provenance
        if metadata is not None:
            self.metadata = metadata

    @property
    def uri(self):
        """Gets the uri of this DataGetDTO.  # noqa: E501

        data URI  # noqa: E501

        :return: The uri of this DataGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DataGetDTO.

        data URI  # noqa: E501

        :param uri: The uri of this DataGetDTO.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def _date(self):
        """Gets the _date of this DataGetDTO.  # noqa: E501

        date or datetime  # noqa: E501

        :return: The _date of this DataGetDTO.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DataGetDTO.

        date or datetime  # noqa: E501

        :param _date: The _date of this DataGetDTO.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def scientific_objects(self):
        """Gets the scientific_objects of this DataGetDTO.  # noqa: E501

        scientific objects URIs on which the data have been collected  # noqa: E501

        :return: The scientific_objects of this DataGetDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._scientific_objects

    @scientific_objects.setter
    def scientific_objects(self, scientific_objects):
        """Sets the scientific_objects of this DataGetDTO.

        scientific objects URIs on which the data have been collected  # noqa: E501

        :param scientific_objects: The scientific_objects of this DataGetDTO.  # noqa: E501
        :type: list[str]
        """

        self._scientific_objects = scientific_objects

    @property
    def variable(self):
        """Gets the variable of this DataGetDTO.  # noqa: E501

        variable URI  # noqa: E501

        :return: The variable of this DataGetDTO.  # noqa: E501
        :rtype: str
        """
        return self._variable

    @variable.setter
    def variable(self, variable):
        """Sets the variable of this DataGetDTO.

        variable URI  # noqa: E501

        :param variable: The variable of this DataGetDTO.  # noqa: E501
        :type: str
        """
        if variable is None:
            raise ValueError("Invalid value for `variable`, must not be `None`")  # noqa: E501

        self._variable = variable

    @property
    def value(self):
        """Gets the value of this DataGetDTO.  # noqa: E501

        can be decimal, integer, boolean, string or date  # noqa: E501

        :return: The value of this DataGetDTO.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DataGetDTO.

        can be decimal, integer, boolean, string or date  # noqa: E501

        :param value: The value of this DataGetDTO.  # noqa: E501
        :type: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def confidence(self):
        """Gets the confidence of this DataGetDTO.  # noqa: E501

        confidence index  # noqa: E501

        :return: The confidence of this DataGetDTO.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this DataGetDTO.

        confidence index  # noqa: E501

        :param confidence: The confidence of this DataGetDTO.  # noqa: E501
        :type: float
        """
        if confidence is not None and confidence > 1:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `1`")  # noqa: E501
        if confidence is not None and confidence < 0:  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

    @property
    def provenance(self):
        """Gets the provenance of this DataGetDTO.  # noqa: E501


        :return: The provenance of this DataGetDTO.  # noqa: E501
        :rtype: DataProvenanceModel
        """
        return self._provenance

    @provenance.setter
    def provenance(self, provenance):
        """Sets the provenance of this DataGetDTO.


        :param provenance: The provenance of this DataGetDTO.  # noqa: E501
        :type: DataProvenanceModel
        """
        if provenance is None:
            raise ValueError("Invalid value for `provenance`, must not be `None`")  # noqa: E501

        self._provenance = provenance

    @property
    def metadata(self):
        """Gets the metadata of this DataGetDTO.  # noqa: E501

        key-value system to store additional information that can be used to query data  # noqa: E501

        :return: The metadata of this DataGetDTO.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DataGetDTO.

        key-value system to store additional information that can be used to query data  # noqa: E501

        :param metadata: The metadata of this DataGetDTO.  # noqa: E501
        :type: dict(str, object)
        """

        self._metadata = metadata

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
        if issubclass(DataGetDTO, dict):
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
        if not isinstance(other, DataGetDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other