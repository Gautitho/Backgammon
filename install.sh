git clone git@github.com:Gautitho/Backgammon.git
sudo apt-get update
sudo apt-get install python3-venv
python3 -m venv .env
source .env/bin/activate
pip install --upgrade pip
pip install django
pip freeze > requirements.txt