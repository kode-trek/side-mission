sudo apt-get update
sudo apt-get install -y php
sudo apt-get install -y apache2
sudo apt-get install -y libapache2-mod-php

sudo chown -R www-data:www-data /var/www/html

sudo gzip /var/www/html/index.html
sudo cp default.htm /var/www/html/
sudo cp diff.sh /var/www/html/
sudo cp writer.php /var/www/html/

cp -rf grab_it.js manifest.json icons/ ~/Desktop
