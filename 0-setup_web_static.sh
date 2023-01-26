#!/usr/bin/env bash
	
sudo apt update
sudo apt install nginx
sudo ufw allow 'Nginx HTTP'
sudo systemctl start nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo echo "to test your Nginx configuration">/data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu /data/ 
sudo chgrp -R ubuntu /data/
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart	
