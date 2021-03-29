# DataCreationDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **str** |  | [optional] 
**_date** | **str** | date or datetime | 
**timezone** | **str** | to specify if the offset is not in the date and if the timezone is different from the default one | [optional] 
**scientific_objects** | **list[str]** | scientific objects URIs on which the data have been collected | [optional] 
**variable** | **str** | variable URI | 
**value** | **object** | can be decimal, integer, boolean, string or date | 
**confidence** | **float** | confidence index | [optional] 
**provenance** | [**DataProvenanceModel**](DataProvenanceModel.md) |  | 
**metadata** | **dict(str, object)** | key-value system to store additional information that can be used to query data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

