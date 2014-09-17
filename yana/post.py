import os

class Post:
	
	def __init__(self):
		self.postName = ""

	def add(self,postName) :
		self.postName = postName;

		if not os.path.exists("post") :
			os.makedirs("post");

		self.post = open("post/"+self.postName+".md",'w+');

	def delete(self,postName):
		self.postName = postName;

		if os.path.exists("post/"+self.postName+".md") :
			os.remove("post/"+self.postName+".md");
			print("success");

		else :
			print("This post not exists.");
