import json
import traceback
import logging
import plantuml

# Configuring logging
logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


#Directory of json response files
JSON_DIR = "./JSON_Responses/"

#json filenames under ./JSON_Responses/ directory
json_files = ["profile_service_response.json", #index 0
					 "posts_management_service_response.json", #index 1
					 "moderation_service_response.json"] #index 2

# concats JSON_DIR & json_files[i] to create string with filepath to needed file
profile_service_dir = (JSON_DIR + json_files[0])
posts_management_dir = (JSON_DIR + json_files[1])
moderation_service_dir = (JSON_DIR + json_files[2])
					 
# List of profile data attribute names equals (x)					 
attribute_name = [" : biography = ", #index 0
        						 " : hyperlink = ", #index 1
        						 " : is_reported = ", #index 2
        						 " : is_shadowbanned = ", #index 3
        						 " : number_of_followers = ", #index 4
        						 " : number_of_posts = ", #index 5
        						 " : number_of_following = ", #index 6:
        						 " : name = ", #index 7
        						 " : is_manual = ", #index 8
        						 " : reason = "] #index 9

# List of profile data attribute names      						 
profile_attribute = ["username", #index 0
        				 "biography", #index 1
        				 "hyperlink", #index 2
        				 "is_reported", #index 3
        				 "is_shadowbanned", #index 4
        				 "number_of_followers", #index 5
        				 "number_of_posts", #index 6
        				 "number_of_following", #index 7
        				 "name", #index 8
        				 "reported_by"] #index 9
        				 
# List of post attributes equals (x)				 
post_attribute = [" : post_caption = ", #index 0
							 " : images = ", #index 1
							 " : comments = ", #index 2
							 " : hashtags = ", #index 3
							 " : date_published = "] #index 4

def load_data():
    """ Opens json files, assigns loaded data from file to variable
        , then returns all variables storing file data"""
    try:
    	with open(profile_service_dir, encoding="utf-8") as profile_file:
        	profile_json = json.load(profile_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	
    try:
    	with open(posts_management_dir, encoding="utf-8") as posts_file:
        	posts_json = json.load(posts_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	
    try:
    	with open(moderation_service_dir, encoding="utf-8") as moderation_file:
        	moderation_json = json.load(moderation_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    return (profile_json, posts_json, moderation_json)

def write_plantuml_file(profile_data, posts_data, moderation_data):
    with open("./PlantUML/plantuml.txt", "w", encoding="utf-8") as plant_file:
      
        # plantuml object nameOfNode
        plant_file.write("@startuml \n")
        plant_file.write("object " + profile_data[profile_attribute[0]] + "\n")
        
         # nameOfNode : nameOfAttribute = attributeValue
        plant_file.writelines(profile_data[profile_attribute[0]] + attribute_name[7] + profile_data[profile_attribute[8]] + "\n")

        for i in range(2):
        	try:
        		plant_file.writelines(profile_data[profile_attribute[0]] + attribute_name[i] + profile_data[profile_attribute[i+1]] + "\n")
        	except Exception as error1:
        		logging.error(error1)
        		
        for i in range(2, 7):
        	try:
        		plant_file.writelines(profile_data[profile_attribute[0]] + attribute_name[i] + str(profile_data[profile_attribute[i+1]]) + "\n")
        	except Exception as error2:
        		logging.error(error2)
		  
        for post in posts_data:
            try:
            	plant_file.write("object post_" + str(post["post_id"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + post_attribute[0] + post["post_caption"] + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + post_attribute[1] + str(post["images"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + post_attribute[2] + str(post["comments"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + post_attribute[3] + str(post["hashtags"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + post_attribute[4] + post["date_published"] + "\n")
            except Exception as error3:
            	logging.critical(error3)
          
            # nameOfNodeOne -> nameOfNodeTwo : plantuml formatted
            plant_file.write(profile_data[profile_attribute[0]] + " -down-> " +
                     "post_" + str(post["post_id"]) + "\n")

        for moderated_post in moderation_data:
            try:
            	plant_file.write("post_" + str(moderated_post["post_id"]) + attribute_name[2] + str(moderated_post["is_reported"]) + "\n")
            	plant_file.write("post_" + str(moderated_post["post_id"]) + attribute_name[8] + str(moderated_post["is_manual"]) + "\n")
            	plant_file.write("post_" + str(moderated_post["post_id"]) + attribute_name[9] + moderated_post["reason"] + "\n")
            except Exception as error4:
            	logging.error(error4)

            if attribute_name[9] in moderated_post:
                plant_file.write("post_" + str(moderated_post["post_id"]) + " : reported_by = " + moderated_post["reported_by"] + "\n")
        plant_file.write("@enduml \n")


def create_plantuml_image():
    """ (create_plantuml_function) reads plantuml.txt
         data and sends it to website to create and capture image"""
    try:
    	plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file("./PlantUML/plantuml.txt", outfile=None, errorfile=None)
    except Exception as error5:
    	logging.critical(error5)

if __name__ == '__main__':
    try:
    	profile, posts, moderation = load_data()
    	write_plantuml_file(profile, posts, moderation)
    	create_plantuml_image()
    except Exception as error6:
    	logging.exception(error6)
    
