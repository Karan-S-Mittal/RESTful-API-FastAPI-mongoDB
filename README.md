# FASTAPI-MongoDB-CRUD App
The application uses fastAPI and MongoDB as backend servers to implement a simple REST API.

> I have used asynchronous functions in most places. 

> FastAPI provides amazing support for asynchronous programming.

> For Database Asynchronous operations, I have used <b>Motor</b> python package for MongoDB.

The API provides a simple API for a student database. The API is capable of performing

1. Retrieve all students (GET)
2. Retrieve single student using student-id (GET)
3. Add a student (POST) 
4. Update a student info (PUT)
5. Delete a student from Database

# Install

MongoDB local server is required to run the project. You can download the same from here.
[MongoDB Community Server](https://docs.mongodb.com/manual/administration/install-community/).

Clone the repositiory and move to the repo-folder.

Install the required version appropriate for your os and get follow the instructions provided in the docs.

> Note - Use Virtual Environment for Python installs.

```
pip install -r requirements.txt
```

# Run
To run the application follow these instruction. if you are inside the root folder, then move into the `app` folder.
then execute the following command.
```
python main.py
```

This will start the server in `localhost:8000`

To access the api endpoints, we have used the FastAPI built-in interface. 
go to this url for that purpose.
`localhost:8000/docs`

test the API endpoints as much as you like!

# Screenshots

1. API Endpoints Page
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-context.png)

2. Get all students in database
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-getstudents.png)

3. Get one student in database with ID
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-get-id.png)

4. Add a student
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-post.png)

5. Update a student's information
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-update.png)

6. delete a student object
![](https://github.com/Karan-S-Mittal/RESTful-API-FastAPI-mongoDB/raw/master/screenshots/fastapi-delete.png)

# Author
Karan Mittal

Thanks for checking the repo out. Please share your thoughts or if you had any problems running the code. 