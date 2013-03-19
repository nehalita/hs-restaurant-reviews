Hello! This is your setting's page. You can change your username, view your past posts, and edit them :).
<br>
<br>
I want my username to be:
<form action="change_username" method="POST">
  <input type="text" name="username" value="{{username}}">
  <button name="user_id" value="{{user_id}}">change username!</button>
</form>
<br>
<br>
Your reviews are:
<br>
<br>
%for review in restaurant_reviews:
  {{!review.to_html()}}
  <br>
  <form action="/user_id/modify_post/{{user_id}}" method="POST">
    <button name="review_to_remove" value="{{review.data['_id']}}">Remove this review</button>
    <button name="review_to_edit" value="{{review.data['_id']}}">Edit this review (doesn't work yet)</button>
  </form>
%end
