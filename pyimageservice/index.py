import tornado.web
import tornado.ioloop

class uploadHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
    
    def post(self):
        files = self.request.files["imgFile"]
        for f in files:
            fh = open(rf"C:\Users\d.takeshi\workspace\python-backend\pyimageservice\img\{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8882/img/{f.filename}")

if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path": r"C:\Users\d.takeshi\workspace\python-backend\pyimageservice\img"})
    ])

    port = 8882
    app.listen(port)
    print(f"Listening to port {port}")

    tornado.ioloop.IOLoop.instance().start()