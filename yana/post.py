import os

class Post:
    def __init__(self):
        self.postName = ""
        self.done = 0

    def add(self, postName):
        self.postName = postName;
        if not os.path.exists("post"):
            os.makedirs("post");

        self.post = open("post/" + self.postName + ".md", 'w+')

        self.post.close()
        self.done = 1




    def delete(self, postName):
        self.postName = postName;

        if os.path.exists("post/" + self.postName + ".md"):
            os.remove("post/" + self.postName + ".md");
        else:
            print("This post not exists.");

        self.done = 1

