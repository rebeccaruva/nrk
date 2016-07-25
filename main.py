import json
import jinja2
import os
import logging
import webapp2

class TimeLineHandler(webapp2.RequestHandler):


class AddEventHandler(webapp2.RequestHandler):


class ExpandListHandler(webapp2.RequestHandler):


class ListHandler(webapp2.RequestHandler):


class QuoteHandler(webapp2.RequestHandler):
    def get(self,template,quote):


class WelcomePageHandler(webapp2.RequestHandler):
    def get(self, template):





jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/time', TimeLineHandler),
  ('/event', AddEventHandler),
  ('/expand'), ExpandListHandler),
  ('/list'), ListHandler),
  ('/quote'), QuoteHandler),
  ('/welcome'), WelcomePageHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
