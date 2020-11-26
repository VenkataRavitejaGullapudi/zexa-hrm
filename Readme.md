# Zexa Human Resource Management System

### To run this project Follow below steps (These are according to windows system so please change your command according to the os)
##### First Make sure that python installed in your system
1. Open Command Prompt
2. Navigate to the Drive or Folder you want to setup
3. Create a directory by the following command
  `mkdir HRMZexa`
4. Change directory to HRMZexa
   `cd HRMZexa`
-- If you not interested to setup virtual enviroment directly go to step-8
5. Install virual environment
  `pip install virtualenv`
6. Next create Virtual environment
  `virtualenv venv`
7. Next activate virual environment
   `venv\Scripts\activate`
8. Clone the repository *HRMZexa Folder* (if you know git commands) or else simply download the git repository and extract it to *HRMZexa Folder*
------------If cloning the repositry `git clone https://github.com/ravi777-developer/zexa-hrm.git` -------------------
9. Navigate into that folder(project folder) if not navigated
    `cd zexa-hrm` or `cd zexa-hrm-master`
10. Install requirements for the project(already included for deployment)
    `pip install -r requirements.txt`
11. Run the server
    `python manage.py runserver` or `python manage.py runserver "localhost" `

// *Only for testing purpose*

// *If you want you can create superuser directly from command prompt using `python manage.py createsuperuser`*

**Credentials for the admin portal**

Username: Raviteja

Password: ravi@skillsme

** You can also check the hosted application at https://zexal-hrm.herokuapp.com/ **
