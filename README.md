# Experimental Flask App
## Author: Jeffrey Wuebbles

## How to start the Virtual Enviroment:
	.\venv\Scripts\activate

## How to generate requirements.txt
Note: Make sure the virtual environment is started before generating requirements.txt

    pip freeze > requirements.txt

## How to install dependencies from requirements.txt:
	
	pip install -r /app/requirements.txt

## How to start the flask app locally:
The syntax is: flask --app <appname> --debug run

	flask --app app --debug run

## Starting MySQL Service on the Local Machine.
### Option 1, Services GUI: <br>
Click the start menu and start typing "Services". <br>
Run "Services" as an administrator. <br>
Find the "MySQL80" service and start it. <br>

### Option 2, Powershell:
Start Powershell as an administrator and run the following command. <br>
```
	Start-Service -Name "MySQL80"
```
## Useful HTML
### HTML for a button that submits a request to the backend:
	<form action="/url_to_submit_to" method="post" id="this_buttons_id"><button type="submit">button_text</button></form>

## Issues and their fixes.
### Cryptography package is required:
	I ran into this issue several times when starting the application for the first time after restarting my machine. 
	How to fix:
	1. Make sure that the mySql service is running.
	2. Sign connect to the mySql server with the MySQL server workbench. 
	I'm currently not sure why this fixes the issue but so far it has a 100% success rate of alleviating the problem.

## Docker Compose
### Starting the containers:
```
	docker-compose.yml up --build
```
### Stopping the containers:
```
	docker-compose down -v
```
test
