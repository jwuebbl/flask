# Jeffrey Wuebbles's Flask App
## Table of Contents
* This section is for notes on running the Flask application locally:
	* [Python Virtual Environment Notes](#pythonVirtualEnvironmentNotes)
		* [How to Create a Python Virtual Environment](#creatingPythonVirtualEnvironment)
		* [How to Start a Python Virtual Environment](#startingPythonVirtualEnvironment)
		* [How to Stop a Python Virtual Environment](#stoppingPythonVirtualEnvironment)
	* [Python Dependencies Notes](#pythonPackageDependenciesNotes)
	* [How to Install Dependencies From requirements.txt](#installingFromRequirementsTxt)
	* [How to Generate the requirements.txt File](#generatingRequirementsTxt)
	* [How to Start the Flask Application Locally](#startingFlaskApp)
	* [Notes on MySQL](#notesOnMySqlOnHost)
		* [How to Start MySQL Through Window's Services GUI](#startingMySqlThroughServices)
		* [How to Start MySQL with Powershell](#startingMySqlThroughPowershell)
* This section is for running the Flask application with Docker Containers:
	* [Notes on Docker Compose](#notesOnDockerCompose)
		* [How to Start the Containers](#howToStartTheDockerContainers)
		* [How to replace the running app container with the updated version](#replaceRunningAppContainer)
		* [How to Stop the Docker Containers](#howToStopTheDockerContainers)
* How to interact with the Production Server: *Note:* Use the same docker-compose commands as used in dev.
	* [How to Connect to the Production EC2 Instance](#connectingToTheProdEc2Instance)
* Troubleshooting Actions:
	* [Issues and Their Fix Actions](#issuesAndFixActions)
	* [Cryptography package is required](#cryptoGraphyPackageIsRequired)

## Python Virtual Environment Notes <a name="pythonVirtualEnvironmentNotes"></a>
### How to create a Python Virtual Environment <a name="creatingPythonVirtualEnvironment"></a>
1. Run the following command from a powershell terminal:

		python -m venv <name_of_virtual_environment>

* Example:

		python -m venv venv


### How to Start a Python Virtual Environment <a name="startingPythonVirtualEnvironment"></a>
1. Run the following command from a powershell terminal:

        .\<name_of_virtual_environment>\Scripts\activate

* Example:

		.\venv\Scripts\activate

### How to Stop a Python Virtual Environment <a name="stoppingPythonVirtualEnvironment"></a>
1. Run the following command from a powershell terminal:

        deactivate

## Python Dependencies Notes <a name="pythonPackageDependenciesNotes"></a>
### How to Install Dependencies From requirements.txt <a name="installingFromRequirementsTxt"></a>
* **Note:** Make sure the python virtual environment is started before running this command.	

		pip install -r .\<path_to_requirements.txt>\requirements.txt

* Example:

		pip install -r .\app\requirements.txt

## How to Generate the requirements.txt File <a name="generatingRequirementsTxt"></a>
* This saves all the python dependencies you have installed in your environment.
* **Note:** Make sure the python virtual environment is started before running this command.

		pip freeze > .\<path_to_requirements.txt>\requirements.txt

* Example:

		pip freeze > .\app\requirements.txt

## How to Start the Flask Application Locally <a name="startingFlaskApp"></a>
* **Note:** Make sure the python virtual environment is started before running this command.

		flask --app .\<path_to_app>\<app_name> --debug run

* Example:

		flask --app .\app\app --debug run

## Notes on MySQL <a name="notesOnMySqlOnHost"></a>
### How to Start MySQL Through Window's Services GUI <a name="startingMySqlThroughServices"></a>
1. Click the start menu and start typing "Services".
2. Run "Services" as an administrator.
3. Find the "MySQL80" service and start it.

### How to Start MySQL with Powershell <a name="startingMySqlThroughPowershell"></a>
1. Start Powershell as an administrator and run the following command:

		Start-Service -Name "MySQL80"

## Notes on Docker Compose <a name="notesOnDockerCompose"></a>
### How to Start the Docker Containers <a name="howToStartTheDockerContainers"></a>

		docker-compose.yml up --build

### How to replace the running app container with the updated version <a name="replaceRunningAppContainer"></a>

		docker-compose up --build --no-deps app

### How to Stop the Docker Containers <a name="howToStopTheDockerContainers"></a>

		docker-compose down -v

## How to Connect to the Production EC2 Instance <a name="connectingToTheProdEc2Instance"></a>
Run the following command from the project's root directory:

		ssh -i "prod.pem" ubuntu@ec2-3-13-98-236.us-east-2.compute.amazonaws.com

## Issues and Their Fix Actions <a name="issuesAndFixActions"></a>
### Cryptography package is required <a name="cryptoGraphyPackageIsRequired"></a>
I ran into this issue several times when starting the application for the first time after restarting my machine.<br>
Fix Actions:
1. Make sure that the MySQL80 service is running.
2. Sign connect to the MySQL server with the MySQL server workbench.<br>
I'm currently not sure why this fixes the issue but so far it has a 100% success rate of alleviating the problem.