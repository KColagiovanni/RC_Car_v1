!#/bin/sh

sudo apt update
sudo apt upgrade -y
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install rpi.gpio
sudo apt install git -y
sudo apt install python3-pip
pip install flask
git clone https://github.com/KColagiovanni/RC_Car_v1.git

echo "python3 ~/RC_Car_v1/app.py" >> ~/.bashrc

echo "All Done!!!! Rebooting now."

sudo shutdown -r now
