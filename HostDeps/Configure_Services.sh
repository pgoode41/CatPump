#!/bin/bash

#################################################################################################
#################################################################################################
function Create_Service {
    service_name="${1}.service"
    service_Config_Path="/etc/systemd/system/${service_name}"
    service_Script_Path="${2}"
    service_Description="${service_name} service"

    echo "[Unit]" > ${service_Config_Path}
    echo "Description=${service_Description}" >> ${service_Config_Path}
    echo "After=network.target" >> ${service_Config_Path}
    echo "After=systemd-user-sessions.service" >> ${service_Config_Path}
    echo "After=network-online.target" >> ${service_Config_Path}
    echo "" >> ${service_Config_Path}

    echo "[Service]" >> ${service_Config_Path}
    echo "User=root" >> ${service_Config_Path}
    echo "Type=simple" >> ${service_Config_Path}
    echo "ExecStart=${service_Script_Path}" >> ${service_Config_Path}
    echo "Restart=on-failure" >> ${service_Config_Path}
    echo "RestartSec=30" >> ${service_Config_Path}
    echo "StartLimitInterval=350" >> ${service_Config_Path}
    echo "StartLimitBurst=10" >> ${service_Config_Path}
    echo "" >> ${service_Config_Path}

    echo "[Install]" >> ${service_Config_Path}
    echo "WantedBy=multi-user.target" >> ${service_Config_Path}

    systemctl daemon-reload

    chmod u+x ${service_Script_Path}

    sudo systemctl start ${service_name}

    sudo systemctl enable ${service_name}

}
#################################################################################################
#################################################################################################

Create_Service "Jeston_SwapSpace" "/home/preston/catpump/HostDeps/swapspace.sh"
Create_Service "Host_Update_Service" "/home/preston/catpump/HostDeps/Update_Service.py"