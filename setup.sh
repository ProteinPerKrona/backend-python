# Setup venv
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

# Start server
uvicorn server:app --reload