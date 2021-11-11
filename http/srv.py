from http.server import HTTPServer, BaseHTTPRequestHandler
from os import curdir, sep

PORT = 3000

class HttpHandler(BaseHTTPRequestHandler):
    
    def server_close(self):
        self.socket.close()
        
    def do_GET(self):
        if self.path == "/":
            self.path = '/index.html'
        if self.path == "/about":
            self.path = '/about.html'
        if self.path == "/contact":
            self.path = '/contact.html'
        try:
            reply = False
            if self.path.endswith('.html'):
                mimtype = 'text/html'
                reply = True
            
            if reply == True:
                f = open(curdir + sep + self.path, 'rb')
                self.send_response(200)
                self.send_header('Content-type', mimtype)
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
        except IOError:
            self.send_error(404, "File Not Found: %s" % self.path )

try:
    httpd = HTTPServer(('127.0.0.1', PORT), HttpHandler)
    print("Started http server on port: ", PORT)
    httpd.serve_forever()
    
except KeyboardInterrupt:
    print("^C received, shutting down the web server")
    httpd.server_close()
    
