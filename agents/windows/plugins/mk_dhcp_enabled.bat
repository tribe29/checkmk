@echo off
set CMK_VERSION="2.2.0p27"
echo ^<^<^<winperf_if_dhcp^>^>^>
wmic path Win32_NetworkAdapterConfiguration get Description, dhcpenabled
