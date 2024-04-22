#!/usr/bin/env python3
# Copyright (C) 2023 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from logging import Logger
from typing import Final

import cmk.utils.paths as paths
from cmk.utils.redis import disable_redis

import cmk.base.config as base_config
from cmk.base.api.agent_based import register as agent_based_register
from cmk.base.check_api import get_check_api_context

from cmk.gui.exceptions import MKUserError
from cmk.gui.session import SuperUserContext
from cmk.gui.utils.script_helpers import gui_context
from cmk.gui.watolib.rulesets import AllRulesets
from cmk.gui.wsgi.blueprints.global_vars import set_global_vars

from cmk.update_config.plugins.pre_actions.utils import ConflictMode
from cmk.update_config.registry import pre_update_action_registry, PreUpdateAction

_DEPRECATED_CHECK_VARIABLES: Final = {
    "AKCP_TEMP_CHECK_DEFAULT_PARAMETERS",
    "ALCATEL_TEMP_CHECK_DEFAULT_PARAMETERS",
    "ARBOR_MEMORY_CHECK_DEFAULT_PARAMETERS",
    "AWSCostAndUageMetrics",
    "AWSEBSStorageTypes",
    "AWSELBHealthMap",
    "AWSNoExceptionsText",
    "AWSRegions",
    "AnyStr",
    "BACKUP_STATE",
    "BALANCE_THRESHOLDS",
    "DELL_IDRAC_FANS_STATE_MAP",
    "DEVICE_TYPE_MAP",
    "ERROR_DETAILS",
    "F5_BIGIP_CLUSTER_CHECK_DEFAULT_PARAMETERS",
    "FAN_FSC_SC2_CHECK_DEFAULT_PARAMETERS",
    "FILER_DISKS_CHECK_DEFAULT_PARAMETERS",
    "K8S_OK_CONDITIONS",
    "KEY_PULSE_SECURE_CPU",
    "MAILQUEUES_LABEL",
    "MAP_ENABLED",
    "MAP_INSTANCE_STATE",
    "MAP_PARAM_TO_TEXT",
    "MAP_QUEUE_STATES",
    "MAP_RPO_STATES",
    "MAP_SERVER_STATUS",
    "MB",
    "MBG_LANTIME_STATE_CHECK_DEFAULT_PARAMETERS",
    "METRICS_INFO_NAMES_PULSE_SECURE_MEM",
    "METRIC_PULSE_SECURE_DISK",
    "METRIC_PULSE_SECURE_LOG",
    "NAME_TRANSLATION",
    "NO_BLOCKING_SESSIONS_MSG",
    "NimbleReadsType",
    "NimbleWritesType",
    "OPNEED_STATUS_MAP",
    "OpenhardwaremonitorTraits",
    "PANDACOM_TEMP_CHECK_DEFAULT_PARAMETERS",
    "RAS_STATUS_MAP",
    "acme_certificates_default_levels",
    "acme_environment_states",
    "acme_sbc_snmp_default_levels",
    "active_mapping",
    "active_vm_levels",
    "ad_replication_default_params",
    "adva_fsp_temp_default_levels",
    "airlaser_default_levels",
    "aironet_default_error_levels",
    "aironet_default_quality_levels",
    "aironet_default_strength_levels",
    "aix_hacmp_resources",
    "akcp_daisy_temp_defaultlevels",
    "akcp_humidity_defaultlevels",
    "akcp_sensor_level_states",
    "akcp_temp_default_levels",
    "alcatel_cpu_default_levels",
    "alcatel_power_aos7_no_power_supply",
    "alcatel_power_aos7_operability_to_status_mapping",
    "alcatel_power_aos7_power_type_mapping",
    "alcatel_power_no_power_supply_info",
    "alcatel_power_operstate_map",
    "alcatel_power_type_map",
    "alcatel_temp",
    "alcatel_timetra_cpu_default_levels",
    "allnet_ip_sensoric_humidity_default_levels",
    "allnet_ip_sensoric_temp_default_levels",
    "ap_state_map",
    "ap_unknown",
    "apc_default_levels",
    "apc_humidity_default_levels",
    "apc_inrow_airflow_default_levels",
    "apc_inrow_temp_default_levels",
    "apc_sts_inputs_default_levels",
    "apc_symmetra_elphase_default_levels",
    "apc_symmetra_ext_temp_default_levels",
    "apc_symmetra_output_default_levels",
    "apc_symmetra_temp_default_levels",
    "arbor_memory_default_levels",
    "arris_cmts_cpu_default_levels",
    "arris_cmts_mem",
    "arris_cmts_temp_default_levels",
    "artec_temp_default_levels",
    "atto_fibrebridge_fcport",
    "avaya_45xx_cpu_default_levels",
    "avaya_88xx_cpu_default_levels",
    "avaya_88xx_default_levels",
    "avaya_chassis_card_operstatus_codes",
    "avaya_chassis_ps_status_codes",
    "avaya_chassis_temp_default_levels",
    "aws_cloudwatch_alarms_limits_default_levels",
    "aws_dynamodb_capacity_defaults",
    "aws_dynamodb_limits_default_levels",
    "aws_ec2_limits_default_levels",
    "aws_elb_limits_default_levels",
    "aws_elb_statistics",
    "aws_elbv2_limits_default_levels",
    "aws_glacier_limits_default_levels",
    "aws_rds_limits_default_levels",
    "aws_s3_limits_default_levels",
    "aws_wafv2_limits_default_levels",
    "azure_agent_info_levels",
    "azure_databases_default_levels",
    "barracuda_mail_latency_default_levels",
    "barracuda_mailq_default_levels",
    "barracuda_system_cpu_util_default_levels",
    "bintec_sensors_fan_default_levels",
    "bintec_sensors_info",
    "bintec_sensors_temp_default_levels",
    "blade_bx_fan_default_error_levels",
    "blade_bx_powerfan_default_levels",
    "blade_bx_status",
    "bluecat_command_server",
    "bluecat_ha",
    "bluecat_ntp",
    "bluenet_sensor_humidity_default_levels",
    "bluenet_sensor_temp_default_levels",
    "brocade_fan_default_levels",
    "brocade_info",
    "brocade_mlx_cpu_default_levels",
    "brocade_mlx_info",
    "brocade_mlx_mem_default_levels",
    "brocade_mlx_states",
    "brocade_mlx_temperature_default_levels",
    "brocade_temp_default_levels",
    "brocade_tm_default_levels",
    "bvip_link_default_levels",
    "bvip_poe_default_levels",
    "bvip_temp_default_levels",
    "bvip_util_default_levels",
    "carel_temp_defaultlevels",
    "ceph_mgrs_default_levels",
    "ceph_osds_default_levels",
    "ceph_status_default_levels",
    "check_mk_only_from_default",
    "checkpoint_memory_default_levels",
    "checkpoint_packets_default_levels",
    "checkpoint_sensorstatus_to_nagios",
    "checkpoint_temp_default_levels",
    "checkpoint_tunnels_default_levels",
    "checkpoint_vsx_default_levels",
    "cisco_cpu_default_levels",
    "cisco_fan_state_mapping",
    "cisco_ip_sla_default_levels",
    "cisco_nexus_cpu_default_levels",
    "cisco_oldcpu_default_levels",
    "cisco_power_sources",
    "cisco_power_states",
    "cisco_qos_default_levels",
    "cisco_sys_mem_default_levels",
    "cisco_temp_perf_envmon_states",
    "cisco_ucs_temp_cpu_default_levels",
    "cisco_ucs_temp_env_default_levels",
    "cisco_ucs_temp_mem_default_levels",
    "cisco_vss_operstatus_names",
    "cisco_vss_role_names",
    "citrix_serverload_default_levels",
    "citrix_sessions_default_levels",
    "climaveneta_alarms",
    "climaveneta_fan_default_levels",
    "climaveneta_sensors",
    "climaveneta_temp_default_levels",
    "cluster_info",
    "cmc_temp_default_levels",
    "cmctc_pcm_m_sensor_types",
    "condition_map",
    "cpsecure_sessions_default_levels",
    "cups_queues_default_levels",
    "datapower_cpu_default_levels",
    "datapower_mem_default_levels",
    "datapower_temp_default_levels",
    "db2_backup_default_levels",
    "db2_connections_default_levels",
    "db2_counters_default_levels",
    "db2_counters_map",
    "db2_mem_default_levels",
    "db2_sort_overflow_default_levels",
    "db2_tablespaces_default_levels",
    "ddn_s2a_faultsbasic_disks_default_levels",
    "ddn_s2a_faultsbasic_fans_default_levels",
    "ddn_s2a_readhits_default_levels",
    "ddn_s2a_stats_default_levels",
    "ddn_s2a_stats_io_default_levels",
    "ddn_s2a_statsdelay_default_levels",
    "decru_fan_default_levels",
    "default_running_ondemand_instance_families",
    "default_running_ondemand_instances",
    "dell_chassis_status_info",
    "dell_chassis_temp_default_levels",
    "dell_compellent_disks_health_map",
    "dell_om_sensors_default_levels",
    "dell_powerconnect_cpu_default_levels",
    "dell_powerconnect_fans_state_performance_map",
    "dell_powerconnect_fans_status2nagios_map",
    "dell_powerconnect_fans_status_map",
    "dell_powerconnect_psu_status2nagios_map",
    "dell_powerconnect_psu_status_map",
    "dell_powerconnect_psu_supply_map",
    "dell_powerconnect_temp_default_values",
    "diskstat_default_levels",
    "diskstat_diskless_pattern",
    "diskstat_inventory_mode",
    "docsis_channels_downstream",
    "docsis_channels_upstream_default_levels",
    "docsis_cm_status_default_levels",
    "domino_mailqueues_defaults",
    "domino_transactions_default_levels",
    "domino_users_default_levels",
    "dotnet_clrmemory_defaultlevels",
    "drbd_cs_map",
    "drbd_disk_default_levels",
    "drbd_disk_map",
    "drbd_ds_map",
    "drbd_general_map",
    "drbd_net_default_levels",
    "drbd_net_map",
    "drbd_stats_default_levels",
    "drbd_stats_map",
    "elasticsearch_cluster_shards",
    "elasticsearch_nodes",
    "eltek_battery_temp_default_variables",
    "eltek_fans_default_variables",
    "eltek_outdoor_temp_default_variables",
    "emc_datadomain_mtree_default_levels",
    "emc_isilon_fan_default_levels",
    "emc_isilon_info",
    "emc_isilon_power_default_levels",
    "emc_isilon_temp_cpu_default_levels",
    "emc_isilon_temp_default_levels",
    "emc_vplex_cpu_default_levels",
    "emcvnx_disks_default_levels",
    "emcvnx_sp_util_default_levels",
    "emcvnx_storage_pools_default_levels",
    "emcvnx_storage_pools_tiering_default_levels",
    "emerson_stat_default",
    "emerson_temp_default",
    "enterasys_cpu_default_levels",
    "enterasys_powersupply_default",
    "enterasys_temp_default_levels",
    "epson_beamer_lamp_default_levels",
    "esx_vsphere_objects_default_levels",
    "etherbox2_temp_default_levels",
    "f5_bigip_chassis_temp_default_params",
    "f5_bigip_conns_default_levels",
    "f5_bigip_cpu_temp_default_params",
    "f5_bigip_fans_default_levels",
    "f5_bigip_interface_states",
    "f5_bigip_mem_default_levels",
    "f5_bigip_pool_default_levels",
    "fan_fsc_sc2_levels",
    "fast_lta_headunit_info",
    "fc_port_admstates",
    "fc_port_default_levels",
    "fc_port_inventory_use_portname",
    "fc_port_no_inventory_admstates",
    "fc_port_no_inventory_opstates",
    "fc_port_no_inventory_phystates",
    "fc_port_no_inventory_types",
    "fc_port_opstates",
    "fc_port_phystates",
    "filehandler_default_levels",
    "filer_disks_default_levels",
    "filesystem_default_levels",
    "filesystem_levels",
    "fireeye_lic",
    "fireeye_mailq",
    "forced_mapping",
    "fortigate_cpu_base_default_levels",
    "fortigate_cpu_default_levels",
    "fortigate_ipsecvpn_default_levels",
    "fortigate_memory_base_default_levels",
    "fortigate_memory_default_levels",
    "fortigate_node_cpu_default_levels",
    "fortigate_node_sessions_default_levels",
    "fortigate_sessions_base_default_levels",
    "fortigate_sessions_default_levels",
    "fortigate_signature_default_levels",
    "fsc_fans_default_levels",
    "fsc_ipmi_mem_status_levels",
    "genua_fan_default_levels",
    "genua_pfstate_default_levels",
    "graylog_cluster_stats_elastic_defaultlevels",
    "graylog_license_default_levels",
    "graylog_nodes_default_levels",
    "graylog_sidecars_default_levels",
    "graylog_sources_default_levels",
    "gude_humidity_default_levels",
    "gude_powerbank_default_levels",
    "gude_relayport_default_levels",
    "gude_temp_default_levels",
    "hitachi_hnas_bossock_default_levels",
    "hitachi_hnas_cpu_default_levels",
    "hitachi_hnas_fpga_default_levels",
    "hivemanger_devices",
    "hivemanger_ng_devices",
    "hp_blade_present_map",
    "hp_blade_psu_inputline_status",
    "hp_blade_psu_status",
    "hp_blade_role_map",
    "hp_blade_status2nagios_map",
    "hp_blade_status_map",
    "hp_eml_sum_map",
    "hp_hh3c_ext_mem_default_levels",
    "hp_mcs_sensors_fan_default_levels",
    "hp_msa_disk_temp_default_levels",
    "hp_msa_health_state_numeric_map",
    "hp_msa_psu_default_levels",
    "hp_msa_psu_temp_default_levels",
    "hp_msa_state_map",
    "hp_msa_state_numeric_map",
    "hp_procurve_cpu_default_levels",
    "hp_procurve_mem_default_levels",
    "hp_procurve_status2nagios_map",
    "hp_procurve_status_map",
    "hp_proliant_cpu_status2nagios_map",
    "hp_proliant_cpu_status_map",
    "hp_proliant_da_cntlr_cond_map",
    "hp_proliant_da_cntlr_role_map",
    "hp_proliant_da_cntlr_state_map",
    "hp_proliant_fans_locale",
    "hp_proliant_fans_status_map",
    "hp_proliant_locale",
    "hp_proliant_psu_levels",
    "hp_proliant_speed_map",
    "hp_proliant_status2nagios_map",
    "hp_proliant_status_map",
    "hp_psu_temp_default_levels",
    "hp_sts_drvbox_cond_map",
    "hp_sts_drvbox_fan_map",
    "hp_sts_drvbox_power_map",
    "hp_sts_drvbox_sp_map",
    "hp_sts_drvbox_temp_map",
    "hp_sts_drvbox_type_map",
    "hpux_multipath_pathstates",
    "hpux_tunables_maxfiles_lim_default_levels",
    "hpux_tunables_nkthread_default_levels",
    "hpux_tunables_nproc_default_levels",
    "hpux_tunables_semmni_default_levels",
    "hpux_tunables_semmns_default_levels",
    "hpux_tunables_shmseg_default_levels",
    "hr_cpu_default_levels",
    "hsrp_states",
    "huawei_channel_default",
    "huawei_cpu_default",
    "huawei_mem_default",
    "huawei_mpu_board_name_start",
    "huawei_osn_laser_default_levels",
    "huawei_osn_power_default_levels",
    "huawei_osn_temp_default_levels",
    "huawei_switch_cpu_default_levels",
    "huawei_switch_hw_oper_state_map",
    "huawei_switch_mem_default_levels",
    "huawei_switch_stack_unknown_role",
    "huawei_switch_temp_default_levels",
    "hwg_humidity_defaultlevels",
    "hwg_temp_defaultlevels",
    "hyperv_vms_default_levels",
    "ibm_imm_fan_default_levels",
    "ibm_mq_queues_default_levels",
    "ibm_storage_ts_fault_nagios_map",
    "ibm_storage_ts_status_nagios_map",
    "ibm_storage_ts_status_name_map",
    "ibm_svc_cpu_default_levels",
    "ibm_svc_enclosurestats_temperature_default_levels",
    "ibm_svc_mdisk_default_levels",
    "ifoperstatus_inventory_porttypes",
    "ifoperstatus_monitor_unused",
    "infoblox_temp_default_levels",
    "informix_dbspaces_default_levels",
    "informix_locks_default_levels",
    "informix_logusage_default_levels",
    "informix_sessions_default_levels",
    "informix_tabextents_default_levels",
    "innovaphone_channels_default_levels",
    "innovaphone_cpu_default_levels",
    "innovaphone_licenses_default_levels",
    "innovaphone_mem_default_levels",
    "innovaphone_temp_default_levels",
    "ipr400_in_voltage_default_levels",
    "ipr400_temp_default_levels",
    "isc_dhcpd_default_levels",
    "j4p_performance_app_sess_default_levels",
    "j4p_performance_mem_default_levels",
    "j4p_performance_serv_req_default_levels",
    "j4p_performance_threads_default_levels",
    "janitza_umg_device_map",
    "janitza_umg_freq_default_levels",
    "janitza_umg_inphase_default_levels",
    "janitza_umg_temp_default_levels",
    "jenkins_queue_default_levels",
    "jolokia_jvm_memory",
    "jolokia_jvm_memory_pools",
    "jolokia_jvm_threading.pool",
    "jolokia_metrics_app_sess_default_levels",
    "jolokia_metrics_cache_hits_default_levels",
    "jolokia_metrics_queue_default_levels",
    "jolokia_metrics_serv_req_default_levels",
    "jolokia_metrics_threads_default_levels",
    "juniper_cpu_default_levels",
    "juniper_mem_default_levels",
    "juniper_screenos_cpu_default_levels",
    "juniper_screenos_temp_default_levels",
    "juniper_temp_default_levels",
    "juniper_trpz_flash_default_levels",
    "keepalived_default_levels",
    "kentix_amp_sensors_smoke_default_levels",
    "kentix_co",
    "kernel_counter_names",
    "kernel_default_levels",
    "kernel_metrics_names",
    "kernel_util_default_levels",
    "knuerr_rms_humidity_default_levels",
    "knuerr_rms_temp_default_levels",
    "levels_azure_sites",
    "levels_azure_storageaccounts",
    "levels_azure_usagedetails",
    "lgp_info_devices",
    "lgp_pdu_aux_states",
    "lgp_pdu_aux_types",
    "liebert_bat_temp_default",
    "liebert_compressor_default_levels",
    "liebert_cooling_default_levels",
    "liebert_cooling_position_default_levels",
    "liebert_fans_condenser_default_levels",
    "liebert_fans_default_levels",
    "liebert_maintenance_default_levels",
    "liebert_reheating_default_levels",
    "linux_nic_check",
    "logins_default_levels",
    "lparstat_default_levels",
    "lvm_lvs_default_levels",
    "map_dev_states",
    "map_luntype",
    "map_memtype",
    "map_operability",
    "map_presence",
    "map_readable_states",
    "map_units",
    "mbg_lantime_ng_refclock_types",
    "mbg_lantime_ng_temp_default_levels",
    "mbg_lantime_refclock_default_levels",
    "mbg_lantime_refclock_gpsstate_map",
    "mbg_lantime_refclock_refmode_map",
    "mbg_lantime_state_default_levels",
    "megaraid_bbu_refvalues",
    "mem_extended_perfdata",
    "mem_linux_default_levels",
    "mem_vmalloc_default_levels",
    "memory_default_levels",
    "memory_win_default_levels",
    "memused_default_levels",
    "mikrotik_signal_default_levels",
    "mongodb_cluster_levels",
    "mongodb_collections_levels",
    "mongodb_connections_default_levels",
    "mongodb_replica_set_levels",
    "mq_queues_default_levels",
    "msexch_dag_copyqueue_default_levels",
    "msexch_database_defaultlevels",
    "msexch_info_store_defaultlevels",
    "msexch_isclienttype_defaultlevels",
    "msexch_rpcclientaccess_defaultlevels",
    "msoffice_licenses_levels",
    "mssql_blocked_sessions_default_levels",
    "mssql_connections_default_levels",
    "mssql_tablespace_default_levels",
    "names",
    "netapp_api_cpu_cm_default_levels",
    "netapp_api_cpu_default_levels",
    "netapp_api_snapshots_default_levels",
    "netapp_cpu_default_levels",
    "netapp_fcpio_default_levels",
    "netctr_counter_indices",
    "netctr_counters",
    "netctr_default_params",
    "netextreme_cpu_util_default_levels",
    "netextreme_fan_default_levels",
    "netextreme_psu_default_levels",
    "netextreme_psu_in_default_levels",
    "netextreme_psu_out_default_levels",
    "netextreme_temp_default_levels",
    "netgear_fans_default_levels",
    "netscaler_cpu_default_levels",
    "netscaler_dnsrates_default_levels",
    "netscaler_ha_cur_states",
    "netscaler_ha_peer_mode",
    "netscaler_health_fan_default_levels",
    "netscaler_health_info",
    "netscaler_health_temp_default_levels",
    "netscaler_mem_default_levels",
    "nimble_latency_default_levels",
    "nodes_info",
    "nullmailer_mailq_default_levels",
    "nvidia_temp_core_default_levels",
    "nvidia_temp_default_levels",
    "omd_apache_patterns",
    "online_mapping",
    "openbsd_sensors_fan_default_levels",
    "openhardwaremonitor_fan_default_levels",
    "openhardwaremonitor_smart_default_levels",
    "openhardwaremonitor_smart_readings",
    "openhardwaremonitor_temperature_default_levels",
    "oracle_dataguard_stats",
    "oracle_diva_csm_tapes_default_levels",
    "oracle_instance_defaults",
    "oracle_jobs_defaults",
    "oracle_locks_defaults",
    "oracle_logswitches_default_levels",
    "oracle_longactivesessions_defaults",
    "oracle_recovery_area_defaults",
    "oracle_sessions_default_levels",
    "oracle_undostat_defaults",
    "palo_alto_sessions",
    "pandacom_temp_default_levels",
    "papouch_th2e_sensors_humidity_default_levels",
    "pfsense_counter_default_levels",
    "pfsense_if_default_levels",
    "poe_default_levels",
    "poe_faulty_status_to_string",
    "porttype_list",
    "poseidon_temp_default_levels",
    "postfix_mailq_default_levels",
    "postgres_bloat_default_levels",
    "postgres_connections_default_levels",
    "printer_supply_ricoh_default_levels",
    "prism_container_default_levels",
    "pse_poe_default_levels",
    "pulse_secure_cpu_util_def_levels",
    "pulse_secure_disk_util_def_levels",
    "pulse_secure_mem_util_def_levels",
    "pulse_secure_temp_def_levels",
    "qlogic_fcport_inventory_admstates",
    "qlogic_fcport_inventory_opstates",
    "qlogic_sanbox_status_map",
    "qmail_stats_default_levels",
    "qnap_fan_default_levels",
    "qnap_hdd_temp_default_levels",
    "quarantine_levels",
    "ra32e_sensors_voltage_defaultlevels",
    "ra32e_temp_defaultlevels",
    "rabbitmq_nodes_default_levels",
    "radio_state_map",
    "radio_unknown",
    "raritan_map_state",
    "raritan_map_type",
    "raritan_map_unit",
    "raritan_pdu_ocprot_current_default_levels",
    "raritan_pdu_plugs_default",
    "rds_licenses_product_versionid_map",
    "received_levels",
    "redis_info_persistence_default_levels",
    "rms200_temp_default_levels",
    "route_state_mapping",
    "route_type_mapping",
    "rstcli_states",
    "safenet_hsm_default_levels",
    "safenet_hsm_events_default_levels",
    "sansymphony_alerts_default_values",
    "sap_hana_connect_state_map",
    "sap_hana_ess_migration_state_map",
    "sap_hana_mem_database_default_levels",
    "sap_hana_mem_resident_default_levels",
    "saprouter_cert_default_levels",
    "security_master_temp_default_levels",
    "sensatronics_temp_default_levels",
    "severity_to_states",
    "shards_info",
    "siemens_plc_temp_default_levels",
    "skype_conferencing_defaultlevels",
    "skype_defaultlevels",
    "skype_edge_defaultlevels",
    "skype_edgeauth_defaultlevels",
    "skype_mediation_server_defaultlevels",
    "skype_mobile_defaultlevels",
    "skype_proxy_defaultlevels",
    "skype_sip_defaultlevels",
    "skype_xmpp_defaultlevels",
    "sles_license_default_levels",
    "smart_temp_default_levels",
    "socomec_outphase_default_levels",
    "sophos_map_oid",
    "splunk_health_default_levels",
    "splunk_license_state_default_levels",
    "splunk_license_usage_default_levels",
    "storcli_pdisks_default_levels",
    "stormshield_cluster_node",
    "stormshield_packets_default_levels",
    "stormshield_updates",
    "strem1_humidity_defaultlevels",
    "strem1_temp_defaultlevels",
    "strem1_wetness_defaultlevels",
    "stulz_humidity_default_levels",
    "stulz_temp_default_levels",
    "switch_cpu_default_levels",
    "sylo_default_levels",
    "symantec_av_updates_default_levels",
    "sync_name_mapping",
    "sync_status_mapping",
    "systemtime_default_values",
    "tasks_info",
    "temp_unitsym",
    "threads_default_levels",
    "tinkerforge_humidity_default_levels",
    "tsm_scratch_default_levels",
    "tsm_session_default_levels",
    "tunnel_states",
    "ucd_mem_default_levels",
    "ucs_bladecenter_fans_temp_default_levels",
    "ucs_bladecenter_psu_chassis_temp_default_levels",
    "ucs_bladecenter_psu_default_levels",
    "ucs_c_rack_server_led_default_levels",
    "ucs_c_rack_server_util_cpu_default_levels",
    "ucs_c_rack_server_util_mem_default_levels",
    "ucs_c_rack_server_util_overall_default_levels",
    "ucs_c_rack_server_util_pci_io_default_levels",
    "ucs_c_rack_server_util_power_default_levels",
    "ups_bat_temp_default",
    "ups_capacity_default_levels",
    "ups_cps_battery",
    "ups_eaton_enviroment_default",
    "ups_in_freq_default_levels",
    "ups_in_voltage_default_levels",
    "ups_modulys_inphase_default_levels",
    "ups_modulys_outphase_default_levels",
    "ups_out_voltage_default_levels",
    "varnish_backend_success_ratio_default_levels",
    "varnish_cache_hit_ratio_default_levels",
    "varnish_esi_default_levels",
    "varnish_worker_thread_ratio_default_levels",
    "veeam_client",
    "veeam_tapejobs_default_levels",
    "vsphere_object_names",
    "wagner_titanus_topsense_airflow_deviation_default_values",
    "wagner_titanus_topsense_info",
    "wagner_titanus_topsense_temperature_default_values",
    "watchdog_sensors_humidity_default_levels",
    "win_netstat_states",
    "win_printer_default_levels",
    "windows_license_default_levels",
    "wut_webtherm_defaultlevels",
    "wut_webtherm_humidity_defaultlevels",
    "zorp_connections",
}


class PreUpdateDeprecatedConfigurationStyle(PreUpdateAction):
    """Make sure users do not use .mk files to configure legacy check plguins"""

    def __call__(self, logger: Logger, conflict_mode: ConflictMode) -> None:
        if conflict_mode in (ConflictMode.INSTALL, ConflictMode.KEEP_OLD):
            return
        base_config.load_all_plugins(
            get_check_api_context,
            local_checks_dir=paths.local_checks_dir,
            checks_dir=paths.checks_dir,
        )
        base_config.load(changed_vars_handler=self.fail_upon_deprecated_check_config)

    @staticmethod
    def fail_upon_deprecated_check_config(changed_variables: set[str]) -> None:
        with disable_redis(), gui_context(), SuperUserContext():
            set_global_vars()
            all_rulesets = AllRulesets.load_all_rulesets()
        unregistered_vars = (
            changed_variables
            - {str(n) for n in agent_based_register.iter_all_discovery_rulesets()}
            - {str(n) for n in agent_based_register.iter_all_host_label_rulesets()}
            - set(all_rulesets.get_rulesets())
        )
        if not (
            problematic_variables := _DEPRECATED_CHECK_VARIABLES.intersection(unregistered_vars)
        ):
            return
        raise MKUserError(
            None,
            "Loading config variables for legacy check plugins is no longer supported. "
            f"Please remove the following variables from your .mk files: {', '.join(sorted(problematic_variables))}",
        )


pre_update_action_registry.register(
    PreUpdateDeprecatedConfigurationStyle(
        name="deprecated_configuration_style",
        title="Deprecated .mk configuration of plugins",
        sort_index=1000,  # check the rulesets first!
    )
)
