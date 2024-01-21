class PostAttributes:
	def __init__(self) -> None:
		self.object_ = "object post_"
		self.post_ = "post_"
		self.post_id = "post_id"
		self.post_caption = "post_caption"
		self.images = "images"
		self.comments = "comments"
		self.hashtags = "hashtags"
		self.date_published = "date_published"
		
class PostAttrEquals:
	def __init__(self) -> None:
		self.post_caption = " : post_caption = "
		self.images = " : images = "
		self.comments = " : comments = "
		self.hashtags = " : hashtags = "
		self.date_published = " : date_published = "
		

class ProfileAttributes:
	def __init__(self) -> None:
		self.name = 'name'
		self.username = 'username'
		self.hyperlink = 'hyperlink'
		self.biography = 'biography'
		self.is_reported = 'is_reported'
		self.is_shadowbanned = 'is_shadowbanned'
		self.number_of_followers = 'number_of_followers'
		self.number_of_posts = 'number_of_posts'
		self.number_of_following = 'number_of_following'
	
class ProfileAttrEquals:
	def __init__(self) -> None:
		self.name = " : name = "
		self.biography = " : biography = "
		self.hyperlink = " : hyperlink = "
		self.is_reported = " : is_reported = "
		self.is_shadowbanned = " : is_shadowbanned = "
		self.number_of_followers = " : number_of_followers = "
		self.number_of_posts = " : number_of_posts = "
		self.number_of_following = " : number_of_following = "
	
class ModerationAttributes:
	def __init__(self) -> None:
		self.post_ = "post_"
		self.post_id = "post_id"
		self.is_reported = "is_reported"
		self.is_manual = "is_manual"
		self.reason = "reason"

class ModerationAttrEquals:
	def __init__(self) -> None:
		self.is_reported = " : is_reported = "
		self.is_manual = " : is_manual = "
		self.reason = " : reason = "
		
class Profile_API_Attributes:
	def __init__(self) -> None:
		self.email = "email"
		self.phone = "phone"
		self.dob = "dob"
		self.age = "age"
		
class UMLCmds:
	def __init__(self) -> None:
		self.start_uml = "@startuml \n"
		self.end_uml = "@enduml \n"
		self.down_diagram = " -down-> "
