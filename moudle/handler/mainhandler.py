import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):			  
        self.render("shequ-detail.html")

class ShequHandler(tornado.web.RequestHandler):
    def get(self):			  
        self.render("comm-detail.html")