import os
import BaseHTTPServer

PORT = os.getenv('PORT', 8080)

class CustomHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write('{"color": "#b978c0"}')

def main():
    server = BaseHTTPServer.HTTPServer(('', PORT), CustomHandler)
    print('Starting server on port %d...' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
