from google.appengine.ext import ndb

class Employee(ndb.Model):
  name = ndb.StringProperty(required=True)
  goal = ndb.StringProperty(required=True)
