<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="src.css">

<title>Register Page</title>

<div id='footer' align='center'>
<form action="src_reg.php" method="post" enctype="multipart/form-data"><table>

<!-- intro -->
<tr><th>
Register Form
<hr><hr></th></tr>

<!-- q1 -->
<tr><td><?php include "query/q1.htm";?><hr></td></tr>
<!-- q2 -->
<tr><td><?php include "query/q2.htm";?><hr></td></tr>
<!-- q3 -->
<tr><td><?php include "query/q3.htm";?><hr></td></tr>

</table><br>
<input type="submit" class="button" value="Create Account" />
<input type="reset" class="button" />
</form></div>

<script src="src.js"></script>
