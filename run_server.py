import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    port = PORT
    while port < 8100:
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}/index.html"
                print(f"==================================================")
                print(f"🍄 버섯 도그하우스 3D 뷰어 로컬 서버 시작!")
                print(f"🌐 접속 주소: {url}")
                print(f"==================================================")
                webbrowser.open(url)
                httpd.serve_forever()
        except OSError:
            port += 1

if __name__ == "__main__":
    start_server()
