
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#nb

def home(request):
    data = """
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wardheere</title>
</head>
<body bgcolor"navy"  style="background-color:blue;"> 
    <h1>  <center>  Welcome All Guys <span style="color:white;" >   myfirst website </span> with open hand </center>  </h1>

    <p> <center> HTTP/HTTPS:  processing the request server side application can communicate to the database if it is required </center> </p>
    <p> <center> Architecture of Web Application: End users can send request to the server side application in following ways: </center> </p>
    <p> <center> ( by typing URL in the browser,by clicking on hyperlinks on the browser,by submitting html forms ) </center> </p>

</body>
</html>
  """

    return HttpResponse(data)
