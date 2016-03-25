This is a Voting Application created using django

Please make sure following applications are installed in your system
1. Django
2. MySQL Server version: 5.7.11 


1. git clone https://github.com/NituAgarwal/VotingApp-Django.git 
2. cd VotingApp-Django


Instruction to setup Django settings with MySQL

1. Open firstproject/settings.py in any editor
2. Update the following information in settings.py 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'databasename', #database name which is created
        'USER': '', # mention username to loging to mysql
        'PASSWORD': '', # mention the password to login to mysql
        'HOST': '',   # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}
3. run command : $python manage.py migrate
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file


Instruction for admin to create questions and choices for voteapp
1. cd firstproject
2. to create admin user: $python manage.py createsuperuser
	It will ask for following details: 
	Username : <Enter username for admin>
	Email address: <this can be left blank>
	Password: <Enter password>
	Password (again):
3. to start the server:  $python manage.py runserver
After server is run, 
1. Go to URL http://localhost:<port_number>/admin
Note: mention port_number as mentioned in terminal
2. Click on Questions
3. To add a question, click on "Add Question" and add desire question and choices
4.You will be able to see Question and Choices with votes on it 

Instructions to run the voting application
Go to URL http://localhost:<port_number>/voteapp
Vote on Question and submit to vote 

To run test cases:
python manage.py test voteapp
Note: voteapp is the application name where tests.py is available

