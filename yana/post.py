import os

class Post:
    def __init__(self):
        self.postName = ""
        self.done = 0

    def add(self, postName):
        self.postName = postName;
        if not os.path.exists("posts"):
            os.makedirs("posts");

        self.post = open("posts/" + self.postName + ".md", 'w+')

        self.post.close()
        self.done = 1




    def delete(self, postName):
        self.postName = postName;

        if os.path.exists("posts/" + self.postName + ".md"):
            os.remove("posts/" + self.postName + ".md");
        else:
            print("This post not exists.");

        self.done = 1

