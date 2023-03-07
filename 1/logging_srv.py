from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from csv import writer
import uuid
hostName = "localhost"
serverPort = 12345
database={}
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        path=str(self.path).split('/')
        self.send_response(200)
        self.end_headers()
        for key in database.keys():
                self.wfile.write(bytes("%s/" % (database.get(key)) , "utf-8"))
        return
        '''
        #if path[0] == "":
        #    path=self.path
        #print("Parsed path: ",path)
        if path[1]=="getKeyList":
            self.send_response(200)
            self.end_headers()
            print("Get key list")
            for key in database.keys():
                self.wfile.write(bytes("%s" % (key) , "utf-8"))
                self.wfile.write(bytes("/n", "utf-8"))
            return
        if path[1]=="getValueByKey":
            self.send_response(200)
            print("Get request for key:",key)
            self.wfile.write(bytes("%s" % (database.get(key)) , "utf-8"))
            return
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>logging-service</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request GET: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>But i parsed: %s</p>" % path[1], "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<p>Key: \"%s\"  Data: \"%s\"</p>" % database, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        '''
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length)
        parsed=list(str(post_data.decode("utf-8")).split("="))
        database[parsed[0]]=parsed[1]
        print("Successfully writen data: ", parsed)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>logging-service</title></head>", "utf-8"))
        print("Answered")
        
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
