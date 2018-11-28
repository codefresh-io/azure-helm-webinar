import os
import random
import BaseHTTPServer

PORT = os.getenv('PORT', 8080)

cats = [
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTz7DnepEt9HKWgFwpdU1U-EkBh_BVyGyl_L2xBA8Maaa3mTQ5E',
    'https://thepawington.com/wp-content/uploads/2014/02/kitten.png',
    'https://ih0.redbubble.net/image.474690746.7074/ap,550x550,12x16,1,transparent,t.u1.png',
    'https://cat-bounce.com/catbounce.png'
]

class CustomHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        #cat = cats[0]
        cat = random.choice(cats)
        self.wfile.write('{"cat": "%s"}' % cat)

def main():
    server = BaseHTTPServer.HTTPServer(('', PORT), CustomHandler)
    print('Starting server on port %d...' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
