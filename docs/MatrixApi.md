# locationiq.MatrixApi

All URIs are relative to *https://eu1.locationiq.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matrix**](MatrixApi.md#matrix) | **GET** /matrix/driving/{coordinates} | Matrix Service


# **matrix**
> DirectionsMatrix matrix(coordinates, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, approaches=approaches, exclude=exclude, annotations=annotations, sources=sources, destinations=destinations, fallback_speed=fallback_speed, fallback_coordinate=fallback_coordinate)

Matrix Service

Computes duration of the fastest route between all pairs of supplied coordinates. Returns the durations or distances or both between the coordinate pairs. Note that the distances are not the shortest distance between two coordinates, but rather the distances of the fastest routes.

### Example

* Api Key Authentication (key):
```python
from __future__ import print_function
import time
import locationiq
from locationiq.rest import ApiException
from pprint import pprint
configuration = locationiq.Configuration()
# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Defining host is optional and default to https://eu1.locationiq.com/v1
configuration.host = "https://eu1.locationiq.com/v1"
# Enter a context with an instance of the API client
with locationiq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = locationiq.MatrixApi(api_client)
    coordinates = '-0.16102,51.523854;-0.15797,51.52326;-0.161593,51.522550' # str | String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
bearings = '10,20;40,30;30,9' # str | Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180 (optional)
radiuses = '500;200;300' # str | Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default) (optional)
generate_hints = 'false' # str | Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String (optional)
approaches = 'curb;curb;curb' # str | Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default) (optional)
exclude = 'toll' # str | Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none. (optional)
annotations = 'distance' # str | Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ] (optional)
sources = 0 # int | Use location with given index as source. [ {index};{index}[;{index} ...] or all (default) ] => index  0 <= integer < #locations (optional)
destinations = 2 # int | Use location with given index as destination. [ {index};{index}[;{index} ...] or all (default) ] (optional)
fallback_speed = 25.65 # float | If no route found between a source/destination pair, calculate the as-the-crow-flies distance,  then use this speed to estimate duration. double > 0 (optional)
fallback_coordinate = 'input' # str | When using a fallback_speed, use the user-supplied coordinate (input), or the snapped location (snapped) for calculating distances. [ input (default), or snapped ] (optional) (default to '"input"')

try:
    # Matrix Service
    api_response = api_instance.matrix(coordinates, bearings=bearings, radiuses=radiuses, generate_hints=generate_hints, approaches=approaches, exclude=exclude, annotations=annotations, sources=sources, destinations=destinations, fallback_speed=fallback_speed, fallback_coordinate=fallback_coordinate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatrixApi->matrix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coordinates** | **str**| String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google&#39;s polyline format with precision 5 | 
 **bearings** | **str**| Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180 | [optional] 
 **radiuses** | **str**| Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double &gt;&#x3D; 0 or unlimited (default) | [optional] 
 **generate_hints** | **str**| Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String | [optional] 
 **approaches** | **str**| Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default) | [optional] 
 **exclude** | **str**| Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none. | [optional] 
 **annotations** | **str**| Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ] | [optional] 
 **sources** | **int**| Use location with given index as source. [ {index};{index}[;{index} ...] or all (default) ] &#x3D;&gt; index  0 &lt;&#x3D; integer &lt; #locations | [optional] 
 **destinations** | **int**| Use location with given index as destination. [ {index};{index}[;{index} ...] or all (default) ] | [optional] 
 **fallback_speed** | **float**| If no route found between a source/destination pair, calculate the as-the-crow-flies distance,  then use this speed to estimate duration. double &gt; 0 | [optional] 
 **fallback_coordinate** | **str**| When using a fallback_speed, use the user-supplied coordinate (input), or the snapped location (snapped) for calculating distances. [ input (default), or snapped ] | [optional] [default to &#39;&quot;input&quot;&#39;]

### Return type

[**DirectionsMatrix**](DirectionsMatrix.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | The request has been made from an unauthorized domain. |  -  |
**404** | No location or places were found for the given input |  -  |
**429** | Request exceeded the rate-limits set on your account |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

