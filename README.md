## Microservice Data Visualizer

This Python application is designed to help visualize microservice data across a posts management microservice, moderation microservice, and profile microservice using PlantUML. Currently, it reads its microservice data from hard-coded JSON files, but eventaully it will include the option to use live data from these microservices.

## Installation

Clone the repository from GitHub
Install the required packages using pip: pip install -r requirements.txt
Run the application: python main.py

## Usage

Since this application reads hard-coded JSON files, you can hard-code these with data from old logs. For example, you can look in a given microservice's logs and find the JSON log with the appropriate information for each microservice. Then, you can paste them into the appropriate JSON files in this application and generate a more visual plantuml diagram:
- __File Paths__: When using these custom modules, ensure you change the file path/Directory to properly import these modules.
- UPDATE - random_user_data_api_app.py file uses an api to generate random user data.
- UPDATE - New Custom modules have been added and are in the development phase, so they are partially incomplete and only have limited functionality at this moment.
- UPDATE - TestingModules.py - is a file to test the new Custom Modules generating png files of plantuml diagrams.

## Contributing

If you would like to contribute to this project, please follow these steps:
- Fork the repository
- Create a new branch for you changes
- Make your changes and commit them to your branch
- Submit a pull request to the original repository

