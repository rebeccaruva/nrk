from google.appengine.api import users
import json
import jinja2
import os
import logging
import webapp2
import urllib2
from checked import Employee
# import schedule
import time

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('login.html')
        self.response.out.write(template.render())


class TimeLineHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('checked.html')
        self.response.write(template.render())

class GifHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('gif.html')
        response = urllib2.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=celebration&fmt=json")
        giphyRand = json.loads(response.read())
        gif = giphyRand["data"]["image_original_url"]
        width = giphyRand["data"]["image_width"]
        width_image = int(width) + 30
        height = giphyRand["data"]["image_height"]
        height_image= int(height) + 70
        gifVariables = {
            'main':self.request.get("main"),
            "gif": gif,
            "image_width": width_image,
            "image_height": height_image
        }
        self.response.out.write(template.render(gifVariables))



class QuoteHandler(webapp2.RequestHandler):
     def get(self):
         template = jinja_environment.get_template('checked.html')
         self.response.out.write(template.render())
#         response = urllib2.urlopen("http://quotes.rest/qod.json")
#         NowDict = json.loads(response.read())
#         Quote = NowDict["contents"]["quotes"][0]["quote"]
#         Author = NowDict["contents"]["quotes"][0]["author"]
#         self.response.out.write("<center>" + "<font color=white> + ' " ' + Quote + ' " ' "<br>" + "-" + Author + "</font>" + "</center>")
         self.response.out.write("<html><center><font color=white>Quote Here</font></center></html>")



class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),
  ('/home', QuoteHandler),
  ('/home', TimeLineHandler),
  ('/home', GifHandler),
  ('/about', AboutHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
