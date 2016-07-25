from google.appengine.api import users
import json
import jinja2
import os
import logging
import webapp2

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(template_dir))

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('login.html')
        self.response.out.write(template.render())

        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Register with your Gmail account</a>.' %
                users.create_login_url('/'))
        self.response.out.write('<html><body>%s</body></html>' % greeting)

"""
class TimeLineHandler(webapp2.RequestHandler):


class AddEventHandler(webapp2.RequestHandler):


class ExpandListHandler(webapp2.RequestHandler):


class ListHandler(webapp2.RequestHandler):


class QuoteHandler(webapp2.RequestHandler):
    def get(self,template,quote):

class EmailHandler(webapp2.RequestHandler):
"""


routes = [
  ('/', LoginHandler),
]
app = webapp2.WSGIApplication(routes, debug=True)
