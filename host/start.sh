sudo apt install npm
sudo apt install mysql.server
sudo apt install python3
sudo pip3 install flask
sudo pip3 install flask_wtf
sudo pip3 install flask_mysqldb
sudo pip3 install pandas
sudo pip3 install openpyxl
service mysql stop
service mysql start
echo "Installation Complete"
clear
mysql -uroot