#!/usr/bin/env bash
# install NGINX if not installed
# create a fake html content , create a symbolic link
# change ownership and group uownership to ubuntu
# updat nginx cofiguration file

which nginx >/dev/null 2>&1
a=$(echo $?)
if [ $a -eq 0 ]
then
	echo "NGINX is already installed"
else
	sudo apt update
	sudo apt install nginx
	sudo ufw allow 'Nginx HTTP'
	sudo systemctl start nginx
fi

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "to test your Nginx configuration">/data/web_static/releases/test/index.html
rm /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/ 
sudo chgrp -R ubuntu /data/

sudo service nginx restart	
