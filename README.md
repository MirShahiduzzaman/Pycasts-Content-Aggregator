# PyCasts Content Aggregator

## Set up Virtual Env (in Windows Powershell)

Initialize virtual env: 'python3 -m venv .venv'

Activate virtual env: '.venv/Scripts/Activate.ps1'

## How to Run
1. Open two instances of PowerShell in the project directory
2. Activate virtual env in both with '.venv/Scripts/Activate.ps1'
3. Run 'python manage.py startjobs' in one Powershell Instance
4. Run 'python manage.py runserver' in the other instance
5. Open http://127.0.0.1:8000/ in browser
6. If not done already, create superuser account with 'python manage.py createsuperuser'
7. Open http://127.0.0.1:8000/admin in browser to view admin page


## Features
### User Page
In this page, the user is able to look through several podcasts relating to Python and click a link to redirect them to the selected episode. To best choose their episode of interest, some information is given such as title, picture, a brief description of the episode, and the link to the episode itself!

<img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/b71ab49b-42d6-4866-a0e9-6f8dab00cc77" width = "" height = "">

### Admin Page
Log In Screen

Before accessing the dashboard, the user needs to be authenticated to ensure no unintended user is able to view the given data. 

<img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/50481a3d-35a9-43b1-95fc-c72c82a5718b" width = "350" height = "300">

Dashboard

After logging in, the admin user is taken to the dashboard, which displays information under 3 categories:
1. Authentication and Authorization
      - groups and users (so far, there are only admin users)
      <img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/7b55b21e-3bc8-4d92-abcf-36da9715551c" width = "500" height = "250">

2. Django APScheduler
    - Django job executions (for the purposes of showing how it works, podcast retrieval jobs were set to execute every 2 minutes, but can be edited to be less/more frequent in '.../podcasts/management/startjobs.py')
    <img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/069a6402-de7e-44f0-849e-a2508bbe57f6" width = "600" height = "300">

    - Django jobs (3 jobs, 2 to retrieve podcast data from 2 different podcast sources and 1 to delete job execution history)
    <img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/12c841a3-6180-4014-9956-4961167b1d5c" width = "600" height = "300">


3. Podcasts
      - Episodes (ordered alphabetically by podcast name)
      <img src = "https://github.com/MirShahiduzzaman/content-aggregator/assets/43242843/e85a3402-3680-47e9-9b16-b93f3a7bd266" width = "600" height = "300">
