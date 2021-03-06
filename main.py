from google.appengine.api import users
from google.appengine.ext import ndb
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

class Goals(ndb.Model):
    text = ndb.StringProperty()
    email = ndb.StringProperty()

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('login.html')
        self.response.out.write(template.render())



"""
class AddEventHandler(webapp2.RequestHandler):
    def get(self):
        checked_template = jinja_env.get_template('checked.html')
        self.response.out.write(checked_template.render())
        #checked_template.put()
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
        width_image = int(width) + 30
        height = giphyRand["data"]["image_height"]
        height_image= int(height) + 70
        templateVariables = {
            'main':self.request.get("main"),
            "gif": gif,
            "image_width": width_image,
            "image_height": height_image
        }
        self.response.out.write(addEvent_template.render(templateVariables))
"""
class MainHandler(webapp2.RequestHandler):

     def get(self):
         template = jinja_environment.get_template('checked.html')
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

         #response = urllib2.urlopen("http://quotes.rest/qod.json")
         #NowDict = json.loads(response.read())
         #Quote = NowDict["contents"]["quotes"][0]["quote"]
         #Author = NowDict["contents"]["quotes"][0]["author"]
         self.response.out.write("<html><center>Quote Here</center></html>")
         #self.response.out.write("<center>" + "<font color=white>" + ' "' + Quote + '" ' "<br>" + "-" + Author + "</font>" + "</center>")

'''     def post(self):
         goals = Goals(text=self.request.get('goalSunday'))
         finalGoal = goals.put()
         time.sleep(.2)
         self.redirect('/home') '''


class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())


jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),
  ('/home', MainHandler),

  ('/about', AboutHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
