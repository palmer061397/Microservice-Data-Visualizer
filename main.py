import json
import logging
import plantuml
import sys
from urllib.error import HTTPError, URLError

# Configuring logging
logging.basicConfig(filename='./Docs/Log_Files/main.log', filemode='w',
                    format='%(asctime)s - Line:%(lineno)d - %(name)s - FuncName: %(funcName)s - Level: %(levelname)s - MSG: %(message)s',
                    level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
logging.info("logging.basicConfig configured successfully.")

try:  # Insers custom module from different directory
    sys.path.append('./Docs/Custom_Modules')
    from JSONAttributeModule import *

    logging.info("Custom Module 'JSONAttributeModule' imported successfully...")
except (ImportError, IOError) as e:
    logging.exception(e)

# Directory of JSON files
JSON_DIR = "./Docs/JSON_Responses/"

# Files under JSON_Responses Directory
JSON_FILES = ["/profile_service_response.json",  # index 0
              "/posts_management_service_response.json",  # index 1
              "/moderation_service_response.json"]  # index 2

# Directory of backup json files
BACKUP_DIR = "./Docs/JSON_Responses/BACKUP_FILES/"
# Files under BACKUP_FILES Directory
BACKUP_FILES = ["/profile_service_repsonse_backup.json",  # index 0
                "/posts_management_service_response_backup.json",  # index 1
                "/moderation_service_reponse_backup.json"]  # index 2


def load_data():
    """ Opens json files, assigns loaded data from files to variables, then returns variables storing file data"""
    try:
        # Loads "JSON_Responses/profile_service_respons.json"
        with open(JSON_DIR + JSON_FILES[0], "r", encoding="utf-8") as profile_file:
            profile_json = json.load(profile_file)
            logging.info("profile_service_response.json loaded successfully...")
    except FileNotFoundError:
        logging.error(e + "File Not Found: FAILSAFE ACTIVATED -- Loading backup file for profile_response...")
        # Backup file "profile_service_response_backup.json"
        with open(BACKUP_DIR + BACKUP_FILES[0], "r", encoding="utf-8") as profile_file:
            profile_json = json.load(profile_file)
            logging.info("Backup File Loaded Succesfully")
    except IOError as e:
        logging.exception(e)

    try:
        # Loads "JSON_Responses/posts_management_service_response.json"
        with open(JSON_DIR + JSON_FILES[1], "r", encoding="utf-8") as posts_file:
            posts_json = json.load(posts_file)
            logging.info("posts_management_service_response.json loaded successfully...")
    except FileNotFoundError:
        logging.error(e + "File Not Found: FAILSAFE ACTIVATED -- Loading backup file for posts_response...")
        # Backup file "posts_management_service_response_backup.json"
        with open(BACKUP_DIR + BACKUP_FILES[1], "r", encoding="utf-8") as posts_file:
            posts_json = json.load(posts_file)
            logging.info("Backup File Loaded Successfully")
    except IOError as e:
        logging.exception(e)

    try:
        # Loads "JSON_Responses/moderation_service_response.json"
        with open(JSON_DIR + JSON_FILES[2], "r", encoding="utf-8") as moderation_file:
            moderation_json = json.load(moderation_file)
            logging.info("moderation_service_response.json loaded successfully...")
    except FileNotFoundError as e:
        logging.error(e + "File Not Found: FAILSAFE ACTIVATED -- Loading backup file for moderation_response...")
        # Backup file "moderation_service_response_backup.json"
        with open(BACKUP_DIR + BACKUP_FILES[2], "r", encoding="utf-8") as moderation_file:
            moderation_json = json.load(moderation_file)
            logging.info("Backup File Loaded Successfully")
    except IOError as e:
        logging.exception(e)
    if profile_json or posts_json or moderation_json is not None:
        logging.info("profile_json, posts_json, moderation_json : is not None: (contains data)")
        return profile_json, posts_json, moderation_json
    else:
        logging.critical("File/s contain None")


def write_plantuml_file(profile_data, posts_data, moderation_data):
    '''Opens 3 files and writes data to files'''

    with open("./Docs/PlantUML_Txt/plantuml.txt", "w", encoding="utf-8") as plant_file:

        # plantuml object nameOfNode
        plant_file.write(UMLCmds.start_uml)
        plant_file.write("object " + profile_data[ProfileAttributes.username] + "\n")
        # nameOfNode : nameOfAttribute = attributreValue
        plant_file.writelines(profile_data[ProfileAttributes.username] + ProfileAttrEquals.name + profile_data[
            ProfileAttributes.name] + "\n" +  # 1
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.biography + profile_data[ProfileAttributes.biography] + "\n" +  # 2
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.hyperlink + profile_data[
            ProfileAttributes.hyperlink] + "\n" +  # 3
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.is_reported + str(
            profile_data[ProfileAttributes.is_reported]) + "\n" +  # 4
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.is_shadowbanned + str(
            profile_data[ProfileAttributes.is_shadowbanned]) + "\n" +  # 5
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_followers + str(
            profile_data[ProfileAttributes.number_of_followers]) + "\n" +  # 6
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_posts + str(
            profile_data[ProfileAttributes.number_of_posts]) + "\n" +  # 7
            profile_data[ProfileAttributes.username] + ProfileAttrEquals.number_of_following + str(
            profile_data[ProfileAttributes.number_of_following]) + "\n")  # 8

        for post in posts_data:
            plant_file.write(PostAttributes.object_ + str(post[PostAttributes.post_id]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.post_caption + post[PostAttributes.post_caption] + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.images + str(post[PostAttributes.images]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.comments + str(post[PostAttributes.comments]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.hashtags + str(post[PostAttributes.hashtags]) + "\n")
            plant_file.write(PostAttributes.post_ + str(post[PostAttributes.post_id]) + PostAttrEquals.date_published + post[PostAttributes.date_published] + "\n") \
 \
                # nameOfNodeOne -> nameOfNodeTwo
            plant_file.write(profile_data[ProfileAttributes.username] + UMLCmds.down_diagram + "post_" + str(post[PostAttributes.post_id]) + "\n")

        for moderated_post in moderation_data:
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.is_reported + str(
                moderated_post[ModerationAttributes.is_reported]) + "\n")
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.is_manual + str(
                moderated_post[ModerationAttributes.is_manual]) + "\n")
            plant_file.write(ModerationAttributes.post_ + str(moderated_post[ModerationAttributes.post_id]) + ModerationAttrEquals.reason + moderated_post[
                ModerationAttributes.reason] + "\n")

            if "reported_by" in moderated_post:
                plant_file.write("post_" + str(moderated_post["post_id"]) + " : reported_by = " + moderated_post["reported_by"] + "\n")
        plant_file.write(UMLCmds.end_uml)


def create_plantuml_image():
    """ create_plantuml_image function reads plantuml.txt
        data and sends it to website to create and capture image"""
    try:
        plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file("./Docs/PlantUML_Txt/plantuml.txt",
                                                                                  outfile="./PlantUML_Images/PlantUML.Main.png",
                                                                                  errorfile="PlantUML_log.log")
    except (plantuml.PlantUMLConnectionError, plantuml.PlantUMLError, plantuml.PlantUMLHTTPError) as e:
        logging.exception(e)
    except FileNotFoundError as e:
        logging.exception(e)


if __name__ == '__main__':
    profile, posts, moderation = load_data()
    write_plantuml_file(profile, posts, moderation)
    create_plantuml_image()
    # Clears resources for logger
    logging.shutdown()
