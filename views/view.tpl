Reviews so far:
<br>
<br>
  %for item in reptaur_reviews:
  <b>{{item['restaurant_name']}}</b> at <b>{{item['restaurant_address']}}</b>
  <br>
    &nbsp; &nbsp; The {{item['restaurant_item']}} was/were
    {{item['item_comments']}} (${{item['item_price']}})
    <br>
    &nbsp; &nbsp; Overall: {{item['restaurant_rating_reason']}} ({{item['restaurant_rating']}}
    of 5) 
  <br>
  <i>review by {{item['user']}} on {{item['time']}}</i>
  <br>
  <br>
  %end
