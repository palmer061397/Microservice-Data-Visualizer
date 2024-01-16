import json
import plantuml
import requests
import logging
import traceback

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_data():
    response = requests.get(
        "https://randomuser.me/api/?format=json", timeout=5000)
    if response.status_code >= 200 & response.status_code <= 299:
    	return response.json()["results"][0]
    else:
    	logging.exception(f"the (response) variable in load_data() function: Status_code = {response.status_code}")
    	


def write_plantuml_file(res):
    l
    # Stores index of firstname and index lastname to write to file
    nodeName = res["name"]["first"] + "_" + res["name"]["last"]
    # Stores nodeName and concats index of email, phone, and age
    # The format is required for plantuml
    jsonOptions = [nodeName + " : email = " + res["email"] + "\n",
    							nodeName + " : phone = " + res["phone"] + "\n",
    							nodeName + " : age = " + str(res["dob"]["age"]) + "\n"]
    try:
    	with open("./plantuml.txt", "w", encoding="utf-8") as pf:
        	pf.write("@startuml \n")
        	pf.write("object " + nodeName + " \n")
        	for i in range(3):
        		pf.write(jsonOptions[i])
        	pf.write("@enduml \n")
    except FileNotFoundError:
    	# writes traceback details to file "app.log"
    	logging.exception(traceback.print_exc())


def create_plantuml_image():
    plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "./plantuml.txt", outfile=None, errorfile=None)


if __name__ == '__main__':
    response_json = load_data()
    if response_json is not None:
        write_plantuml_file(response_json)
        create_plantuml_image()
