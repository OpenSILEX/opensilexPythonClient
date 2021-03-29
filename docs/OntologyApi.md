# opensilexClientTools.OntologyApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_class_property_restriction**](OntologyApi.md#add_class_property_restriction) | **POST** /ontology/rdf_type_property_restriction | Add a rdf type property restriction
[**check_ur_is_types**](OntologyApi.md#check_ur_is_types) | **GET** /ontology/check_rdf_types | 
[**create_property**](OntologyApi.md#create_property) | **POST** /ontology/property | Create a RDF property
[**delete_class_property_restriction**](OntologyApi.md#delete_class_property_restriction) | **DELETE** /ontology/rdf_type_property_restriction | Delete a rdf type property restriction
[**delete_property**](OntologyApi.md#delete_property) | **DELETE** /ontology/property | Delete a property
[**get_classes**](OntologyApi.md#get_classes) | **GET** /ontology/rdf_types | Return classes models definitions with properties for a list of rdt types
[**get_data_properties**](OntologyApi.md#get_data_properties) | **GET** /ontology/data_properties | Search data properties tree
[**get_object_properties**](OntologyApi.md#get_object_properties) | **GET** /ontology/object_properties | Search object properties tree
[**get_properties**](OntologyApi.md#get_properties) | **GET** /ontology/properties | Search properties tree
[**get_property**](OntologyApi.md#get_property) | **GET** /ontology/property | Return property model definition detail
[**get_rdf_type**](OntologyApi.md#get_rdf_type) | **GET** /ontology/rdf_type | Return class model definition with properties
[**get_sub_classes_of**](OntologyApi.md#get_sub_classes_of) | **GET** /ontology/subclasses_of | Search sub-classes tree of an RDF class
[**get_uri_label**](OntologyApi.md#get_uri_label) | **GET** /ontology/uri_label | Return associated rdfs:label of an uri if exists
[**update_class_property_restriction**](OntologyApi.md#update_class_property_restriction) | **PUT** /ontology/rdf_type_property_restriction | Update a rdf type property restriction
[**update_property**](OntologyApi.md#update_property) | **PUT** /ontology/property | Update a RDF property


# **add_class_property_restriction**
> ObjectUriResponse add_class_property_restriction(authorization, body=body, accept_language=accept_language)

Add a rdf type property restriction



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
body = opensilexClientTools.OWLClassPropertyRestrictionDTO() # OWLClassPropertyRestrictionDTO | Property description (optional)


try:
    # Add a rdf type property restriction
    api_response = api_instance.add_class_property_restriction(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->add_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OWLClassPropertyRestrictionDTO**](OWLClassPropertyRestrictionDTO.md)| Property description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_ur_is_types**
> list[URITypesDTO] check_ur_is_types(uris, rdf_types, authorization, accept_language=accept_language)





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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
uris = ['uris_example'] # list[str] | URIs
rdf_types = ['rdf_types_example'] # list[str] | rdf_types list you want to check on the given uris list


try:
    # 
    api_response = api_instance.check_ur_is_types(uris, rdf_types, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->check_ur_is_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uris** | [**list[str]**](str.md)| URIs | 
 **rdf_types** | [**list[str]**](str.md)| rdf_types list you want to check on the given uris list | 


### Return type

[**list[URITypesDTO]**](URITypesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_property**
> ObjectUriResponse create_property(authorization, body=body, accept_language=accept_language)

Create a RDF property



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
body = opensilexClientTools.RDFPropertyDTO() # RDFPropertyDTO | Property description (optional)


try:
    # Create a RDF property
    api_response = api_instance.create_property(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->create_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RDFPropertyDTO**](RDFPropertyDTO.md)| Property description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_class_property_restriction**
> ObjectUriResponse delete_class_property_restriction(rdf_type, property_uri, authorization, accept_language=accept_language)

Delete a rdf type property restriction



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type
property_uri = 'property_uri_example' # str | Property URI


try:
    # Delete a rdf type property restriction
    api_response = api_instance.delete_class_property_restriction(rdf_type, property_uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->delete_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type | 
 **property_uri** | **str**| Property URI | 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_property**
> ObjectUriResponse delete_property(authorization, property_uri=property_uri, property_type=property_type, accept_language=accept_language)

Delete a property



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
property_uri = 'property_uri_example' # str | Property URI (optional)
property_type = 'property_type_example' # str | Property type (optional)


try:
    # Delete a property
    api_response = api_instance.delete_property(property_uri=property_uri, property_type=property_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->delete_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_uri** | **str**| Property URI | [optional] 
 **property_type** | **str**| Property type | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_classes**
> list[RDFTypeDTO] get_classes(rdf_type, authorization, parent_type=parent_type, accept_language=accept_language)

Return classes models definitions with properties for a list of rdt types



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
rdf_type = ['rdf_type_example'] # list[str] | RDF classes URI
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)


try:
    # Return classes models definitions with properties for a list of rdt types
    api_response = api_instance.get_classes(rdf_type, parent_type=parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_classes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | [**list[str]**](str.md)| RDF classes URI | 
 **parent_type** | **str**| Parent RDF class URI | [optional] 


### Return type

[**list[RDFTypeDTO]**](RDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_properties**
> list[ResourceTreeDTO] get_data_properties(authorization, domain=domain, accept_language=accept_language)

Search data properties tree



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI (optional)


try:
    # Search data properties tree
    api_response = api_instance.get_data_properties(domain=domain, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_data_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object_properties**
> list[ResourceTreeDTO] get_object_properties(authorization, domain=domain, accept_language=accept_language)

Search object properties tree



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI (optional)


try:
    # Search object properties tree
    api_response = api_instance.get_object_properties(domain=domain, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_object_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> list[ResourceTreeDTO] get_properties(authorization, domain=domain, accept_language=accept_language)

Search properties tree



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
domain = 'domain_example' # str | Domain URI (optional)


try:
    # Search properties tree
    api_response = api_instance.get_properties(domain=domain, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain URI | [optional] 


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_property**
> RDFPropertyDTO get_property(authorization, uri=uri, rdf_type=rdf_type, domain_rdf_type=domain_rdf_type, accept_language=accept_language)

Return property model definition detail



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
uri = 'uri_example' # str | Property URI (optional)
rdf_type = 'rdf_type_example' # str | Property type (optional)
domain_rdf_type = 'domain_rdf_type_example' # str | Property type (optional)


try:
    # Return property model definition detail
    api_response = api_instance.get_property(uri=uri, rdf_type=rdf_type, domain_rdf_type=domain_rdf_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| Property URI | [optional] 
 **rdf_type** | **str**| Property type | [optional] 
 **domain_rdf_type** | **str**| Property type | [optional] 


### Return type

[**RDFPropertyDTO**](RDFPropertyDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rdf_type**
> RDFTypeDTO get_rdf_type(rdf_type, authorization, parent_type=parent_type, accept_language=accept_language)

Return class model definition with properties



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
rdf_type = 'rdf_type_example' # str | RDF type URI
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)


try:
    # Return class model definition with properties
    api_response = api_instance.get_rdf_type(rdf_type, parent_type=parent_type, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_rdf_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rdf_type** | **str**| RDF type URI | 
 **parent_type** | **str**| Parent RDF class URI | [optional] 


### Return type

[**RDFTypeDTO**](RDFTypeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_classes_of**
> list[ResourceTreeDTO] get_sub_classes_of(authorization, parent_type=parent_type, ignore_root_classes=ignore_root_classes, accept_language=accept_language)

Search sub-classes tree of an RDF class



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
parent_type = 'parent_type_example' # str | Parent RDF class URI (optional)
ignore_root_classes = false # bool | Flag to determine if only sub-classes must be include in result (optional) (default to false)


try:
    # Search sub-classes tree of an RDF class
    api_response = api_instance.get_sub_classes_of(parent_type=parent_type, ignore_root_classes=ignore_root_classes, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_sub_classes_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_type** | **str**| Parent RDF class URI | [optional] 
 **ignore_root_classes** | **bool**| Flag to determine if only sub-classes must be include in result | [optional] [default to false]


### Return type

[**list[ResourceTreeDTO]**](ResourceTreeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uri_label**
> str get_uri_label(uri, authorization, accept_language=accept_language)

Return associated rdfs:label of an uri if exists



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
uri = 'uri_example' # str | URI to get label from


try:
    # Return associated rdfs:label of an uri if exists
    api_response = api_instance.get_uri_label(uri, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->get_uri_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uri** | **str**| URI to get label from | 


### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_class_property_restriction**
> ObjectUriResponse update_class_property_restriction(authorization, body=body, accept_language=accept_language)

Update a rdf type property restriction



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
body = opensilexClientTools.OWLClassPropertyRestrictionDTO() # OWLClassPropertyRestrictionDTO | Property description (optional)


try:
    # Update a rdf type property restriction
    api_response = api_instance.update_class_property_restriction(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->update_class_property_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OWLClassPropertyRestrictionDTO**](OWLClassPropertyRestrictionDTO.md)| Property description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_property**
> ObjectUriResponse update_property(authorization, body=body, accept_language=accept_language)

Update a RDF property



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
api_instance = opensilexClientTools.OntologyApi(pythonClient)
body = opensilexClientTools.RDFPropertyDTO() # RDFPropertyDTO | Property description (optional)


try:
    # Update a RDF property
    api_response = api_instance.update_property(body=body, )
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OntologyApi->update_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RDFPropertyDTO**](RDFPropertyDTO.md)| Property description | [optional] 


### Return type

[**ObjectUriResponse**](ObjectUriResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
