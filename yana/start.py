import os
import json
 
class Start:
    def __init__(self):
        self.siteName = "";
        self.siteTitle = "";
        self.siteAuthor = "";
        self.siteRepo = "";
     
    def create(self,siteName,siteTitle,siteAuthor,siteRepo) :
        self.siteName = siteName;
        self.siteTitle = siteTitle;
        self.siteAuthor = siteAuthor;
        self.siteRepo = siteRepo;
 
        if not os.path.exists(self.siteName) :

            data = json.dumps({"title" : self.siteTitle , "author" : self.siteAuthor, "repository" : self.siteRepo});
            os.makedirs(self.siteName);
            config = open(self.siteName+'/yana.json','w+');
            config.write(data);
            print("your site created successfully :)");

        else :

            print("This directory currently exits.Chose another name or delete directory");




