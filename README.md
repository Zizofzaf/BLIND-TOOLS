# BLIND-TOOLS

sudo apt update
sudo apt install git

git clone https://github.com/Zizofzaf/BLIND-TOOLS.git

cd blind-tools

sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python tools.py
