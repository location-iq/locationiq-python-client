# locationiq.MatchingApi

All URIs are relative to *https://eu1.locationiq.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**matching**](MatchingApi.md#matching) | **GET** /matching/driving/{coordinates} | Matching Service


# **matching**
> DirectionsMatching matching(coordinates, generate_hints=generate_hints, approaches=approaches, exclude=exclude, bearings=bearings, radiuses=radiuses, steps=steps, annotations=annotations, geometries=geometries, overview=overview, timestamps=timestamps, gaps=gaps, tidy=tidy, waypoints=waypoints)

Matching Service

Matching API matches or snaps given GPS points to the road network in the most plausible way.  Please note the request might result multiple sub-traces.  Large jumps in the timestamps (> 60s) or improbable transitions lead to trace splits if a complete matching could not be found. The algorithm might not be able to match all points. Outliers are removed if they can not be matched successfully.

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
    api_instance = locationiq.MatchingApi(api_client)
    coordinates = '-0.16102,51.523854;-0.15797,51.52326;-0.161593,51.522550' # str | String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google's polyline format with precision 5
generate_hints = 'false' # str | Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String (optional)
approaches = 'curb;curb;curb' # str | Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default) (optional)
exclude = 'toll' # str | Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none. (optional)
bearings = 'None' # str | Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180 (optional)
radiuses = 'None' # str | Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double >= 0 or unlimited (default) (optional)
steps = 'true' # str | Returned route steps for each route leg [ true, false (default) ] (optional)
annotations = 'false' # str | Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ] (optional) (default to '"false"')
geometries = 'polyline' # str | Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ] (optional) (default to '"polyline"')
overview = 'simplified' # str | Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ] (optional) (default to '"simplified"')
timestamps = '200;300;900' # str | Timestamps for the input locations in seconds since UNIX epoch. Timestamps need to be monotonically increasing. [ {timestamp};{timestamp}[;{timestamp} ...]  integer seconds since UNIX epoch (optional)
gaps = 'split' # str | Allows the input track splitting based on huge timestamp gaps between points. [ split (default), ignore ] (optional) (default to '"split"')
tidy = 'false' # str | Allows the input track modification to obtain better matching quality for noisy tracks. [ true, false (default) ] (optional) (default to '"false"')
waypoints = '0;1;2' # str | Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. [ {index};{index};{index}... ] (optional)

try:
    # Matching Service
    api_response = api_instance.matching(coordinates, generate_hints=generate_hints, approaches=approaches, exclude=exclude, bearings=bearings, radiuses=radiuses, steps=steps, annotations=annotations, geometries=geometries, overview=overview, timestamps=timestamps, gaps=gaps, tidy=tidy, waypoints=waypoints)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchingApi->matching: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coordinates** | **str**| String of format {longitude},{latitude};{longitude},{latitude}[;{longitude},{latitude} ...] or polyline({polyline}) or polyline6({polyline6}). polyline follows Google&#39;s polyline format with precision 5 | 
 **generate_hints** | **str**| Adds a Hint to the response which can be used in subsequent requests, see hints parameter. Input Value - true (default), false Format - Base64 String | [optional] 
 **approaches** | **str**| Keep waypoints on curb side. Input Value - {approach};{approach}[;{approach} ...] Format - curb or unrestricted (default) | [optional] 
 **exclude** | **str**| Additive list of classes to avoid, order does not matter. input Value - {class}[,{class}] Format - A class name determined by the profile or none. | [optional] 
 **bearings** | **str**| Limits the search to segments with given bearing in degrees towards true north in clockwise direction. List of positive integer pairs separated by semi-colon and bearings array should be equal to length of coordinate array. Input Value :- {bearing};{bearing}[;{bearing} ...] Bearing follows the following format : bearing {value},{range} integer 0 .. 360,integer 0 .. 180 | [optional] 
 **radiuses** | **str**| Limits the search to given radius in meters Radiuses array length should be same as coordinates array, eaach value separated by semi-colon. Input Value - {radius};{radius}[;{radius} ...] Radius has following format :- double &gt;&#x3D; 0 or unlimited (default) | [optional] 
 **steps** | **str**| Returned route steps for each route leg [ true, false (default) ] | [optional] 
 **annotations** | **str**| Returns additional metadata for each coordinate along the route geometry.  [ true, false (default), nodes, distance, duration, datasources, weight, speed ] | [optional] [default to &#39;&quot;false&quot;&#39;]
 **geometries** | **str**| Returned route geometry format (influences overview and per step) [ polyline (default), polyline6, geojson ] | [optional] [default to &#39;&quot;polyline&quot;&#39;]
 **overview** | **str**| Add overview geometry either full, simplified according to highest zoom level it could be display on, or not at all. [ simplified (default), full, false ] | [optional] [default to &#39;&quot;simplified&quot;&#39;]
 **timestamps** | **str**| Timestamps for the input locations in seconds since UNIX epoch. Timestamps need to be monotonically increasing. [ {timestamp};{timestamp}[;{timestamp} ...]  integer seconds since UNIX epoch | [optional] 
 **gaps** | **str**| Allows the input track splitting based on huge timestamp gaps between points. [ split (default), ignore ] | [optional] [default to &#39;&quot;split&quot;&#39;]
 **tidy** | **str**| Allows the input track modification to obtain better matching quality for noisy tracks. [ true, false (default) ] | [optional] [default to &#39;&quot;false&quot;&#39;]
 **waypoints** | **str**| Treats input coordinates indicated by given indices as waypoints in returned Match object. Default is to treat all input coordinates as waypoints. [ {index};{index};{index}... ] | [optional] 

### Return type

[**DirectionsMatching**](DirectionsMatching.md)

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

