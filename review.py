import pymongo
from bottle import SimpleTemplate

class Review(object):
  def __init__(self, data):
    self.data = data

  def to_html(self):
    #Each review always has a restaurant name
    template = "<b>{{item['restaurant_name']}}</b>"

    #Add address if there is one
    if 'restaurant_address' in self.data:
      template += " at <b>{{item['restaurant_address']}}</b>"

    ###ITEM TEXT FORMATTING###
    item_exists = 'restaurant_item' in self.data
    item_has_comments = 'item_comments' in self.data
    item_has_price = 'item_price' in self.data

    #text regarding the name of what you ate
    if item_exists:
      template += "<br> &nbsp; &nbsp; The {{item['restaurant_item']}} was/were "
    elif item_has_comments or item_has_price:
      template += "<br> &nbsp; &nbsp; The item was "

    #text regarding how you felt about what you ate
    if item_has_comments:
      template += "{{item['item_comments']}}"
    elif item_exists:
      template += "eaten"

    #text regarding the price of what you ate
    if (item_exists or item_has_comments) and item_has_price:
      template += ", "

    if item_has_price:
      template+= "${{item['item_price']}}"

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

    #Each review always has a reviewer and time
    template += '''<br>
      <i>review by {{item['user']}} on {{item['time']}}</i>
      '''
    return SimpleTemplate(template).render(item = self.data)
