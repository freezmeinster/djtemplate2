import os
from django.conf import settings
from django.core.management import call_command

APP_TEMPLATES = next(os.walk(os.path.join(settings.BASE_DIR, "data/app_templates")))[1]

def check_target(name):
    target_path = os.path.join(settings.BASE_DIR, "apps/%s" % name)
    if not os.path.isdir(target_path):
        return True
    else:
        return False

def check_name_conflick(name):
    apps_list = next(os.walk(os.path.join(settings.BASE_DIR, "apps")))[1]
    apps_list = apps_list +['admin', 'admindocs', 'auth' ,'contenttypes' ,'flatpages','gis','humanize',
                        'messages','postgres','redirects','sessions','sitemaps','sites','staticfiles'
                        'syndication']
    if name in apps_list:
        return True
    else:
        return False

def run():
    print("========== Hello to app creator ========== \n")
    name = input("Apps name: ")
    if check_name_conflick(name) or not check_target(name):
        print("Sorry, but you can't use %s as name because this name already taken" % name)
        exit()

    apps_type = input("Select apps template %s:" % APP_TEMPLATES)
    if apps_type not in APP_TEMPLATES:
        print("Please be serious, select one on the list !!!")
        exit()

    app_path = os.path.join(settings.BASE_DIR, "apps/%s" % name)
    template_path = os.path.join(settings.BASE_DIR, "data/app_templates/%s" % apps_type)
    os.mkdir(app_path)
    call_command("startapp", name, app_path, template=template_path)
    print("Congratulation apps %s successfuly created" % name)
    

