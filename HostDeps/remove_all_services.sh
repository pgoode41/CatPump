#!/bin/bash

function remove_service {
    serviceName="${1}.service"
    systemctl stop ${serviceName}
    systemctl disable ${serviceName}
    #rm /etc/systemd/system/${1}
    rm "/lib/systemd/system/${serviceName}"
    systemctl daemon-reload
    systemctl reset-failed
}

remove_service "Start_All_Containers"
remove_service "Jeston_SwapSpace"
remove_service "pump_boot_actions" 
remove_service "jetson_full_power"
remove_service "flask"


