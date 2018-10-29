# locationiq.ReverseApi

All URIs are relative to *https://eu1.locationiq.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reverse**](ReverseApi.md#reverse) | **GET** /reverse.php | Reverse Geocoding


# **reverse**
> Location reverse(lat, lon, format, normalizecity, addressdetails=addressdetails, accept_language=accept_language, namedetails=namedetails, extratags=extratags)

Reverse Geocoding

Reverse geocoding is the process of converting a coordinate or location (latitude, longitude) to a readable address or place name. This permits the identification of nearby street addresses, places, and/or area subdivisions such as a neighborhood, county, state, or country.

### Example
```python
from __future__ import print_function
import time
import locationiq
from locationiq.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
configuration = locationiq.Configuration()
configuration.api_key['key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['key'] = 'Bearer'

# create an instance of the API class
api_instance = locationiq.ReverseApi(locationiq.ApiClient(configuration))
lat = 17.24 # float | Latitude of the location to generate an address for.
lon = 74.25 # float | Longitude of the location to generate an address for.
format = "json" # str | Format to geocode. Only JSON supported for SDKs
normalizecity = 1 # int | Normalizes village to city level data to city
addressdetails = 1 # int | Include a breakdown of the address into elements. Defaults to 1. (optional) (default to 1)
accept_language = "en" # str | Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language=native (optional)
namedetails = 0 # int | Include a list of alternative names in the results. These may include language variants, references, operator and brand. (optional)
extratags = 0 # int | Include additional information in the result if available, e.g. wikipedia link, opening hours. (optional)

try:
    # Reverse Geocoding
    api_response = api_instance.reverse(lat, lon, format, normalizecity, addressdetails=addressdetails, accept_language=accept_language, namedetails=namedetails, extratags=extratags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReverseApi->reverse: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude of the location to generate an address for. | 
 **lon** | **float**| Longitude of the location to generate an address for. | 
 **format** | **str**| Format to geocode. Only JSON supported for SDKs | 
 **normalizecity** | **int**| Normalizes village to city level data to city | 
 **addressdetails** | **int**| Include a breakdown of the address into elements. Defaults to 1. | [optional] [default to 1]
 **accept_language** | **str**| Preferred language order for showing search results, overrides the value specified in the Accept-Language HTTP header. Defaults to en. To use native language for the response when available, use accept-language&#x3D;native | [optional] 
 **namedetails** | **int**| Include a list of alternative names in the results. These may include language variants, references, operator and brand. | [optional] 
 **extratags** | **int**| Include additional information in the result if available, e.g. wikipedia link, opening hours. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

