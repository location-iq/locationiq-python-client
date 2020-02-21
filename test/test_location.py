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

import openapi_client
from openapi_client.models.location import Location  # noqa: E501
from openapi_client.rest import ApiException

class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Location
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.location.Location()  # noqa: E501
        if include_optional :
            return Location(
                distance = 1.337, 
                place_id = '0', 
                licence = '0', 
                osm_type = '0', 
                osm_id = '0', 
                boundingbox = [
                    '0'
                    ], 
                lat = '0', 
                lon = '0', 
                display_name = '0', 
                _class = '0', 
                type = '0', 
                importance = 1.337, 
                address = {"house_number":"3894","road":"Spring Mill Way","residential":"Hunter’s Point","village":"Landen","city":"Landen","county":"Warren County","state":"Ohio","postcode":"45039","country":"United States of America","country_code":"us","state_code":"oh"}, 
                namedetails = {"name":"\"Empire State Building\""}, 
                matchquality = openapi_client.models.matchquality.matchquality(
                    matchcode = '0', 
                    matchtype = '0', 
                    matchlevel = '0', )
            )
        else :
            return Location(
        )

    def testLocation(self):
        """Test Location"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
