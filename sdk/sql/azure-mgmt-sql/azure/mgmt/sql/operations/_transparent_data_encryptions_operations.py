# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import IO, Optional, TYPE_CHECKING, Union, overload

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_get_request(
    resource_group_name,  # type: str
    server_name,  # type: str
    database_name,  # type: str
    tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-02-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{tdeName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "databaseName": _SERIALIZER.url("database_name", database_name, 'str'),
        "tdeName": _SERIALIZER.url("tde_name", tde_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_create_or_update_request(
    resource_group_name,  # type: str
    server_name,  # type: str
    database_name,  # type: str
    tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-02-01-preview"))  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{tdeName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "databaseName": _SERIALIZER.url("database_name", database_name, 'str'),
        "tdeName": _SERIALIZER.url("tde_name", tde_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    if content_type is not None:
        _headers['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )


def build_list_by_database_request(
    resource_group_name,  # type: str
    server_name,  # type: str
    database_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2021-02-01-preview"))  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption")  # pylint: disable=line-too-long
    path_format_arguments = {
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "databaseName": _SERIALIZER.url("database_name", database_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _headers['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_params,
        headers=_headers,
        **kwargs
    )

# fmt: on
class TransparentDataEncryptionsOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.SqlManagementClient`'s
        :attr:`transparent_data_encryptions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @distributed_trace
    def get(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.LogicalDatabaseTransparentDataEncryption
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

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
        parameters,  # type: _models.LogicalDatabaseTransparentDataEncryption
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]
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
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
        parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]
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


    @distributed_trace
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        tde_name,  # type: Union[str, "_models.TransparentDataEncryptionName"]
        parameters,  # type: Union[_models.LogicalDatabaseTransparentDataEncryption, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional[_models.LogicalDatabaseTransparentDataEncryption]
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

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
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
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.LogicalDatabaseTransparentDataEncryption"]
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
         ~azure.core.paging.ItemPaged[~azure.mgmt.sql.models.LogicalDatabaseTransparentDataEncryption]
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize("LogicalDatabaseTransparentDataEncryptionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_database.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption"}  # type: ignore
