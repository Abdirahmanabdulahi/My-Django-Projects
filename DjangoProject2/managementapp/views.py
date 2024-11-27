from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def adminconsole(request):
     data = """
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wardheere</title>
</head>
<body bgcolor"navy"  style="background-color:blue;"> <br><br><br><br><br><br><br>
    <h1>  <center> welcome <span style="color:white;" >    admin Pages </span> here </center>  </h1>


    <p> <center> Guleed  Welcome with open hand </center> </p>
    <p> <center> Guure Welcome with open hand </center> </p>
    <p> <center> Guutaale Welcome with open hand </center> </p>
   

</body>
</html>
  """
     return HttpResponse(data)



def adminemployees(request):
     data = """
      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wardheere</title>
</head>
<body bgcolor"navy"  style="background-color:blue;"> <br><br><br><br><br><br><br>
    <h1>  <center> welcome <span style="color:white;" >    Employee Pages </span> here </center>  </h1>


    <p> <center> Khaalid  Welcome with open hand </center> </p>
    <p> <center> Khadro Welcome with open hand </center> </p>
    <p> <center> Khaali Welcome with open hand </center> </p>
   

</body>
</html>
  """
     return HttpResponse(data)


