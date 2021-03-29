# opensilexClientTools.ScientificObjectsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scientific_object**](ScientificObjectsApi.md#create_scientific_object) | **POST** /core/scientific_objects | Create a scientific object for the given experiment
[**delete_scientific_object**](ScientificObjectsApi.md#delete_scientific_object) | **DELETE** /core/scientific_objects/{uri} | Delete a scientific object
[**export_csv**](ScientificObjectsApi.md#export_csv) | **POST** /core/scientific_objects/export | Export a given list of scientific object URIs to csv data file
[**get_scientific_object_data_files_provenances**](ScientificObjectsApi.md#get_scientific_object_data_files_provenances) | **GET** /core/scientific_objects/{uri}/datafiles/provenances | Get provenances of datafiles linked to this scientific object
[**get_scientific_object_data_provenances**](ScientificObjectsApi.md#get_scientific_object_data_provenances) | **GET** /core/scientific_objects/{uri}/data/provenances | Get provenances of data that have been measured on this scientific object
[**get_scientific_object_detail**](ScientificObjectsApi.md#get_scientific_object_detail) | **GET** /core/scientific_objects/{uri} | Get scientific object detail
[**get_scientific_object_detail_by_experiments**](ScientificObjectsApi.md#get_scientific_object_detail_by_experiments) | **GET** /core/scientific_objects/{uri}/experiments | Get scientific object detail for each experiments, a null value for experiment in response means a properties defined outside of any experiment (shared object).
[**get_scientific_object_variables**](ScientificObjectsApi.md#get_scientific_object_variables) | **GET** /core/scientific_objects/{uri}/variables | Get variables measured on this scientific object
[**get_scientific_objects_children**](ScientificObjectsApi.md#get_scientific_objects_children) | **GET** /core/scientific_objects/children | Get list of scientific object children
[**get_scientific_objects_list_by_uris**](ScientificObjectsApi.md#get_scientific_objects_list_by_uris) | **POST** /core/scientific_objects/by_uris | Get scientific objet list of a given experiment URI
[**get_used_types**](ScientificObjectsApi.md#get_used_types) | **GET** /core/scientific_objects/used_types | get used scientific object types
[**import_csv**](ScientificObjectsApi.md#import_csv) | **POST** /core/scientific_objects/import | Import a CSV file for the given experiment URI and scientific object type.
[**search_scientific_objects**](ScientificObjectsApi.md#search_scientific_objects) | **GET** /core/scientific_objects | Search list of scientific objects
[**search_scientific_objects_with_geometry_list_by_uris**](ScientificObjectsApi.md#search_scientific_objects_with_geometry_list_by_uris) | **GET** /core/scientific_objects/geometry | Get scientific objet list with geometry of a given experiment URI
[**update_scientific_object**](ScientificObjectsApi.md#update_scientific_object) | **PUT** /core/scientific_objects | Update a scientific object for the given experiment
[**validate_csv2**](ScientificObjectsApi.md#validate_csv2) | **POST** /core/scientific_objects/import_validation | Validate a CSV file for the given experiment URI and scientific object type.


# **create_scientific_object**
> ObjectUriResponse create_scientific_object(body, authorization, accept_language=accept_language)

Create a scientific object for the given experiment



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
body = opensilexClientTools.ScientificObjectCreationDTO() # ScientificObjectCreationDTO | Scientific object description


try:
    # Create a scientific object for the given experiment
    api_response = api_instance.create_scientific_object(body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->create_scientific_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScientificObjectCreationDTO**](ScientificObjectCreationDTO.md)| Scientific object description | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scientific_object**
> ObjectUriResponse delete_scientific_object(uri, authorization, experiment=experiment, accept_language=accept_language)

Delete a scientific object



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | scientific object URI
experiment = '\"http://example.com/\"' # str | Experiment URI (optional)


try:
    # Delete a scientific object
    api_response = api_instance.delete_scientific_object(uri, experiment=experiment, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->delete_scientific_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| scientific object URI | 
 **experiment** | **str**| Experiment URI | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_csv**
> export_csv(authorization, body=body, accept_language=accept_language)

Export a given list of scientific object URIs to csv data file



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
body = opensilexClientTools.ScientificObjectCsvExportDTO() # ScientificObjectCsvExportDTO | CSV export configuration (optional)


try:
    # Export a given list of scientific object URIs to csv data file
    api_instance.export_csv(body=body, )
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->export_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScientificObjectCsvExportDTO**](ScientificObjectCsvExportDTO.md)| CSV export configuration | [optional] 


### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_object_data_files_provenances**
> list[ProvenanceGetDTO] get_scientific_object_data_files_provenances(uri, authorization, accept_language=accept_language)

Get provenances of datafiles linked to this scientific object



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | Scientific Object URI


try:
    # Get provenances of datafiles linked to this scientific object
    api_response = api_instance.get_scientific_object_data_files_provenances(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_object_data_files_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Scientific Object URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_object_data_provenances**
> list[ProvenanceGetDTO] get_scientific_object_data_provenances(uri, authorization, accept_language=accept_language)

Get provenances of data that have been measured on this scientific object



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | Scientific Object URI


try:
    # Get provenances of data that have been measured on this scientific object
    api_response = api_instance.get_scientific_object_data_provenances(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_object_data_provenances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Scientific Object URI | 


### Return type

[**list[ProvenanceGetDTO]**](ProvenanceGetDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_object_detail**
> ScientificObjectDetailDTO get_scientific_object_detail(uri, authorization, experiment=experiment, accept_language=accept_language)

Get scientific object detail



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://opensilex.org/set/scientific-objects/so-1357dz_pg_34zm4384wwveg_323_37arch2017-03-30\"' # str | scientific object URI
experiment = '\"http://opensilex.org/set/experiments/21ik1_cims-on\"' # str | Experiment URI (optional)


try:
    # Get scientific object detail
    api_response = api_instance.get_scientific_object_detail(uri, experiment=experiment, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_object_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| scientific object URI | 
 **experiment** | **str**| Experiment URI | [optional] 


### Return type

[**ScientificObjectDetailDTO**](ScientificObjectDetailDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_object_detail_by_experiments**
> list[ScientificObjectDetailByExperimentsDTO] get_scientific_object_detail_by_experiments(uri, authorization, accept_language=accept_language)

Get scientific object detail for each experiments, a null value for experiment in response means a properties defined outside of any experiment (shared object).



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | scientific object URI


try:
    # Get scientific object detail for each experiments, a null value for experiment in response means a properties defined outside of any experiment (shared object).
    api_response = api_instance.get_scientific_object_detail_by_experiments(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_object_detail_by_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| scientific object URI | 


### Return type

[**list[ScientificObjectDetailByExperimentsDTO]**](ScientificObjectDetailByExperimentsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_object_variables**
> list[NamedResourceDTO] get_scientific_object_variables(uri, authorization, accept_language=accept_language)

Get variables measured on this scientific object



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
uri = '\"http://example.com/\"' # str | Scientific Object URI


try:
    # Get variables measured on this scientific object
    api_response = api_instance.get_scientific_object_variables(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_object_variables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Scientific Object URI | 


### Return type

[**list[NamedResourceDTO]**](NamedResourceDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_objects_children**
> list[ScientificObjectNodeWithChildrenDTO] get_scientific_objects_children(authorization, parent=parent, experiment=experiment, facility=facility, page=page, page_size=page_size, accept_language=accept_language)

Get list of scientific object children



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
parent = '\"http://example.com/\"' # str | Parent object URI (optional)
experiment = '\"http://example.com/\"' # str | Experiment URI (optional)
facility = '\"diaphen:serre-2\"' # str | Facility (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Get list of scientific object children
    api_response = api_instance.get_scientific_objects_children(parent=parent, experiment=experiment, facility=facility, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_objects_children: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent** | **str**| Parent object URI | [optional] 
 **experiment** | **str**| Experiment URI | [optional] 
 **facility** | **str**| Facility | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ScientificObjectNodeWithChildrenDTO]**](ScientificObjectNodeWithChildrenDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scientific_objects_list_by_uris**
> list[ScientificObjectNodeDTO] get_scientific_objects_list_by_uris(authorization, experiment=experiment, body=body, accept_language=accept_language)

Get scientific objet list of a given experiment URI



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
experiment = '\"http://example.com/\"' # str | Experiment URI (optional)
body = [opensilexClientTools.list[str]()] # list[str] | Scientific object uris (optional)


try:
    # Get scientific objet list of a given experiment URI
    api_response = api_instance.get_scientific_objects_list_by_uris(experiment=experiment, body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_scientific_objects_list_by_uris: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| Experiment URI | [optional] 
 **body** | **list[str]**| Scientific object uris | [optional] 


### Return type

[**list[ScientificObjectNodeDTO]**](ScientificObjectNodeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_used_types**
> list[ListItemDTO] get_used_types(authorization, experiment=experiment, accept_language=accept_language)

get used scientific object types



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
experiment = '\"http://example.com/\"' # str | Experiment URI (optional)


try:
    # get used scientific object types
    api_response = api_instance.get_used_types(experiment=experiment, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->get_used_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| Experiment URI | [optional] 


### Return type

[**list[ListItemDTO]**](ListItemDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_csv**
> CSVValidationDTO import_csv(description, file, authorization, accept_language=accept_language)

Import a CSV file for the given experiment URI and scientific object type.



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
description = 'description_example' # str | File description with metadata
file = '/path/to/file.txt' # file | Data file


try:
    # Import a CSV file for the given experiment URI and scientific object type.
    api_response = api_instance.import_csv(description, file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->import_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| File description with metadata | 
 **file** | **file**| Data file | 


### Return type

[**CSVValidationDTO**](CSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scientific_objects**
> list[ScientificObjectNodeDTO] search_scientific_objects(authorization, experiment=experiment, rdf_types=rdf_types, name=name, parent=parent, germplasm=germplasm, factor_levels=factor_levels, facility=facility, existence_date=existence_date, creation_date=creation_date, order_by=order_by, page=page, page_size=page_size, accept_language=accept_language)

Search list of scientific objects



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
experiment = '\"http://example.com/\"' # str | Experiment URI (optional)
rdf_types = ['\"vocabulary:Plant\"'] # list[str] | RDF type filter (optional)
name = '.*' # str | Regex pattern for filtering by name (optional) (default to .*)
parent = '\"http://example.com/\"' # str | Parent URI (optional)
germplasm = '\"http://aims.fao.org/aos/agrovoc/c_1066\"' # str | Germplasm URI (optional)
factor_levels = ['\"vocabulary:IrrigationStress\"'] # list[str] | Factor levels URI (optional)
facility = '\"diaphen:serre-2\"' # str | Facility (optional)
existence_date = '2013-10-20' # date | Date to filter object existence (optional)
creation_date = '2013-10-20' # date | Date to filter object creation (optional)
order_by = ['\"name=asc\"'] # list[str] | List of fields to sort as an array of fieldName=asc|desc (optional)
page = 0 # int | Page number (optional) (default to 0)
page_size = 20 # int | Page size (optional) (default to 20)


try:
    # Search list of scientific objects
    api_response = api_instance.search_scientific_objects(experiment=experiment, rdf_types=rdf_types, name=name, parent=parent, germplasm=germplasm, factor_levels=factor_levels, facility=facility, existence_date=existence_date, creation_date=creation_date, order_by=order_by, page=page, page_size=page_size, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->search_scientific_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| Experiment URI | [optional] 
 **rdf_types** | [**list[str]**](str.md)| RDF type filter | [optional] 
 **name** | **str**| Regex pattern for filtering by name | [optional] [default to .*]
 **parent** | **str**| Parent URI | [optional] 
 **germplasm** | **str**| Germplasm URI | [optional] 
 **factor_levels** | [**list[str]**](str.md)| Factor levels URI | [optional] 
 **facility** | **str**| Facility | [optional] 
 **existence_date** | **date**| Date to filter object existence | [optional] 
 **creation_date** | **date**| Date to filter object creation | [optional] 
 **order_by** | [**list[str]**](str.md)| List of fields to sort as an array of fieldName&#x3D;asc|desc | [optional] 
 **page** | **int**| Page number | [optional] [default to 0]
 **page_size** | **int**| Page size | [optional] [default to 20]


### Return type

[**list[ScientificObjectNodeDTO]**](ScientificObjectNodeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scientific_objects_with_geometry_list_by_uris**
> list[ScientificObjectNodeDTO] search_scientific_objects_with_geometry_list_by_uris(experiment, authorization, accept_language=accept_language)

Get scientific objet list with geometry of a given experiment URI



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
experiment = '\"http://example.com/\"' # str | Context URI


try:
    # Get scientific objet list with geometry of a given experiment URI
    api_response = api_instance.search_scientific_objects_with_geometry_list_by_uris(experiment, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->search_scientific_objects_with_geometry_list_by_uris: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | **str**| Context URI | 


### Return type

[**list[ScientificObjectNodeDTO]**](ScientificObjectNodeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scientific_object**
> ObjectUriResponse update_scientific_object(body, authorization, accept_language=accept_language)

Update a scientific object for the given experiment



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
body = opensilexClientTools.ScientificObjectCreationDTO() # ScientificObjectCreationDTO | Scientific object description


try:
    # Update a scientific object for the given experiment
    api_response = api_instance.update_scientific_object(body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->update_scientific_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScientificObjectCreationDTO**](ScientificObjectCreationDTO.md)| Scientific object description | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_csv2**
> CSVValidationDTO validate_csv2(description, file, authorization, accept_language=accept_language)

Validate a CSV file for the given experiment URI and scientific object type.



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
api_instance = opensilexClientTools.ScientificObjectsApi(pythonClient)
description = 'description_example' # str | File description with metadata
file = '/path/to/file.txt' # file | Data file


try:
    # Validate a CSV file for the given experiment URI and scientific object type.
    api_response = api_instance.validate_csv2(description, file, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScientificObjectsApi->validate_csv2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**| File description with metadata | 
 **file** | **file**| Data file | 


### Return type

[**CSVValidationDTO**](CSVValidationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
