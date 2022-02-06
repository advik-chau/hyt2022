<?php
include_once "header.php";
?>

<form class="animate container align-items-center col-sm-3 mt-4" method="post" action="includes/login.inc.php">

    <div>
        <label for="email"><b>Email: </b></label>
        <input type="text" placeholder="xyz@gmail.com" name="email" required>
    </div>
    <br>
    <div>
        <label for="password"><b>Password: </b></label>
        <input required type="password" placeholder="" name="pwd" required>
    </div>
    <br>
    <button type="submit" name="submit" class="btn btn-primary">Log In</button>
    <br>
    <span class="psw">Forgot Password?</span>
    </div>
</form>

<?php
include_once "footer.php";
?>