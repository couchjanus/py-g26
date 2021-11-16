import cherrypy
import os
import random
import string

conf = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'global.conf')

class Server(object):
    @cherrypy.expose
    def index(self):
        if 'counter' not in cherrypy.session:
            cherrypy.session['counter'] = 0
            cherrypy.session['counter'] += 1
             
        return """
        <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>

    <link href="/static/css/app.css" rel="stylesheet">
</head>
<body>
        <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/profile">Profile</a></li>
        </ul>
        <h1>Hello Cerry Python</h1>
        <h2>Counter = """ + str(cherrypy.session['counter'])+""" </h2>
        </body>
        """
       
    
    
    @cherrypy.expose
    def contact(self):
        return """
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/profile">Profile</a></li>
    </ul>
    <h1>Contact page</h1>
    
    <p>Contact us please</p>
    """
    @cherrypy.expose
    def profile(self, count=16):
        gen = ''.join(random.sample(string.hexdigits, int(count)))
        html = """
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/contact">Contact</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/profile">Profile</a></li>
            </ul>
            <h1>Dashboard</h1>
            <form method="get" action="generate">
                <label>Enter number: <input type="text" value="16" name="count"></label>
                <button type="submit">Let's Generate</button>
            </form>  
        """
        res = "<strong>"+gen+"</strong>"
        
        return html+res
    @cherrypy.expose
    def generate(self, count=8):
        count = int(count) if int(count) <= len(string.hexdigits) else len(string.hexdigits)
        return ''.join(random.sample(string.hexdigits, count))
    @cherrypy.expose
    def about(self):
        return """
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/contact">Contact</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/profile">Profile</a></li>
    </ul>
    <h1>About page</h1>
    
    <p>Nla nla bla</p>
    """
if __name__ == '__main__':
    server = Server()
    # conf = {
    #     'server.socket_port': 3000,
    #     'engine.autoreload.on': True,
    #     'log.screen': True,
    #     'checker.on': True, 
    #     'restart_enable': True
    # }
    # cherrypy.config.update({'global': conf})
    # cherrypy.tree.mount(server, '/', config={'global': conf})
    
    cherrypy.config.update(conf)
    cherrypy.tree.mount(server, '/', conf)
    
    config = {
        '/':{
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static':{
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(server, '/', config)