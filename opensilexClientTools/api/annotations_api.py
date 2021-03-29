# coding: utf-8

"""
    OpenSilex API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: INSTANCE-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from opensilexClientTools.api_client import ApiClient


class AnnotationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def count_annotations(self, **kwargs):  # noqa: E501
        """Count annotations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_annotations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str target: Target URI
        :param str accept_language: Request accepted language
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.count_annotations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.count_annotations_with_http_info(**kwargs)  # noqa: E501
            return data

    def count_annotations_with_http_info(self, **kwargs):  # noqa: E501
        """Count annotations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_annotations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str target: Target URI
        :param str accept_language: Request accepted language
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['target', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count_annotations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'target' in params:
            query_params.append(('target', params['target']))  # noqa: E501

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations/count', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_annotation(self, **kwargs):  # noqa: E501
        """Create an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param AnnotationCreationDTO body:
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_annotation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_annotation_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_annotation_with_http_info(self, **kwargs):  # noqa: E501
        """Create an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_annotation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param AnnotationCreationDTO body:
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_annotation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectUriResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_annotation(self, uri, **kwargs):  # noqa: E501
        """Delete an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Annotation URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_annotation_with_http_info(uri, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_annotation_with_http_info(uri, **kwargs)  # noqa: E501
            return data

    def delete_annotation_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Delete an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_annotation_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Annotation URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `delete_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uri' in params:
            path_params['uri'] = params['uri']  # noqa: E501

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations/{uri}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectUriResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_annotation(self, uri, **kwargs):  # noqa: E501
        """Get an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Event URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: AnnotationGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_annotation_with_http_info(uri, **kwargs)  # noqa: E501
        else:
            (data) = self.get_annotation_with_http_info(uri, **kwargs)  # noqa: E501
            return data

    def get_annotation_with_http_info(self, uri, **kwargs):  # noqa: E501
        """Get an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_annotation_with_http_info(uri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uri: Event URI (required)
        :param str authorization: Authentication token (required)
        :param str accept_language: Request accepted language
        :return: AnnotationGetDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uri', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_annotation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `get_annotation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uri' in params:
            path_params['uri'] = params['uri']  # noqa: E501

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations/{uri}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnotationGetDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_annotations(self, **kwargs):  # noqa: E501
        """Search annotations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_annotations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str description: Description (regex)
        :param str target: Target URI
        :param str motivation: Motivation URI
        :param str author: Author URI
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[AnnotationGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_annotations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_annotations_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_annotations_with_http_info(self, **kwargs):  # noqa: E501
        """Search annotations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_annotations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str description: Description (regex)
        :param str target: Target URI
        :param str motivation: Motivation URI
        :param str author: Author URI
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[AnnotationGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['description', 'target', 'motivation', 'author', 'order_by', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_annotations" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `search_annotations`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `search_annotations`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'description' in params:
            query_params.append(('description', params['description']))  # noqa: E501
        if 'target' in params:
            query_params.append(('target', params['target']))  # noqa: E501
        if 'motivation' in params:
            query_params.append(('motivation', params['motivation']))  # noqa: E501
        if 'author' in params:
            query_params.append(('author', params['author']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
            collection_formats['order_by'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AnnotationGetDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_motivations(self, **kwargs):  # noqa: E501
        """Search motivations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_motivations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str name: Motivation name regex pattern
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[MotivationGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_motivations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.search_motivations_with_http_info(**kwargs)  # noqa: E501
            return data

    def search_motivations_with_http_info(self, **kwargs):  # noqa: E501
        """Search motivations  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_motivations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param str name: Motivation name regex pattern
        :param list[str] order_by: List of fields to sort as an array of fieldName=asc|desc
        :param int page: Page number
        :param int page_size: Page size
        :param str accept_language: Request accepted language
        :return: list[MotivationGetDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'order_by', 'page', 'page_size', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_motivations" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `search_motivations`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'page_size' in params and params['page_size'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `search_motivations`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501
            collection_formats['order_by'] = 'multi'  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations/motivations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MotivationGetDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_annotation(self, **kwargs):  # noqa: E501
        """Update an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param AnnotationUpdateDTO body: Annotation description
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_annotation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.update_annotation_with_http_info(**kwargs)  # noqa: E501
            return data

    def update_annotation_with_http_info(self, **kwargs):  # noqa: E501
        """Update an annotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_annotation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authentication token (required)
        :param AnnotationUpdateDTO body: Annotation description
        :param str accept_language: Request accepted language
        :return: ObjectUriResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', ]  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_annotation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        #if 'authorization' in params:
        #    header_params['Authorization'] = params['authorization']  # noqa: E501
        #if 'accept_language' in params:
        #    header_params['Accept-Language'] = params['accept_language']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/core/annotations', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ObjectUriResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
