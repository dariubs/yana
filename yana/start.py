import os
 
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

            os.makedirs(self.siteName);
            config = open(self.siteName+'/yana.json','w+');
            config.write('{"title" : "'+self.siteTitle+'",\n'+'"author" : "'+self.siteAuthor+'",\n'+'"repository" : "'+self.siteRepo+'"'+'}\n');
            print("your site created successfully :)");

        else :

            print("This directory currently exits.Chose another name or delete directory");


