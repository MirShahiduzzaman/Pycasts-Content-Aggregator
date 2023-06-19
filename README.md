# Content Aggregator

# Set up Virtual Env
To initialize virtual env: python3 -m venv .venv
To activate virtual env in Windows: .venv/Scripts/Activate.ps1

# How to Run
Open two instances of PowerShell in the project directory (.../pycasts)
Activate virtual env in both with '.venv/Scripts/Activate.ps1'
Run 'python manage.py startjobs' in one Powershell Instance
Run 'python manage.py runserver' in the other instance
Open http://127.0.0.1:8000/ in browser
Open http://127.0.0.1:8000/admin in browser to view admin page (You would have set up the password during venv setup)
