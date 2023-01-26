#!/usr/bin/env bash
# install NGINX if not installed
# create a fake html content , create a symbolic link
# change ownership and group uownership to ubuntu
# updat nginx cofiguration file

which nginx >/dev/null 2>&1
a=$(echo $?)
if [ $a -eq 1 ]
then
	
	sudo apt update
	sudo apt install nginx
	sudo ufw allow 'Nginx HTTP'
	sudo systemctl start nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "to test your Nginx configuration">/data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/ 
sudo chgrp -R ubuntu /data/

sudo printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        server_name _;
        add_header X-Served-By $hostname;
        location /hbnb_static/ {
                alias /data/web_static/current/;
                index index.html index.htm;
        }

        if ($request_filename ~ redirect_me){
                rewrite ^ https://youtube.com permanent;
        }
        error_page 404 /404.html;
        location = /404.html {
                internal;
        }
}" > /etc/nginx/sites-available/default

sudo service nginx restart	
