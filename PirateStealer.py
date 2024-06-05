from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import traceback
import requests

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # Sessizce loglamak için.

    def do_GET(self):
        try:
            # Gelen isteği işle
            parsed_path = parse.urlparse(self.path)
            query = parse.parse_qs(parsed_path.query)
            
            # Gelen tokeni al
            discord_token = query.get('token', [None])[0]
            
            if discord_token:
                # Webhook URL'ini buraya ekleyin
                webhook_url = 'https://discord.com/api/webhooks/1247814141020999692/CPnfRflw67I4x-0hGhep1rPVCd7Vazz_tXmIXbA5iCBwsZMFAEyC71gZVWCZYRNDWkio'
                
                # Webhooka gönderilecek mesajı hazırla
                message = "Kullanıcı siteye girdi!"
                
                # Webhooka mesajı gönder
                requests.post(webhook_url, json={'content': message})
                
                # Yanıt gönder
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Webhooka mesaj gönderildi!")
            else:
                # Eğer token yoksa hata döndür
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Token belirtilmemiş.")
                
        except Exception as e:
            # İstisna durumlarını işle
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"İç sunucu hatası")
            traceback.print_exc()

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Sunucu port {port} üzerinde başlatıldı...')
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
