#!/usr/bin/env bash
# setup for deployment
apt-get -y update
apt-get -y install nginx
SRC="/etc/nginx/sites-available/default"
STATIC="\\\tlocation /hbnb_static/ {\n\t\t alias /data/web_static_current/;\n\t}\n"
sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
echo "Hello World" | sudo tee "/data/web_static/releases/test/index.html"
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"
sudo chown -R ubuntu:ubuntu "/data/"
sudo sed -i "35i $STATIC" $SRC
sudo service nginx restart
