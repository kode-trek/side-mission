sudo rm -rf /var/www/html/"$1"
sudo cp -rf "$1" /var/www/html/
sudo chown -R www-data:www-data /var/www/html
