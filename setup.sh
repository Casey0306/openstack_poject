#!/bin/bash
echo "Enter application env var"
echo "Enter OPENSTACK-API-IP:"
read OPENSTACKAPIIP
echo "ENTER OPENSTACK-PROJECT-NAME:"
read OPENSTACKPROJECTNAME
sudo apt update
sleep 30
sudo apt -y upgrade
sleep 30
sudo apt install -y git
sleep 10
sudo apt install -y python3-pip
sleep 10
sudo apt install -y virtualenv
sleep 10
sudo apt install -y nginx
sleep 10
virtualenv --python=python3.6 app
sleep 1
source app/bin/activate
sleep 1
git clone https://github.com/Casey0306/openstack_poject.git
sleep 10
cd openstack_poject
sleep 1
pip install -r requirements.txt
sleep 10
sudo cat /dev/null > .env
{
  echo "OPENSTACK_API_IP='$OPENSTACKAPIIP'"
  echo "OPENSTACK_PROJECT_NAME='$OPENSTACKPROJECTNAME'"
} > .env
sleep 1
deactivate
sleep 1
cd
sleep 2
touch start_flask.sh
chmod 755 start_flask.sh
sleep 1
{
	    echo "source /root/app/bin/activate"
        echo "cd /root/openstack_poject/"
        echo "python rest_api.py"
} > start_flask.sh
sleep 1
{
	    echo "[Unit]"
        echo "Description=Flaskweb"
        echo ""
        echo "[Service]"
        echo "ExecStart=/bin/bash '/root/start_flask.sh'"
        echo "Type=oneshot"
        echo ""
	    echo "[Install]"
	    echo "WantedBy=multi-user.target"
	    echo "Alies=flaskapi.service"
} > /etc/systemd/system/flaskweb.service
sleep 2
systemctl daemon-reload
sleep 2
systemctl enable flaskweb.service
sleep 2

rm /etc/nginx/sites-enabled/default
sleep 1
touch /etc/nginx/sites-enabled/rest_api
sleep 1
{
        echo "server {"
        echo "# прослушивание порта 80 (http)"
        echo "listen 80;"
        echo "server_name _;"
        echo ""
        echo "# запись доступа и журналы ошибок в /var/log"
        echo "access_log /var/log/rest_api_access.log;"
	    echo "error_log /var/log/rest_api_error.log;"
	    echo ""
        echo "location / {"
        echo "# переадресация запросов приложений на сервер flask"
        echo "proxy_pass http://localhost:5000;"
	    echo "proxy_redirect off;"
	    echo 'proxy_set_header Host $host;'
	    echo 'proxy_set_header X-Real-IP $remote_addr;'
	    echo 'proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;'
	    echo "   }"
	    echo "}"
} > /etc/nginx/sites-enabled/rest_api
sleep 5
systemctl reload nginx
sleep 2
systemctl enable nginx
sleep 2
systemctl restart nginx
sleep 2