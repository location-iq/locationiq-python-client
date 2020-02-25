# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import locationiq
from locationiq.models.directions_nearest import DirectionsNearest  # noqa: E501
from locationiq.rest import ApiException

class TestDirectionsNearest(unittest.TestCase):
    """DirectionsNearest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DirectionsNearest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = locationiq.models.directions_nearest.DirectionsNearest()  # noqa: E501
        if include_optional :
            return DirectionsNearest(
                code = '0', 
                waypoints = [
                    locationiq.models.directions_nearest_waypoints.directions_nearest_waypoints(
                        nodes = [
                            1.337
                            ], 
                        distance = 1.337, 
                        location = [
                            1.337
                            ], 
                        name = '0', )
                    ]
            )
        else :
            return DirectionsNearest(
        )

    def testDirectionsNearest(self):
        """Test DirectionsNearest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
