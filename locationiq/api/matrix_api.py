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


class MatrixApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def matrix(self, coordinates, **kwargs):  # noqa: E501
        """Matrix Service  # noqa: E501

        Computes duration of the fastest route between all pairs of supplied coordinates. Returns the durations or distances or both between the coordinate pairs. Note that the distances are not the shortest distance between two coordinates, but rather the distances of the fastest routes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.matrix(coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5 (required)
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180
        :param str radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        :param str generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        :param str approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        :param str exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        :param str annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        :param int sources: Use location with given index as source. [ {index};{index}[;{index} ...] or all (default) ] => index  0 <= integer < #locations
        :param int destinations: Use location with given index as destination. [ {index};{index}[;{index} ...] or all (default) ]
        :param float fallback_speed: If no route found between a source/destination pair, calculate the as-the-crow-flies distance,  then use this speed to estimate duration. double > 0
        :param str fallback_coordinate: When using a fallback_speed, use the user-supplied coordinate (input), or the snapped location (snapped) for calculating distances. [ input (default), or snapped ]
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DirectionsMatrix
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.matrix_with_http_info(coordinates, **kwargs)  # noqa: E501

    def matrix_with_http_info(self, coordinates, **kwargs):  # noqa: E501
        """Matrix Service  # noqa: E501

        Computes duration of the fastest route between all pairs of supplied coordinates. Returns the durations or distances or both between the coordinate pairs. Note that the distances are not the shortest distance between two coordinates, but rather the distances of the fastest routes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.matrix_with_http_info(coordinates, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str coordinates: String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5 (required)
        :param str bearings: Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180
        :param str radiuses: Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default)
        :param str generate_hints: Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String
        :param str approaches: Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default)
        :param str exclude: Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none.
        :param str annotations: Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ]
        :param int sources: Use location with given index as source. [ {index};{index}[;{index} ...] or all (default) ] => index  0 <= integer < #locations
        :param int destinations: Use location with given index as destination. [ {index};{index}[;{index} ...] or all (default) ]
        :param float fallback_speed: If no route found between a source/destination pair, calculate the as-the-crow-flies distance,  then use this speed to estimate duration. double > 0
        :param str fallback_coordinate: When using a fallback_speed, use the user-supplied coordinate (input), or the snapped location (snapped) for calculating distances. [ input (default), or snapped ]
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DirectionsMatrix, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['coordinates', 'bearings', 'radiuses', 'generate_hints', 'approaches', 'exclude', 'annotations', 'sources', 'destinations', 'fallback_speed', 'fallback_coordinate']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method matrix" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'coordinates' is set
        if self.api_client.client_side_validation and ('coordinates' not in local_var_params or  # noqa: E501
                                                        local_var_params['coordinates'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `coordinates` when calling `matrix`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'coordinates' in local_var_params:
            path_params['coordinates'] = local_var_params['coordinates']  # noqa: E501

        query_params = []
        if 'bearings' in local_var_params and local_var_params['bearings'] is not None:  # noqa: E501
            query_params.append(('bearings', local_var_params['bearings']))  # noqa: E501
        if 'radiuses' in local_var_params and local_var_params['radiuses'] is not None:  # noqa: E501
            query_params.append(('radiuses', local_var_params['radiuses']))  # noqa: E501
        if 'generate_hints' in local_var_params and local_var_params['generate_hints'] is not None:  # noqa: E501
            query_params.append(('generate_hints', local_var_params['generate_hints']))  # noqa: E501
        if 'approaches' in local_var_params and local_var_params['approaches'] is not None:  # noqa: E501
            query_params.append(('approaches', local_var_params['approaches']))  # noqa: E501
        if 'exclude' in local_var_params and local_var_params['exclude'] is not None:  # noqa: E501
            query_params.append(('exclude', local_var_params['exclude']))  # noqa: E501
        if 'annotations' in local_var_params and local_var_params['annotations'] is not None:  # noqa: E501
            query_params.append(('annotations', local_var_params['annotations']))  # noqa: E501
        if 'sources' in local_var_params and local_var_params['sources'] is not None:  # noqa: E501
            query_params.append(('sources', local_var_params['sources']))  # noqa: E501
        if 'destinations' in local_var_params and local_var_params['destinations'] is not None:  # noqa: E501
            query_params.append(('destinations', local_var_params['destinations']))  # noqa: E501
        if 'fallback_speed' in local_var_params and local_var_params['fallback_speed'] is not None:  # noqa: E501
            query_params.append(('fallback_speed', local_var_params['fallback_speed']))  # noqa: E501
        if 'fallback_coordinate' in local_var_params and local_var_params['fallback_coordinate'] is not None:  # noqa: E501
            query_params.append(('fallback_coordinate', local_var_params['fallback_coordinate']))  # noqa: E501

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
            '/matrix/driving/{coordinates}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DirectionsMatrix',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
