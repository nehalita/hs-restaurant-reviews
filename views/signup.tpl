<a href="/login">HSers, log in here!</a>
<p> Please sign in below: </p>
<form action="/signup" method="POST">
  <table>
    <tr>
      <td>Email: </td>
      <td> <input type="text" size="30" maxlength="50" name="email"> </td>
      <td> 
        %if user_error:
        <td>{{user_error}} </td>
        <a href="/login">Login here!</a> </td>
        %end
    </tr>
    <tr>
      <td>Password: </td>
      <td> <input type="password" size="30" maxlength="50" name="password">
      </td>
    </tr>
    <tr>
      <td>Confirm Password: </td>
      <td> <input type="password" size="30" maxlength="50" name="passwordconf">
      </td>
      %if pw_error:
      <td> {{pw_error}} </td>
      %end
    </tr>
  </table>
  <input type="submit" name="submit" value="add me">
</form>

<a href="/login">If you already have an account, log in here!</a>
