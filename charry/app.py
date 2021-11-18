import cherrypy
import os
import random
import string
from jinja2 import Environment, FileSystemLoader
from product import Product

conf = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'global.conf')

class Server(object):
    def __init__(self) -> None:
        self.env = Environment(loader=FileSystemLoader('./templates'))
        self.product = Product()
        
    @cherrypy.expose
    def index(self):
        template = self.env.get_template('index.html')
        return template.render(title='Happy Shopping')
    @cherrypy.expose
    def about(self):
        template = self.env.get_template('index.html')
        return template.render(title='Read About Us')
    
    @cherrypy.expose
    def create(self):
        template = self.env.get_template('create.html')
        return template.render()
    
    @cherrypy.expose
    def store(self, name, price, description, picture):
        picture = 'https://picsum.photos/id/'+picture+'/200'
        self.product.create((name, price, description, picture))
        template = self.env.get_template('create.html')
        return template.render()
    
    @cherrypy.expose
    def catalog(self):
        products = self.product.all()
        template = self.env.get_template('catalog.html')
        return template.render(products=products, title='Happy Shopping')
    
if __name__ == '__main__':
    server = Server()
    
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