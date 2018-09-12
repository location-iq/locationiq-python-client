# locationiq.BalanceApi

All URIs are relative to *https://eu1.locationiq.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balance**](BalanceApi.md#balance) | **GET** /balance.php | 


# **balance**
> Balance balance()



The Balance API provides a count of request credits left in the user's account for the day. Balance is reset at midnight UTC everyday (00:00 UTC).

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
api_instance = locationiq.BalanceApi(locationiq.ApiClient(configuration))

try:
    api_response = api_instance.balance()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BalanceApi->balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Balance**](Balance.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

