import traceback
import logging
from urllib.error import HTTPError, URLError
import plantuml
import requests
import sys

# Configuring logging module for logs
logging.basicConfig(filename='./Docs/Log_Files/random_user_data_api_log_file.log',
                    filemode='w',
                    format='%(asctime)s - Line:%(lineno)d - %(name)s - FuncName: %(funcName)s - Level: %(levelname)s - MSG: %(message)s',
                    level=logging.INFO)

try: # Insers custom module from different directory
    sys.path.append('./Docs/Custom_Modules')
    from JSONAttributeModule import *
    logging.info("Custom Module 'JSONAttributeModule' imported successfully.")
except (ImportError, IOError) as e:
    logging.exception(e)



# API Address
api_address = "https://randomuser.me/api/?format=json"

def load_data():
    """ Requests api which returns json format and returns value of index"""
    try:
        response = requests.get(api_address, timeout=5000)
    except (HTTPError, URLError) as e:
        # logs exception to specified log file from above
        logging.exception(e)

    
    if response.ok:
        logging.info("Successful: web returned status code {0}".format(response.status_code))
        return response.json()["results"][0]
    else:
        logging.error("'reponse' call returned status code: status code = {0}".format(response.status_code))


def write_plantuml_file(res):
    """opens/creates plantuml.txt and writes data to file"""

    node_data_choices = {"email" : " : email = ", #index 0
    					 "phone" : " : phone = ", #index 1
    					 "age" : " : age = "} #index 2
    
    # Stores index of firstname and index lastname to write to file
    node_name = res["name"]["first"] + "_" + res["name"]["last"]

    # Stores nodeName and concats index of email, phone, and age
    # The format is required for plantuml
    json_options = [node_name + node_data_choices["email"] + res[Profile_API_Attributes.email] + "\n",
    				node_name + node_data_choices["phone"] + res[Profile_API_Attributes.phone] + "\n",
    				node_name + node_data_choices["age"] + str(res[Profile_API_Attributes.dob][Profile_API_Attributes.age]) + "\n"]
    
    try:
        with open("./Docs/PlantUML_Txt/plantuml.txt", "w", encoding="utf-8") as plant_txt:
            plant_txt.write(UMLCmds.start_uml)
            plant_txt.write("object " + node_name + " \n")
            for i in range(3):
                plant_txt.write(json_options[i])
            plant_txt.write(UMLCmds.end_uml)
            logging.info("Successful: plantuml.txt opened and data to file written. ")

    except FileNotFoundError as e:
        logging.error(e)
        logging.info(traceback.print_exc())

def create_plantuml_image():
    """ reads plantuml.txt data and sends to webiste to generate palntuml diagram in png format"""
    try:
        plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file("./Docs/PlantUML_Txt/plantuml.txt", outfile="./PlantUML_Images/API_Profile_Diagram.png", errorfile=None)
        logging.info("Connection to plantuml.com/plantuml/img/ : successful")
        logging.info("Processing file plantuml.txt successful.")
    except (FileNotFoundError, plantuml.PlantUMLConnectionError, plantuml.PlantUMLError, plantuml.PlantUMLHTTPError) as e:
        logging.exception(e)

if __name__ == '__main__':
    # assigns 'load_data()'' function to variable 'response_json''
    response_json = load_data()
    # checks that response_json variable contains data, if None raise exception and log to log file
    if response_json is not None:
        write_plantuml_file(response_json)
        create_plantuml_image()
        logging.info("Successful: 'random_user_data_api.py' executed")
    else:
        #logs exception to 'random_user_data_api_log_file.log'
        logging.critical("(response_json) variable contains no data")
        
