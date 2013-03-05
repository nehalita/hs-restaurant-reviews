import os
import pymongo
import bottle
import time
import review as r
from urlparse import urlparse

MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL:
  connection = pymongo.Connection(MONGO_URL, safe=True)
  db = connection[urlparse(MONGO_URL).path[1:]]
else:
  connection = pymongo.Connection('localhost', safe=True)
  db = connection.hs_food

@bottle.route('/')
def reroute_to_main_page():
  return bottle.redirect('/main')

user = "Reptaur"
stats = ["RECENT: Someone just wrote about Romy's Cajun Rice!", "POPULAR: People seem to go to Chipotle a lot...", "ACCLAIMED: People looooove 'Snice!"]
location = "Hacker School HQ"

@bottle.route('/main')
def post_main_page():
  main_var = dict(user = user, stat_rows = stats, location = location)
  return bottle.template('main', main_var = main_var)

@bottle.route('/add_review', method="GET")
def add_restaurant_review():
  add_var = dict(user=user)
  return bottle.template('add_review', add_var=add_var)

@bottle.route('/add_review', method="POST")
def add_review_to_db():
  restaurant_review_entry = {}

  add_var = dict(user=user)
  for item in bottle.request.forms.items():
    print item
    if item[0] == "restaurant_name" and item[1] == "":
      add_var['error'] = "Error: Please enter restaurant name, silly!"
      return bottle.template('add_review', add_var=add_var)

    if item[0] == "user" and item[1] == "":
      item[1] = "unnamed user"

    if item[0] != 'submit' and item[1] != "":
      restaurant_review_entry[item[0]] = item[1]
  restaurant_review_entry['time'] = time.strftime("%a, %b %d %Y %I:%M%p", time.localtime())

  try:
    db.reviews.insert(restaurant_review_entry)
  except:
    add_var['error'] = "Error: Couldn't add this to the db for some reason, are you clicking submit too many times?"
    return bottle.template('add_review', add_var=add_var)

  return bottle.redirect('view')

@bottle.route('/view')
def view_current_views():
  reptaur_reviews = [r.Review(data) for data in db.reviews.find()]
  #import pdb
  #pdb.set_trace()
  return bottle.template('view', reptaur_reviews = reptaur_reviews)

if __name__ == '__main__':
  if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
    port = int(os.environ.get('PORT', 5000))
    print "port = %d" % port
    bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  else:
    bottle.debug(True) #dev only, not for production
    bottle.run(host='localhost', port=8081, reloader=True) #dev only