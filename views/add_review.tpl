%if 'error' in add_var:
<b>{{add_var['error']}} </b>
  <br>
  <br>
%end
<form action="add_review" method="POST">
Please type a name for your review to be filed under:
  <input type="text" name="user">
  <br>
  <br>

<b>Whadja get? Tell me!</b>
  <br>

  Restaurant Name:
  <input type="text" name="restaurant_name">
  at
  <input type="text" placeholder="(address)" name="restaurant_address">
  <br>

  Whadja get?
  <input type="text" name="restaurant_item" placeholder="food item(s)">
  <br>

  Didja like it?
  <input type="text" name="item_comments">
  <br>

  How much was it? $
  <input type="text" name="item_price">
  <br>
  <br>

<b>Overall Comments</b>
  <br>
  Overall Rating (1=meh, 5=omg yes):
  <select name="restaurant_rating">
    <option></option>
    <option> 1 </option>
    <option> 2 </option>
    <option> 3 </option>
    <option> 4 </option>
    <option> 5 </option>
  </select>
  <br>

  Why?
  <input type="text" name="restaurant_rating_reason">
  <br>

  <input type="checkbox" name="is_recommended">
  I recommend this place
  <br>
  <br>

  <input type="submit" value="add review!">

</form>

