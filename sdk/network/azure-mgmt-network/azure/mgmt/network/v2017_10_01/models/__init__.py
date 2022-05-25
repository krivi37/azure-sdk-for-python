# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AddressSpace
from ._models_py3 import ApplicationGateway
from ._models_py3 import ApplicationGatewayAuthenticationCertificate
from ._models_py3 import ApplicationGatewayAvailableSslOptions
from ._models_py3 import ApplicationGatewayAvailableSslPredefinedPolicies
from ._models_py3 import ApplicationGatewayAvailableWafRuleSetsResult
from ._models_py3 import ApplicationGatewayBackendAddress
from ._models_py3 import ApplicationGatewayBackendAddressPool
from ._models_py3 import ApplicationGatewayBackendHealth
from ._models_py3 import ApplicationGatewayBackendHealthHttpSettings
from ._models_py3 import ApplicationGatewayBackendHealthPool
from ._models_py3 import ApplicationGatewayBackendHealthServer
from ._models_py3 import ApplicationGatewayBackendHttpSettings
from ._models_py3 import ApplicationGatewayConnectionDraining
from ._models_py3 import ApplicationGatewayFirewallDisabledRuleGroup
from ._models_py3 import ApplicationGatewayFirewallRule
from ._models_py3 import ApplicationGatewayFirewallRuleGroup
from ._models_py3 import ApplicationGatewayFirewallRuleSet
from ._models_py3 import ApplicationGatewayFrontendIPConfiguration
from ._models_py3 import ApplicationGatewayFrontendPort
from ._models_py3 import ApplicationGatewayHttpListener
from ._models_py3 import ApplicationGatewayIPConfiguration
from ._models_py3 import ApplicationGatewayListResult
from ._models_py3 import ApplicationGatewayPathRule
from ._models_py3 import ApplicationGatewayProbe
from ._models_py3 import ApplicationGatewayProbeHealthResponseMatch
from ._models_py3 import ApplicationGatewayRedirectConfiguration
from ._models_py3 import ApplicationGatewayRequestRoutingRule
from ._models_py3 import ApplicationGatewaySku
from ._models_py3 import ApplicationGatewaySslCertificate
from ._models_py3 import ApplicationGatewaySslPolicy
from ._models_py3 import ApplicationGatewaySslPredefinedPolicy
from ._models_py3 import ApplicationGatewayUrlPathMap
from ._models_py3 import ApplicationGatewayWebApplicationFirewallConfiguration
from ._models_py3 import ApplicationSecurityGroup
from ._models_py3 import ApplicationSecurityGroupListResult
from ._models_py3 import AuthorizationListResult
from ._models_py3 import Availability
from ._models_py3 import AvailableProvidersList
from ._models_py3 import AvailableProvidersListCity
from ._models_py3 import AvailableProvidersListCountry
from ._models_py3 import AvailableProvidersListParameters
from ._models_py3 import AvailableProvidersListState
from ._models_py3 import AzureAsyncOperationResult
from ._models_py3 import AzureReachabilityReport
from ._models_py3 import AzureReachabilityReportItem
from ._models_py3 import AzureReachabilityReportLatencyInfo
from ._models_py3 import AzureReachabilityReportLocation
from ._models_py3 import AzureReachabilityReportParameters
from ._models_py3 import BGPCommunity
from ._models_py3 import BackendAddressPool
from ._models_py3 import BgpPeerStatus
from ._models_py3 import BgpPeerStatusListResult
from ._models_py3 import BgpServiceCommunity
from ._models_py3 import BgpServiceCommunityListResult
from ._models_py3 import BgpSettings
from ._models_py3 import ConnectionMonitor
from ._models_py3 import ConnectionMonitorDestination
from ._models_py3 import ConnectionMonitorListResult
from ._models_py3 import ConnectionMonitorParameters
from ._models_py3 import ConnectionMonitorQueryResult
from ._models_py3 import ConnectionMonitorResult
from ._models_py3 import ConnectionMonitorResultProperties
from ._models_py3 import ConnectionMonitorSource
from ._models_py3 import ConnectionResetSharedKey
from ._models_py3 import ConnectionSharedKey
from ._models_py3 import ConnectionStateSnapshot
from ._models_py3 import ConnectivityDestination
from ._models_py3 import ConnectivityHop
from ._models_py3 import ConnectivityInformation
from ._models_py3 import ConnectivityIssue
from ._models_py3 import ConnectivityParameters
from ._models_py3 import ConnectivitySource
from ._models_py3 import DhcpOptions
from ._models_py3 import Dimension
from ._models_py3 import DnsNameAvailabilityResult
from ._models_py3 import EffectiveNetworkSecurityGroup
from ._models_py3 import EffectiveNetworkSecurityGroupAssociation
from ._models_py3 import EffectiveNetworkSecurityGroupListResult
from ._models_py3 import EffectiveNetworkSecurityRule
from ._models_py3 import EffectiveRoute
from ._models_py3 import EffectiveRouteListResult
from ._models_py3 import EndpointServiceResult
from ._models_py3 import EndpointServicesListResult
from ._models_py3 import Error
from ._models_py3 import ErrorDetails
from ._models_py3 import ExpressRouteCircuit
from ._models_py3 import ExpressRouteCircuitArpTable
from ._models_py3 import ExpressRouteCircuitAuthorization
from ._models_py3 import ExpressRouteCircuitListResult
from ._models_py3 import ExpressRouteCircuitPeering
from ._models_py3 import ExpressRouteCircuitPeeringConfig
from ._models_py3 import ExpressRouteCircuitPeeringListResult
from ._models_py3 import ExpressRouteCircuitRoutesTable
from ._models_py3 import ExpressRouteCircuitRoutesTableSummary
from ._models_py3 import ExpressRouteCircuitServiceProviderProperties
from ._models_py3 import ExpressRouteCircuitSku
from ._models_py3 import ExpressRouteCircuitStats
from ._models_py3 import ExpressRouteCircuitsArpTableListResult
from ._models_py3 import ExpressRouteCircuitsRoutesTableListResult
from ._models_py3 import ExpressRouteCircuitsRoutesTableSummaryListResult
from ._models_py3 import ExpressRouteServiceProvider
from ._models_py3 import ExpressRouteServiceProviderBandwidthsOffered
from ._models_py3 import ExpressRouteServiceProviderListResult
from ._models_py3 import FlowLogInformation
from ._models_py3 import FlowLogStatusParameters
from ._models_py3 import FrontendIPConfiguration
from ._models_py3 import GatewayRoute
from ._models_py3 import GatewayRouteListResult
from ._models_py3 import IPAddressAvailabilityResult
from ._models_py3 import IPConfiguration
from ._models_py3 import InboundNatPool
from ._models_py3 import InboundNatRule
from ._models_py3 import InboundNatRuleListResult
from ._models_py3 import IpsecPolicy
from ._models_py3 import Ipv6ExpressRouteCircuitPeeringConfig
from ._models_py3 import LoadBalancer
from ._models_py3 import LoadBalancerBackendAddressPoolListResult
from ._models_py3 import LoadBalancerFrontendIPConfigurationListResult
from ._models_py3 import LoadBalancerListResult
from ._models_py3 import LoadBalancerLoadBalancingRuleListResult
from ._models_py3 import LoadBalancerProbeListResult
from ._models_py3 import LoadBalancerSku
from ._models_py3 import LoadBalancingRule
from ._models_py3 import LocalNetworkGateway
from ._models_py3 import LocalNetworkGatewayListResult
from ._models_py3 import LogSpecification
from ._models_py3 import MetricSpecification
from ._models_py3 import NetworkInterface
from ._models_py3 import NetworkInterfaceAssociation
from ._models_py3 import NetworkInterfaceDnsSettings
from ._models_py3 import NetworkInterfaceIPConfiguration
from ._models_py3 import NetworkInterfaceIPConfigurationListResult
from ._models_py3 import NetworkInterfaceListResult
from ._models_py3 import NetworkInterfaceLoadBalancerListResult
from ._models_py3 import NetworkSecurityGroup
from ._models_py3 import NetworkSecurityGroupListResult
from ._models_py3 import NetworkWatcher
from ._models_py3 import NetworkWatcherListResult
from ._models_py3 import NextHopParameters
from ._models_py3 import NextHopResult
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationPropertiesFormatServiceSpecification
from ._models_py3 import OutboundNatRule
from ._models_py3 import PacketCapture
from ._models_py3 import PacketCaptureFilter
from ._models_py3 import PacketCaptureListResult
from ._models_py3 import PacketCaptureParameters
from ._models_py3 import PacketCaptureQueryStatusResult
from ._models_py3 import PacketCaptureResult
from ._models_py3 import PacketCaptureResultProperties
from ._models_py3 import PacketCaptureStorageLocation
from ._models_py3 import PatchRouteFilter
from ._models_py3 import PatchRouteFilterRule
from ._models_py3 import Probe
from ._models_py3 import PublicIPAddress
from ._models_py3 import PublicIPAddressDnsSettings
from ._models_py3 import PublicIPAddressListResult
from ._models_py3 import PublicIPAddressSku
from ._models_py3 import QueryTroubleshootingParameters
from ._models_py3 import Resource
from ._models_py3 import ResourceNavigationLink
from ._models_py3 import RetentionPolicyParameters
from ._models_py3 import Route
from ._models_py3 import RouteFilter
from ._models_py3 import RouteFilterListResult
from ._models_py3 import RouteFilterRule
from ._models_py3 import RouteFilterRuleListResult
from ._models_py3 import RouteListResult
from ._models_py3 import RouteTable
from ._models_py3 import RouteTableListResult
from ._models_py3 import SecurityGroupNetworkInterface
from ._models_py3 import SecurityGroupViewParameters
from ._models_py3 import SecurityGroupViewResult
from ._models_py3 import SecurityRule
from ._models_py3 import SecurityRuleAssociations
from ._models_py3 import SecurityRuleListResult
from ._models_py3 import ServiceEndpointPropertiesFormat
from ._models_py3 import SubResource
from ._models_py3 import Subnet
from ._models_py3 import SubnetAssociation
from ._models_py3 import SubnetListResult
from ._models_py3 import TagsObject
from ._models_py3 import Topology
from ._models_py3 import TopologyAssociation
from ._models_py3 import TopologyParameters
from ._models_py3 import TopologyResource
from ._models_py3 import TroubleshootingDetails
from ._models_py3 import TroubleshootingParameters
from ._models_py3 import TroubleshootingRecommendedActions
from ._models_py3 import TroubleshootingResult
from ._models_py3 import TunnelConnectionHealth
from ._models_py3 import Usage
from ._models_py3 import UsageName
from ._models_py3 import UsagesListResult
from ._models_py3 import VerificationIPFlowParameters
from ._models_py3 import VerificationIPFlowResult
from ._models_py3 import VirtualNetwork
from ._models_py3 import VirtualNetworkConnectionGatewayReference
from ._models_py3 import VirtualNetworkGateway
from ._models_py3 import VirtualNetworkGatewayConnection
from ._models_py3 import VirtualNetworkGatewayConnectionListEntity
from ._models_py3 import VirtualNetworkGatewayConnectionListResult
from ._models_py3 import VirtualNetworkGatewayIPConfiguration
from ._models_py3 import VirtualNetworkGatewayListConnectionsResult
from ._models_py3 import VirtualNetworkGatewayListResult
from ._models_py3 import VirtualNetworkGatewaySku
from ._models_py3 import VirtualNetworkListResult
from ._models_py3 import VirtualNetworkListUsageResult
from ._models_py3 import VirtualNetworkPeering
from ._models_py3 import VirtualNetworkPeeringListResult
from ._models_py3 import VirtualNetworkUsage
from ._models_py3 import VirtualNetworkUsageName
from ._models_py3 import VpnClientConfiguration
from ._models_py3 import VpnClientParameters
from ._models_py3 import VpnClientRevokedCertificate
from ._models_py3 import VpnClientRootCertificate
from ._models_py3 import VpnDeviceScriptParameters


from ._network_management_client_enums import (
    Access,
    ApplicationGatewayBackendHealthServerHealth,
    ApplicationGatewayCookieBasedAffinity,
    ApplicationGatewayFirewallMode,
    ApplicationGatewayOperationalState,
    ApplicationGatewayProtocol,
    ApplicationGatewayRedirectType,
    ApplicationGatewayRequestRoutingRuleType,
    ApplicationGatewaySkuName,
    ApplicationGatewaySslCipherSuite,
    ApplicationGatewaySslPolicyName,
    ApplicationGatewaySslPolicyType,
    ApplicationGatewaySslProtocol,
    ApplicationGatewayTier,
    AssociationType,
    AuthenticationMethod,
    AuthorizationUseStatus,
    BgpPeerState,
    ConnectionState,
    ConnectionStatus,
    DhGroup,
    Direction,
    EffectiveRouteSource,
    EffectiveRouteState,
    EffectiveSecurityRuleProtocol,
    EvaluationState,
    ExpressRouteCircuitPeeringAdvertisedPublicPrefixState,
    ExpressRouteCircuitPeeringState,
    ExpressRouteCircuitPeeringType,
    ExpressRouteCircuitSkuFamily,
    ExpressRouteCircuitSkuTier,
    IPAllocationMethod,
    IPVersion,
    IkeEncryption,
    IkeIntegrity,
    IpsecEncryption,
    IpsecIntegrity,
    IssueType,
    LoadBalancerSkuName,
    LoadDistribution,
    NetworkOperationStatus,
    NextHopType,
    Origin,
    PcError,
    PcProtocol,
    PcStatus,
    PfsGroup,
    ProbeProtocol,
    ProcessorArchitecture,
    Protocol,
    ProvisioningState,
    PublicIPAddressSkuName,
    RouteFilterRuleType,
    RouteNextHopType,
    SecurityRuleAccess,
    SecurityRuleDirection,
    SecurityRuleProtocol,
    ServiceProviderProvisioningState,
    Severity,
    TransportProtocol,
    UsageUnit,
    VirtualNetworkGatewayConnectionStatus,
    VirtualNetworkGatewayConnectionType,
    VirtualNetworkGatewaySkuName,
    VirtualNetworkGatewaySkuTier,
    VirtualNetworkGatewayType,
    VirtualNetworkPeeringState,
    VpnClientProtocol,
    VpnType,
)

__all__ = [
    'AddressSpace',
    'ApplicationGateway',
    'ApplicationGatewayAuthenticationCertificate',
    'ApplicationGatewayAvailableSslOptions',
    'ApplicationGatewayAvailableSslPredefinedPolicies',
    'ApplicationGatewayAvailableWafRuleSetsResult',
    'ApplicationGatewayBackendAddress',
    'ApplicationGatewayBackendAddressPool',
    'ApplicationGatewayBackendHealth',
    'ApplicationGatewayBackendHealthHttpSettings',
    'ApplicationGatewayBackendHealthPool',
    'ApplicationGatewayBackendHealthServer',
    'ApplicationGatewayBackendHttpSettings',
    'ApplicationGatewayConnectionDraining',
    'ApplicationGatewayFirewallDisabledRuleGroup',
    'ApplicationGatewayFirewallRule',
    'ApplicationGatewayFirewallRuleGroup',
    'ApplicationGatewayFirewallRuleSet',
    'ApplicationGatewayFrontendIPConfiguration',
    'ApplicationGatewayFrontendPort',
    'ApplicationGatewayHttpListener',
    'ApplicationGatewayIPConfiguration',
    'ApplicationGatewayListResult',
    'ApplicationGatewayPathRule',
    'ApplicationGatewayProbe',
    'ApplicationGatewayProbeHealthResponseMatch',
    'ApplicationGatewayRedirectConfiguration',
    'ApplicationGatewayRequestRoutingRule',
    'ApplicationGatewaySku',
    'ApplicationGatewaySslCertificate',
    'ApplicationGatewaySslPolicy',
    'ApplicationGatewaySslPredefinedPolicy',
    'ApplicationGatewayUrlPathMap',
    'ApplicationGatewayWebApplicationFirewallConfiguration',
    'ApplicationSecurityGroup',
    'ApplicationSecurityGroupListResult',
    'AuthorizationListResult',
    'Availability',
    'AvailableProvidersList',
    'AvailableProvidersListCity',
    'AvailableProvidersListCountry',
    'AvailableProvidersListParameters',
    'AvailableProvidersListState',
    'AzureAsyncOperationResult',
    'AzureReachabilityReport',
    'AzureReachabilityReportItem',
    'AzureReachabilityReportLatencyInfo',
    'AzureReachabilityReportLocation',
    'AzureReachabilityReportParameters',
    'BGPCommunity',
    'BackendAddressPool',
    'BgpPeerStatus',
    'BgpPeerStatusListResult',
    'BgpServiceCommunity',
    'BgpServiceCommunityListResult',
    'BgpSettings',
    'ConnectionMonitor',
    'ConnectionMonitorDestination',
    'ConnectionMonitorListResult',
    'ConnectionMonitorParameters',
    'ConnectionMonitorQueryResult',
    'ConnectionMonitorResult',
    'ConnectionMonitorResultProperties',
    'ConnectionMonitorSource',
    'ConnectionResetSharedKey',
    'ConnectionSharedKey',
    'ConnectionStateSnapshot',
    'ConnectivityDestination',
    'ConnectivityHop',
    'ConnectivityInformation',
    'ConnectivityIssue',
    'ConnectivityParameters',
    'ConnectivitySource',
    'DhcpOptions',
    'Dimension',
    'DnsNameAvailabilityResult',
    'EffectiveNetworkSecurityGroup',
    'EffectiveNetworkSecurityGroupAssociation',
    'EffectiveNetworkSecurityGroupListResult',
    'EffectiveNetworkSecurityRule',
    'EffectiveRoute',
    'EffectiveRouteListResult',
    'EndpointServiceResult',
    'EndpointServicesListResult',
    'Error',
    'ErrorDetails',
    'ExpressRouteCircuit',
    'ExpressRouteCircuitArpTable',
    'ExpressRouteCircuitAuthorization',
    'ExpressRouteCircuitListResult',
    'ExpressRouteCircuitPeering',
    'ExpressRouteCircuitPeeringConfig',
    'ExpressRouteCircuitPeeringListResult',
    'ExpressRouteCircuitRoutesTable',
    'ExpressRouteCircuitRoutesTableSummary',
    'ExpressRouteCircuitServiceProviderProperties',
    'ExpressRouteCircuitSku',
    'ExpressRouteCircuitStats',
    'ExpressRouteCircuitsArpTableListResult',
    'ExpressRouteCircuitsRoutesTableListResult',
    'ExpressRouteCircuitsRoutesTableSummaryListResult',
    'ExpressRouteServiceProvider',
    'ExpressRouteServiceProviderBandwidthsOffered',
    'ExpressRouteServiceProviderListResult',
    'FlowLogInformation',
    'FlowLogStatusParameters',
    'FrontendIPConfiguration',
    'GatewayRoute',
    'GatewayRouteListResult',
    'IPAddressAvailabilityResult',
    'IPConfiguration',
    'InboundNatPool',
    'InboundNatRule',
    'InboundNatRuleListResult',
    'IpsecPolicy',
    'Ipv6ExpressRouteCircuitPeeringConfig',
    'LoadBalancer',
    'LoadBalancerBackendAddressPoolListResult',
    'LoadBalancerFrontendIPConfigurationListResult',
    'LoadBalancerListResult',
    'LoadBalancerLoadBalancingRuleListResult',
    'LoadBalancerProbeListResult',
    'LoadBalancerSku',
    'LoadBalancingRule',
    'LocalNetworkGateway',
    'LocalNetworkGatewayListResult',
    'LogSpecification',
    'MetricSpecification',
    'NetworkInterface',
    'NetworkInterfaceAssociation',
    'NetworkInterfaceDnsSettings',
    'NetworkInterfaceIPConfiguration',
    'NetworkInterfaceIPConfigurationListResult',
    'NetworkInterfaceListResult',
    'NetworkInterfaceLoadBalancerListResult',
    'NetworkSecurityGroup',
    'NetworkSecurityGroupListResult',
    'NetworkWatcher',
    'NetworkWatcherListResult',
    'NextHopParameters',
    'NextHopResult',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'OperationPropertiesFormatServiceSpecification',
    'OutboundNatRule',
    'PacketCapture',
    'PacketCaptureFilter',
    'PacketCaptureListResult',
    'PacketCaptureParameters',
    'PacketCaptureQueryStatusResult',
    'PacketCaptureResult',
    'PacketCaptureResultProperties',
    'PacketCaptureStorageLocation',
    'PatchRouteFilter',
    'PatchRouteFilterRule',
    'Probe',
    'PublicIPAddress',
    'PublicIPAddressDnsSettings',
    'PublicIPAddressListResult',
    'PublicIPAddressSku',
    'QueryTroubleshootingParameters',
    'Resource',
    'ResourceNavigationLink',
    'RetentionPolicyParameters',
    'Route',
    'RouteFilter',
    'RouteFilterListResult',
    'RouteFilterRule',
    'RouteFilterRuleListResult',
    'RouteListResult',
    'RouteTable',
    'RouteTableListResult',
    'SecurityGroupNetworkInterface',
    'SecurityGroupViewParameters',
    'SecurityGroupViewResult',
    'SecurityRule',
    'SecurityRuleAssociations',
    'SecurityRuleListResult',
    'ServiceEndpointPropertiesFormat',
    'SubResource',
    'Subnet',
    'SubnetAssociation',
    'SubnetListResult',
    'TagsObject',
    'Topology',
    'TopologyAssociation',
    'TopologyParameters',
    'TopologyResource',
    'TroubleshootingDetails',
    'TroubleshootingParameters',
    'TroubleshootingRecommendedActions',
    'TroubleshootingResult',
    'TunnelConnectionHealth',
    'Usage',
    'UsageName',
    'UsagesListResult',
    'VerificationIPFlowParameters',
    'VerificationIPFlowResult',
    'VirtualNetwork',
    'VirtualNetworkConnectionGatewayReference',
    'VirtualNetworkGateway',
    'VirtualNetworkGatewayConnection',
    'VirtualNetworkGatewayConnectionListEntity',
    'VirtualNetworkGatewayConnectionListResult',
    'VirtualNetworkGatewayIPConfiguration',
    'VirtualNetworkGatewayListConnectionsResult',
    'VirtualNetworkGatewayListResult',
    'VirtualNetworkGatewaySku',
    'VirtualNetworkListResult',
    'VirtualNetworkListUsageResult',
    'VirtualNetworkPeering',
    'VirtualNetworkPeeringListResult',
    'VirtualNetworkUsage',
    'VirtualNetworkUsageName',
    'VpnClientConfiguration',
    'VpnClientParameters',
    'VpnClientRevokedCertificate',
    'VpnClientRootCertificate',
    'VpnDeviceScriptParameters',
    'Access',
    'ApplicationGatewayBackendHealthServerHealth',
    'ApplicationGatewayCookieBasedAffinity',
    'ApplicationGatewayFirewallMode',
    'ApplicationGatewayOperationalState',
    'ApplicationGatewayProtocol',
    'ApplicationGatewayRedirectType',
    'ApplicationGatewayRequestRoutingRuleType',
    'ApplicationGatewaySkuName',
    'ApplicationGatewaySslCipherSuite',
    'ApplicationGatewaySslPolicyName',
    'ApplicationGatewaySslPolicyType',
    'ApplicationGatewaySslProtocol',
    'ApplicationGatewayTier',
    'AssociationType',
    'AuthenticationMethod',
    'AuthorizationUseStatus',
    'BgpPeerState',
    'ConnectionState',
    'ConnectionStatus',
    'DhGroup',
    'Direction',
    'EffectiveRouteSource',
    'EffectiveRouteState',
    'EffectiveSecurityRuleProtocol',
    'EvaluationState',
    'ExpressRouteCircuitPeeringAdvertisedPublicPrefixState',
    'ExpressRouteCircuitPeeringState',
    'ExpressRouteCircuitPeeringType',
    'ExpressRouteCircuitSkuFamily',
    'ExpressRouteCircuitSkuTier',
    'IPAllocationMethod',
    'IPVersion',
    'IkeEncryption',
    'IkeIntegrity',
    'IpsecEncryption',
    'IpsecIntegrity',
    'IssueType',
    'LoadBalancerSkuName',
    'LoadDistribution',
    'NetworkOperationStatus',
    'NextHopType',
    'Origin',
    'PcError',
    'PcProtocol',
    'PcStatus',
    'PfsGroup',
    'ProbeProtocol',
    'ProcessorArchitecture',
    'Protocol',
    'ProvisioningState',
    'PublicIPAddressSkuName',
    'RouteFilterRuleType',
    'RouteNextHopType',
    'SecurityRuleAccess',
    'SecurityRuleDirection',
    'SecurityRuleProtocol',
    'ServiceProviderProvisioningState',
    'Severity',
    'TransportProtocol',
    'UsageUnit',
    'VirtualNetworkGatewayConnectionStatus',
    'VirtualNetworkGatewayConnectionType',
    'VirtualNetworkGatewaySkuName',
    'VirtualNetworkGatewaySkuTier',
    'VirtualNetworkGatewayType',
    'VirtualNetworkPeeringState',
    'VpnClientProtocol',
    'VpnType',
]
