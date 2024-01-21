<style>
textarea {
	resize: none;
}
</style>

<table>
<tr><td>name:</td><td><input id="id1" name="name" type="text"></tr></td>
<tr><td>age:</td><td><input id="id2" name="age" type="number" min=0 max=120></tr></td>
<tr><td><input type="button" value="Add" onclick="f1()"></tr></td>
<tr><td><textarea id="id3" rows=12 readonly></textarea></tr></td>
</table>

<form action="src.php" method="post" enctype="multipart/form-data">
<textarea id="id4" name="in" rows=12 readonly hidden></textarea>
<input type="submit" class="button" />
<input type="reset" class="button" />
</form>

<script src="src.js"></script>
