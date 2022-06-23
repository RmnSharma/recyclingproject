# recyclingproject
{% load staticfiles %}

<html>
<head>
<title>first html page</title>
<link href="{% static 'bootstrap/css/bootstrap.min.css' %}" type="text/css" rel="stylesheet" />
<link href="{% static 'bootstrap/css/bootstrap-grid.min.css' %}" type="text/css" rel="stylesheet" />
<link href="{% static 'bootstrap/css/bootstrap-reboot.min.css' %}" type="text/css" rel="stylesheet" />
<style>
</style>
<link href="{% static 'style.css' %}" type="text/css" rel="stylesheet" />
</head>
<body>

<div class="container">

<div class="row p-2 bg-primary">
<div class="col-md-12">
<h1 class="text-center display-3">My Pics</h1>
</div>
</div>

<div class="row p-2f bg-info">
< 
<img src="{% static 'image/sharma.jpg' %}" height="500" width="100%" />
</div>
<div class="col-md-6">
<h2 class="text-warning">About Me</h2>
<p>This is my website.</p>
<button class="btn btn-success">Read More</button>

<table class="table table-bordered table-striped">
<tr class="bg-dark text-light">
<th>Sr no</th>
<th> name </th>
</tr>
<tr>
<td>1</td>
<td>Raman</td>
</tr>
<tr>
<td>2</td>
<td>preet</td>
</tr>
<tr>
<td>3</td>
<td>sharma</td>
</tr>
</table>

</div>
</div>

<div class="row p-4 bg-warning" id="product">

<div class="col-md-4">
<img src="{% static 'image/pic.jpg' %}" height="400" width="100%" />
<h4>me</h4>
</div>
<div class="col-md-4">
<img src="{% static 'image/pic2.jpg' %}" height="400" width="100%" />
<h4>Raman</h4>
</div>
<div class="col-md-4">
<img src="{% static 'image/pic3.jpg' %}" height="400" width="100%" />
<h4>Preet</h4>
</div>
</div>

<div class="row bg-info">
<div class="col-mid-7">
<p>&copy; copyright 2021 All Rights Reserved</p>
</div>
<div class="col-md-5">

</body>
</html>
</html>
