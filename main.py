import os
import pymongo
import bottle
import time
import review as r
import bson
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

username = "Reptaur"
stats = ["RECENT: Someone just wrote about Romy's Cajun Rice!", "POPULAR: People seem to go to Chipotle a lot...", "ACCLAIMED: People looooove 'Snice!"]
location = "Hacker School HQ"

@bottle.route('/main')
def post_main_page():
  main_var = dict(user = username, stat_rows = stats, location = location)
  return bottle.template('main', main_var = main_var)

@bottle.route('/add_review', method="GET")
def add_restaurant_review():
  add_var = dict(user="", restaurant_name="", restaurant_address="", restaurant_item="", item_comments="", item_price="", restaurant_ranking="", restaurant_rating="", restaurant_rating_reason="")
  return bottle.template('add_review', add_var=add_var)

@bottle.route('/add_review', method="POST")
def add_review_to_db():
  add_var={}
  restaurant_review_entry = {}

  for item in bottle.request.forms.items():
    #bottle.request.forms.items() returns a tuple, hence the ugly code before
    print item
    add_var[item[0]] = item[1]

    if item[0] == "user" and item[1] == "":
      restaurant_review_entry[item[0]] = "unnamed user"

    if item[0] != 'submit' and item[1] != "":
      restaurant_review_entry[item[0]] = item[1]
  restaurant_review_entry['time'] = time.strftime("%a, %b %d %Y %I:%M%p", time.localtime())

  #before adding to db, see if there's a restaurant name, otherwise send back with fields entered
  if 'restaurant_name' not in restaurant_review_entry:
    add_var['error'] = "Error: Please enter restaurant name, silly!"
    print add_var['restaurant_address']
    return bottle.template('add_review', add_var=add_var)

  if 'preview_selected' in restaurant_review_entry:
    entry_preview = r.Review(restaurant_review_entry).to_html()
    add_var['preview_selected'] = entry_preview
    print add_var
    return bottle.template('add_review', add_var=add_var)



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

@bottle.route('/restaurant/:restaurant_name')
def view_restaurant_reviews(restaurant_name):
  restaurant_reviews = [r.Review(review) for review in db.reviews.find({'restaurant_name': restaurant_name})]
  return bottle.template('restaurant_view', restaurant_reviews = restaurant_reviews, restaurant_name = restaurant_name)

@bottle.route('/users/:username')
def view_users_reviews(username):
  restaurant_reviews = [r.Review(review) for review in db.reviews.find({'user': username})]
  return bottle.template('user_view', username = username, restaurant_reviews = restaurant_reviews)

@bottle.route('/users/remove_post/:username', method='POST')
def remove_review(username):
  #import pdb
  #pdb.set_trace()
  id_to_remove = bottle.request.forms.get('review_to_remove')
  object_id = bson.objectid.ObjectId(id_to_remove)
  db.reviews.remove({'_id': object_id})
  return bottle.redirect('/users/'+username)


if __name__ == '__main__':
  if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
    port = int(os.environ.get('PORT', 5000))
    print "port = %d" % port
    bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
  else:
    bottle.debug(True) #dev only, not for production
    bottle.run(host='localhost', port=8081, reloader=True) #dev only
