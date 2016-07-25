from google.appengine.api import users
import json
import jinja2
import os
import logging
import webapp2

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), users.create_logout_url('/')))
        else:
            greeting = ('<a href="%s">Register with your Gmail account</a>.' %
                users.create_login_url('/'))
        self.response.out.write('<html><body>%s</body></html>' % greeting)





jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
routes = [
  ('/', LoginHandler),

]
app = webapp2.WSGIApplication(routes, debug=True)
