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
        response = urllib2.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=celebration&fmt=json")
        giphyRand = json.loads(response.read())
        gif = giphyRand["data"]["image_original_url"]
        gifVariables = {
            "gif": gif
        }
        self.response.out.write(template.render(gifVariables))

#class AddEventHandler(webapp2.RequestHandler):
#    def get(self):
#        template = jinja_environment.get_template('addEvent.html')
#        self.response.out.write(template.render())
class AddEventHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('checked.html')
        self.response.out.write(main_template.render())
    def post(self):
        results_template = env.get_template('addEvent.html')

#class ExpandListHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")

class QuoteHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('checked.html')
        self.response.out.write(template.render())
        '''response = urllib2.urlopen("http://quotes.rest/qod.json")
        NowDict = json.loads(response.read())
        Quote = NowDict["contents"]["quotes"][0]["quote"]
        #Author = NowDict["contents"]["author"]
        self.response.out.write(Quote)'''
        self.response.out.write("hello world")

<<<<<<< HEAD
=======
#class ListHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")

#class EmailHandler(webapp2.RequestHandler):
#    def get (self):
#        self.response.out.write("example return!!")


>>>>>>> 4496c3e7aa5069ca8d29f81acdf51bf5ad1373c5

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),
  ('/home', QuoteHandler),
<<<<<<< HEAD
  ('/home', TimeLineHandler),
  ('/checked-list', ExpandListHandler),
  ('/add-event', AddEventHandler),
=======
#  ('/list', ListHandler),
  ('/home', TimeLineHandler),
#  ('/checked-list', ExpandListHandler),
#  ('/email', EmailHandler),
#  ('/add-event', AddEventHandler),
>>>>>>> 4496c3e7aa5069ca8d29f81acdf51bf5ad1373c5
  ('/gif', GifHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
