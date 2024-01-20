import json
import traceback
import logging
from urllib.error import HTTPError, URLError
import plantuml
import sys

sys.path.insert(0, '/storage/emulated/0/Documents/Pydroid3/Personal_Projects/microservice_visualizer/Docs/Custom_Modules/')
from JSONAttributeModule import *

#Configuring logging
logging.basicConfig(filename='./Docs/Log_Files/main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# Directory of JSON files
JSON_DIR = "./Docs/JSON_Responses/"

# Files under JSON_Responses Directory
json_files = ["/profile_service_response.json", #index 0
	      "/posts_management_service_response.json", #index 1
	      "/moderation_service_response.json"] #index 2
					 
# Directory of backup json files					 
BACKUP_DIR = "./Docs/JSON_Responses/Backup_Files/"
# Files under Backup_Files Directory
backup_files = ["/profile_service_repsonse_backup.json", #index 0
				"/posts_management_service_response_backup.json", #index 1
				"/moderation_service_reponse_backup.json"] #index 2
					   

def load_data():
    """ Opens json files, assigns loaded data from files to variables
        , then returns variables storing file data"""
    try:
    	# Loads "JSON_Responses/profile_service_response.json""
    	with open(JSON_DIR + json_files[0], "r" ,encoding="utf-8") as profile_file:
        	profile_json = json.load(profile_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	# Backup file "profile_service_reponse_backup.json""
    	with open(BACKUP_DIR + backup_files[0], "r", encoding="utf-8") as profile_file:
    		profile_json = json.load(profile_file)
    		logging.info("File not found: FAILSAFE_ACTIVATED -- Loading backup file under Backup_Files DIRECTORY...")
    except IOError as e:
	logging.critical(e)
    try:
    	# Loads "JSON_Responses/posts_management_service_response.json""
    	with open(JSON_DIR + json_files[1], "r", encoding="utf-8") as posts_file:
        	posts_json = json.load(posts_file)
    except FileNotFoundError as e:
    	logging.exception(traceback.print_exc())
    	# Backup file "posts_management_service_reponse_backup.json""
    	with open(BACKUP_DIR + backup_files[1], "r", encoding="utf-8") as posts_file:
    		posts_json = json.load(posts_file)
    		logging.info("File not found: FAILSAFE_ACTIVATED -- Loading backup file under Backup_Files DIRECTORY...")
    except IOError as e:
    	logging.critical(e)
    	
    	
    try:
    	# Loads "JSON_Responses/moderation_service_response.json"
    	with open(JSON_DIR + json_files[2], "r", encoding="utf-8") as moderation_file:
        	moderation_json = json.load(moderation_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	# Backup file "moderation_service_response_backup.json""
    	with open(BACKUP_DIR + backup_files[2], "r", encoding="utf-8") as moderation_file:
    		moderation_json = json.load(moderation_file)
    		logging.info("File not found: FAILSAFE_ACTIVATED -- Loading backup file under Backup_Files DIRECTORY...")
    except IOError as e:
    	logging.critical(e)
    	
    return (profile_json, posts_json, moderation_json)


def write_plantuml_file(profile_data, posts_data, moderation_data):
    with open("./Docs/PlantUML_Txt/plantuml.txt", "w", encoding="utf-8") as plant_file:
        
        # plantuml object nameOfNode
        plant_file.write(UMLCmds.start_uml)
        plant_file.write("object " + profile_data[ProfileAttributes.username] + "\n")
        # nameOfNode : nameOfAttribute = attributeValue
        plant_file.writelines(profile_data[ProfileAttributes.username] + ProfileAttrEquals.name + profile_data[ProfileAttributes.name] + "\n" + #1
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.biography + profile_data[ProfileAttributes.biography] + "\n" + #2
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.hyperlink + profile_data[ProfileAttributes.hyperlink] + "\n" + #3
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.is_reported + str(profile_data[ProfileAttributes.is_reported]) + "\n" + #4
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.is_shadowbanned + str(profile_data[ProfileAttributes.is_shadowbanned]) + "\n" + #5
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_followers + str(profile_data[ProfileAttributes.number_of_followers]) + "\n" + #6
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_posts + str(profile_data[ProfileAttributes.number_of_posts]) + "\n" + #7
        								  profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_following + str(profile_data[ProfileAttributes.number_of_following]) + "\n") #8

        for post in posts_data:
            plant_file.write(PostAttributes.object_ + str(post[PostAttributes.post_id]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.post_caption + post[PostAttributes.post_caption] + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.images + str(post[PostAttributes.images]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.comments + str(post[PostAttributes.comments]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.hashtags + str(post[PostAttributes.hashtags]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.date_published + post[PostAttributes.date_published] + "\n")
          
            # nameOfNodeOne -> nameOfNodeTwo
            plant_file.write(profile_data[ProfileAttributes.username] + UMLCmds.down_diagram + "post_" + str(post[PostAttributes.post_id]) + "\n")

        for moderated_post in moderation_data:
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.is_reported + str(moderated_post[ModerationAttributes.is_reported]) + "\n")
            		
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.is_manual + str(moderated_post[ModerationAttributes.is_manual]) + "\n")
                     
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.reason + moderated_post[ModerationAttributes.reason] + "\n")

            if "reported_by" in moderated_post:
                plant_file.write("post_" + str(moderated_post["post_id"]) + " : reported_by = " + moderated_post["reported_by"] + "\n")
        plant_file.write(UMLCmds.end_uml)


def create_plantuml_image():
    """ (create_plantuml_function) reads plantuml.txt
         data and sends it to website to create and capture image"""
    try:
    	plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file(
        "./Docs/PlantUML_Txt/plantuml.txt", outfile="./PlantUML_Images/PlantUML_Main.png", errorfile="PlantUML_log.log")
    except (plantuml.PlantUMLConnectionError, plantuml.PlantUMLError, plantuml.PlantUMLHTTPError) as e:
        logging.critical(e)
    except (FileNotFoundError) as e:
    	logging.critical(e)


if __name__ == '__main__':
    profile, posts, moderation = load_data()
    write_plantuml_file(profile, posts, moderation)
    create_plantuml_image()
    
