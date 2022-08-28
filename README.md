Create vartual enviornment 
python3 -m venv myvenv

activate vartual enviornment
myvenv\Scripts\activate

install the required packages
pip install -r requirements.txt

create admin user 
python manage.py createsuperuser

run server
python manage.py runserver

admin url: 
http://127.0.0.1:8000/admin
in admin pannel we need to add all the required informati (bus info, schedule info, driver info)


applicaiton url:
http://127.0.0.1:8000
