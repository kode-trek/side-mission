sudo apt-get update
sudo apt-get install -y apache2
sudo mkdir -p /var/www/btnhd.com/public_html
sudo chown -R $USER:$USER /var/www/btnhd.com/public_html
sudo chmod -R 755 /var/www
echo 'hello, world!' > /var/www/btnhd.com/public_html/index.htm
sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/btnhd.com.conf

#<VirtualHost *:80>
#        ServerAdmin info@btnhd.com
#        ServerName btnhd.com
#        ServerAlias www.btnhd.com
#        DocumentRoot /var/www/btnhd.com/public_html
#        ErrorLog ${APACHE_LOG_DIR}/error.log
#        CustomLog ${APACHE_LOG_DIR}/access.log combined
#</VirtualHost>

sudo a2ensite btnhd.com.conf
sudo a2dissite 000-default.conf
sudo service apache2 restart

#sudo nano /etc/hosts
#127.0.0.1       localhost
#127.0.1.1       300E4C-300E5C-300E7C
#192.168.1.101 btnhd.com

## The following lines are desirable for IPv6 capable hosts
#::1     ip6-localhost ip6-loopback
#fe00::0 ip6-localnet
#ff00::0 ip6-mcastprefix
#ff02::1 ip6-allnodes
#ff02::2 ip6-allrouters


