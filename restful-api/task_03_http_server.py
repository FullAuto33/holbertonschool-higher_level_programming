from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimplerServer(BaseHTTPRequestHandler):
    """
    SimplerServer - A subclass of BaseHTTPRequestHandler to adapt its methods.
    """
    def do_GET(self):
        """
        do_GET - A method handling get responses from web server.
        """
        dataSet = {"name": "John", "age": 30, "city": "New York"}
        infoSet = {"version": "1.0", "description":
                   "A simple API built with http.server"}
        endpointDict = {"/data": dataSet,
                        "/info": infoSet,
                        "/status": "OK",
                        "/": "Hello, this is a simple API!"}
        if self.path in endpointDict:
            self.send_response(200)
            if isinstance(endpointDict[self.path], dict):
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(endpointDict[self.path])
                                     .encode("utf8"))
            elif isinstance(endpointDict[self.path], str):
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(str(endpointDict[self.path])
                                 .encode("utf8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimplerServer):
    """
    run - Function to run webserver and learn about http methods.
    """
    server_address = ("localhost", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
