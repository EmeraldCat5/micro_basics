from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import uuid
hostName = "localhost"
serverPort = 12346
logging="http://localhost:12346"
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Started GET")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>facade-service</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Not implemented</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        print("Ended GET")
        
        
    def do_POST(self):
        print("Started POST")
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length)
        self.wfile.write(bytes("Not implemented", "utf-8"))
        print("Ended POST")
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
