%if 'error' in add_var:
<b>{{add_var['error']}} </b>
  <br>
  <br>
%end
<form action="add_review" method="POST">
    <b> Username for your entry <a href="/settings"> change your username here</a></b>
  <br>
  {{add_var['user']}}
  <br>
  <br>

<b>Wheredja go? Tell me!</b>
  <br>

  Restaurant Name:
  <input type="text" id="restaurant_name" name="restaurant_name" value="{{add_var['restaurant_name']}}">
  <button type="button" id="address" name="address" value="{{add_var['address']}}">Find Addresses</button>
  <br>
  <div id="restaurant-js"></div>
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
  <button name="preview_selected" value="true">preview this entry</button>
  <br>
  %if 'preview_selected' in add_var and 'error' not in add_var:
    <br>
    Your review would look like:
    <br>
    {{!add_var['preview_selected']}}
    <br>
    <br>
  %end
  <input type="submit" value="add review!">
  <input type="hidden" id="res" name="restaurant_chosen" value="{{add_var['restaurant_chosen']}}">
  <input type="hidden" id="add" name="address_chosen" value="{{add_var['address_chosen']}}">
</form>

<br>
<a href="/main">Go back to the main page</a>


<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="/static/handlebars.js"></script>
<script src="/static/handlebars_files.js"></script>
<script src="/static/restaurant_finder.js"></script>
