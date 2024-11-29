from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def workspace(request):
    data = """
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wardheere</title>
</head>
<body bgcolor"navy"  style="background-color:blue;"> <br><br><br><br><br><br><br>
    <h1>  <center> welcome <span style="color:white;" >    Students Pages </span> here </center>  </h1>


    <p> <center> Maryamo  Welcome with open hand </center> </p>
    <p> <center> Maariyo  Welcome with open hand </center> </p>
    <p> <center> muuno  Welcome with open hand </center> </p>
   

</body>
</html>
  """
    return HttpResponse(data)