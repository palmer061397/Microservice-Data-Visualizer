class PostAttributes:
		object_ = "object post_"
		post_ = "post_"
		post_id = "post_id"
		post_caption = "post_caption"
		images = "images"
		comments = "comments"
		hashtags = "hashtags"
		date_published = "date_published"
		
class PostAttrEquals:
		post_caption = " : post_caption = "
		images = " : images = "
		comments = " : comments = "
		hashtags = " : hashtags = "
		date_published = " : date_published = "
		

class ProfileAttributes:
	name = 'name'
	username = 'username'
	hyperlink = 'hyperlink'
	biography = 'biography'
	is_reported = 'is_reported'
	is_shadowbanned = 'is_shadowbanned'
	number_of_followers = 'number_of_followers'
	number_of_posts = 'number_of_posts'
	number_of_following = 'number_of_following'
	
class ProfileAttrEquals:
	name = " : name = "
	biography = " : biography = "
	hyperlink = " : hyperlink = "
	is_reported = " : is_reported = "
	is_shadowbanned = " : is_shadowbanned = "
	number_of_followers = " : number_of_followers = "
	number_of_posts = " : number_of_posts = "
	number_of_following = " : number_of_following = "
	
class ModerationAttributes:
		post_ = "post_"
		post_id = "post_id"
		is_reported = "is_reported"
		is_manual = "is_manual"
		reason = "reason"

class ModerationAttrEquals:
		is_reported = " : is_reported = "
		is_manual = " : is_manual = "
		reason = " : reason = "
		
class Profile_API_Attributes:
		email = "email"
		phone = "phone"
		dob = "dob"
		age = "age"
		
class UMLCmds:
	start_uml = "@startuml \n"
	end_uml = "@enduml \n"
	down_diagram = " -down-> "
