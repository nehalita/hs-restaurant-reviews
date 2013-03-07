%if 'error' in add_var:
<b>{{add_var['error']}} </b>
  <br>
  <br>
%end
<form action="add_review" method="POST">
  <b> Who are you? </b>
  <br>
Type in a username:
  <input type="text" name="user" value="{{add_var['user']}}">
  <br>
  <br>

<b>Wheredja go? Tell me!</b>
  <br>

  Restaurant Name:
  <input type="text" name="restaurant_name" value="{{add_var['restaurant_name']}}">
  at
  <input type="text" placeholder="(address)" name="restaurant_address" value="{{add_var['restaurant_address']}}">
  <br>
  <br>
<b>Whadja get?</b>
<br>
  Whadja get?
  <input type="text" name="restaurant_item" placeholder="food item(s)" value="{{add_var['restaurant_item']}}">
  <br>

  Howdja like it?
  <input type="text" name="item_comments" value="{{add_var['item_comments']}}">
  <br>

  How much was it? $
  <input type="text" name="item_price" value="{{add_var['item_price']}}">
  <br>
  <br>

<b>Overall Comments</b>
  <br>
  Overall Rating (1=meh, 5=omg yes):
  <select name="restaurant_rating">
    <option> {{add_var['restaurant_rating']}} </option>
    <option> 1 </option>
    <option> 2 </option>
    <option> 3 </option>
    <option> 4 </option>
    <option> 5 </option>
  </select>
  <br>

  Why?
  <input type="text" name="restaurant_rating_reason" value="{{add_var['restaurant_rating_reason']}}">
  <br>
  %if 'is_recommended' in add_var:
    <input type="checkbox" name="is_recommended" checked>
  %else:
    <input type="checkbox" name="is_recommended">
  %end
  I recommend this place
  <br>
  <br>

  <input type="submit" value="add review!">
</form>

