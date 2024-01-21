#!/bin/bash
sudo apt-get update
sudo apt-get install -y php
sudo apt-get install -y apache2
sudo apt-get install -y libapache2-mod-php
sudo apt-get install mysql-server

sudo chown -R www-data:www-data /var/www/html
sudo gzip /var/www/html/index.html
