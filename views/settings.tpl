%if username != 'Anonmyous User':
    Hello! This is your setting's page. You can change your username, view your past posts, and edit them :).
%else:
    Hello! As an anonymous user, you cannot adjust your settings page but here is what you could do as a logged in user. 
%end
<br>
<br>
I want my username to be:
<form action="change_username" method="POST">
  <input type="text" name="username" value="{{username}}">
  <button name="user_id" value="{{user_id}}">change username!</button>
</form>
<br>
<br>
%if restaurant_reviews:
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
%else:
You have no reviews, feel free to <a href='/add_review'>add one</a><br>
%end
<br>
<a href='/main'>Go back to the main page</a>
