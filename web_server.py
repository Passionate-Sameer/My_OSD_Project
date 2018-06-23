#This is a WEB SERVER that interacts with the client

from wsgiref.simple_server import make_server                   #Python's bundled WSGI server
from src.osd.proxyService import proxy_server
from configuration_files import conf_file

global_conf = conf_file.g_conf

appli = proxy_server.app_factory(global_conf)

httpd = make_server('', 8005, appli)
print("Serving on port 8005...")
#httpd.handle_request()                                          #Wait for a single request, serve it and quit
httpd.serve_forever()                                           #Serve the requests forever without quitting





