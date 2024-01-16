#pylint:disable=C0209
#pylint:disable=C0103
#pylint:disable=C0301
#pylint:disable=W0718
import traceback
import logging
import plantuml
import requests

#configuring logging module for logs
logging.basicConfig(filename='random_user_data_api_log_file.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# API address
api_address= "https://randomuser.me/api/?format=json"

def load_data():
    """ Requests api which returns json format and returns index [results][0]"""
    try:
    	response = requests.get(api_address, timeout=5000)
    	logging.info("Line 19: request.get('https://randomuser.me/api/?format=json') successful. ")
    except Exception as e:
    		#logs exception to 'random_user_data_api_log_file.log'
    		return logging.critical(e)
    		
    		
    returned_status_code = response.ok
    if returned_status_code is True:
    	logging.info("Successful: web returned status code {0}".format(response.status_code))
    	return response.json()["results"][0]
    #logs exception to 'random_user_data_api_log_file.log'
    return logging.exception("'response' in load_data() function: Expected status_code >=200 & <= 299 but Returned Status_code = {0}".format(response.status_code))
    	


def write_plantuml_file(res):
    """opens plantuml.txt and writes data to file"""
    
    node_data_choices = [" : email = ", #index 0
    										" : phone = ", #index 1
    										" : age = "] #index 2
    										
    # Stores index of firstname and index lastname to write to file
    node_name = res["name"]["first"] + "_" + res["name"]["last"]
    
    # Stores nodeName and concats index of email, phone, and age
    # The format is required for plantuml
    json_options = [node_name + node_data_choices[0] + res["email"] + "\n",
    						 node_name + node_data_choices[1] + res["phone"] + "\n",
    						 node_name + node_data_choices[2] + str(res["dob"]["age"]) + "\n"]
    try:
    	with open("./plantuml.txt", "w", encoding="utf-8") as plant_txt:
        	plant_txt.write("@startuml \n")
        	plant_txt.write("object " + node_name + " \n")
        	for i in range(3):
        		plant_txt.write(json_options[i])
        	plant_txt.write("@enduml \n")
        	logging.info("Successful: plantuml.txt opened and data to file written.")
    except FileNotFoundError:
    	#logs exception to 'random_user_data_api_log_file.log'
    	return logging.exception(traceback.print_exc())


def create_plantuml_image():
    """ reads plantuml.txt data and sends it to website to generate and capture image"""
    try:
    	plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "./plantuml.txt", outfile=None, errorfile=None)
    except FileNotFoundError as e:
    	#logs exception to 'random_user_data_api_log_file.log'
    	logging.critical(e)


if __name__ == '__main__':
    # assigns 'load_data()'' function to variable 'response_json''
    response_json = load_data()
    if response_json is not None:
        write_plantuml_file(response_json)
        create_plantuml_image()
        logging.info("Successful: 'random_user_data_api.py' executed")
    else:
        #logs exception to 'random_user_data_api_log_file.log'
        logging.critical("(response_json) variable contains no data")
        
