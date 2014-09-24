import sys
from yana import start


def main():
    commands = (
        'create',
        'post',
        'ls',
        'export',
        'help'
    )

    if commands[0] in sys.argv :
        create()
    elif commands[1] in sys.argv:
        post()
    elif commands[2] in sys.argv:
        ls
    elif commands[3] in sys.argv:
        export()
    elif commands[4] in sys.argv:
        commands_help()
    else :
        not_found()


def create():
    print("Site name*:",end=' ')
    site_name = input()
    if len(site_name)<1 :
        print('try again.you most enter a name for your website folder.')
        return 0
    print("Site Title:",end=' ')
    site_title = input()
    print("Author :",end=' ')
    author = input()
    print("repo address :",end=' ')
    repo = input()

    start_var = start.Start()
    start_var.create(site_name,site_title,author,repo)

def post():
    pass
    #check if yana.json exists
        #create post

def ls():
    pass

def export():
    pass

def not_found():
    print("command not found.\nTry 'yana help'")

def commands_help():
    print("Hello!\nyana is a static site generator.")

if __name__ == '__main__':
    main()