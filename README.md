# Experimental Flask App
## Author: Jeffrey Wuebbles
## How to start the Virtual Enviroment:
	.\venv\Scripts\activate

## How to install dependencies:
	
	pip install flask
	pip install flask-mysql

## How to start the flask app:
The syntax is: flask --app <appname> --debug run

	flask --app app --debug run

## Useful Database Commands: 
### Creating the database:
	CREATE DATABASE myapp;

### Using the database (In database developer tool): 
	USE myapp;

### Creating the 'accounts' table:
	CREATE TABLE IF NOT EXISTS `accounts` (
		id int(11) NOT NULL AUTO_INCREMENT,
		username varchar(50) NOT NULL unique,
		password varchar(255) NULL,
		email varchar(100) NULL,
		chips INT NOT NULL,
		PRIMARY KEY (id)
	);

### Inserting a record into the 'accounts' table:
#### Explicitly defining the primary key (MySQL Workbench): 
	INSERT INTO `accounts` (`id`, `username`, `password`, `email`, `chips`) VALUES (1, 'a', 'a', 'a@a.com', 100);
#### Allowing the primary key to auto-generate (In the code):
	"INSERT INTO accounts (id, username, password, email, chips) VALUES (NULL, %s, NULL, NULL, %s)", (username, 100))

## Starting MySQL Service
### Option 1, Services GUI: <br>
Click the start menu and start typing "Services". <br>
Run "Services" as an administrator. <br>
Find the "MySQL80" service and start it. <br>

### Option 2, Powershell:
Start Powershell as an administrator and run the following command. <br>

	Start-Service -Name "MySQL80"

## Useful HTML
### HTML for a button that submits a request to the backend:
	<form action="/url_to_submit_to" method="post" id="this_buttons_id"><button type="submit">button_text</button></form>
