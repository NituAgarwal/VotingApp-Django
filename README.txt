This is a Voting Application created using django

Framework Required:
1. Django
2. MySQL

Instruction to setup Django settings with MySQL

1. Open firstproject/settings.py
2. Update the following information in settings.py 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'VOTEPOLL', #database name
        'USER': '', # mention username to loging to mysql
        'PASSWORD': '', # mention the password to login to mysql
        'HOST': '',   # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}

Instructions to run the Project

1. Download the project https://github.com/NituAgarwal/VotingApp-Django by clicking on "Download ZIP" and save it in desired locatio
2. Extract files
3. Open terminal
4. Go to the location where project files are extracted
5. move to firstproject directory
6. manage.py file will be available. Run the cmd:
	python manage.py runserver
7. Go to URL http://localhost:<port_number>/voteapp 
Note: mention port_number as mentioned in terminal


Instruction for admin to create questions and choices for voteapp

After server is run, 
1. Go to URL http://localhost:<port_number>/admin
2. Click on Questions
3. You will be able to see Questions and Choices with votes on it
4. To add a question, click on "Add Question" and add desire questions and choices

Currently one user for admin is created
username:admin
password:1
