Fastest way to start Airflow in Docker to use MacOS:
 

1. Download Docker:

    > Set up an application
    
    > Choose the Docker menu whale menu > Preferences from the menu bar and configure the runtime options described below.
    
    
2. On the General tab, you can configure when to start and update Docker:

    > Automatically check for updates: By default, Docker Desktop is configured to check for newer versions automatically. If you have installed Docker Desktop as part of an organization, you may not be able to update Docker Desktop yourself. In that case, upgrade your existing organization to a Team plan and clear this checkbox to disable the automatic check for updates.

    > Start Docker Desktop when you log in: Automatically starts Docker Desktop when you open your session.

    > Include VM in Time Machine backups: Select this option to back up the Docker Desktop virtual machine. This option is disabled by default.

    > Use gRPC FUSE for file sharing: Clear this checkbox to use the legacy osxfs file sharing instead.

    > Send usage statistics: Docker Desktop sends diagnostics, crash reports, and usage data. This information helps Docker improve and troubleshoot the application. Clear the check box to opt out.

    > Show weekly tips: Displays useful advice and suggestions about using Docker.

    > Open Docker Desktop dashboard at startup: Automatically opens the dashboard when starting Docker Desktop.
    
    
    
3. Open Visual Studio Code 

    
    > Open terminal : mkdir airflow  >>> cd airflow
     
    
    > curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.1.2/docker-compose.yaml   -  To deploy Airflow on Docker Compose, you should fetch docker-compose.yaml.
    
    
    > mkdir ./dags ./logs ./plugins    create the necessary directories 
    
    
    > echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env   - create user and password 
    
    
    > docker-compose up airflow-init  -  On all operating systems, you need to run database migrations and create the first user account. To do it, run
    
    
    > docker-compose up  -  Now you can start all services
    

    > python3 -m venv sandbox - create python environment 

    > pip install -r requirements.txt install python deps 

    
    > Go to localhost:8080 

    > Go to your DAG directory and create your first dag by command  > touch newfile.py
    
    >  Go you the UI , and check your dags is implemented !



5. API connection
Open Visual Studio Code and open new terminal:

    >  curl -sSL https://install.astronomer.io | sudo bash -s -- v0.21.0  - install astronomer
    
    >  mkdir airflow-2 - cd airlfow-2
    
    >  code .   - create .env file
    
    >  astro dev init   - initialize astronomer
    
    >  FROM astronomerio/ap-airflow:2.0.0-1.dev2-buster-onbuild  - Change the docker image of Airflow in the Dockerfile 
    
    >  AIRFLOW__API__AUTH_BACKEND=airflow.api.auth.backend.basic_auth  - Change the authentication backend for the API in .env
    
    >  astro dev start
    
    > curl --verbose 'http://localhost:8080/api/v1/variables' \
-H 'content-type: application/json' \
--user "admin:admin"   - check the API 

    > Go to localhost:8080 
    
    > Click "Connection" : add key and value
    
    > Go to your terminal and run : curl --verbose 'http://localhost:8080/api/v1/variables' \
-H 'content-type: application/json' \
--user "admin:admin"   - check the API is working

    > cd .. - back 
    
    > git clone https://github.com/marclamberti/airflow-2-demo-api.git  - Set up the UI
    
    > cd airflow-2-demo-api.git  - you can see variable-manager
    
    > sudo apt get install npm - install npm  
    
    > npm start 
    
    > Go to localhost:3000 - Airflow Variable Manager and Create variable : key and value
    
    > Go to the UI and check created Variables 
    
    
