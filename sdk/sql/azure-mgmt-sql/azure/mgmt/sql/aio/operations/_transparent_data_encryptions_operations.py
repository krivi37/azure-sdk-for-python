# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._transparent_data_encryptions_operations import build_create_or_update_request, build_get_request, build_list_by_database_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class TransparentDataEncryptionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.aio.SqlManagementClient`'s
        :attr:`transparent_data_encryptions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        tde_name: Union[str, "_models.TransparentDataEncryptionName"],
        **kwargs: Any
    ) -> _models.LogicalDatabaseTransparentDataEncryption:
        """Gets a logical database's transparent data encryption.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the logical database for which the transparent data
         encryption is defined. Required.
        :type database_name: str
        :param tde_name: The name of the transparent data encryption configuration. "current" Required.
        :type tde_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogicalDatabaseTransparentDataEncryption or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', self._config.api_version))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.LogicalDatabaseTransparentDataEncryption]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            database_name=database_name,
            tde_name=tde_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('LogicalDatabaseTransparentDataEncryption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{tdeName}"}  # type: ignore


    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        tde_name: Union[str, "_models.TransparentDataEncryptionName"],
        parameters: _models.LogicalDatabaseTransparentDataEncryption,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]:
        """Updates a logical database's transparent data encryption configuration.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the logical database for which the security alert policy is
         defined. Required.
        :type database_name: str
        :param tde_name: The name of the transparent data encryption configuration. "current" Required.
        :type tde_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :param parameters: The database transparent data encryption. Required.
        :type parameters: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogicalDatabaseTransparentDataEncryption or None or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        tde_name: Union[str, "_models.TransparentDataEncryptionName"],
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]:
        """Updates a logical database's transparent data encryption configuration.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the logical database for which the security alert policy is
         defined. Required.
        :type database_name: str
        :param tde_name: The name of the transparent data encryption configuration. "current" Required.
        :type tde_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :param parameters: The database transparent data encryption. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogicalDatabaseTransparentDataEncryption or None or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        tde_name: Union[str, "_models.TransparentDataEncryptionName"],
        parameters: Union[_models.LogicalDatabaseTransparentDataEncryption, IO],
        **kwargs: Any
    ) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]:
        """Updates a logical database's transparent data encryption configuration.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the logical database for which the security alert policy is
         defined. Required.
        :type database_name: str
        :param tde_name: The name of the transparent data encryption configuration. "current" Required.
        :type tde_name: str or ~azure.mgmt.sql.models.TransparentDataEncryptionName
        :param parameters: The database transparent data encryption. Is either a model type or a IO
         type. Required.
        :type parameters: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: LogicalDatabaseTransparentDataEncryption or None or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption or None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', self._config.api_version))  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional[_models.LogicalDatabaseTransparentDataEncryption]]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, 'LogicalDatabaseTransparentDataEncryption')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            database_name=database_name,
            tde_name=tde_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata['url'],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('LogicalDatabaseTransparentDataEncryption', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('LogicalDatabaseTransparentDataEncryption', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{tdeName}"}  # type: ignore


    @distributed_trace
    def list_by_database(
        self,
        resource_group_name: str,
        server_name: str,
        database_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.LogicalDatabaseTransparentDataEncryption"]:
        """Gets a list of the logical database's transparent data encryption.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the logical database for which the transparent data
         encryption is defined. Required.
        :type database_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either LogicalDatabaseTransparentDataEncryption or the
         result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', self._config.api_version))  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.LogicalDatabaseTransparentDataEncryptionListResult]

        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_database_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    database_name=database_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_database.metadata['url'],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                
                request = build_list_by_database_request(
                    resource_group_name=resource_group_name,
                    server_name=server_name,
                    database_name=database_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("LogicalDatabaseTransparentDataEncryptionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_database.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption"}  # type: ignore
