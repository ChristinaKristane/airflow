Fastest way to start Airflow to use MacOS without Docker :
1. Installing the VM:
    > Go to the virtualbox page: https://www.virtualbox.org/wiki/Downloads
  
    > Select your operating system, to download VirtualBox
    
    > Once it is downloaded, double click on it and follow the instructions to install it on your computer

    > Once installed, open Virtual Box and you should obtain the following output
 
2. Setting up the Virtual Machine:  
    > Download ViertualBox and set-up an application
    > downloaded the Virtual Machine, you should have a file called AirflowVM.ova and Double click on it (You might NEED to uncheck Import hard drives as VDI if case you get an error after importing it related to 'medium')
    > Click on "Start" and wait for the VM to start until you get the following output from it
 
 3. SSH and Visual Studio Code

    > Access the VM in SSH and connect Visual Studio Code through it.
    
    > Open your terminal and type: ssh -p 2222 airflow@localhost
    
    > Enter the password: airflow

4. Open Terminal :
    > python3 -m venv sandbox - create python environment
    
    > source sandbox/bin/activate - activate python evironment
    
    > pip install wheel   - install python module
    
    > pip install apache-airflow==2.0.1 --constraint https://gist.githubusercontent.com/marclamberti/742efaef5b2d94f44666b0aec020be7c/raw/21c88601337250b6fd93f1adceb55282fb07b7ed/constraint.txt
    
    > airflow db init - initializate db
    
    > airflow websever 
    
    > cd airflow
    
    > mkdir dags
    
    > touch newfile.py (Input the code inside file first.dag)
    
    > airflow websever 
    
    > Open second terminal and enter command - airflow scheduler 
    
    > Go to localhost:8080 put login and password: admin admin
    
    > Check you DAGS: you can see following file newfile.py is implemented .

