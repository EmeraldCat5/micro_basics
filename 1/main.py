from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import requests
import uuid
hostName = "localhost"
serverPort = 8080
logging="http://localhost:12345"
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/all":
            print("Starint \"all\"")
            '''
            keys=list(requests.get(logging+"/getKeyList").text)
            print("Key list:", keys)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            for key in keys:
                value=requests.get(logging+"/getValueByKey/"+key).text
                self.wfile.write(bytes("<p>Key: %s  Data: %s </p>" % (key,value) , "utf-8"))

            '''
            x=str(requests.get(logging+"/all/").text).split('/')
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            for y in x:
                if y == "":
                    break
                self.wfile.write(bytes("<p>Value: %s </p>" %(y), "utf-8"))
            return
        print("Started GET")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>facade-service</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request GET: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        print("Ended GET")
        
        
    def do_POST(self):
        print("Started POST")
        content_length = int(self.headers['Content-Length']) 
        post_data = self.rfile.read(content_length)
        temp=str(post_data.decode("utf-8")).split("=")
        ident=uuid.uuid4()
        parsed=dict({ident:temp[1]})
        print("Received data: ",temp[1], ". Generated id: ", ident)
        try:
            x = requests.post(logging, data=parsed)
        except:
            print("Error with ", ident)
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("An error occured"), "utf-8")
            return
        print("Sended: ", parsed)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Success", "utf-8"))
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
