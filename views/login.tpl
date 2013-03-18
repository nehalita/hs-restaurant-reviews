<p> Please sign in below with your Hackerschool Credentials or with your login/pw for this site: </p>

<br>
%if user_error:
  <br>
  {{user_error}}
  <br>
%end

<form action="/login" method="POST">
  <table>
    <tr>
      <td>Email: </td>
      <td> <input type="text" size="30" maxlength="50" name="email"> </td>
      <td>
        % if user_error != "":
        <a href="/signup">Sign up for a new account here!</a> </td>
        %end
    </tr>
    <tr>
      <td>Password: </td>
      <td> <input type="password" size="30" maxlength="50" name="password"> </td>
      <td> {{pw_error}} </td>
    </tr>
  </table>
  <input type="submit" name="submit" value="submit">
</form>

<a href="/signup">If you're new, create an account here!</a>
