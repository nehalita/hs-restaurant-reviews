Hey {{main_var['user']}}!
<br>
<br>
You're looking at the restaurants visited by <b>{{main_var['location']}}</b>!
<br> <br>
%for item in main_var['stat_rows']:
&nbsp;&nbsp;&nbsp; <i>{{item}}</i> <br>
%end

<br>
<a href="/add_review">Add a restuarant review :D</a>
<br>
<a href="/view">Browse the restaurants your HSers have gone to</a>
