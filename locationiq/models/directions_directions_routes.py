# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from locationiq.configuration import Configuration


class DirectionsDirectionsRoutes(object):
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
        'legs': 'list[object]',
        'weight_name': 'str',
        'geometry': 'str',
        'weight': 'float',
        'distance': 'float',
        'duration': 'float'
    }

    attribute_map = {
        'legs': 'legs',
        'weight_name': 'weight_name',
        'geometry': 'geometry',
        'weight': 'weight',
        'distance': 'distance',
        'duration': 'duration'
    }

    def __init__(self, legs=None, weight_name=None, geometry=None, weight=None, distance=None, duration=None, local_vars_configuration=None):  # noqa: E501
        """DirectionsDirectionsRoutes - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legs = None
        self._weight_name = None
        self._geometry = None
        self._weight = None
        self._distance = None
        self._duration = None
        self.discriminator = None

        if legs is not None:
            self.legs = legs
        if weight_name is not None:
            self.weight_name = weight_name
        if geometry is not None:
            self.geometry = geometry
        if weight is not None:
            self.weight = weight
        if distance is not None:
            self.distance = distance
        if duration is not None:
            self.duration = duration

    @property
    def legs(self):
        """Gets the legs of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The legs of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: list[object]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this DirectionsDirectionsRoutes.


        :param legs: The legs of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: list[object]
        """

        self._legs = legs

    @property
    def weight_name(self):
        """Gets the weight_name of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The weight_name of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: str
        """
        return self._weight_name

    @weight_name.setter
    def weight_name(self, weight_name):
        """Sets the weight_name of this DirectionsDirectionsRoutes.


        :param weight_name: The weight_name of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: str
        """

        self._weight_name = weight_name

    @property
    def geometry(self):
        """Gets the geometry of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The geometry of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: str
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this DirectionsDirectionsRoutes.


        :param geometry: The geometry of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: str
        """

        self._geometry = geometry

    @property
    def weight(self):
        """Gets the weight of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The weight of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this DirectionsDirectionsRoutes.


        :param weight: The weight of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: float
        """

        self._weight = weight

    @property
    def distance(self):
        """Gets the distance of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The distance of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this DirectionsDirectionsRoutes.


        :param distance: The distance of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: float
        """

        self._distance = distance

    @property
    def duration(self):
        """Gets the duration of this DirectionsDirectionsRoutes.  # noqa: E501


        :return: The duration of this DirectionsDirectionsRoutes.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this DirectionsDirectionsRoutes.


        :param duration: The duration of this DirectionsDirectionsRoutes.  # noqa: E501
        :type: float
        """

        self._duration = duration

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DirectionsDirectionsRoutes):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DirectionsDirectionsRoutes):
            return True

        return self.to_dict() != other.to_dict()
