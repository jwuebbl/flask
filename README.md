# Experimental Flask App
## Author: Jeffrey Wuebbles

## Useful Database Commands: 
### Creating the database:
	CREATE DATABASE myapp;

### Using the database (In database developer tool): 
	USE myapp;

### Creating the 'accounts' table:
	CREATE TABLE IF NOT EXISTS `accounts` (
		`id` int(11) NOT NULL AUTO_INCREMENT,
		`username` varchar(50) NOT NULL,
		`password` varchar(255) NOT NULL,
		`email` varchar(100) NOT NULL,
		PRIMARY KEY (`id`)
	);

### Inserting a record into the 'accounts' table:
#### Explicitly defining the primary key: 
	INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES (1, 'a', 'a', 'a@a.com');
#### Allowing the primary key to auto-generate:
	INSERT INTO accounts VALUES (NULL, 'aa', 'a', 'a');

## Starting MySQL Service
### Option 1, Services GUI: <br>
Click the start menu and start typing "Services". <br>
Run "Services" as an administrator. <br>
Find the "MySQL80" service and start it. <br>

### Option 2, Powershell:
Start Powershell as an administrator and run the following command. <br>

	Start-Service -Name "MySQL80"
