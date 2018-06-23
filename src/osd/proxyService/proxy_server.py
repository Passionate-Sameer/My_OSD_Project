
class Application(object):

    def __init__(self, conf, logger=None, account_ring=None,
                 container_ring=None, object_ring=None):
        self.osd_dir = conf.get('osd_dir', '/export/.osd_meta_config')
        print(self.osd_dir)

    def __call__(self, env, start_response):
        str_env = "Below is the content of 'environ' dictionary received from WISGI Web Server.\n\n"
        for key, value in env.items():
            if type(key) == str and type(value) == str:
                str_env = str_env + str(key) + ": " + str(value) + "\n"
        bin_env = str_env.encode('utf-8')
        response_body = bin_env
        status_code = '200 SAMEER'                                  #Response Status Code & Message
        headers = [('Content-type', 'text/plain')]                  
        response_headers = [                                        #Response Headers, wrapped as a list of tupled pairs 
            ('Content-Type', 'text/plain'),                         #[(Header name, Header value)]
            ('Content-Length', str(len(response_body)))
        ]
        start_response(status_code, headers)
        return [response_body]


def app_factory(global_conf, **local_conf):                 #local_conf is a dictionary
    conf = global_conf.copy()                               #Copy global_conf dictionary to conf dictionary
    conf.update(local_conf)                                 #Add local_conf dictionary items in conf dictionary
    app = Application(conf)                                 #Create object of Application class passing conf dictionary
    return app





















































