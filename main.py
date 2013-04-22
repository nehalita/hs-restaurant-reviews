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
    CONNECTION = pymongo.Connection(MONGO_URL, safe=True)
    db = CONNECTION[urlparse(MONGO_URL).path[1:]]
else:
    CONNECTION = pymongo.Connection('localhost', safe=True)
    db = CONNECTION.hs_food

STATS = ["RECENT: Someone just wrote about Romy's Cajun Rice!", "POPULAR: People seem to go to Chipotle a lot...", "ACCLAIMED: People looooove 'Snice!"]
LOCATION = "Hacker School HQ"

@bottle.route('/main')
def post_main_page():
    username = sign_up.get_username()
    main_var = dict(user = username, stat_rows = STATS, location = LOCATION)
    return bottle.template('main', main_var = main_var)

@bottle.route('/add_review', method="GET")
def add_restaurant_review():
    username = sign_up.get_username()
    if username:
        add_var = dict(user=username, restaurant_name="", restaurant_address="",
                restaurant_item="", item_comments="", item_price="",
                restaurant_ranking="", restaurant_rating="",
                restaurant_rating_reason="")
        return bottle.template('add_review', add_var=add_var)
    else:
        return bottle.template('login',
                dict(user_error="Sorry, you need to be logged in to submit a review, please log below:", pw_error=""))

@bottle.route('/add_review', method="POST")
def add_review_to_db():
    add_var = {}
    restaurant_review_entry = {}

    username = sign_up.get_username()

    for key, value in bottle.request.forms.items():
        print "%s: %s" % (key, value)
        add_var[key] = value

        restaurant_review_entry["user"] = username
        add_var['user'] = username

        if key != 'submit' and value != "":
            restaurant_review_entry[key] = value
    restaurant_review_entry['time'] = time.strftime("%a, %b %d %Y %I:%M%p",
            time.localtime())

    #see if there's a restaurant name, otherwise send back with fields entered
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
    except pymongo.errors.PyMongoError:
        add_var['error'] = "Error: Couldn't add this to the db"
        return bottle.template('add_review', add_var=add_var)

    return bottle.redirect('view')

@bottle.route('/view')
def view_current_views():
    reviews = r.get_all_reviews(db)
    return bottle.template('view', reviews = reviews)

@bottle.route('/restaurant/:restaurant_name')
def view_restaurant_reviews(restaurant_name):
    restaurant_reviews = r.get_reviews_by(db,
            'restaurant_name', restaurant_name)
    #4sq_api_query_link = "https://api.foursquare.com/v2/venues/search?v=20130311&client_id=JSM3WVVM1OTXSHTUALUK1VADIKD5TGS3IQT2H5CX40TC4M1V&client_secret=KZ1Q4UGUJZD21TLPMK3SJY1YBUCBHGQN2X5MLRKVXYV5YVVA&query=%s&intent=browse&ll=40.726576,-74.000645&radius=400" % (restaurant_name)
    return bottle.template('restaurant_view', restaurant_reviews = restaurant_reviews, restaurant_name = restaurant_name)

@bottle.route('/settings')
def show_users_settings():
    email = sign_up.get_email()
    restaurant_reviews = r.get_reviews_by(db, 'user_id', email)
    username = sign_up.get_username()
    return bottle.template('settings', restaurant_reviews = restaurant_reviews, username = username, user_id = email)

@bottle.route('/change_username', method="POST")
def change_users_username():
    username_to_change = bottle.request.forms.get('username')
    user_id = bottle.request.forms.get('user_id')
    manage_users.change_username(user_id, username_to_change)
    return bottle.redirect('/settings')

@bottle.route('/users/:username')
def direct_to_user_id(username):
    restaurant_review_by_username = r.get_reviews_by(db, 'user', username)
    one_review = restaurant_review_by_username[0]
    user_id = one_review.data['user_id']
    return bottle.redirect('/user_id/'+user_id)

@bottle.route('/user_id/:user_id')
def view_users_reviews(user_id):
    restaurant_reviews = r.get_reviews_by(db, 'user_id', user_id)
    return bottle.template('user_view', user_id = user_id, restaurant_reviews = restaurant_reviews)

@bottle.route('/user_id/modify_post/:user_id', method='POST')
def remove_review(user_id):
    id_to_remove = bottle.request.forms.get('review_to_remove')
    id_to_edit = bottle.request.forms.get('review_to_edit')
    if id_to_remove:
        object_id = bson.objectid.ObjectId(id_to_remove)
        db.reviews.remove({'_id': object_id})
    return bottle.redirect('/settings')


@bottle.route('/static/:filename#.*#')
def server_static(filename):
    #import pdb; pdb.set_trace()
    return bottle.static_file(filename, root='static')

if __name__ == '__main__':
    if os.environ.get('ENVIRONMENT') == 'PRODUCTION':
        port = int(os.environ.get('PORT', 5000))
        print "port = %d" % port
        bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        bottle.debug(True) #dev only, not for production
        bottle.run(host='localhost', port=8081, reloader=True) #dev only
