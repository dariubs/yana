#!/usr/bin/python3
from yana import start
from yana import post

app = start.Start();

#get user info
# site_name = input("Site Name (directory of files)*: ");
# site_title = input("Site title* : ");
# site_author = input("Your name : ");
# site_repo = input("Site repository :");

#create app
#app.create(site_name,site_title,site_author,site_repo);

new_post = post.Post();

post_name = input("post name* :")

new_post.add(post_name);

post_name = input("post name* :")

new_post.delete(post_name);
