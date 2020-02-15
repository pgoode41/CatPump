#!/bin/bash

#################################################################################################
#################################################################################################
function Create_Service {
    service_name="${1}.service"
    service_Config_Path="/lib/systemd/system/${service_name}"
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

function Flask_Service_Config {
    service_name="flask.service"
    service_Config_Path="/lib/systemd/system/flask.service"
    service_Script_Path="${1}"
    service_Description="${service_name} service"


    echo "[Unit]" > ${service_Config_Path}
    echo "Description=Flask web server" >> ${service_Config_Path}
    echo "[Install]" >> ${service_Config_Path}
    echo "WantedBy=multi-user.target" >> ${service_Config_Path}
    echo "[Service]" >> ${service_Config_Path}
    echo "User=root" >> ${service_Config_Path}
    echo "PermissionsStartOnly=true" >> ${service_Config_Path}
    echo "ExecStart=/usr/bin/python3 ${service_Script_Path}" >> ${service_Config_Path}
    echo "TimeoutSec=600" >> ${service_Config_Path}
    echo "Restart=on-failure" >> ${service_Config_Path}
    echo "RuntimeDirectoryMode=755" >> ${service_Config_Path}

    flaskConfig='/etc/init/flask.conf'
    script_path=${1}

    echo 'description "flask"' > ${flaskConfig}
    echo 'start on stopped rc RUNLEVEL=[2345]' >> ${flaskConfig}
    echo 'respawn' >> ${flaskConfig}
    echo "exec python3 ${script_path}" >> ${flaskConfig}



    systemctl daemon-reload
    chown root ${service_Script_Path}
    chmod u+x ${service_Script_Path}
    sudo systemctl start ${service_name}
    sudo systemctl enable ${service_name}
    
}

function Catpump_Api_Service_Create {
    docker pull pgoode41/catpump-api 
    docker run -d -p 8085:8085 -p 8086:8086 --restart=always --privileged --runtime=nvidia pgoode41/catpump-api 
}

function Jetson_Full_Power {
    #Set 10Watt(full power)
    #Barrel Power only
    sudo nvpmodel -m 0
}

function Kube_Services_Create {
    cp /etc/rancher/k3s/k3s.yaml ~
    export KUBECONFIG='/etc/rancher/k3s/k3s.yaml'
    kubectl apply -f ${1}/Deploy.yaml
}
#################################################################################################
#################################################################################################


Create_Service "Start_All_Containers" "/home/preston/catpump/HostDeps/Start_All_Containers.sh"
Create_Service "Jeston_SwapSpace" "/home/preston/catpump/HostDeps/swapspace.sh"
Create_Service "pump_boot_actions" "/home/preston/catpump/HostDeps/pump_boot_actions.py"
Create_Service "jetson_full_power" "/home/preston/catpump/HostDeps/jetson_full_power.sh"
#Flask_Service_Config "/home/preston/catpump/HostDeps/Update_Service.py"
#Catpump_Api_Service_Create
#Jetson_Full_Power
#Kube_Services_Create "/home/preston/catpump/HostDeps"
