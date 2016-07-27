from google.appengine.api import users
from google.appengine.ext import ndb
import json
import jinja2
import os
import logging
import webapp2
import urllib2
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
        # template = jinja_environment.get_template('gif.html')
        response = urllib2.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=celebration&fmt=json")
        giphyRand = json.loads(response.read())
        gif = giphyRand["data"]["image_original_url"]
        width = giphyRand["data"]["image_width"]
        width = int(width) + 20
        height = giphyRand["data"]["image_height"]
        height = int(height) + 45
        gifVariables = {
            "gif": gif,
            "image_width": width,
            "image_height": height
        }
        self.response.out.write(template.render(gifVariables))

class AddEventHandler(webapp2.RequestHandler):
    def get(self):
        checked_template = jinja_env.get_template('checked.html')
        self.response.out.write(checked_template.render())
    def post(self):
        addEvent_template = jinja_env.get_template('addEvent.html')
        # template_variables = {
        #     'main':self.request.get("main")
        #     }
        # self.response.out.write(addEvent_template.render(template_variables))
        # template = jinja_environment.get_template('gif.html')
        response = urllib2.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=celebration&fmt=json")
        giphyRand = json.loads(response.read())
        gif = giphyRand["data"]["image_original_url"]
        width = giphyRand["data"]["image_width"]
        width = int(width) + 20
        height = giphyRand["data"]["image_height"]
        height = int(height) + 45
        templateVariables = {
            'main':self.request.get("main"),
            "gif": gif,
            "image_width": width,
            "image_height": height
        }
        self.response.out.write(addEvent_template.render(templateVariables))

#class ExpandListHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")

class QuoteHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('checked.html')
        self.response.out.write(template.render())
        #response = urllib2.urlopen("http://quotes.rest/qod.json")
        #NowDict = json.loads(response.read())
        #Quote = NowDict["contents"]["quotes"][0]["quote"]
        #Author = NowDict["contents"]["quotes"][0]["author"]
        #self.response.out.write("<center>" + ' " ' + Quote + ' " ' "<br>" + "-" + Author + "</center>")
        self.response.out.write("<html><center>Quote Here</center></html>")


#class ListHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")

#class EmailHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),
  ('/home', QuoteHandler),
  ('/home', TimeLineHandler),
#  ('/checked-list', ExpandListHandler),
#  ('/add-event', AddEventHandler),
  ('/addEvent', AddEventHandler),
  ('/gif', GifHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
