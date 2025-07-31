import http.server
import ssl

server_address = ('localhost', 4443)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               certfile="certificate.crt",
                               keyfile="private.key",
                               ssl_version=ssl.PROTOCOL_TLS)
print("🔐 Serving on https://localhost:4443")
httpd.serve_forever()
