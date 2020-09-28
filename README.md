# Python Flask App
The following web application is designed to be pushed to AWS Beanstalk to simply understand how easy is to deploy web apps with beanstalk. The program demonstrate a simple student information system that allows you to add and delete a student record. The program uses JWT token based authentication mechanism and mysql as database.

Few things to consider:

 1. SQLALCHEMY ORM: In the example I have used scoped_session which
    allows multiple session to be created and remove. The catch is if
    you do not remove the session after a task you will see bizzare
    behavior with data transaction.


2.  Make sure the primary key is set to AUTO_INCREMENT for both the tables. I have added the schema that can be used to import.

3.  Once you have configure database on Amazon RDS make sure the app has proper access. For demonstration purpose I open access to public. In production you would definitely want to check your


Resources:

[https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)

[https://dev.to/totally_chase/python-using-jwt-in-cookies-with-a-flask-app-and-restful-api-2p75](https://dev.to/totally_chase/python-using-jwt-in-cookies-with-a-flask-app-and-restful-api-2p75)

[https://hackersandslackers.com/flask-sqlalchemy-database-models/](https://hackersandslackers.com/flask-sqlalchemy-database-models/)
