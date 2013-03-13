import os
import pymongo
import bottle
import manage_users
import hs_auth
import main

from urlparse import urlparse

MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL:
  connection = pymongo.Connection(MONGO_URL, safe=True)
  db = connection[urlparse(MONGO_URL).path[1:]]
else:
  connection = pymongo.Connection('localhost', safe=True)
  db = connection.todolist

@bottle.route('/')
def default_login():
  #eventually ask if there's a cookie so i can redirect to a logged in page
  return bottle.redirect('/login')

@bottle.route('/login', method='GET')
def get_login_info():
  return bottle.template('login', dict(user_error="", pw_error=""))

@bottle.route('/login', method='POST')
def log_user_in():
  email = bottle.request.forms.get('email')
  password = bottle.request.forms.get('password')

  hs_user_info = hs_auth.authenticate_with_hs(email, password)
  if hs_user_info:
    print hs_user_info
    user_info = manage_users.get_info_from_db(email)

    if not user_info:
      #user is a hackerschooler but isn't in my db so add them to db
      username = "%s %s" % (hs_user_info['first_name'], hs_user_info['last_name'])
      manage_users.add_user(email, username)

    session_id = manage_users.start_session(email)
    cookie = manage_users.get_cookie(session_id)
    bottle.response.set_cookie("session", cookie)
    bottle.redirect('main')
  else:
    error_message = "We couldn't log you in; check your hackerschool email and pw and try again :D"
    return bottle.template('login', dict(user_error = "", pw_error = error_message))

def get_session():
  cookie = bottle.request.get_cookie("session")
  if cookie == None:
    print "Sorry, no cookie in the cookie jar"
    return None
  else:
    session_id = manage_users.get_session_from_cookie(cookie)
    if session_id:
      session = manage_users.get_session_from_db(session_id)
      return session
    else:
      print "Sorry, your cookie didn't generate properly"
      return None

@bottle.route('/logout', method='GET')
def logout_user():
  session = get_session()
  if session:
    manage_users.end_session(session['_id'])
    bottle.response.set_cookie("session", "")
    bottle.redirect('/login')
  else:
    bottle.redirect('/login', dict(user_error = "", pw_error = ""))

def get_username():
  session = get_session()
  email = session['email']
  user_info = manage_users.get_info_from_db(email)
  return user_info['username']

'''
#Not allowing signups for now, will modify code later when I'm ready
@bottle.route('/signup', method='GET')
def get_user_and_pw():
  return bottle.template('signup', dict(pw_error = "", user_error = ""))

@bottle.route('/signup', method='POST')
def store_user_and_pw():
  email = bottle.request.forms.get('email')
  password = bottle.request.forms.get('password')
  username = bottle.request.forms.get('username')

  if password == pwconf:
    user_error_check = manage_users.add_user(email, username)
    if user_error_check == None:
      entry = db.users.find_one({"_id": email})
      hashed_pw = entry["password"]
      #Houston we are a go, the pws match and the user is not in the system

      #THIS IS WHERE THE MAGIC HAPPENS
      session_id = manage_users.start_session(email)
      cookie = manage_users.get_cookie(session_id)
      bottle.response.set_cookie("session", cookie)
      bottle.redirect('/todo')
    else:
      pw_error_message = "Your passwords do not match"
      return bottle.template('signup', dict(pw_error = "", user_error =
                                            user_error_check))
  else:
    return bottle.template('signup', dict(pw_error = pw_error_message, user_error = ""))
'''

if __name__ == '__main__':
  if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
    port = int(os.environ.get('PORT', 5000))
    print "port = %d" % port
    bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  else:
    bottle.debug(True) #dev only, not for production
    bottle.run(host='localhost', port=8082, reloader=True) #dev only
