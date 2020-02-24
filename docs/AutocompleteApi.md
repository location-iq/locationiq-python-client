# openapi_client.AutocompleteApi

All URIs are relative to *https://eu1.locationiq.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](AutocompleteApi.md#autocomplete) | **GET** /autocomplete.php | 


# **autocomplete**
> list[object] autocomplete(q, normalizecity, limit=limit, viewbox=viewbox, bounded=bounded, countrycodes=countrycodes, accept_language=accept_language, tag=tag)



The Autocomplete API is a variant of the Search API that returns place predictions in response to an HTTP request.  The request specifies a textual search string and optional geographic bounds.  The service can be used to provide autocomplete functionality for text-based geographic searches, by returning places such as businesses, addresses and points of interest as a user types. The Autocomplete API can match on full words as well as substrings. Applications can therefore send queries as the user types, to provide on-the-fly place predictions.

### Example

* Api Key Authentication (key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: key
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# Defining host is optional and default to https://eu1.locationiq.com/v1
configuration.host = "https://eu1.locationiq.com/v1"
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AutocompleteApi(api_client)
    q = 'Empire state' # str | Address to geocode
normalizecity = 1 # int | For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs.
limit = 10 # int | Limit the number of returned results. Default is 10. (optional) (default to 10)
viewbox = '-132.84908,47.69382,-70.44674,30.82531' # str | The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - `max_lon,max_lat,min_lon,min_lat` or `min_lon,min_lat,max_lon,max_lat` - are accepted in any order as long as they span a real box.  (optional)
bounded = 1 # int | Restrict the results to only items contained with the viewbox (optional)
countrycodes = 'us' # str | Limit search to a list of countries. (optional)
accept_language = 'en' # str | Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native (optional)
tag = 'place' # str | Restricts the autocomplete search results to elements of specific OSM class and type.  Example - To restrict results to only class place and type city: tag=place:city, To restrict the results to all of OSM class place: tag=place (optional)

try:
    api_response = api_instance.autocomplete(q, normalizecity, limit=limit, viewbox=viewbox, bounded=bounded, countrycodes=countrycodes, accept_language=accept_language, tag=tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AutocompleteApi->autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Address to geocode | 
 **normalizecity** | **int**| For responses with no city value in the address section, the next available element in this order - city_district, locality, town, borough, municipality, village, hamlet, quarter, neighbourhood - from the address section will be normalized to city. Defaults to 1 for SDKs. | 
 **limit** | **int**| Limit the number of returned results. Default is 10. | [optional] [default to 10]
 **viewbox** | **str**| The preferred area to find search results.  To restrict results to those within the viewbox, use along with the bounded option. Tuple of 4 floats. Any two corner points of the box - &#x60;max_lon,max_lat,min_lon,min_lat&#x60; or &#x60;min_lon,min_lat,max_lon,max_lat&#x60; - are accepted in any order as long as they span a real box.  | [optional] 
 **bounded** | **int**| Restrict the results to only items contained with the viewbox | [optional] 
 **countrycodes** | **str**| Limit search to a list of countries. | [optional] 
 **accept_language** | **str**| Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language&#x3D;native | [optional] 
 **tag** | **str**| Restricts the autocomplete search results to elements of specific OSM class and type.  Example - To restrict results to only class place and type city: tag&#x3D;place:city, To restrict the results to all of OSM class place: tag&#x3D;place | [optional] 

### Return type

**list[object]**

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

