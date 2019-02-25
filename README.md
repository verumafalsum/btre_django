# BTRE Django

Site for real estate search and interaction with realtors.

## Running project
Python 3.5 or higher and virtualenv are required.
Run the following commands to create virtual enviroment:
```bash
python3 -m virtualenv venv
```
After creating a virtual environment activate it:

### Linux
```bash
source venv/bin/activate
```
### Windows
```
venv\Scripts\activate.bat
```
After activation install dependencies:
```bash
pip install -r requirements.txt
```
After the installation you need to run database migrations:
```bash
python manage.py migrate
python manage.py runserver
```
