# opensilexClientTools.DevicesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DevicesApi.md#create_device) | **POST** /core/devices | Create a device
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /core/devices/{uri} | Delete a device
[**export_devices**](DevicesApi.md#export_devices) | **GET** /core/devices/export | export devices
[**export_list**](DevicesApi.md#export_list) | **GET** /core/devices/exportList | export devices
[**get_device**](DevicesApi.md#get_device) | **GET** /core/devices/{uri} | Get device detail
[**get_device_data_files_provenances**](DevicesApi.md#get_device_data_files_provenances) | **GET** /core/devices/{uri}/datafiles/provenances | Get provenances of datafiles linked to this device
[**get_device_data_provenances**](DevicesApi.md#get_device_data_provenances) | **GET** /core/devices/{uri}/data/provenances | Get provenances of data that have been measured on this device
[**get_device_variables**](DevicesApi.md#get_device_variables) | **GET** /core/devices/{uri}/variables | Get variables measured by the device
[**search_device_data**](DevicesApi.md#search_device_data) | **GET** /core/devices/{uri}/data | Search device data
[**search_devices**](DevicesApi.md#search_devices) | **GET** /core/devices | Search devices
[**update_device**](DevicesApi.md#update_device) | **PUT** /core/devices | Update a device


# **create_device**
> ObjectUriResponse create_device(authorization, body=body, check_only=check_only, accept_language=accept_language)

Create a device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
body = opensilexClientTools.DeviceCreationDTO() # DeviceCreationDTO | Device description (optional)
check_only = false # bool | Checking only (optional) (default to false)


try:
    # Create a device
    api_response = api_instance.create_device(body=body, check_only=check_only, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->create_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCreationDTO**](DeviceCreationDTO.md)| Device description | [optional] 
 **check_only** | **bool**| Checking only | [optional] [default to false]


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> ObjectUriResponse delete_device(uri, authorization, accept_language=accept_language)

Delete a device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | Device URI


try:
    # Delete a device
    api_response = api_instance.delete_device(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_devices**
> export_devices(authorization, name_pattern=name_pattern, rdf_type=rdf_type, year=year, existence_date=existence_date, brand_pattern=brand_pattern, model_pattern=model_pattern, serial_number_pattern=serial_number_pattern, metadata=metadata, accept_language=accept_language)

export devices



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
name_pattern = '.*' # str | Regex pattern for filtering by name (optional) (default to .*)
rdf_type = '\"vocabulary:SensingDevice\"' # str | RDF type filter (optional)
year = 2017 # int | Search by year (optional)
existence_date = '2013-10-20' # date | Date to filter device existence (optional)
brand_pattern = '\".*\"' # str | Regex pattern for filtering by brand (optional)
model_pattern = '\".*\"' # str | Regex pattern for filtering by model (optional)
serial_number_pattern = '\".*\"' # str | Regex pattern for filtering by serial number (optional)
metadata = '\"{}\"' # str | Search by metadata (optional)


try:
    # export devices
    api_instance.export_devices(name_pattern=name_pattern, rdf_type=rdf_type, year=year, existence_date=existence_date, brand_pattern=brand_pattern, model_pattern=model_pattern, serial_number_pattern=serial_number_pattern, metadata=metadata, )
except ApiException as e:
    print("Exception when calling DevicesApi->export_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_pattern** | **str**| Regex pattern for filtering by name | [optional] [default to .*]
 **rdf_type** | **str**| RDF type filter | [optional] 
 **year** | **int**| Search by year | [optional] 
 **existence_date** | **date**| Date to filter device existence | [optional] 
 **brand_pattern** | **str**| Regex pattern for filtering by brand | [optional] 
 **model_pattern** | **str**| Regex pattern for filtering by model | [optional] 
 **serial_number_pattern** | **str**| Regex pattern for filtering by serial number | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_list**
> export_list(authorization, devices_list=devices_list, accept_language=accept_language)

export devices



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
devices_list = ['\"dev:set/sensor_01\"'] # list[str] | List of device URI (optional)


try:
    # export devices
    api_instance.export_list(devices_list=devices_list, )
except ApiException as e:
    print("Exception when calling DevicesApi->export_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices_list** | [**list[str]**](str.md)| List of device URI | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceGetDetailsDTO get_device(uri, authorization, accept_language=accept_language)

Get device detail



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | device URI


try:
    # Get device detail
    api_response = api_instance.get_device(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| device URI | 


### Return type

[**DeviceGetDetailsDTO**](DeviceGetDetailsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_files_provenances**
> list[ProvenanceGetDTO] get_device_data_files_provenances(uri, authorization, accept_language=accept_language)

Get provenances of datafiles linked to this device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | Device URI


try:
    # Get provenances of datafiles linked to this device
    api_response = api_instance.get_device_data_files_provenances(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_data_files_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_data_provenances**
> list[ProvenanceGetDTO] get_device_data_provenances(uri, authorization, accept_language=accept_language)

Get provenances of data that have been measured on this device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | Device URI


try:
    # Get provenances of data that have been measured on this device
    api_response = api_instance.get_device_data_provenances(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_data_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_variables**
> list[NamedResourceDTO] get_device_variables(uri, authorization, accept_language=accept_language)

Get variables measured by the device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | Device URI


try:
    # Get variables measured by the device
    api_response = api_instance.get_device_variables(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_device_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_device_data**
> list[DataGetDTO] search_device_data(uri, authorization, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search device data



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
uri = '\"http://example.com/\"' # str | Device URI
start_date = '\"2020-08-21T00:00:00+01:00\"' # str | Search by minimal date (optional)
end_date = '\"2020-09-21T00:00:00+01:00\"' # str | Search by maximal date (optional)
timezone = '\"Europe/Paris\"' # str | Precise the timezone corresponding to the given dates (optional)
experiment = ['\"http://opensilex/set/experiments/ZA17\"'] # list[str] | Search by experiment uris (optional)
variable = ['\"http://opensilex.dev/variable#variable.2020-08-21_11-21-23entity6_method6_quality6_unit6\"'] # list[str] | Search by variables (optional)
min_confidence = 0.5 # float | Search by minimal confidence index (optional)
max_confidence = 0.5 # float | Search by maximal confidence index (optional)
provenance = ['\"http://opensilex.dev/provenance/1598001689415\"'] # list[str] | Search by provenance uri (optional)
metadata = '\"{ \\\"LabelView\\\" : \\\"side90\\\",\\n\\\"paramA\\\" : \\\"90\\\"}\"' # str | Search by metadata (optional)
order_by = ['\"date=desc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search device data
    api_response = api_instance.search_device_data(uri, start_date=start_date, end_date=end_date, timezone=timezone, experiment=experiment, variable=variable, min_confidence=min_confidence, max_confidence=max_confidence, provenance=provenance, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->search_device_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Device URI | 
 **start_date** | **str**| Search by minimal date | [optional] 
 **end_date** | **str**| Search by maximal date | [optional] 
 **timezone** | **str**| Precise the timezone corresponding to the given dates | [optional] 
 **experiment** | [**list[str]**](str.md)| Search by experiment uris | [optional] 
 **variable** | [**list[str]**](str.md)| Search by variables | [optional] 
 **min_confidence** | **float**| Search by minimal confidence index | [optional] 
 **max_confidence** | **float**| Search by maximal confidence index | [optional] 
 **provenance** | [**list[str]**](str.md)| Search by provenance uri | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DataGetDTO]**](DataGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_devices**
> list[DeviceGetDTO] search_devices(authorization, name_pattern=name_pattern, rdf_type=rdf_type, year=year, existence_date=existence_date, brand_pattern=brand_pattern, model_pattern=model_pattern, serial_number_pattern=serial_number_pattern, metadata=metadata, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search devices



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
name_pattern = '.*' # str | Regex pattern for filtering by name (optional) (default to .*)
rdf_type = '\"vocabulary:SensingDevice\"' # str | RDF type filter (optional)
year = 2017 # int | Search by year (optional)
existence_date = '2013-10-20' # date | Date to filter device existence (optional)
brand_pattern = '\".*\"' # str | Regex pattern for filtering by brand (optional)
model_pattern = '\".*\"' # str | Regex pattern for filtering by model (optional)
serial_number_pattern = '\".*\"' # str | Regex pattern for filtering by serial number (optional)
metadata = '\"{ \\\"Group\\\" : \\\"weather station\\\",\\n\\\"Group2\\\" : \\\"A\\\"}\"' # str | Search by metadata (optional)
order_by = ['\"namePattern=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search devices
    api_response = api_instance.search_devices(name_pattern=name_pattern, rdf_type=rdf_type, year=year, existence_date=existence_date, brand_pattern=brand_pattern, model_pattern=model_pattern, serial_number_pattern=serial_number_pattern, metadata=metadata, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->search_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_pattern** | **str**| Regex pattern for filtering by name | [optional] [default to .*]
 **rdf_type** | **str**| RDF type filter | [optional] 
 **year** | **int**| Search by year | [optional] 
 **existence_date** | **date**| Date to filter device existence | [optional] 
 **brand_pattern** | **str**| Regex pattern for filtering by brand | [optional] 
 **model_pattern** | **str**| Regex pattern for filtering by model | [optional] 
 **serial_number_pattern** | **str**| Regex pattern for filtering by serial number | [optional] 
 **metadata** | **str**| Search by metadata | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[DeviceGetDTO]**](DeviceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> ObjectUriResponse update_device(body, authorization, accept_language=accept_language)

Update a device



### Example
```python
from __future__ import print_function
import time
import opensilexClientTools
from opensilexClientTools.rest import ApiException
from pprint import pprint

# create an instance of the API class
pythonClient = opensilexClientTools.ApiClient()
pythonClient.connect_to_phis_ws(api_id="ws_custom",username="guest@opensilex.org",password="guest",host="https://localhost")
api_instance = opensilexClientTools.DevicesApi(pythonClient)
body = opensilexClientTools.DeviceCreationDTO() # DeviceCreationDTO | Device description


try:
    # Update a device
    api_response = api_instance.update_device(body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->update_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeviceCreationDTO**](DeviceCreationDTO.md)| Device description | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
