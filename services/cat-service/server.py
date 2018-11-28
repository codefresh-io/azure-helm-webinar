import os
import BaseHTTPServer

PORT = os.getenv('PORT', 8080)

class CustomHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write('{"cat": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz7DnepEt9HKWgFwpdU1U-EkBh_BVyGyl_L2xBA8Maaa3mTQ5E"}')

def main():
    server = BaseHTTPServer.HTTPServer(('', PORT), CustomHandler)
    print('Starting server on port %d...' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
