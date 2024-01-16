import json
import traceback
import logging
import plantuml

# Configuring logging
logging.basicConfig(filename='main.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)


#DIR of json files
JSON_DIR = "./JSON_Responses"

#json filenames
json_files = ["/profile_service_response.json", #index 0
			  "/posts_management_service_response.json", #index 1
			  "/moderation_service_response.json"] #index 2
					 
# List of attribute names equals (x)					 
username_data = [" : biography = ", #index 0
        		 " : hyperlink = ", #index 1
        		 " : is_reported = ", #index 2
        		 " : is_shadowbanned = ", #index 3
        		 " : number_of_followers = ", #index 4
        		 " : number_of_posts = ", #index 5
        		 " : number_of_following = ", #index 6:
        		 " : name = "] #index 7

# List of attribute names      						 
info_list = ["username", #index 0
        	 "biography", #index 1
        	 "hyperlink", #index 2
        	 "is_reported", #index 3
        	 "is_shadowbanned", #index 4
        	 "number_of_followers", #index 5
        	 "number_of_posts", #index 6
        	 "number_of_following", #index 7
        	 "name"] #index 8

def load_data():
    """ Opens json files, assigns loaded data from file to variable
        , then returns all variables storing file data"""
    try:
    	with open(JSON_DIR + json_files[0], encoding="utf-8") as profile_file:
        	profile_json = json.load(profile_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	
    try:
    	with open(JSON_DIR + json_files[1], encoding="utf-8") as posts_file:
        	posts_json = json.load(posts_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    	
    try:
    	with open(JSON_DIR + json_files[2], encoding="utf-8") as moderation_file:
        	moderation_json = json.load(moderation_file)
    except FileNotFoundError:
    	logging.exception(traceback.print_exc())
    return (profile_json, posts_json, moderation_json)

def write_plantuml_file(profile_data, posts_data, moderation_data):
    with open("./plantuml.txt", "w", encoding="utf-8") as plant_file:
      
        # plantuml object nameOfNode
        plant_file.write("@startuml \n")
        plant_file.write("object " + profile_data[info_list[0]] + "\n")
        
         # nameOfNode : nameOfAttribute = attributeValue
        plant_file.writelines(profile_data[info_list[0]] + username_data[7] + profile_data[info_list[8]] + "\n" +
        					  profile_data[info_list[0]] + username_data[0] + profile_data[info_list[1]] + "\n" +
        					  profile_data[info_list[0]] + username_data[1] + profile_data[info_list[2]] + "\n" +
        					  profile_data[info_list[0]] + username_data[2] + str(profile_data[info_list[3]]) + "\n" +
        					  profile_data[info_list[0]] + username_data[3] + str(profile_data[info_list[4]]) + "\n" +
        					  profile_data[info_list[0]] + username_data[4] + str(profile_data[info_list[5]]) + "\n" +
        					  profile_data[info_list[0]] + username_data[5] + str(profile_data[info_list[6]]) + "\n" +
        					  profile_data[info_list[0]] + username_data[6] + str(profile_data[info_list[7]]) + "\n"
        					  )

        for post in posts_data:
            try:
            	plant_file.write("object post_" + str(post["post_id"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + " : post_caption = " + post["post_caption"] + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + " : images = " + str(post["images"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + " : comments = " + str(post["comments"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + " : hashtags = " + str(post["hashtags"]) + "\n")
            	plant_file.write("post_" + str(post["post_id"]) + " : date_published = " + post["date_published"] + "\n")
            except Exception as e:
            	logging.critical(e)
          
            # nameOfNodeOne -> nameOfNodeTwo : plantuml formatted
            plant_file.write(profile_data["username"] + " -down-> " +
                     "post_" + str(post["post_id"]) + "\n")

        for moderated_post in moderation_data:
            plant_file.write("post_" + str(moderated_post["post_id"]) +
                     " : is_reported = " + str(moderated_post["is_reported"]) + "\n")
            plant_file.write("post_" + str(moderated_post["post_id"]) +
                     " : is_manual = " + str(moderated_post["is_manual"]) + "\n")
            plant_file.write("post_" + str(moderated_post["post_id"]) +
                     " : reason = " + moderated_post["reason"] + "\n")

            if "reported_by" in moderated_post:
                plant_file.write("post_" + str(moderated_post["post_id"]) + " : reported_by = " + moderated_post["reported_by"] + "\n")
        plant_file.write("@enduml \n")


def create_plantuml_image():
    """ (create_plantuml_function) reads plantuml.txt
         data and sends it to website to create and capture image"""
    try:
    	plantuml.PlantUML("http://www.plantuml.com/plantuml/img/").processes_file("./plantuml.txt", outfile=None, errorfile=None)
    except Exception as e:
    	logging.critical(e)

if __name__ == '__main__':
    try:
    	profile, posts, moderation = load_data()
    	write_plantuml_file(profile, posts, moderation)
    	create_plantuml_image()
    except Exception as e:
    	logging.exception(e)
    
