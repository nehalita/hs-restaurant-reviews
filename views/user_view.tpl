Here are {{user_id}}'s review so far!!!
<br>
<br>
%for review in restaurant_reviews:
  {{!review.to_html()}}
  <br>
  <br>
%end
<br>
<a href='/view'>Go back to restaurant reviews</a>
<br>
<br>
<a href='/main'>Go to main page</a>
