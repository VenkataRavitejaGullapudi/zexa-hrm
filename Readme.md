# Zexa Human Resource Management System
Zexal Human Resource Management application is a system to help the managers to see all the employees and change their positions more easily. Currently this system is only for the administrator to access to view each employee (including managers) with their name, age, gender, employee ID, current position (title), salary and related department. The administrator can add, edit and remove any employee on the list. An employee can also be set as ‘Retired’ or ‘Fired’ without being deleted. 

In the admin page, There will be Users and Groups in the authentication. On clicking on the users you can see all the users of the system. Currently only one admin user. On clicking on Groups you can add a group of users and set different permissions to the different users. i.e., Along with admins we can add other users with some functionalities.

Coming to the main app section,  On Clicking on employees, you can see all the details of the employees and you can query or search based on max fields and other can be seen in the filter i.e., you can filter based on the different column values. On clicking the record you can update/ delete the record.  We can also delete multiple employees or mark status of the multiple employees at a time by selecting them and choosing an action at the top of the table  and click on go. Add pagination with 10 employees per page is currently set. We can filter according the columns by clicking on the filters that are available on the right side.
On clicking on the Departments, you can see the available departments in the company and total employees in the company. The total employees will be initially zero. After inserting or adding an employee to the particular department in the employee table, the total employee count will be automatically in increased and also deleted if you remove an employee. 
On clicking on the Roles, You can see the available roles in the company.
Department and Roles are linked to employees table.
On clicking on the Department_managers you can see the manager of the each department.
On clicking on the Payroll you can see the payroll details and internally who had added the payroll is also loaded based on the current admin user.
All the operations like editing, deleting, updating records can be done on clicking on the record in any table.
You can go to the admin page as follows.
When you run the project you will initially goes to home page of the  system. As project is not about the other users.. Go to the admin page by clicking on the "Enter admin page button " on the header. Then it asks for the login credentials to enter into the project. Enter the username as "Raviteja" and password as "ravi@skillsme". (You can add as many admins you want currently only one admin).
Next you will be navigated to the Admin Home Page

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
8. Clone the repository *HRMZexa Folder* (if you know git commands and git currently installed) 
or else simply download the git repository and extract it to *HRMZexa Folder* that you have created and also added venv

------------If cloning the repositry `git clone https://github.com/ravi777-developer/zexa-hrm.git` -------------------
9. Navigate into that folder(project folder) if not navigated

    `cd zexa-hrm` or `cd zexa-hrm-master`
    
10. Install requirements for the project(already included for deployment)

    `pip install -r requirements.txt`
    
    `pip install django` //incase version mismatch run django cmd seperately
    
11. Run the server
    `python manage.py runserver` or `python manage.py runserver "localhost" `

// *Only for testing purpose*

// *If you want you can create superuser directly from command prompt using `python manage.py createsuperuser`*

**Credentials for the admin portal**

Username: Raviteja

Password: ravi@skillsme

** You can also check the hosted application at https://zexal-hrm.herokuapp.com/ **
