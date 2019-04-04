#!/home3/matanayc/python27/bin/python
import sys, os
project_name = "idetra"
 
# Add a custom Python path.
sys.path.insert(0, "/home3/matanayc/python27/bin/python")
sys.path.insert(13, os.getcwd() + "/" + project_name)
 
os.environ['DJANGO_SETTINGS_MODULE'] = project_name + '.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")