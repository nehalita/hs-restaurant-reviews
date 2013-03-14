import os
import pymongo
import bottle
import time
import review as r
import bson
import sign_up
import manage_users
from urlparse import urlparse

MONGO_URL = os.environ.get('MONGOHQ_URL')

if MONGO_URL:
  connection = pymongo.Connection(MONGO_URL, safe=True)
  db = connection[urlparse(MONGO_URL).path[1:]]
else:
  connection = pymongo.Connection('localhost', safe=True)
  db = connection.hs_food

@bottle.route('/')
def reroute_to_login():
  return bottle.redirect('/login')

stats = ["RECENT: Someone just wrote about Romy's Cajun Rice!", "POPULAR: People seem to go to Chipotle a lot...", "ACCLAIMED: People looooove 'Snice!"]
location = "Hacker School HQ"

@bottle.route('/main')
def post_main_page():
  username = sign_up.get_username()
  main_var = dict(user = username, stat_rows = stats, location = location)
  return bottle.template('main', main_var = main_var)

@bottle.route('/add_review', method="GET")
def add_restaurant_review():
  username = sign_up.get_username()
  if username:
    add_var = dict(user=username, restaurant_name="", restaurant_address="", restaurant_item="", item_comments="", item_price="", restaurant_ranking="", restaurant_rating="", restaurant_rating_reason="")
    return bottle.template('add_review', add_var=add_var)
  else:
    return bottle.template('login', dict(user_error="Sorry, you need to be logged in to submit a review, please log below:", pw_error=""))

@bottle.route('/add_review', method="POST")
def add_review_to_db():
  add_var={}
  restaurant_review_entry = {}

  for key, value in bottle.request.forms.items():
    print "%s: %s" % (key, value)
    add_var[key] = value

    if key == "user" and value == "":
      restaurant_review_entry[key] = "unnamed user"

    if key != 'submit' and value != "":
      restaurant_review_entry[key] = value
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

  #we're ready to add entry to db
  restaurant_review_entry['user_id'] = sign_up.get_email()

  try:
    db.reviews.insert(restaurant_review_entry)
  except:
    add_var['error'] = "Error: Couldn't add this to the db for some reason, are you clicking submit too many times?"
    return bottle.template('add_review', add_var=add_var)

  return bottle.redirect('view')

@bottle.route('/view')
def view_current_views():
  reviews = r.get_all_reviews(db)
  #import pdb
  #pdb.set_trace()
  return bottle.template('view', reviews = reviews)

@bottle.route('/restaurant/:restaurant_name')
def view_restaurant_reviews(restaurant_name):
  restaurant_reviews = [r.Review(review) for review in db.reviews.find({'restaurant_name': restaurant_name})]
  restaurant_reviews = r.get_reviews_by(db, 'restaurant_name', restaurant_name)
  #4sq_api_query_link = "https://api.foursquare.com/v2/venues/search?v=20130311&client_id=JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V&client_secret=KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA&query=%s&intent=browse&ll=40.726576,-74.000645&radius=400" % (restaurant_name)
  return bottle.template('restaurant_view', restaurant_reviews = restaurant_reviews, restaurant_name = restaurant_name)

@bottle.route('/settings')
def show_users_settings():
  email = sign_up.get_email()
  restaurant_reviews = r.get_reviews_by(db, 'user_id', email)
  return "working on it"

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
