
python3 -m venv env
source env/bin/activate
pip install Flask

pip freeze > requirements.txt
pip install -r requirements.txt
deactivate

python3 todo.py
gunicorn --bind 0.0.0.0:5000 wsgi:app
