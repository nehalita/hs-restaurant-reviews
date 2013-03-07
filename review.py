import pymongo
from bottle import SimpleTemplate

class Review(object):
  def __init__(self, data):
    self.data = data

  def to_html(self):
    #Each review always has a restaurant name
    template = ""
    template = "<b><a href='/restaurant/{{item['restaurant_name']}}'>{{item['restaurant_name']}}</a></b>"

    #Add address if there is one
    if 'restaurant_address' in self.data:
      template += " at <b>{{item['restaurant_address']}}</b>"

    ###ITEM TEXT FORMATTING###
    item_exists = 'restaurant_item' in self.data
    item_has_comments = 'item_comments' in self.data
    item_has_price = 'item_price' in self.data

    #text regarding the name of what you ate
    if item_exists:
      template += "<br> &nbsp; &nbsp; I had the {{item['restaurant_item']}}"
      if item_has_price:
        template += " for ${{item['item_price']}}"
      if item_has_comments:
        template += " and {{item['item_comments']}}"

    ###ITEM OVERALL FORMATTING###
    comment_exists = 'restaurant_rating_reason' in self.data
    rating_exists = 'restaurant_rating' in self.data

    if comment_exists or rating_exists:
      template += "<br> &nbsp; &nbsp; Overall: "

    if comment_exists:
      template += "{{item['restaurant_rating_reason']}}"
      if rating_exists:
        template += ", "

    if rating_exists:
      template += "{{item['restaurant_rating']}} of 5"

    if 'is_recommended' in self.data:
      template += "<br> &nbsp; &nbsp; I recommend this place!"
    #Each review always has a reviewer and time
    template += '''<br>
      <i>review by <a href="/users/{{item['user']}}">{{item['user']}}</a> on {{item['time']}}</i>
      '''
    return SimpleTemplate(template).render(item = self.data)
