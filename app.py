
import plantuml
import requests
import logging
import traceback

#configuring logging module for logs
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_data():
    """Requests api which returns json format and returns results[0]"""
    response = requests.get(
        "https://randomuser.me/api/?format=json", timeout=5000)
    returned_status_code = response.status_code
    if returned_status_code >= 200 & returned_status_code <= 299:
    	return response.json()["results"][0]
    return logging.exception("'response' in load_data() function: Expected status_code >=200 & <= 299 but Returned Status_code = {0}".format(response.status_code))
    	


def write_plantuml_file(res):
    """opens plantuml.txt and writes data to file"""
    
    # Stores index of firstname and index lastname to write to file
    # The format is required for plantuml
    node_name = res["name"]["first"] + "_" + res["name"]["last"]
    # Stores nodeName and concats index of email, phone, and age
    # The format is required for plantuml
    json_options = [node_name + " : email =" + res["email"] + "\n",
    						 node_name + " : phone = " + res["phone"] + "\n",
    						 node_name + " : age = " + str(res["dob"]["age"]) + "\n"]
    try:
    	with open("./plantuml.txt", "w", encoding="utf-8") as plant_file:
        	plant_file.write("@startuml \n")
        	plant_file.write("object " + node_name + " \n")
        	for i in range(3):
        		plant_file.write(json_options[i])
        	plant_file.write("@enduml \n")
    except FileNotFoundError:
    	# writes traceback details to file "app.log"
    	logging.exception(traceback.print_exc())


def create_plantuml_image():
    """ (create_plantuml_function) reads plantuml.txt
         data and sends it to website to create and capture image"""
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "./plantuml.txt", outfile=None, errorfile=None)


if __name__ == '__main__':
    response_json = load_data()
    if response_json is not None:
        write_plantuml_file(response_json)
        create_plantuml_image()
        
