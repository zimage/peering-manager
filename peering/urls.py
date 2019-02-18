from django.conf.urls import url
from . import views

app_name = "peering"

urlpatterns = [
    # Autonomous Systems
    url(
        r"^autonomous-systems/$", views.ASList.as_view(), name="autonomous_system_list"
    ),
    url(
        r"^autonomous-systems/add/$",
        views.ASAdd.as_view(),
        name="autonomous_system_add",
    ),
    url(
        r"^autonomous-systems/import/$",
        views.ASImport.as_view(),
        name="autonomous_system_import",
    ),
    url(
        r"^autonomous-systems/(?P<asn>[0-9]+)/$",
        views.ASDetails.as_view(),
        name="autonomous_system_details",
    ),
    url(
        r"^autonomous-systems/(?P<asn>[0-9]+)/edit/$",
        views.ASEdit.as_view(),
        name="autonomous_system_edit",
    ),
    url(
        r"^autonomous-systems/(?P<asn>[0-9]+)/delete/$",
        views.ASDelete.as_view(),
        name="autonomous_system_delete",
    ),
    url(
        r"^autonomous-systems/delete/$",
        views.ASBulkDelete.as_view(),
        name="autonomous_system_bulk_delete",
    ),
    url(
        r"^autonomous-systems/(?P<asn>[\w-]+)/direct-peering-sessions/$",
        views.AutonomousSystemDirectPeeringSessions.as_view(),
        name="autonomous_system_direct_peering_sessions",
    ),
    url(
        r"^autonomous-systems/(?P<asn>[\w-]+)/ix-peering-sessions/$",
        views.AutonomousSystemInternetExchangesPeeringSessions.as_view(),
        name="autonomous_system_internet_exchange_peering_sessions",
    ),
    # BGP Communities
    url(r"^communities/$", views.CommunityList.as_view(), name="community_list"),
    url(r"^communities/add/$", views.CommunityAdd.as_view(), name="community_add"),
    url(
        r"^communities/import/$",
        views.CommunityImport.as_view(),
        name="community_import",
    ),
    url(
        r"^communities/(?P<pk>[0-9]+)/$",
        views.CommunityDetails.as_view(),
        name="community_details",
    ),
    url(
        r"^communities/(?P<pk>[0-9]+)/edit/$",
        views.CommunityEdit.as_view(),
        name="community_edit",
    ),
    url(
        r"^communities/(?P<pk>[0-9]+)/delete/$",
        views.CommunityDelete.as_view(),
        name="community_delete",
    ),
    url(
        r"^communities/delete/$",
        views.CommunityBulkDelete.as_view(),
        name="community_bulk_delete",
    ),
    url(
        r"^communities/edit/$",
        views.CommunityBulkEdit.as_view(),
        name="community_bulk_edit",
    ),
    # Configuration Templates
    url(
        r"^templates/$",
        views.ConfigTemplateList.as_view(),
        name="configuration_template_list",
    ),
    url(
        r"^templates/add/$",
        views.ConfigTemplateAdd.as_view(),
        name="configuration_template_add",
    ),
    url(
        r"^templates/(?P<pk>[0-9]+)/$",
        views.ConfigTemplateDetails.as_view(),
        name="configuration_template_details",
    ),
    url(
        r"^templates/(?P<pk>[0-9]+)/edit/$",
        views.ConfigTemplateEdit.as_view(),
        name="configuration_template_edit",
    ),
    url(
        r"^templates/(?P<pk>[0-9]+)/delete/$",
        views.ConfigTemplateDelete.as_view(),
        name="configuration_template_delete",
    ),
    url(
        r"^templates/delete/$",
        views.ConfigTemplateBulkDelete.as_view(),
        name="configuration_template_bulk_delete",
    ),
    # Direct Peering Sessions
    url(
        r"^direct-peering-sessions/$",
        views.DirectPeeringSessionList.as_view(),
        name="direct_peering_session_list",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/$",
        views.DirectPeeringSessionDetails.as_view(),
        name="direct_peering_session_details",
    ),
    url(
        r"^direct-peering-sessions/add/(?P<asn>[0-9]+)/$",
        views.DirectPeeringSessionAdd.as_view(),
        name="direct_peering_session_add",
    ),
    url(
        r"^direct-peering-sessions/edit/$",
        views.DirectPeeringSessionBulkEdit.as_view(),
        name="direct_peering_session_bulk_edit",
    ),
    url(
        r"^direct-peering-sessions/delete/$",
        views.DirectPeeringSessionBulkDelete.as_view(),
        name="direct_peering_session_bulk_delete",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/edit/$",
        views.DirectPeeringSessionEdit.as_view(),
        name="direct_peering_session_edit",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/delete/$",
        views.DirectPeeringSessionDelete.as_view(),
        name="direct_peering_session_delete",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/disable/$",
        views.DirectPeeringSessionDisable.as_view(),
        name="direct_peering_session_disable",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/enable/$",
        views.DirectPeeringSessionEnable.as_view(),
        name="direct_peering_session_enable",
    ),
    url(
        r"^direct-peering-sessions/(?P<pk>[0-9]+)/update-routing-policies/$",
        views.DirectPeeringSessionUpdateRoutingPolicies.as_view(),
        name="direct_peering_session_update_routing_policies",
    ),
    # Internet Exchanges
    url(
        r"^internet-exchanges/$",
        views.InternetExchangeList.as_view(),
        name="internet_exchange_list",
    ),
    url(
        r"^internet-exchanges/add/$",
        views.InternetExchangeAdd.as_view(),
        name="internet_exchange_add",
    ),
    url(
        r"^internet-exchanges/import/$",
        views.InternetExchangeImport.as_view(),
        name="internet_exchange_import",
    ),
    url(
        r"^internet-exchanges/peeringdb-import/$",
        views.InternetExchangePeeringDBImport.as_view(),
        name="internet_exchange_peeringdb_import",
    ),
    url(
        r"^internet-exchanges/delete/$",
        views.InternetExchangeBulkDelete.as_view(),
        name="internet_exchange_bulk_delete",
    ),
    url(
        r"^internet-exchanges/edit/$",
        views.InternetExchangeBulkEdit.as_view(),
        name="internet_exchange_bulk_edit",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/$",
        views.InternetExchangeDetails.as_view(),
        name="internet_exchange_details",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/edit/$",
        views.InternetExchangeEdit.as_view(),
        name="internet_exchange_edit",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/delete/$",
        views.InternetExchangeDelete.as_view(),
        name="internet_exchange_delete",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/add-peering-session/$",
        views.InternetExchangePeeringSessionAdd.as_view(),
        name="internet_exchange_peering_session_add",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/update-communities/$",
        views.InternetExchangeUpdateCommunities.as_view(),
        name="internet_exchange_update_communities",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/update-routing-policies/$",
        views.InternetExchangeUpdateRoutingPolicies.as_view(),
        name="internet_exchange_update_routing_policies",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/peering-sessions/$",
        views.InternetExchangePeeringSessions.as_view(),
        name="internet_exchange_peering_sessions",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/import-from-router$",
        views.InternetExchangeImportFromRouter.as_view(),
        name="internet_exchange_import_from_router",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/peers/$",
        views.InternetExchangePeers.as_view(),
        name="internet_exchange_peers",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/configuration/$",
        views.InternetExchangeConfig.as_view(),
        name="internet_exchange_configuration",
    ),
    url(
        r"^internet-exchanges/(?P<slug>[\w-]+)/update-session-states/$",
        views.InternetExchangeUpdateSessionStates.as_view(),
        name="internet_exchange_update_session_states",
    ),
    # Internet Exchange Peering Sessions
    url(
        r"^internet-exchange-peering-sessions/$",
        views.InternetExchangePeeringSessionList.as_view(),
        name="internet_exchange_peering_session_list",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/$",
        views.InternetExchangePeeringSessionDetails.as_view(),
        name="internet_exchange_peering_session_details",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/edit/$",
        views.InternetExchangePeeringSessionEdit.as_view(),
        name="internet_exchange_peering_session_edit",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/delete/$",
        views.InternetExchangePeeringSessionDelete.as_view(),
        name="internet_exchange_peering_session_delete",
    ),
    url(
        r"^internet-exchange-peering-sessions/add_from_peeringdb/$",
        views.InternetExchangePeeringSessionAddFromPeeringDB.as_view(),
        name="internet_exchange_peering_session_add_from_peeringdb",
    ),
    url(
        r"^internet-exchange-peering-sessions/edit/$",
        views.InternetExchangePeeringSessionBulkEdit.as_view(),
        name="internet_exchange_peering_session_bulk_edit",
    ),
    url(
        r"^internet-exchange-peering-sessions/delete/$",
        views.InternetExchangePeeringSessionBulkDelete.as_view(),
        name="internet_exchange_peering_session_bulk_delete",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/disable/$",
        views.InternetExchangePeeringSessionDisable.as_view(),
        name="internet_exchange_peering_session_disable",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/enable/$",
        views.InternetExchangePeeringSessionEnable.as_view(),
        name="internet_exchange_peering_session_enable",
    ),
    url(
        r"^internet-exchange-peering-sessions/(?P<pk>[0-9]+)/update-routing-policies/$",
        views.InternetExchangePeeringSessionUpdateRoutingPolicies.as_view(),
        name="internet_exchange_peering_session_update_routing_policies",
    ),
    # Routers
    url(r"^routers/$", views.RouterList.as_view(), name="router_list"),
    url(r"^routers/add/$", views.RouterAdd.as_view(), name="router_add"),
    url(r"^routers/import/$", views.RouterImport.as_view(), name="router_import"),
    url(
        r"^routers/(?P<pk>[0-9]+)/$",
        views.RouterDetails.as_view(),
        name="router_details",
    ),
    url(
        r"^routers/(?P<pk>[0-9]+)/edit/$",
        views.RouterEdit.as_view(),
        name="router_edit",
    ),
    url(
        r"^routers/(?P<pk>[0-9]+)/delete/$",
        views.RouterDelete.as_view(),
        name="router_delete",
    ),
    url(
        r"^routers/delete/$",
        views.RouterBulkDelete.as_view(),
        name="router_bulk_delete",
    ),
    url(r"^routers/edit/$", views.RouterBulkEdit.as_view(), name="router_bulk_edit"),
    # Routing Policies
    url(
        r"^routing-policies/$",
        views.RoutingPolicyList.as_view(),
        name="routing_policy_list",
    ),
    url(
        r"^routing-policies/add/$",
        views.RoutingPolicyAdd.as_view(),
        name="routing_policy_add",
    ),
    url(
        r"^routing-policies/import/$",
        views.RoutingPolicyImport.as_view(),
        name="routing_policy_import",
    ),
    url(
        r"^routing-policies/(?P<pk>[0-9]+)/$",
        views.RoutingPolicyDetails.as_view(),
        name="routing_policy_details",
    ),
    url(
        r"^routing-policies/(?P<pk>[0-9]+)/edit/$",
        views.RoutingPolicyEdit.as_view(),
        name="routing_policy_edit",
    ),
    url(
        r"^routing-policies/(?P<pk>[0-9]+)/delete/$",
        views.RoutingPolicyDelete.as_view(),
        name="routing_policy_delete",
    ),
    url(
        r"^routing-policies/delete/$",
        views.RoutingPolicyBulkDelete.as_view(),
        name="routing_policy_bulk_delete",
    ),
    url(
        r"^routing-policies/edit/$",
        views.RoutingPolicyBulkEdit.as_view(),
        name="routing_policy_bulk_edit",
    ),
]
