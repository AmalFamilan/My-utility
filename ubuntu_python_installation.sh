sudo apt update
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev
python3 --version
ls -la /usr/bin/python3
sudo rm /usr/bin/python3
sudo ln -s python3.10 /usr/bin/python3
python3 --version
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
python3.10 -m pip --version
python3.10 -m pip install ipython