MONITORING_PLUGINS := monitoring-plugins
MONITORING_PLUGINS_VERS := 2.3
MONITORING_PLUGINS_DIR := $(MONITORING_PLUGINS)-$(MONITORING_PLUGINS_VERS)

MONITORING_PLUGINS_PATCHING := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-patching
MONITORING_PLUGINS_BUILD := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-build
MONITORING_PLUGINS_INSTALL := $(BUILD_HELPER_DIR)/$(MONITORING_PLUGINS_DIR)-install

#MONITORING_PLUGINS_INSTALL_DIR := $(INTERMEDIATE_INSTALL_BASE)/$(MONITORING_PLUGINS_DIR)
MONITORING_PLUGINS_BUILD_DIR := $(PACKAGE_BUILD_DIR)/$(MONITORING_PLUGINS_DIR)
#MONITORING_PLUGINS_WORK_DIR := $(PACKAGE_WORK_DIR)/$(MONITORING_PLUGINS_DIR)

MONITORING_PLUGINS_CONFIGUREOPTS := \
    --prefix=$(OMD_ROOT) \
    --libexecdir=$(OMD_ROOT)/lib/nagios/plugins \
    --with-snmpget-command=$(OMD_ROOT)/bin/snmpget \
    --with-snmpgetnext-command=$(OMD_ROOT)/bin/snmpgetnext

$(MONITORING_PLUGINS): $(MONITORING_PLUGINS_BUILD)

$(MONITORING_PLUGINS_BUILD): $(MONITORING_PLUGINS_PATCHING)
	cd $(MONITORING_PLUGINS_BUILD_DIR) ; ./configure $(MONITORING_PLUGINS_CONFIGUREOPTS)
	$(MAKE) -C $(MONITORING_PLUGINS_BUILD_DIR) all
	$(RM) plugins-scripts/check_ifoperstatus plugins-scripts/check_ifstatus
	$(TOUCH) $@

$(MONITORING_PLUGINS_INSTALL): $(MONITORING_PLUGINS_BUILD)
	$(MAKE) DESTDIR=$(DESTDIR) -C $(MONITORING_PLUGINS_BUILD_DIR) install
	# FIXME: pack these with SUID root
	install -m 755 $(MONITORING_PLUGINS_BUILD_DIR)/plugins-root/check_icmp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	install -m 755 $(MONITORING_PLUGINS_BUILD_DIR)/plugins-root/check_dhcp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins
	ln -sf check_icmp $(DESTDIR)$(OMD_ROOT)/lib/nagios/plugins/check_host

	# Copy package documentations to have these information in the binary packages
	$(MKDIR) $(DESTDIR)$(OMD_ROOT)/share/doc/$(MONITORING_PLUGINS)
	set -e ; for file in ACKNOWLEDGEMENTS AUTHORS CODING COPYING FAQ NEWS README REQUIREMENTS SUPPORT THANKS ; do \
	   install -m 644 $(MONITORING_PLUGINS_BUILD_DIR)/$$file $(DESTDIR)$(OMD_ROOT)/share/doc/$(MONITORING_PLUGINS); \
	done
	$(TOUCH) $@
