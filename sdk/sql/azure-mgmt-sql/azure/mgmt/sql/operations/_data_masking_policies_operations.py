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
    from typing import Any, Callable, Dict, Optional, TypeVar
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_create_or_update_request(
    resource_group_name,  # type: str
    server_name,  # type: str
    database_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2014-04-01"))  # type: str
    data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
    content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "databaseName": _SERIALIZER.url("database_name", database_name, 'str'),
        "dataMaskingPolicyName": _SERIALIZER.url("data_masking_policy_name", data_masking_policy_name, 'str'),
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


def build_get_request(
    resource_group_name,  # type: str
    server_name,  # type: str
    database_name,  # type: str
    subscription_id,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop('api_version', _params.pop('api-version', "2014-04-01"))  # type: str
    data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
    accept = _headers.pop('Accept', "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str'),
        "serverName": _SERIALIZER.url("server_name", server_name, 'str'),
        "databaseName": _SERIALIZER.url("database_name", database_name, 'str'),
        "dataMaskingPolicyName": _SERIALIZER.url("data_masking_policy_name", data_masking_policy_name, 'str'),
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
class DataMaskingPoliciesOperations(object):
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.sql.SqlManagementClient`'s
        :attr:`data_masking_policies` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")


    @overload
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        parameters,  # type: _models.DataMaskingPolicy
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.DataMaskingPolicy
        """Creates or updates a database data masking policy.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param parameters: Parameters for creating or updating a data masking policy. Required.
        :type parameters: ~azure.mgmt.sql.models.DataMaskingPolicy
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DataMaskingPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        parameters,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.DataMaskingPolicy
        """Creates or updates a database data masking policy.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param parameters: Parameters for creating or updating a data masking policy. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DataMaskingPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """


    @distributed_trace
    def create_or_update(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        parameters,  # type: Union[_models.DataMaskingPolicy, IO]
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.DataMaskingPolicy
        """Creates or updates a database data masking policy.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :param parameters: Parameters for creating or updating a data masking policy. Is either a model
         type or a IO type. Required.
        :type parameters: ~azure.mgmt.sql.models.DataMaskingPolicy or IO
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DataMaskingPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', self._config.api_version))  # type: str
        data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
        content_type = kwargs.pop('content_type', _headers.pop('Content-Type', None))  # type: Optional[str]
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataMaskingPolicy]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, 'DataMaskingPolicy')

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            database_name=database_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            data_masking_policy_name=data_masking_policy_name,
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

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('DataMaskingPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}"}  # type: ignore


    @distributed_trace
    def get(
        self,
        resource_group_name,  # type: str
        server_name,  # type: str
        database_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> _models.DataMaskingPolicy
        """Gets a database data masking policy.

        :param resource_group_name: The name of the resource group that contains the resource. You can
         obtain this value from the Azure Resource Manager API or the portal. Required.
        :type resource_group_name: str
        :param server_name: The name of the server. Required.
        :type server_name: str
        :param database_name: The name of the database. Required.
        :type database_name: str
        :keyword data_masking_policy_name: The name of the database for which the data masking rule
         applies. Default value is "Default". Note that overriding this default value may result in
         unsupported behavior.
        :paramtype data_masking_policy_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DataMaskingPolicy or the result of cls(response)
        :rtype: ~azure.mgmt.sql.models.DataMaskingPolicy
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop('api_version', _params.pop('api-version', self._config.api_version))  # type: str
        data_masking_policy_name = kwargs.pop('data_masking_policy_name', "Default")  # type: str
        cls = kwargs.pop('cls', None)  # type: ClsType[_models.DataMaskingPolicy]

        
        request = build_get_request(
            resource_group_name=resource_group_name,
            server_name=server_name,
            database_name=database_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            data_masking_policy_name=data_masking_policy_name,
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

        deserialized = self._deserialize('DataMaskingPolicy', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/dataMaskingPolicies/{dataMaskingPolicyName}"}  # type: ignore

