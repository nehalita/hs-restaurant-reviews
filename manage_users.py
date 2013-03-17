import hashlib
import random
import string
import hmac
import bson
import os
import pymongo
from urlparse import urlparse

#### MANDATORY DB STUFF, NEED TO GET RID OF THIS
MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL:
  connection = pymongo.Connection(MONGO_URL, safe=True)
  db = connection[urlparse(MONGO_URL).path[1:]]
else:
  connection = pymongo.Connection('localhost', safe=True)
  db = connection.hs_food

def add_user(email, username):
  try:
    users = db.users
    users.insert({'_id': email, 'username': username})
  except pymongo.errors.DuplicateKeyError as e:
    return "You're already in the database" % (email)
  except:
    return "Pymongo error, retry"

def start_session(email):
  sessions = db.sessions
  session = {"email": email}
  try:
    sessions.insert(session)
  except:
    print "Unexpected error on start_session:", sys.exc_info()[0]
    return -1
  return str(session['_id'])

def hash_string(string_to_hash):
  KEYWORD = "HASH ME"
  return hmac.new(KEYWORD, string_to_hash).hexdigest()

def get_cookie(session_id):
  #hashes the session_id as the cookie
  return "%s|%s" % (session_id, hash_string(session_id))

def get_session_from_cookie(cookie):
  session_id = cookie.split("|")[0]
  if (get_cookie(session_id) == cookie):
    return session_id
  else:
    print "You've got a rotten cookie, aka the cookie you put in doesn't match what I excpected"

def get_session_from_db(session_id):
  sessions = db.sessions
  try:
    object_id = bson.objectid.ObjectId(session_id)
    session = sessions.find_one({'_id': object_id})
    return session
  except:
    print "Had issues retrieving your session_id from the db"
    return None

def end_session(session_id):
  sessions = db.sessions
  try:
    object_id = bson.objectid.ObjectId(session_id)
    sessions.remove({'_id': object_id})
    print "removed session"
  except:
    print "unable to remove session"
  return

def get_info_from_db(email):
  #determines if email is in local database and returns all info if it is
  users = db.users
  try:
    user_info = users.find_one({'_id': email})
    return user_info
  except:
    print "Need to create a new acct"
    return None

def change_username(user_id, new_username):
  user_id = str(user_id)
  try:
    db.users.update({'_id': user_id}, {'$set': {'username': new_username}})
  except:
    print user_id, new_username
    print "Couldn't change the username"

'''
#I should only need this if I'm creating accts
def email_matches_password(user_info, password):
  pw = user_info['password']
  past_salt = pw.split(",")[1]
  return hash_pw(password, past_salt) == pw

def check_if_pws_match(password, pwconf):
  if password != pwconf:
    return "Your passwords do not match"

def make_salt():
  salt = ""
  for i in range(5):
    salt += random.choice(string.ascii_letters)
  return salt

def hash_pw(password, salt=None):
  if salt == None:
    salt = make_salt()
  return "%s,%s" % (hashlib.sha1(password+salt).hexdigest(), salt)
  '''
