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
'''
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s"><center><h2>Gmail Login</h2></center></a>.' %
                users.create_login_url('/home'))
        self.response.out.write('<html><body><center><h1>%s</h1></center></body></html>' % greeting)
'''

class TimeLineHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('checked.html')
        self.response.write(template.render())

#class AddEventHandler(webapp2.RequestHandler):


#     def job():
#         print("I'm working...")
#
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
#
#     def get (self):
#         self.response.out.write("example return!!")
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)


class AddEventHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('addEvent.html')
        self.response.out.write(template.render())

class ExpandListHandler(webapp2.RequestHandler):
    def get (self):
        self.response.out.write("example return!!")

class QuoteHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('checked.html')
        self.response.out.write(template.render())
        response = urllib2.urlopen("http://quotes.rest/qod.json")
        NowDict = json.loads(response.read())
        Quote = NowDict["contents"]["quotes"][0]["quote"]
        #Author = NowDict["contents"]["author"]
        self.response.out.write(Quote)

class ListHandler(webapp2.RequestHandler):
    def get (self):
        self.response.out.write("example return!!")

class EmailHandler(webapp2.RequestHandler):
    def get (self):
        self.response.out.write("example return!!")






jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),
  ('/home', QuoteHandler),
  ('/list', ListHandler),
  ('/home', TimeLineHandler),
  ('/checked-list', ExpandListHandler),
  ('/email', EmailHandler),
  ('/add-event', AddEventHandler)
]
app = webapp2.WSGIApplication(routes, debug=True)
