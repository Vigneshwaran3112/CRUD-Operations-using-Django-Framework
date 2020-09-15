# CRUD-Operations-using-Django-Framework
It performs create, retrive, update and delete operations in MYSQL Database using python DJANGO WEB FRAMEWORK.

# First INSTALLATION SETUP
  1. Download and Install Python from official website: https://www.python.org/downloads/ then install it.
  2. Download and Install XAMPP SERVER from official website: https://www.apachefriends.org/ then install it.
       - because now i use mysql database
  3. Then, now install VIRTUAL ENVIRONMENT for our djanog project,
       - open CMD, type pip install virtualenv, then hit enter
       - create virtual environment so,
         - open CMD, type virtualenv venv, then hit enter ( venv is just a name for virtual environment so, i named venv. it is not mandatory to use same name. )
         - change cmd directory to you are create virtualenv folder, then activate virtual environment, type venv\Scripts\activate, then hit enter
  4. Install Mysql client so, activate your virtual environment
       - open CMD, type venv\Scripts\activate because now you are install all packages in virtual environment
       - type, pip install mysqlclient, then hit enter
         -  any errors are throwed or any problems are occur to installing mysql client
         - then follow another method to install mysql client
       - open your browser, then goto https://www.lfd.uci.edu/~gohlke/pythonlibs/ url then scroll down your webpage and find it mysqlclient,
       - then download mysqlclient for suitable your python version( mysqlclient cp38 something ) and then your cp38 number and python 3.8 version number is same then download it.
       - then copy download file to change directory into your virtual environment folder, then follows these below commands
         - type pip install mysqlclient-1.4.6-cp38-cp38-win_amd64.whl, ( this is you are download file name )
         - then mysql client is successfully installed on your virtual environment
   5. Install Django - pip install django, then hit enter
   6. Then, installation is fully completed
   
# CREATE NEW DJANGO PROJECT
  1. first activate virtual environment
       - open CMD, type venv\Scripts\activate, then hit enter
  2. type django-admin startproject << your project name >>, then hit enter
  3. change directory to your project folder from virtual environment
       - cd << your project name >>
  4. type python manage.py migration, then hit enter
  5. type python manage.py runserver, then hit enter # this command is used to run your django project
  6. open browser and type localhost\8000 on your addressbar then hit enter and it displayed django named webpage
       - because your project as successfully runned
 
# CREATE NEW DJANGO APP
  1. type python manage.py << your app name >>, hit enter
       -then your app successfully created for your project
       
# SETUP DJANGO SETTING CONFIG
  1. first choose editor software to edit files, but i used pycharm IDLE and SUBLIME TEXT software
  2. go to your django project named folder inside your project
  3. then open setting folder on your editor, then find DATABASE variable
       - because now i changed the django default database SQLIT3 into MYSQL database and edit it. ( follows the my setting.py file )

# THEN CODE FOR CRUD OPERATIONS
  1. first you are create database same as your setting.py file
       - open xampp control pannel
       - click to start apache and mysql 
       - click admin in mysql
       - then automatically open mysql database ui
       - click New, then right side display create new database
       - type database name same as setting.py database 'name'
       -then close it.
  2. next create table for database using models.py file
  3. then create template and static folder for web design
  4. and open views.py file then create project views and code it
  5. create url path for your views in urls.py file 
  6. then, your project is fully completed and any dout refer project
       
