# coding: utf-8

"""
    LocationIQ

    LocationIQ provides flexible enterprise-grade location based solutions. We work with developers, startups and enterprises worldwide serving billions of requests everyday. This page provides an overview of the technical aspects of our API and will help you get started.  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from locationiq.api_client import ApiClient
from locationiq.exceptions import (
    ApiTypeError,
    ApiValueError
)


class MatchingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def matching(self, coordinates, **kwargs):  # noqa: E501
        """Matching Service  # noqa: E501

        Matching API matches or snaps given GPS points to the road network in the most plausible way.  Please note the request might result multiple sub-traces.  Large jumps in the timestamps (> 60s) or improbable transitions lead to trace splits if a complete matching could not be found. The algorithm might not be able to match all points. Outliers are removed if they can not be matched successfully.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.matching(coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5 (required)
        :param str generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        :param str approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        :param str exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180
        :param str radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        :param str steps: Returned route steps for each route leg [ true, false (default) ]
        :param str annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        :param str geometries: Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ]
        :param str overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ]
        :param str timestamps: Timestamps for the input locations in seconds since UNIX epoch. Timestamps need to be monotonically increasing. [ {timestamp};{timestamp}[;{timestamp} ...]  integer seconds since UNIX epoch
        :param str gaps: Allows the input track splitting based on huge timestamp gaps between points. [ split (default), ignore ]
        :param str tidy: Allows the input track modification to obtain better matching quality for noisy tracks. [ true, false (default) ]
        :param str waypoints: Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. [ {index};{index};{index}... ]
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DirectionsMatching
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.matching_with_http_info(coordinates, **kwargs)  # noqa: E501

    def matching_with_http_info(self, coordinates, **kwargs):  # noqa: E501
        """Matching Service  # noqa: E501

        Matching API matches or snaps given GPS points to the road network in the most plausible way.  Please note the request might result multiple sub-traces.  Large jumps in the timestamps (> 60s) or improbable transitions lead to trace splits if a complete matching could not be found. The algorithm might not be able to match all points. Outliers are removed if they can not be matched successfully.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.matching_with_http_info(coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5 (required)
        :param str generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        :param str approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        :param str exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180
        :param str radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        :param str steps: Returned route steps for each route leg [ true, false (default) ]
        :param str annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        :param str geometries: Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ]
        :param str overview: Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ]
        :param str timestamps: Timestamps for the input locations in seconds since UNIX epoch. Timestamps need to be monotonically increasing. [ {timestamp};{timestamp}[;{timestamp} ...]  integer seconds since UNIX epoch
        :param str gaps: Allows the input track splitting based on huge timestamp gaps between points. [ split (default), ignore ]
        :param str tidy: Allows the input track modification to obtain better matching quality for noisy tracks. [ true, false (default) ]
        :param str waypoints: Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. [ {index};{index};{index}... ]
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DirectionsMatching, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['coordinates', 'generate_hints', 'approaches', 'exclude', 'bearings', 'radiuses', 'steps', 'annotations', 'geometries', 'overview', 'timestamps', 'gaps', 'tidy', 'waypoints']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method matching" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'coordinates' is set
        if self.api_client.client_side_validation and ('coordinates' not in local_var_params or  # noqa: E501
                                                        local_var_params['coordinates'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `coordinates` when calling `matching`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'coordinates' in local_var_params:
            path_params['coordinates'] = local_var_params['coordinates']  # noqa: E501

        query_params = []
        if 'generate_hints' in local_var_params and local_var_params['generate_hints'] is not None:  # noqa: E501
            query_params.append(('generate_hints', local_var_params['generate_hints']))  # noqa: E501
        if 'approaches' in local_var_params and local_var_params['approaches'] is not None:  # noqa: E501
            query_params.append(('approaches', local_var_params['approaches']))  # noqa: E501
        if 'exclude' in local_var_params and local_var_params['exclude'] is not None:  # noqa: E501
            query_params.append(('exclude', local_var_params['exclude']))  # noqa: E501
        if 'bearings' in local_var_params and local_var_params['bearings'] is not None:  # noqa: E501
            query_params.append(('bearings', local_var_params['bearings']))  # noqa: E501
        if 'radiuses' in local_var_params and local_var_params['radiuses'] is not None:  # noqa: E501
            query_params.append(('radiuses', local_var_params['radiuses']))  # noqa: E501
        if 'steps' in local_var_params and local_var_params['steps'] is not None:  # noqa: E501
            query_params.append(('steps', local_var_params['steps']))  # noqa: E501
        if 'annotations' in local_var_params and local_var_params['annotations'] is not None:  # noqa: E501
            query_params.append(('annotations', local_var_params['annotations']))  # noqa: E501
        if 'geometries' in local_var_params and local_var_params['geometries'] is not None:  # noqa: E501
            query_params.append(('geometries', local_var_params['geometries']))  # noqa: E501
        if 'overview' in local_var_params and local_var_params['overview'] is not None:  # noqa: E501
            query_params.append(('overview', local_var_params['overview']))  # noqa: E501
        if 'timestamps' in local_var_params and local_var_params['timestamps'] is not None:  # noqa: E501
            query_params.append(('timestamps', local_var_params['timestamps']))  # noqa: E501
        if 'gaps' in local_var_params and local_var_params['gaps'] is not None:  # noqa: E501
            query_params.append(('gaps', local_var_params['gaps']))  # noqa: E501
        if 'tidy' in local_var_params and local_var_params['tidy'] is not None:  # noqa: E501
            query_params.append(('tidy', local_var_params['tidy']))  # noqa: E501
        if 'waypoints' in local_var_params and local_var_params['waypoints'] is not None:  # noqa: E501
            query_params.append(('waypoints', local_var_params['waypoints']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/matching/driving/{coordinates}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsMatching',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)