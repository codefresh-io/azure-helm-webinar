import os
import random
import BaseHTTPServer

PORT = os.getenv('PORT', 8080)

class CustomHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        #color = '#b978c0'
        color = '#%06x' % random.randint(0, 0xFFFFFF)
        self.wfile.write('{"color": "'+color+'"}')

def main():
    server = BaseHTTPServer.HTTPServer(('', PORT), CustomHandler)
    print('Starting server on port %d...' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
