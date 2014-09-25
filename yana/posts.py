import os

class Post:
    def __init__(self):
        self.post_name = ""
        self.done = 0

    def add(self, post_name):
        self.post_name = post_name

        if not os.path.exists("posts"):
            os.makedirs("posts")

        self.post = open("posts/{}.md".format(self.post_name), 'w+')

        self.post.close()
        self.done = 1




    def delete(self, post_name):
        self.post_name = post_name;

        if os.path.exists("posts/" + self.post_name + ".md"):
            os.remove("posts/" + self.post_name + ".md");
        else:
            print("This post not exists.");

        self.done = 1

