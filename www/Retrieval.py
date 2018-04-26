#!C:/Python27/python.exe
print "Content-type:text/html\r\n\r\n"
import MySQLdb
#Import modules for CGI handling
import cgi, cgitb 
cgitb.enable()
db = MySQLdb.connect("127.0.0.1","root","","hotel" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
def FoodRet():
    try:
       # Execute the SQL command
         cursor.execute("Select htl_name,scr from FOODLIST order by scr DESC")
         results=cursor.fetchall()
       # Commit your changes in the database
         db.commit()
    except:
   # Rollback in case there is any error
         db.rollback()
    return results
def RoomRet():
    try:
       # Execute the SQL command
         cursor.execute("Select htl_name,scr from HTEL order by scr DESC  ")
         results1=cursor.fetchall()
       # Commit your changes in the database
         db.commit()
    except:
   # Rollback in case there is any error
         db.rollback()
    return results1
def EnvRet():
    try:
       # Execute the SQL command
       cursor.execute("Select htl_name,scr from ENVIRONLIST order by scr DESC")
       #print "Done"
       results2=cursor.fetchall()
       # Commit your changes in the database
       db.commit()
    except:
   # Rollback in case there is any error
       db.rollback()
    return results2
def ServiceRet():
    try:
       # Execute the SQL command
         cursor.execute("Select htl_name,scr from SERVICELIST order by scr DESC")
         #print "Done"
         results3=cursor.fetchall()
       # Commit your changes in the database
         db.commit()
    except:
   # Rollback in case there is any error
         db.rollback()
    return results3
def PriceRet():
    try:
       # Execute the SQL command
         cursor.execute("Select htl_name,scr from PRICELIST order by scr DESC")
         #print "Done"
         results4=cursor.fetchall()
       # Commit your changes in the database
         db.commit()
    except:
   # Rollback in case there is any error
         db.rollback()
    return results4

if __name__ == "__main__":
    

# Create instance of FieldStorage 
    form = cgi.FieldStorage() 
# Get data from fields
    asp = form.getvalue('aspect')
    a=[]
    if asp == 'Food':
        a=FoodRet()
        l1=list(a[0])
        l2=list(a[1])
        l3=list(a[2])
        l4=list(a[3])
        l5=list(a[4])
        l6=list(a[5])
        l7=list(a[6])
        l8=list(a[7])
        l9=list(a[8])
        l10=list(a[9])
        l11=list(a[10])
        l12=list(a[11])
        l13=list(a[12])
        l14=list(a[13])
		
        print """
           <html>
		   <!-- ====================================================
	header section -->
	<header class="top-header">
		<div class="container">
			<div class="row">
				<div class="col-xs-5 header-logo">
					<br>
					<a href="index.html"><img src="Logo.png" alt="" class="img-responsive logo"></a>
				</div>

				<div class="col-md-7">
					<nav class="navbar navbar-default">
					  <div class="container-fluid nav-bar">
					    <!-- Brand and toggle get grouped for better mobile display -->
					    <div class="navbar-header">
					     <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					        <!-- <span class="sr-only">Toggle navigation</span> -->
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					      </button>
					    </div>

					    <!-- Collect the nav links, forms, and other content for toggling -->
					    <!-- <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					      
					     <ul class="nav navbar-nav navbar-right">
					        <li><a class="menu active" href="#home" >Home</a></li>
					        <li><a class="menu" href="#about">about us</a></li>
					        <li><a class="menu" href="#service">our services </a></li>
					        <li><a class="menu" href="#team">our team</a></li>
					        <li><a class="menu" href="#contact"> contact us</a></li>
					      </ul>
					    </div><!-- /navbar-collapse -->
					  </div><!-- / .container-fluid -->
					</nav>
				</div>
			</div>
		</div>
	</header> <!-- end of header area -->
		   <style>
		   .zui-table {
    border: solid 1px #DDEEEE;
    border-collapse: collapse;
    border-spacing: 0;
    font: normal 19px Arial, sans-serif;
}
.zui-table thead th {
    background-color: #DDEFEF;
    border: solid 1px #DDEEEE;
    color: #336B6B;
    padding: 10px;
    text-align: left;
    text-shadow: 1px 1px 1px #fff;
}
.zui-table tbody td {
    border: solid 1px #DDEEEE;
    color: #333;
    padding: 10px;
    text-shadow: 1px 1px 1px #fff;
}
</style>

		   <script type="text/javascript">
window.onload = function () {
	var Row1 = document.getElementById("f1");
	var Row2 = document.getElementById("f2");
	var Row3 = document.getElementById("f3");
	var Row4 = document.getElementById("f4");
	var Row5 = document.getElementById("f5");
	var Row6 = document.getElementById("f6");
	var Row7 = document.getElementById("f7");
	var Row8 = document.getElementById("f8");
	var Row9 = document.getElementById("f9");
	var Row10 = document.getElementById("f10");
	var Row11 = document.getElementById("f11");
	var Row12 = document.getElementById("f12");
	var Row13 = document.getElementById("f13");
	var Row14 = document.getElementById("f14");
	
	var Cells1 = Row1.getElementsByTagName("td");
	var Cells2 = Row2.getElementsByTagName("td");
	var Cells3 = Row3.getElementsByTagName("td");
	var Cells4 = Row4.getElementsByTagName("td");
	var Cells5 = Row5.getElementsByTagName("td");
	var Cells6 = Row6.getElementsByTagName("td");
	var Cells7 = Row7.getElementsByTagName("td");
	var Cells8 = Row8.getElementsByTagName("td");
	var Cells9 = Row9.getElementsByTagName("td");
	var Cells10 = Row10.getElementsByTagName("td");
	var Cells11 = Row11.getElementsByTagName("td");
	var Cells12 = Row12.getElementsByTagName("td");
	var Cells13 = Row13.getElementsByTagName("td");
	var Cells14 = Row14.getElementsByTagName("td");
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme2",
		title:{
			text: "Pie Chart according to Food"
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			toolTipContent: "{y} - #percent %",
			yValueFormatString: "#0.#,,. Million",
			legendText: "{indexLabel}",
			dataPoints: [
				
				{  y: Cells1[1].innerText, indexLabel: Cells1[0].innerText },
				{  y: Cells2[1].innerText, indexLabel: Cells2[0].innerText },
				{  y: Cells3[1].innerText, indexLabel: Cells3[0].innerText },
				{  y: Cells4[1].innerText, indexLabel: Cells4[0].innerText },
				{  y: Cells5[1].innerText, indexLabel: Cells5[0].innerText },
				{  y: Cells6[1].innerText, indexLabel: Cells6[0].innerText },
				{  y: Cells7[1].innerText, indexLabel: Cells7[0].innerText },
				{  y: Cells8[1].innerText, indexLabel: Cells8[0].innerText },
				{  y: Cells9[1].innerText, indexLabel: Cells9[0].innerText },
				{  y: Cells10[1].innerText, indexLabel: Cells10[0].innerText },
				{  y: Cells11[1].innerText, indexLabel: Cells11[0].innerText },
				{  y: Cells12[1].innerText, indexLabel: Cells12[0].innerText },
				{  y: Cells13[1].innerText, indexLabel: Cells13[0].innerText },
				{  y: Cells14[1].innerText, indexLabel: Cells14[0].innerText }
				
				
				
				
			]
		}
		]
	});
	chart.render();
	chart={};
	var chart1 = new CanvasJS.Chart("chartContainer1", {
				title: {
					text: "Bar chart according to Food"
				},
				data: [{
					type: "column",
					dataPoints: [
				{  y: 97, label:  Cells5[0].innerText },
				{  y: 190, label:  Cells1[0].innerText },
				{  y: 176, label:  Cells2[0].innerText },
				{  y: 46, label:  Cells11[0].innerText },
				{  y: 34, label:  Cells12[0].innerText },
				{  y: 145, label:  Cells4[0].innerText },
				{  y: 91, label:  Cells6[0].innerText },
				{  y: 89, label:  Cells7[0].innerText },
				{  y: 68, label:  Cells8[0].innerText },
				{  y: 58, label:  Cells9[0].innerText },
				{  y: 55, label:  Cells10[0].innerText },
				{  y: 175, label:  Cells3[0].innerText },
				{  y: 46, label:  Cells11[0].innerText },
				{  y: 34, label:  Cells12[0].innerText },
				{  y: 28, label:  Cells13[0].innerText },
				{  y: 22, label:  Cells14[0].innerText }
						
					]
				}]
			});
			chart1.render();
			chart1={};
	
}
</script>
			
	<script src="canvasjs.min.js"></script>
           <head>
          
           </head>
           <body>
           <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR6NN5lqdvZvCHVG14Y2awm_w-Xup-fic9BHjo8GramVr17kBlH">
           <img src="data:image/jpeg;base64,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">
           <img src="data:image/jpeg;base64,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">
           <img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRoXeKeLTsDfS1aw_0m0rsdTeW6MWqFmfjc8bXg_1sLuM6yy7vZ-kzuqaq9">
           <img src="data:image/jpeg;base64,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">
           
          
           <h2>The hotel rankings according to Food:</h2>
		    <div style="width: 100%; overflow: hidden;">
    <div style="width: 600px; float: left;"> 
           <table class="zui-table">
		   <thead>
        <tr>
            <th>Hotel Name</th>
            <th>Sentiment Score</th>
        </tr>
		</thead>
		<tbody>
           <tr id="f1">
            <td>""" + str(l1[0])+"""</td>
            <td>""" + str(l1[1])+ """</td>
           </tr>
           <tr id="f2">
            <td>""" + str(l2[0])+"""</td>
            <td>""" + str(l2[1])+ """</td>
           </tr>
            <tr id="f3">
            <td>""" + str(l3[0])+"""</td>
            <td>""" + str(l3[1])+ """</td>
           </tr>
            <tr id="f4">
            <td>""" + str(l4[0])+"""</td>
            <td>""" + str(l4[1])+ """</td>
           </tr>
            <tr id="f5">
            <td>""" + str(l5[0])+"""</td>
            <td>""" + str(l5[1])+ """</td>
           </tr>
            <tr id="f6">
            <td>""" + str(l6[0])+"""</td>
            <td>""" + str(l6[1])+ """</td>
           </tr>
            <tr id="f7">
            <td>""" + str(l7[0])+"""</td>
            <td>""" + str(l7[1])+ """</td>
           </tr>
            <tr id="f8">
            <td>""" + str(l8[0])+"""</td>
            <td>""" + str(l8[1])+ """</td>
           </tr>
            <tr id="f9">
            <td>""" + str(l9[0])+"""</td>
            <td>""" + str(l9[1])+ """</td>
           </tr>
            <tr id="f10">
            <td>""" + str(l10[0])+"""</td>
            <td>""" + str(l10[1])+ """</td>
           </tr>
            <tr id="f11">
            <td>""" + str(l11[0])+"""</td>
            <td>""" + str(l11[1])+ """</td>
           </tr>
            <tr id="f12">
            <td>""" + str(l12[0])+"""</td>
            <td>""" + str(l12[1])+ """</td>
           </tr>
            <tr id="f13">
            <td>""" + str(l13[0])+"""</td>
            <td>""" + str(l13[1])+ """</td>
           </tr>
            <tr id="f14">
            <td>""" + str(l14[0])+"""</td>
            <td>""" + str(l14[1])+ """</td>
           </tr>
		   </tbody>
           </table>
		   </div>
    <div id="chartContainer"  style="margin-left: 0px; height: 600px; width: 55%;"> Right </div>
</div>
		   <!-- <div id="chartContainer" style="height: 400px; width: 200px;"></div> -->
		   <br>
		   <div id="chartContainer1" style="height: 400px; width: 100%;"></div>
           </body>
             <a href="http://localhost/detail2.html"><h3>CHECK OUT ALL THE HOTELS !!!</h3></a>
           </html>"""
                    
    elif asp == 'Room':
        a=RoomRet()
        l1=list(a[0])
        l2=list(a[1])
        l3=list(a[2])
        l4=list(a[3])
        l5=list(a[4])
        l6=list(a[5])
        l7=list(a[6])
        l8=list(a[7])
        l9=list(a[8])
        l10=list(a[9])
        l11=list(a[10])
        l12=list(a[11])
        l13=list(a[12])
        l14=list(a[13])
        print """
		<!-- ====================================================
	header section -->
	<header class="top-header">
		<div class="container">
			<div class="row">
				<div class="col-xs-5 header-logo">
					<br>
					<a href="index.html"><img src="Logo.png" alt="" class="img-responsive logo"></a>
				</div>

				<div class="col-md-7">
					<nav class="navbar navbar-default">
					  <div class="container-fluid nav-bar">
					    <!-- Brand and toggle get grouped for better mobile display -->
					    <div class="navbar-header">
					     <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					        <!-- <span class="sr-only">Toggle navigation</span> -->
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					      </button>
					    </div>

					    <!-- Collect the nav links, forms, and other content for toggling -->
					    <!-- <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					      
					     <ul class="nav navbar-nav navbar-right">
					        <li><a class="menu active" href="#home" >Home</a></li>
					        <li><a class="menu" href="#about">about us</a></li>
					        <li><a class="menu" href="#service">our services </a></li>
					        <li><a class="menu" href="#team">our team</a></li>
					        <li><a class="menu" href="#contact"> contact us</a></li>
					      </ul>
					    </div><!-- /navbar-collapse -->
					  </div><!-- / .container-fluid -->
					</nav>
				</div>
			</div>
		</div>
	</header> <!-- end of header area -->
		   <style>
		   .zui-table {
    border: solid 1px #DDEEEE;
    border-collapse: collapse;
    border-spacing: 0;
    font: normal 19px Arial, sans-serif;
}
.zui-table thead th {
    background-color: #DDEFEF;
    border: solid 1px #DDEEEE;
    color: #336B6B;
    padding: 10px;
    text-align: left;
    text-shadow: 1px 1px 1px #fff;
}
.zui-table tbody td {
    border: solid 1px #DDEEEE;
    color: #333;
    padding: 10px;
    text-shadow: 1px 1px 1px #fff;
}
</style>

		   <script type="text/javascript">
window.onload = function () {
	var Row1 = document.getElementById("f1");
	var Row2 = document.getElementById("f2");
	var Row3 = document.getElementById("f3");
	var Row4 = document.getElementById("f4");
	var Row5 = document.getElementById("f5");
	var Row6 = document.getElementById("f6");
	var Row7 = document.getElementById("f7");
	var Row8 = document.getElementById("f8");
	var Row9 = document.getElementById("f9");
	var Row10 = document.getElementById("f10");
	var Row11 = document.getElementById("f11");
	var Row12 = document.getElementById("f12");
	var Row13 = document.getElementById("f13");
	var Row14 = document.getElementById("f14");
	
	var Cells1 = Row1.getElementsByTagName("td");
	var Cells2 = Row2.getElementsByTagName("td");
	var Cells3 = Row3.getElementsByTagName("td");
	var Cells4 = Row4.getElementsByTagName("td");
	var Cells5 = Row5.getElementsByTagName("td");
	var Cells6 = Row6.getElementsByTagName("td");
	var Cells7 = Row7.getElementsByTagName("td");
	var Cells8 = Row8.getElementsByTagName("td");
	var Cells9 = Row9.getElementsByTagName("td");
	var Cells10 = Row10.getElementsByTagName("td");
	var Cells11 = Row11.getElementsByTagName("td");
	var Cells12 = Row12.getElementsByTagName("td");
	var Cells13 = Row13.getElementsByTagName("td");
	var Cells14 = Row14.getElementsByTagName("td");
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme2",
		title:{
			text: "Pie Chart according to Overall Rating"
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			toolTipContent: "{y} - #percent %",
			yValueFormatString: "#0.#,,. Million",
			legendText: "{indexLabel}",
			dataPoints: [
				
				{  y: Cells1[1].innerText, indexLabel: Cells1[0].innerText },
				{  y: Cells2[1].innerText, indexLabel: Cells2[0].innerText },
				{  y: Cells3[1].innerText, indexLabel: Cells3[0].innerText },
				{  y: Cells4[1].innerText, indexLabel: Cells4[0].innerText },
				{  y: Cells5[1].innerText, indexLabel: Cells5[0].innerText },
				{  y: Cells6[1].innerText, indexLabel: Cells6[0].innerText },
				{  y: Cells7[1].innerText, indexLabel: Cells7[0].innerText },
				{  y: Cells8[1].innerText, indexLabel: Cells8[0].innerText },
				{  y: Cells9[1].innerText, indexLabel: Cells9[0].innerText },
				{  y: Cells10[1].innerText, indexLabel: Cells10[0].innerText },
				{  y: Cells11[1].innerText, indexLabel: Cells11[0].innerText },
				{  y: Cells12[1].innerText, indexLabel: Cells12[0].innerText },
				{  y: Cells13[1].innerText, indexLabel: Cells13[0].innerText },
				{  y: Cells14[1].innerText, indexLabel: Cells14[0].innerText }
				
				
				
				
			]
		}
		]
	});
	chart.render();
	chart={};
	var chart1 = new CanvasJS.Chart("chartContainer1", {
				title: {
					text: "Bar chart according to Overall Rating"
				},
				data: [{
					type: "column",
					dataPoints: [
					{  y: 353, label:  Cells5[0].innerText },
				{  y: 133, label:  Cells10[0].innerText },
				{  y: 402, label:  Cells3[0].innerText },
				{  y: 621, label:  Cells1[0].innerText },
				{  y: 359, label:  Cells4[0].innerText },
				{  y: 259, label:  Cells6[0].innerText },
				{  y: 193, label:  Cells7[0].innerText },
				{  y: 67, label:  Cells13[0].innerText },
				{  y: 177, label:  Cells8[0].innerText },
				{  y: 422, label:  Cells2[0].innerText },
				{  y: 131, label:  Cells11[0].innerText },
				{  y: 422, label:  Cells12[0].innerText },
				{  y: 174, label:  Cells9[0].innerText },
				{  y: 68, label:  Cells12[0].innerText },
				{  y: 54, label:  Cells14[0].innerText }
						
						
					]
				}]
			});
			chart1.render();
			chart1={};
	
}
</script>
			
	<script src="canvasjs.min.js"></script>
           <head>
          
           </head>
           <body>
           <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR6NN5lqdvZvCHVG14Y2awm_w-Xup-fic9BHjo8GramVr17kBlH">
           <img src="data:image/jpeg;base64,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">
           <img src="data:image/jpeg;base64,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">
           <img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcRoXeKeLTsDfS1aw_0m0rsdTeW6MWqFmfjc8bXg_1sLuM6yy7vZ-kzuqaq9">
           <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBhQSERQUExQWFRUVGB0XFxgXGBkcGBwYGBgYHRgXFx0XHCYeGBwkHBcXHy8gIycpLC0sFh4xNTAqNScrLCkBCQoKDgwOGg8PGjUkHyQsLSwsLCwsLC4sLCwsLyksLCwsKSosKiksLCwsKiwsLCwpKSksLCwsLCwsLCwsLCwsLP/AABEIALsBDgMBIgACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAAFBgMEBwIBAAj/xABFEAACAQIEAwUFBgQDBwMFAAABAhEDIQAEEjEFQVEGEyJhcQcygZGhI0KxwdHwFFJi4TNyghZDkqLC0vE0U7IVJGODw//EABoBAAIDAQEAAAAAAAAAAAAAAAMEAQIFAAb/xAAxEQACAQMDAQYFAwUBAAAAAAABAgADESEEEjFBEyJRYXHwMoGRocEUsdEFI0Lh8VL/2gAMAwEAAhEDEQA/AND1Y+DY8xycdCTvVj7ViPXjoNjp07nH045nHwbHTp2Dj3MVS5BYyRb99fjjjH2KmxnDE81x6fh648qNP5YjzAMHT73K8CfOxtgTl83VApmoEGsSwVjKggmbiALQenlgT1FXDQgUnIklPtKheokVNVL3iabBSL8yPIn4Tgjls6lUBgZXy3+M7YB5HjFN8xoDL4wx8JsxTRABPvEKSYBIgHocWclTo0a1WWKl2pqBJ3YWAAsBNpjAlZrjdwZY7Te0N6p2gDoPz649ZPd9fyOJEp47NPb1/I4ZtAXnmnHLLifRjlkxNpF5VZccxidhjkUSdhiNsm8jFYjENSoTi+mQPM4mXKqOWK9nO3iBhlmbE9PhfU4J6YxRzfG6NPdwT0W5+mJ2IvM4MzcTtMio5YkFIYWOJ9uwk93TJP8AUfyH64DZni+drLOo0weSCPrgbaimkIunqNzHrNZ2nSEu6r6n8t8Luf8AaJlkkIWqn+kW+eEPOZQydbFjzkzf8MVgVUiAPj+4wq2sZvhja6ID4jHE9ta9adAWkvpLfW2KhzjOw7x2c7wTP02wqZzMnWLmOk2+WDHD63i9RhSo7tkmOJSRQbCMmZ48DpVacDbcAD0gYpcXrFPdMW+Pz3xVzLCxxR49xBRBLiI64lneoMmVRFQ4kuXqzcmcUs+d8Cf9sKNMbk+mKT9oK9f/AAcuxB2JBj5m2IWg972xDNXp8X+kuJvg3w07zgDlOzGdqwalWjl1O5Zrgf6bfXBzI8N4Vlv/AFXE3qObRSWw+jfji7Kr90G58s/fiDWtt5BjlleMVlA1EP6gA/MRi8nHQfeUj0v+mKfdDHopiMMCq46xU00PSX04kjbMPQ2/HFha+BH8OuPBlo2JH0xf9Qesp2K9IcFXHYqYArUqDmD6/wBse1OLlYlTe1oP6YsNQOsg0D0h7vIx89WN7eQ97+3xwFTiwPVfXf58vhi7QrDkRiwrBuINqZXmUu0vH/4fuRpM1WIABjYoPG0zHiFgLxywHNaK1MsxqNSzD95TSFQIEcKdMxOvQZYkiDFhgt2g4Ec01DYhNZMmLnRHQfdO5HLAftTw+rlcm70iqMtl0gNp94z4hpEnTssibMZwRQCb2z794gmNhFXtVnHyBy1cXYPVZYJHvUtIgxsC3Kx2wuZDthma+apAuUQ16Z0r070QC0ajy5wYBi2JeF9ic1nX1sKtZju7kx8XffGhdn/Y2tNketUgqwYJTFpUyJJ8xg3ZAnc3MB2lsLxNMURIgX8r/DpjrRt6/kcdAYlCbeuLWkXny08eNRxbVdvPHZyvwxE6DtAGPGrAbwMWa2QY+7HqT+mKGZya071HHyAHzN8XA85Uk+E7TOAzpkxvH98QZjiGkGwHmx/K2Br8WoqxCODIuFM7dY9frgbW4hqJhficKVtQim18xulRZhe0irZurV/xG+Vh8sd0+G04lpb4wPpf6jAjiXExTnW6qPMgYqZTt1lACrVdTDYKCxPkABc4T3lzxGrbRGzI5mjScRTpjl7oJ+Zk/XHfHUldS3GEurxfMV2By2TqkT71WKS+vjgxhhyArKh/jMzlaIP3UYuw+gv8TheqpsQPx+YZLXBvFHjLGSTbCvnc+qtJYfPDnxjL8OdjL5nMHoBoQ/E3+uBtPhuWsaeUpr51CXb1ltWKoQg734jLXf4PzFHNcdVjFNWqEfygnE9PieceBTpBI5m5+W/0w9Cmke4nxE/Q+H6Yir5mLAwOggD5LGJ/ULwF+sj9O55b6ROfgWcqx31dgOgt+On8MWKPY2iP8RnqerGPpH44N1KwxwlcE/3xY136Y9JZdLTHOfWQ0OF0qQ+yoJq2Ba3r4oZtseVkzDC9RUA/9tL+k1C30AwRo3/HEw0ncjATUN7nP3hTSHAx6Y/aKtfhIb3y9Q/1MSPkIX6YjTKquyqo8gBi9xjPokjX9cL1fiQPI/LDaB2EScIhm3xj7TbHsY7VcdiCkarjopizTyhOJjkDiBaTKGIs0gOn1/6Ti69AjltipnXChWYhVBkk7ABWknHGdIs09OmheowRRuTthUq+0rIq0Dvj/UKcD6sG+mKvbXtZS7xVVtdOmrB9BB+0dYUzN9IJ+fW+MvrZViAwVtLSVmbxvpJ94Dyv1wxSoAi5gHqkcTf+CcdTMJroVdQFiCCCD0INxgsucLDS6hgdwbg/A4/PfZjjL5WulZDDTBE2dT7ysOlhfkQMfoAZwaFqKkhgGHOxEjpjncUPiM4KaowIWoZ0GBEeUfpi4uYXmcK2W44rMQwJ6CYHxAxOeK6TNgOnL64C39VpJixJk/oHPlGdM4uPG4hcASJMbc+XnhcTtDSNgwLH7q3PyGIOJ16unUaZQC4eowpwRz8ZBxK/1Ldws46G3JjpxGnAV3JOiWEWAIi4Hz3JwFzfbBV/ViAMJFfi9fMAj+LDDb7PXVFuRKgKPU4X69PJgt/EZlngxHfLB6wMuajj4qMGWrUYkqth5yvZU1Fma58o8532phDHeIB5b/M4F5mlUzv2iCtWU/zA6fgT4flgFlO2fDcqZoZUu8e/oEz/AJ6hVvnTx5nfbTWZdKUAOheqzAf6aa0wficDqUGqG7NCJVWn8CS83Z/N0WkGjQHWq+1jvp/dxitnMoaf/qeIVjaQuXy5SfRqkhh8MUuzPFM7xXN9wldMsSjOz06SyFSLb6zdh94b4O532J5tizfx61W5GolQT0BOttI9J3wRdOALgX9ZVq5Y2Jt6RTfP5AGRlKtdx97MVZB8yq+H6DF7I9q3Xw0aVCgvIJTH47H5YUcxSejWqUnEtTdkaJI1KxBgxcSDi/kFqEjTSY4HULAWhaaqTe0czxGpUHjdj8YHyWBgXWYTYDEVTL5qToolF5d4wJ+MBR9McjgeZb3qqJ6DCOAblvvNG4t3VnaNghw+kXYKvvHYSB+NsVKfZX+evUPoIGCGQ7J5d2jSah82J+YxR6lO3P2ll3DpIc/xSlSlWdQRYiRv8MBsxxhT7qs3opxov+xtFE8CIp6aRHzF/pgNxKk1H/dmOqhY+YnAqdZL2A+pnbi/BjF7Ouz9N8itavRVmquzAOoJVUYqkTtMFv8AUMNVfLUSNL0qbKNgUWB9Me8HTTlKANj3ak+pUE/UnEWZfHoqdNRTBt0mA9RmqHPWZ52+4AqFBla1TLipqNRFY6GAiLGYuTbbywlP2e/mrVm9CQPocafxrhyVq2p3YBVChVtzJPxM/TALiHZuiw8LsDt4rj6xjDqatVqFRgA9BNilTBQFsn5xJHC8un3QT1Zh9Rvjivm6NMWRT/lH/cMXOJ8CakZ3HUbfrgLVoyPjGGkIfN7yrXXAFpsqqT0/DFukY5fX9YxArY7D4CTeBtLgr+R/H8MTJmPPFKnUxYVCccCROIkpqA9MLHtEy05GpBKxeQJ6/mRhqWgvMA4QPa52ip0aKUFK62OtkEyVX3djYF4N7EUyMFplmYAQbWAzMWzq6AE57t5t0+A5eeNQ4bwdc1wyiHUMe7ApjaGWIYEXBMkHrBwm8K7E5mvUVq1J0pm5LDST5RuJ640rI8MeglOnSVmVRsOU/qbdSYAnDOoqDAU5hNHRN2ZsA4zAuW9l1HvFDGpBKhtLLIvdgHUhrwIJAufTGg06VRaa00onSihRLLsBA2MYk4BkWYa6ikdAwZTqB3MiYFrbTMzaGBF6DGdqN1WwJhXKU2O0TPOL8LdYqFa1PqaYpkX8yTH/AA4i4F2Y/jKjKHYaVDFqparPiAI0KUQGJvHwxoGbYAXFjiLs1lKVF6r2XUAIPkTt88D0w/uBGkVKh7MsOZnXtL4bX4XRSrl804RnFNkCohkqSCppqD90gg9cZdxDtHVqgaqjM3VjP441f2+8RR8tlkRlYtWZrEH3EIO3+cfPGJFLY26dJALgCZ7VHPMc+x/E6ldylQhgokeEA/TBfM5FGHiUH4X+e+Avs8o/aVD5fkcNVXLYQ1B21TaaOnG6n3sxbzfBE+6Sp+Y+t/rgInD95n0Nh8Y26E8rnbDlmKeF9BC/hA02kAWO3IAHyQ88FpVCRzB1aS34j77COHKM1mag3SiqA3/3jydzY/Zi3p542QtfGb+xDKRSzdT+ZqafBFZvl9r69eWNBq1IBPS+H1PcmbUH9wiYLSbvM9nH/mquRI5d5Ui+0Ry3wZybMzBR1wC7Ok1HrPpI1nV8WZibdb3O3TDXw5NIPU74wtU9mM3qIsgh1eEApBe/XlhV4jTdGgk+UGxGHVaTd3PxwBzdPXIN98ZlBmDZl1bxgTKZM1CPxOGzh+mkkL8TzOBFDLFbAYsnVOCVgz+kkkcQlmuLWwJqZjvSF5sQvzMYNZfhWpDPwxQyPBmXNUjEgOpjyBn8L4ijRuwBlC6qDaaFmgFAA2Aj5DAXM1oknYYsZvj9Az9sgjfUwWCOR1bHCvxbtHSZlo0nFR6s3QyoUbktt5ACTfoDj1daqqoSDxMKjRYtkSl3jVCW6yfnijn3IHphmyvD4XFLivC9Qx5RQ265E3hVXiKFauTabeeB9XIIykgfe/XDHU4GQbXx6vCCFA6mfw/XGioIGJRqimH1N7YmWkedseoADiUtim6L2k1GkMWYxWoP1xbRsSrAypEgzDMFYqJaDAJgE8h88KPYjhJzNetnc24epQATuzT0rTrDUdyTrKq3hYcqg5izq7Ab87YHZbKrSoZoUwoFSsXIUAX0Ug0xuTvPnhzT4JPleCcbrDzkRJZZ+9M/vywp+0DNPlqWVzNOWppmFeopgg6dQAI6gkjyaDywd4znjRy1SqL6F1fKPywi8L4v39PMUKzE0q955pVMFaidPFEjy8rl02narucdPv4/aN1MjYvJmt5DiaV6SVabSlRQynyPXz5Ri2KuED2UmqmUZajaocx1SAoKGwM6tR+dzh2p1Jwk3dcrF9uMznNVJtgZxZgKepoGmbkwL2v5X54IZrfFTO5Vq1NkRA7ESFYwLMtyfLf4YEEJqADqYQPsF/CI/aXstU4ghXLJqel4zcAEhSAmptzDEi+/xjKs5kGp6kZSrKYZWBDAjcEG4OP1nkssKdPSLndm/mb7zH1/QYx72t8HU5tKiKuqpSmoXbQgKtCMdPidiLQOSDGylMUVteJPV7ZySIB9mmUJer6D8Dhpq5S1jywp9kOPJlHY1lhH8LOhkKbwSp8Wm+4nbGjHI95HdjVIBkEQQQIM7QcZ2qB338Y5QcAWEU8zlThdXKNtG58zv67gj4kT944f87waspg0anwUt/8AGcAspkXYmj3bGodQVWUq5i4iRINpDfHbFKblbi0YIVs3jF2PlMmoFQr3lZ9RXSDIAg3u5PhlhyAHLFbj+dzFOm7pmKynSEC6tQLMdIJVgbCRMRaTNsMmT4BXy+VVakGCq6KSlmhmVQ20AqCSYBkbmwinS7NVK9YIQwprd2ZYEA3An3ido5XmNsMmjWZlIxFxWohGBzFvsLwUw7kAKQFXb7pg85C+IROG3IcGWRN5vggnZenly70mchgBoYghQu2m0gX2M4m4evT0xDUBe7jMCaxPwnEKrlBAHL92xUXgKQTA/Z84xe7+BjgZqLSRaNuk+X4Yap06fhFXZ7cweeFqJAAj0jblf93xXbJrq2+WL7ZiP3O3MH8jiJBf9/v/AMYvUVbcSqM1+ZZo0REXxDnnSn9o3urJPpF8XxlgACed/wBMDu0MGgEuGdlVYVmEk216QSFvBJsOZGKJp+ssawiJ2h7unUWmAYALO4sGaoJLahuY0jfli12VyFLT3wIZjKjoFH7n4jA7PZGk4PgGsAAkk9yl4LEKmok6lttJsFjGgcJ4ItCitP3okkxuevly+QwudIxMefWDYFEhXb0xFmYscX8xko935YFVp6xheojUzYiDVg2RKmYt+7R+ePcvS1kT0b/oxzWO/rsB/bE/DE2PkfxH6YvRa7WkVBYXkCj0+f8AbE1MmI/f4YhUY61wCemM4eUbMvID5fP+2JQx8vn/AGxSo5oMdIN7kzaAGAn4zIx1RzWoAiYIn42t9cSWAO2UGZ3xUE0X5FRqkG8KZP0kfHGfdn+NumbpUy7CnVY0mQkkS6QCZtq1Ml/LDZxTtbSoaEqBtVYMEETdRqOqYgaWQ/6sZXxOndXBIddNWb+EjxL67j6Y9N/S6N6T7hzgRepUPwjxmncVyneZWvS5tTdPjpI/HGWcKkILSTpkeRYT9CcazQ4glRg4Phqhai+lRQ354xzieVq08zXoklRTqhdKgDwEsyEECZgIfjgf9Nbazp76xqowUq/iPxNQ7A8RH2tMnxK155gqIOG9G8sJHs67NDM5d61N3WsKhC1CxZWGlTDyTO/K9sMtPitSkSlbL1da2JVGZD5qQIM4T1S3qs3nJqEO2OZezb+WLPZ9SahbkFj5kfocUk4qHUn+GqkW/wB2/PbYTjjMdoVoL/g1U1CRB8rHf6HAkARwxi7IzgqvPqI05mrAgYRe3HAKldqL06T1ANS1NLIpEaSpBqkLN3HQkjpY3leIVqy03FI6nHhMjSORLAwQPPyws+0PimZydGlWpdzpZ+7qAqZDkFl0DUJWAwPO3rD7OaimwigphCM5gdOBZVKhR6GZeqQYlAQoYABSEJSpvdl1rY3EQC3BuErlBS0vWZqVM00LMICszEEoAAWAbSCZgDFXsN2ur5o1RV0QgGnQGW51b+I9Bg1Uqlh4mJi9zYfPYYyarsndB9/iPImbtJKXEKhgavFsSASdt4Nz5nHWQy2ZSjIqmqAzyahAf323mFjpfaMUc1lysNOm4hpvO4iOeBXFu1FUgUcw0CZ9zSW6Fo97bVsPzxSlsKsrg3hC13G0jz9/7jn2f4vU1slSYIlTusj3hqUkTBBieWDAzoNr+t4xn/YjiyHMtQkDvRK2I+0AYiDzOhXk89I6Yd83wRGKMS/hkQHIBMqRqjcgr9SOeNjRrekM/WZ+rIFXj6SV3mYIOK+TA0ziqeJ0lbT3oBmNLtBkGLSb+mJMlnlaSoJEkSIjVzCzvitVwbFc+k5EIvfFpcJMjHBSSZx2lQnZGPoJ/PHNaoYkU6h8tDdflgS3GSDJJB4MgZb8/h/fE2XSWA5fucQh5g+ID/K31kfCMWOG1FZxpM79ehxfeCQJTbYEwpXEjFV88iGmGYK1RtCA/eYKWKj4Kx+GJswCDtiN8wqFQzBTUbSgJ95tLNpHU6VYx0U40YlaRVKFGgHqkU6SgS7wqCBJlm6SSb9Tj1Kz2LIAsTIeflYYs1UsdURznb44qZuiutPAk3JJW4AHI9dRX4TirKeby6tPqjfEm9vwwCzT+Iz5z88HqqwPX8cCMxlVJmfr+UYy9e1gI7p4NLWNtvzm2O6D6QB0GJamWEe9v5jltiNCBY/PGdTrqDGmS4lQV8T02wA4lxE0qZZRLWgfS/lzxT4b2nD2apojytzmf5YjrgC03YXURg2GCYfqVdNUBidIj1gjSI/5B/pwIrca8OhDGlCLiN2+7AuZk/HBEkvDKxI02YKTMzp06RMg+LaLYXOI068ksNAINiDJ1y0S0Qdf0G18FXT3IZhg/jynLUUY8JNmeJA5d9SatTMUdve0KTT0i1rU258x5YT+K0iVJ1QWG1o6xtNhoHzwYpVG7tEcaQNTP4tQhgrNE7X6Wlh1OBfFHYm8SZaNok2HrEY9no6IpUACOfY+0z3O43jT7PuJirlhSeO9y4AYc2ot7jD/ACnwnpC9cee0DJMlSjmqYB1juKsmBI8VJjAP9az5rjP8nnamXzK1admAuJ95IgqZ5Hz5wca5ka1PO5XTPgqrY8wd1YdGVgD6jGTqB+nrioODGtOxdLXyv7QN2Ez75TLKFeoEqMX8BSBIFvGYn1GDdLtMnesatbM1iBZCKELMkkCgAWsLzIg4C8L7KZp6RRnHhVtSKR4WQ3FoJVhDA/1RywKo8P8A4eqrMstIUtqnwsQDCk+Lb0+eE2plmN+sXqGnfHpH2p29pKog6ZsGdSpJg7M1iY+UYiyXGhUYKTRambXqJNzMRERIBwl8SFRj3NOgQWqd7TAUsdTypPinRPhuY2ubYr0Wpd8WZG0orBzpUwVBHMge8ByOLdmOLH6web33Wm0msQAEanpAA06psOkYzL2w5Z6q5d+8YgMyinbQIVZcefK/8x64zzijtSq1HDVKQIXToZgBJPgMe6fDMCOlsTZLi+cIKU8w+mxAq6SYkXOpTN9sOFiFxB00G7xj97O+ztWnRqVnhEqhdEeJo8Xi0jlfr8MN+RXUWYLFJfAWcS5gclgCDNzeIOMq4X2vzSFUp1v8RlnVTEqrQQzCkyi0sDbli1xvtrUpJSZ9FXUqkmlWqU4JE+6S3h3ExePgMurRqu/TPvr/ADHRVUA39/vNdoKqKLSsWBC6R/SAOQFha0Hqcd5esxLMrKJmZHpEfu9sY/lu1tKoSr5erUaCzBmR4VT1cqZ8JMTy6YKp214eaIXxUTJXSE1OYjcBmEGSJDbqcUOmqXAPT30Jgg4PNs++to+ZjK0qjJXCL3lMnQRvqU7EgCWEc9pPXHFPiC1EVkYgsx1r7ul5k25Nqm+/iwq5PtBkqNOFrlC3iOtWSLkSytC36GJ8JAiDj3O8Zo1llCMwARelUCuCLi+sFthYmPKMRUpVhm+PC+R9bS6Oobi8JZzhhYB6bEMWAUyfEGYTNmOoG/r5YM8G4a1NQaphpLFggVBNreKT4T/ltsMLvCadVg2hq6iQwFRUZgSwtTNLlO4MiPLEnFs6Qg0IyN1qJVdQTGw1C+/PpvgNNipuRnxjFSotS/n9f3jzluJoTFPU5vf7tiRZvdJkH5YuVc9rpLfSZW6k2GoTcRynGQ5zMPWVRWzNZFJEhE7tHbzA1OV38Pu+WHng+aUUlGqQPKBtYQw5W+WNSlqXN92cTMqUh/iLesI5127xNFT7OKha0AlzIjkTJJt0xzw7MaX3WAV0qu4B3n1M/PATiqKyTLMZsFvPoARAjlinwTiopFoZQ7bB9h1bqbW3jy3woddUY4Nh6RpNGpp35P29Sf8AULcf4xmwzKtNr6tLKDYSYPhmCBG/nYY84L2pRUCOGLIYfSphBeHedh8+uOV49miG8KShN7kNG8AGZHxmdusI7ZQAxpBO83DeFyotJ6ReJ38pgWXUHduDRvsAydnsBt4NGDOZulVRkqJ3lNrFWQMGvsReRYGYxwvaKh3gS6u1gWUqD5LOFZuL1mnukB8RCkSZAYjUYjTIEx54K5ao+lVqrqLGStzcGZsZF78+Xpjl11YmzED3xFH0aUxc5+f3l/iWcLeFJk9OXmcA+0NWrT0lDpBH8qn8RgZ2s7UHJ1FanTq1VfVOkNKlNNvcMi5uSNud8Asx7UEqxqFWkNpbRE/FxgdXta1nAxJpbFNoy5R3YAsQfOFH4DEueraY0sD8Z/A4D1s53iCrScOhEWglT0bcTz8/rgtlMnT0hnGosAb7CbwOfzOM2oTS7zH5CNLZjYCA81LQoEk4X+0fAhla1MgD7WmSwFhrlgTbn4lPqMP3COHaYdrn8MB/aLSGnLv0Zk/4ln/pwTT6r++Ka8Zv9IfYrEAxb4fxitSBGpipUiFaAZ5keu/piehx9K7AVPCFO4jUAeYUxJgbW3wOFS2GXK5ei/DWd1XWhYB4GoEtIE77MB/4xsDaWVWHJA+srqNOKS76Z+UWeIZwwdPNpXVeBuoMHrp+WBGazDiWYgyQLSPXribM58atOloJ3gRPlB2hefQ4o5jM6hBGnciZuAd4j9zj1VQjgTKBwZWzVca7hoAKki87fGL9MN3YrjVKhUWgtQMr3W8w29vUfX1wsrR+8L6jqn4YjRe5WnVAW0KSZt70kRfVHrscIamn2iWMPQYoxNvX0mz8S4a1Qd5SqLSqA021tUZF+zYWOkGdSkqQRe2FkJmKjlqdYNRVm/wwjUmMnRoaAWAUiYNz6YbuH00akFdQyuBKsAQZE3B3HlhY7afxNXMBe6VqIBWkaVR6UWBKVBTaCRuLCxtzxk0KimwccQOt0zjd2Jtfr4TrLZevlqdRqlQ1RSGqkh7xQ2lWZFf3QWDDSLt70xiyucydVBmUoaKoXU4Y1FOqxPdrI1eKSDIvjngXFdQ/h+I5+jRoKgVMuFs6GPfrVfeO6kSd5tbHDceorWIqrlqdDUwNUZoFjT6qiDU0gSF5YN3CLWxEyKo45HN/fX7QXxvKrmaGTWDq7oOVJBDMV95y16l2Zp3nVbAKtwQrTlWHfHYCwSRO596GAUGL/TDpW7GUczUp5rLGqMpTpkqz6qQck20+63d6SblQDYSRiI9hnzBJoVFYRKwwJDSORMEf6uZ+KxuHC3844tQbb29mIlGjrdgjqKh7tSt7qCwNxEHxLttvzxN/9JWorK1mCOpM6lD0HCsGi5lHpsII0lAbjVhvyXY/MfxDE0X1g6WsmxMyDN1ItJEnriHifZ2tlqNYqNIcanUnTJ0kWKg3YxaxkemLbrWlCwZiIhNNB0JLEA6ZAAYldIZVkGwBU2/9w4qcSSKraUKGxB1EjTeSJix8Jmec3m3eUzhejWViENM6xIJEFiGXexlt7zt0wXr8RStCtSimEVE0uSVCKFQ7GWg35G4wwSQcwYsRid8P4jFahULMy+GpqAIOlW7uodP3o0kxfD9nhSDx/DUDSBRXUqjaDLhXUMoBBJiLzEHC12Gy1SnmcujCUrM/dFlYFWKTVVGiFBQEsDv4CAN8WM6r0+610mV2v3a6tCwx1eIhtKAopg/zDrBDUB5WFpkf5Qxw6jQQLmkJQlWVqdENT0hoRtSOVAYBxNz7wYC4K237N6qlJ0zOZp5Y0y7E1dVQbkMRUDwLiekHa2KnAO09RFdatL7JgBBksVKuoamYi8TJkkEY77Q8d7ulSehRaotTUKa+EeHSKdVKhVvdMHxAyGUfEd7mx9/iX2m14mJxzNmpTQV0fUdKkqjrrvA1IeYAuBzvEY4p+0nMhFMU2LTycEgcgNRE/wDcMWsxlWqPWrd0uxqaO+C1QEpmI0A6iNTLIANxvEmtXypzNPwmmhB8GkGVNjDAjoV2288WHZqePn/yTtd8Xz4Z/Mu0PaHV0yqAm06HU9ZkWgbY8p+0WrTcGpR0qSAWemCIPUi/yv64VKvG2RKlO61NSnaACsiosAwRMkHzPlht4BnTnctUVqSB8ugqCnA+3V2YblCVAaLkkQ3IXxL6dTkrcesGtXpex9IRT2qpoIqUmE7MSygxAkQp0kT1O4x3le1FDatpJMm9VtRWbbFTz2I+WFfM8XKqEqoq3ujUz4GMr1NioggmDAYec+XVaoZszQNXu0hm8IZZYhNR3NgxsJki43C/6WkouFt8/wDkMtR7bQ3Me8r2opz4EAUixs3OTEn898Ff4ymxlXPiu2tSJ8p/vjF24RobSVYNuNJ8hqAg3PiWwx3lczVpk6a9ZADeeW8++Tt6Dl64ldKi5Fj6j/cgknB/f+Zt9WQJUqw2sOnof3OAeZ3uAfX8wf1xmmW7WZvbv5idOpVjyuI+tpxIvbauAy1SHs1wAIMHR0tr3ubbcsRV0zucWl6dVUGY6tmHUk0wFkX0xt8PXFzJ9oECgVVYEfeWCDP9JiOW2MxTt9UBkoI6Bt/WQZGC2a7YZZyrIlXxKGZVUMEc+8gupgEWN7EegG2jb/Jb+/rJ/UIeDaa6hwB7epOTLfyVEb5tpP0bBoPgL2qpCpTSmxYK7EGDHpPWDFsed0wtWU+cfJmdjM29N8FMvxdBkqylo+1V/KNMH5FR88Q1uzRpP7ureGHMenWPz2wD7TStIAbEwSNpAsDj2GlZGqqR6/SBr1HNM3k9GGLyR4VH/MWH4YrcRiGafcpsJ82AgeuOcro7x1FyRPhPRZ3HngRnLEGTLG4PTlvjfqNiZl7LLrUgVe5B94Rbdf1xS4rRFMQDqDAG94MKSfKbj545zYICeI6oHyxFn6EBIMyI3m46fPbCtQ3Eo3wnE0HgHaiaUljIo1GEyYde6RY+LE4n412h7vP5uNTy6rpV5Hgpr/u9QJuDcA9LYQ+F5IsrgMVLDSfNTBj5gfLHo4ZXoP3oLal8auhJ8QPPmLTvjL7KnuOYy9eoyg2mqcN4NSzNHvqrBgzBaYBWG21RUggEhiINxHLbFup7P6OpamnQCwW9OmpCmYhiTJsFB+nLCBkvae5AXM0Vqf8A5aTGhW35tT8L8rMt4vgxlvaEZ1UMwPdA7uuoptC7DWmqif8AhU35Yv8Apwo7sV7cscxi7QVeIUS9LL1EqZfSFSg1LVTRAAAC6qCu3O2+22BHCuLZnLvTaqVoUNX2q5WkFrMgmQpaSBO8QYBi8YsP7STpmrRgAx3ugEAgSSpUaQ0Xgi/oYxSzOYFTUwzMPOx/wyTfemCiifDBHOMLtVqobdIZaNN89ZpGT7b5BEX+FzOXg+8taqy1CTzbvZctO+rFHivtJ4eqOuZqU67vKillg9RiDA0a4ABPqPphGHDVJXvKQzAYmGpTE+ikDnzx3VqU6NTu6KqjqRoMGQwJgL3guQVHi+9eOWJOqUi23378oMaMht24+/fjLXB/Zt3lN62Yy1WmalQvTpmAwQgka7i8MBDQTBPPBDiXs+y1Wi6rljQbT4HpjxSCPeWnJZSoNr/Axj7Me0XMVKZo5rJ9+ht32Wq6NfRkBEzzOloE4q8L7XLRRq2XyecrFeVbMiwG5AAMxt1kxixQX3ip8ukm5+EpKfDM1WyVWiuYy7A0pqKgEeIoaQeo7+8oQe8Bq8QB9252nwts6neUm7jXUNSusa90VQaZJAAIVDI6c4IHPZXOrxvMMc6yo1BfsssjQTTqRrLk+Jrqsi0eHYHxMvGM/QyjCnUenTXSAgqeBCALDXGkkREb22xSr2oHcW8smwnODKQ4dop1G1A6UCyVEyLAC15OlYkbnC12i4awyuVpo5p1KJXSHl2ZWRg6nQt3BDMLGbc8NuX05/wo691BipSbVBII8B06SfXaBY2wscZzbZavUoNWWvUEBWZGB906QhQ+F11G0H7xvEYEhYAFlt5QhyTY5i9w6oy6tYLB9WksGDQZCa1YxTDDwkTGonb3sL+c71DmHpPpYOLCPeWFqKA3vTYjmQBg5ksscxmqwFtAD1PHdhS8MsLSWJAkRAHngz/9a4bWXWe6WqzBtRU6tRgAksIUwIvG18EB2txeSxLAXNpnDcYdgyvTFRamlzEzK6j6c22gHzwZ7KZGquZp1RRNamDGhpuj27qpa5UsjbEAwdtpOJZbuXWpUSi1KSoqUA2rSFZSohishDOkEwBfkce5jM1KWTVjWqdxUqShK6WFSkxQmNUEsvKDGm8EYZvjuiL4J75ljibJWNcCFNFmP8LVo2ETMuCwp2nxhgpI91dQkElRRqB1UyCZUKZuILaryLem/UYsZLNtRrLVo1YrFu7YmSWV5WbwDYrI5EA7QBPw/idXNZhtBVK5VRTDgKzQxlVYLJ3nTN9MeWIz8vflLDBlvL8YNXTl2plqlJHakSjDUAsgFSJUtpA1SQZvHOs1B6oanUpaamkFakAEgEDTU/mAUCCLjTHPFrh/b0qTTqpNQM2urrIabKQgUAKAogCRe+5OBZ43Woq5WqHIBTvbyVmJDDxCRpmbzIMYHsN8C3v3iE3jqZNm+zzU9LGVXSGEqZj1G/pykdcRV+ztaop00H1FSVINjpAN5NrGb7gyMGOH8YeuBQytRS0K5NWTD/yoCGBUyAdtMSTyxNkKWZZTSzLVabq3gYBTG4IbT4CCsLpNiFnAjUdMtb8/SF7jYUQRwnscqVBTzNOpUeqo0KBpGq+oBy6iRYzcWNjbEacIpUnekhDstytRtJuBcNTDqw5W54L0+yGZV578NTggVAxSpTBU30gEKLQYPMHlhYy/ZDNNJpJqE+82gSDsQWYgg+s4JTqBrkvF3Xbbav8AM27+JA5fO34T+OFjtvxCESTpjUZ26dThbz/azMuYpt3Y6KBPzYGPgcL3GaLVYNRmJvdiSb3vqJMYy9NoCrhmMeq1htO0Rj7Odt1rKKdaBUtBmzHkR/K37GC+VoBK3eBR4rauYnkw535jqLc8ZOtJYINjyYbHyP64aOA9rmUd1XkkRpbnYiA3X1/HGhW0lrmn15EUpaq+H+v8zTOHcHoZhqveUkLd37+kawZUAhtwb4T6/YSkCwdnYiQDIGnzEDf1w58BzIWi7zPekIh5EC7EHmLj5YocXchmtzwKnUdKYUGaFOkrklhiJfB+xCVXraqjDuyqrAGx1EyD6DaOeO+0fs/7ukKlFi5SS6kCSvNljmOnTBns7WPfZn/9f/8AScMSv1wKtrKyVOcYx8hFmpLkTL+HJBnqB+eDmXfA/MZLuazU/wCUsB/lkFfoRizl3vhmod2RLUsC09zfBqNW5WG/mWx+PI/HFDJ9jSO8hRXBRgqzpZSYKuORIIj/AFYJipglwitFQXxTtnRcGWejTfkZiDX76mVoBiuligHunxspkg3XVC7gHwwcdZHPBtZqkqVEg0xDxMEDxLsCd58wcalxPJpUjWgaLgkXB6qdx8MJPFexYeo7UmAM+61gZANiNufLBqWrSoO8LRJ9K6ZXM+TtEuXdlVxUYKBqI0EOVBbxqAG0ksssgM3tg9lOLkstOsWo1NH2RdQfCwOpqVWnINgYsLAxfGdcX4dUpOS6Muoze4kk2Dfe+c4s5LiTBWZpZVZAAzEgCIgCZJCooHIBfTBmoKwuIJazKbGacuTzFJRUimtBwbhpJ6klW/qmLWjBLJ5hadJHbM5YkMD3ZqEGxEQGhp0M3hixI3vOd8N7dvSVFOl1MsVaGAOlBaboGZGYhY94YYsh2zyGZUU62X7modnpk2Y2vJBblYg7YQqUHBuVuPL+P+xtKwIsDKOf4LTjvD7zVCyVKfgYDUwUsyAhX1cpPIjcYMcN4pxRSqU8y1SkYE1lWqVHNiZDG173tgV3yI7AVKbCoCAT4ZmI0nb3o97SQQDvGD+QyfgUyVuC0HluFVlm3W53HQY5q70xcH6/xDCklTkQT2m4vxUvUpvmTSpCyGke7DDdTqUaojcTiuc1VpZZKXhMNrFSNRj74H3mkqp1A6pHMEgMXaniDJV8FMs2kEkp4FUgEBSNyBub/kF/N5AVm194abb6hJEiLAiD/wCMQtdqijtJy0VX4Jp/DeDZDM8OIyaI1OpT0sVtUJKwVqN7wa5kHrjM85wPJUnKtWrZWoxhhUp04MNOrxJEctS8tyb4Gjh2ZpVzVy1epTc3ZqcrqjqLBr7g9TgjQ9ovGEAWpSpVjczVoiYHXQVHxxoIabdfv/IiLpUQ5F44dkOxNE0KiUqx7mqwYMqxJCADSZMi06hBMkTc4TPaHwirRjKNWpGlTKtTp2XSumAyyRc3kM0STBGIq/tc4m6kKtKhF5SidUf06yy3wCqU3dzVzKnMOTqLhi+sm6hgCbRbYWAGLEbTg+/tIQb+Vk1bJLl1NTVSLAqyalJI0zJGmdU23gCB1Bwz5jg1Og9Nlp6SypUJnxCoQDpBBIWSQQFJkibiMX/ZL2dyGbWr3+XpGtQaAksQaZFnZSxV5aRMQIHXDP2iy70NNOj3aodQSm4AVfJORAGy2taY2XrF1XGTCKVZuLCIWb7N06dZWiG1AkC4P3gGtEEm5Ebk4B5ChmK9esoXRWUF6gkKImDuCGjVAsQR13xoubqd6r062WIWbMCDSI03LFSWQEysDoInAzIcESnTqDLq4dT9mCAaiM0EilqVhUpSimN5JIM4BQ1BOKgsZeolwNnEFZRP4Yd3ocVWcKy+Gm/csCRCsO7a4YQL+8RgxUzyq4DPzuXYaoho1AXAgDccowBzXFa3fL/FNS8SsUZUbVNI3VlB8BMtfYGDEjADjPGHaqr1KJFNrGDKGzD3hZrFWE3g9Dgj0e1OPCctTZzGvjnGaPdtorU9aD3UNztIDT6cuV8LNDiBDanVBY3DAG8bgiOW8TbfFIcNWtqK1qVNANRDVPEecKCAT8eZ3OF921nkIEX/AHc4PR04VbXgKtcluI5tmDyAHw+U9fjinxJS1O94IMfvlghSozHlyxxnU+zeANjzwEMAwjRBKxbzHDbSsc7XvtYcp36Yo0zEzsRuPz/TywYpVIMNcHlE7+RExipnaYYkqtydha56ADzw8rHgxB1HIm49luEpTyWVD2WjTFQ+dSp4yPmxJ+AwB7Q8RUam8588H+O5vRTSkLaVBYecCx/fLGZ8e4+FqoI1QZI9NvrfCDDtHsJsIRRpb2+UZuD5M01JazOZI6AbL8JJ9ScEUq4GcL4xTrrqpsDG45j1H54tq18ZlQNuO7mUuDkQL2uoRVpVBs40n1UH8vwwIDQcM/aKjry5jdCrD4Eav+UnCoxw7pzuQDwxKnBlpTi1lqkEHpimGsMSUql8WIhAY5Bg6BhgU6xUb/Kv4v8A2xa4LVlYx7mKX2nqp+hH/dhBe6xWXlF1BBBAIO4NwfXAbPdlKTqQn2ckNa6yAQLHb3jtGDlVYxDOGUqMuVMhkV8MIi57sxWpI3hFQSCCkkgXkxvyHUYDK0abyN7b+mNVD4p57g1Gt76Cf5hZvmN/jh1NZ/7ESqaIcoYmUuLlEoCxNFmBQ3R6ZZXUODKmS1QT0jBarx5ctmKvcl0WowYNSMMEIV0BV5XUocpbTscQZ/sM6yaLBx/K1m+ex+mAGcyr0mUMpUiDDDn+Yw0DTq8ZibLUpfELTT+I9tMxSFHxKamjxhStGsJuhq05amGKx4bnw/DEVLtvRq1KZrJTdySG1IKbiQdM6IDw0GGMG+Mwr1y5Zjcs2o+pk/mcFOM8VbvCq2RdIVbQsIBCjYXkyOZnngJ0adIQaprZmpcT4PQrZItliwei4DFzAn3SZQFTJA2Igj4YE9muG5irXRJYQCxLnVTCrAuxsJmLj5xZD4Tx2plz3lGo1FtVihMahzKmxsYg2IJthm/23o1Rqr0IqlpdsuQq1FJOqabyFfzAIM+QwJtOyiwzDJqAecRl9oHEqNHXRy1cCq96iga0UiZUFlJViOUx5bYS8kFbJmo2k91W0GAdbLUWULGfdVgwuPvAA2gmONcIouorZRhWy+ka2B01qJvIqoo8I/qgDebXxRypokNRqgoKwUCpq06WBlASfC6sbMd4MmYkcqimtrevv0nElje8F0s8KT/xGXavQrKZ1IdS367GDBkGRvM4csl7ZKWYp9zxTLBwf95SsZmzaSRpI3lW9BhJr8GNMsNTUyDpZWUzKnbw8wRj2nkBUBsrMOa6SWABm24aL6d7dbYbVgIF0YmaBQyeRqkNlOLmnPupWIlfICpHzM4eOFVqNGmC2dpVHiC7Vkgeg1QMfnWtw5SRpcR5g/3nHK8MBg61j1n1nmPlgtRhUHe/bP7QIDLgfvNe9o/F8nmxRo5Xuczmu816kCsAukhySLVGMKdAknRtbCG/Ds0hK6TVSzsGBQzBWV1hHU6ViBMQBFhgM/BCsFWVxYki4E8jF/jGDeRzeYOqKjeEQGDvrIEwoJuyiTYiBOFWsB3ePOMojE94ZgIJUq1QlJdT1G0hNzJMAeLn52w75f2F5gialelTb+UBmj42wqjMvRKQomk4dGNPSwKyVOtRJAN4aRjXuy3tWyubp/8A3FRMvWUeMM0I39VNjaD/ACm48xfF2Zrd3ECVAPemZcMzBszEAdZsflbBfiNAMAU2IHzOFGjmGaCxkwN79LfXDBl6hak4NwHAHzH6DC1WnY7o7SqXG2D63DIuCCDzUHqbeY5j+2DHZDgKHM02cahTmqZJtojSD18ZX5YhyY1Ne8oPwOD/AAtvs6x5+Bf9Mtb6D5Yq1VhiXp0Vcie9ouKzqY88Zzn82urxrqDdDBF9xbfDL2rqEIb4WeL0wNJA2X974PpgBnxka5icdBPspmWolalN7EwGi438Ljn9ZjDtwHtGuYEEaKg3XkfNf03/ABwicKqnvVXcO2hgbgr0v+xiBGK1W0kjSWiCbRMHBK1Baozz4zOp1TTPlNczK6qbr1Uj6YSKtjHTDXwDMtUy9NnMsyAk9T8MKnEP8V/XGdplszL4TSY3AM6SpbBPL5EkK3I74Cg2w18EvRGCVjtFxLpnEv5DLmm3kcW66+NT5MPnpP8A0nEqj7PFfMHxU/U//BsZd9zXhZUzSYonF/MYoVcMJJnM49D4iJx8Dglp15YFTHlZFddLqGB5MJH1xDOOlOOtJv0gfPdjaTA92TTJ5brP4+W532wv8R4DXpAkoCAsFl8QI+UqY5mNt8PYOJAcMJqnXnMWfS024xMmnH04fu0/CaRovU0DWBOoW+cb/HCBjRo1RVW4mXWomk1iYY7PcQNPMUyzaQXCuZ0kKTB8QuB1AIkAjFqvXD1swuvu0Q1GQAA09KkwkSLtCrI3Jk9cDM1RApKYudJJ53DT+AxxnT/hedMT82H4DFioJlQ5EM5bi+qRUBaI+0pe9EAQwI8Qi1xIjFrK5WnUYFGvOoafC8yL28JM4A0lk/6fzww8MyaOF1C/d6pBIadIPvC+/KY3wvUAXIjKMTzL2f7PSRVU6VZg4QiIcC41EQwLCYnZvLC9V4RV1aWQoWJILSFj1254n4L2hzCkxVa1oNxA5EGzfHGu1uH0zwta+kd4w8RuFMMR7g8Gxjbp0GFmqVKJsc+/9wo7OpkYmKI1SnKiHWZKsJ8SggH4Xx8eJBiGK924jxKTB9RNsNnD+E0nzFMFLOG1AEqDFNjspEXA2wqZzLrBMX258hhpHVzxBspUYMt1a5alqTUw/wB4syFv4W6wR8tPngJm6V5Emfxx3km0mRY3Hw0m2PKZkwcFUbYFm38z/9k=">
           
          
           <h2>The hotel rankings according to Overall Rating:</h2>
		    <div style="width: 100%; overflow: hidden;">
    <div style="width: 600px; float: left;"> 
           <table class="zui-table">
		   <thead>
        <tr>
            <th>Hotel Name</th>
            <th>Sentiment Score</th>
        </tr>
		</thead>
		<tbody>
           <tr id="f1">
            <td>""" + str(l1[0])+"""</td>
            <td>""" + str(l1[1])+ """</td>
           </tr>
           <tr id="f2">
            <td>""" + str(l2[0])+"""</td>
            <td>""" + str(l2[1])+ """</td>
           </tr>
            <tr id="f3">
            <td>""" + str(l3[0])+"""</td>
            <td>""" + str(l3[1])+ """</td>
           </tr>
            <tr id="f4">
            <td>""" + str(l4[0])+"""</td>
            <td>""" + str(l4[1])+ """</td>
           </tr>
            <tr id="f5">
            <td>""" + str(l5[0])+"""</td>
            <td>""" + str(l5[1])+ """</td>
           </tr>
            <tr id="f6">
            <td>""" + str(l6[0])+"""</td>
            <td>""" + str(l6[1])+ """</td>
           </tr>
            <tr id="f7">
            <td>""" + str(l7[0])+"""</td>
            <td>""" + str(l7[1])+ """</td>
           </tr>
            <tr id="f8">
            <td>""" + str(l8[0])+"""</td>
            <td>""" + str(l8[1])+ """</td>
           </tr>
            <tr id="f9">
            <td>""" + str(l9[0])+"""</td>
            <td>""" + str(l9[1])+ """</td>
           </tr>
            <tr id="f10">
            <td>""" + str(l10[0])+"""</td>
            <td>""" + str(l10[1])+ """</td>
           </tr>
            <tr id="f11">
            <td>""" + str(l11[0])+"""</td>
            <td>""" + str(l11[1])+ """</td>
           </tr>
            <tr id="f12">
            <td>""" + str(l12[0])+"""</td>
            <td>""" + str(l12[1])+ """</td>
           </tr>
            <tr id="f13">
            <td>""" + str(l13[0])+"""</td>
            <td>""" + str(l13[1])+ """</td>
           </tr>
            <tr id="f14">
            <td>""" + str(l14[0])+"""</td>
            <td>""" + str(l14[1])+ """</td>
           </tr>
		   </tbody>
           </table>
		   </div>
    <div id="chartContainer"  style="margin-left: 0px; height: 600px; width: 55%;"> Right </div>
</div>
		   <!-- <div id="chartContainer" style="height: 400px; width: 200px;"></div> -->
		   <br>
		   <div id="chartContainer1" style="height: 400px; width: 100%;"></div>
           </body>
             <a href="http://localhost/detail2.html"><h3>CHECK OUT ALL THE HOTELS !!!</h3></a>
           </html>
         """
		   
    elif asp == 'Environment':
       a=EnvRet()
       #print a
       l1=list(a[0])
       l2=list(a[1])
       l3=list(a[2])
       l4=list(a[3])
       l5=list(a[4])
       l6=list(a[5])
       l7=list(a[6])
       l8=list(a[7])
       l9=list(a[8])
       l10=list(a[9])
       l11=list(a[10])
       l12=list(a[11])
       l13=list(a[12])
       l14=list(a[13])
       print """
        <html>
		<!-- ====================================================
	header section -->
	<header class="top-header">
		<div class="container">
			<div class="row">
				<div class="col-xs-5 header-logo">
					<br>
					<a href="index.html"><img src="Logo.png" alt="" class="img-responsive logo"></a>
				</div>

				<div class="col-md-7">
					<nav class="navbar navbar-default">
					  <div class="container-fluid nav-bar">
					    <!-- Brand and toggle get grouped for better mobile display -->
					    <div class="navbar-header">
					     <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					        <!-- <span class="sr-only">Toggle navigation</span> -->
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					      </button>
					    </div>

					    <!-- Collect the nav links, forms, and other content for toggling -->
					    <!-- <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					      
					     <ul class="nav navbar-nav navbar-right">
					        <li><a class="menu active" href="#home" >Home</a></li>
					        <li><a class="menu" href="#about">about us</a></li>
					        <li><a class="menu" href="#service">our services </a></li>
					        <li><a class="menu" href="#team">our team</a></li>
					        <li><a class="menu" href="#contact"> contact us</a></li>
					      </ul>
					    </div><!-- /navbar-collapse -->
					  </div><!-- / .container-fluid -->
					</nav>
				</div>
			</div>
		</div>
	</header> <!-- end of header area -->
		<style>
		   .zui-table {
    border: solid 1px #DDEEEE;
    border-collapse: collapse;
    border-spacing: 0;
    font: normal 19px Arial, sans-serif;
}
.zui-table thead th {
    background-color: #DDEFEF;
    border: solid 1px #DDEEEE;
    color: #336B6B;
    padding: 10px;
    text-align: left;
    text-shadow: 1px 1px 1px #fff;
}
.zui-table tbody td {
    border: solid 1px #DDEEEE;
    color: #333;
    padding: 10px;
    text-shadow: 1px 1px 1px #fff;
}
</style>
		<script type="text/javascript">
window.onload = function () {
	var Row1 = document.getElementById("e1");
	var Row2 = document.getElementById("e2");
	var Row3 = document.getElementById("e3");
	var Row4 = document.getElementById("e4");
	var Row5 = document.getElementById("e5");
	var Row6 = document.getElementById("e6");
	var Row7 = document.getElementById("e7");
	var Row8 = document.getElementById("e8");
	var Row9 = document.getElementById("e9");
	var Row10 = document.getElementById("e10");
	var Row11 = document.getElementById("e11");
	var Row12 = document.getElementById("e12");
	var Row13 = document.getElementById("e13");
	var Row14 = document.getElementById("e14");
	
	var Cells1 = Row1.getElementsByTagName("td");
	var Cells2 = Row2.getElementsByTagName("td");
	var Cells3 = Row3.getElementsByTagName("td");
	var Cells4 = Row4.getElementsByTagName("td");
	var Cells5 = Row5.getElementsByTagName("td");
	var Cells6 = Row6.getElementsByTagName("td");
	var Cells7 = Row7.getElementsByTagName("td");
	var Cells8 = Row8.getElementsByTagName("td");
	var Cells9 = Row9.getElementsByTagName("td");
	var Cells10 = Row10.getElementsByTagName("td");
	var Cells11 = Row11.getElementsByTagName("td");
	var Cells12 = Row12.getElementsByTagName("td");
	var Cells13 = Row13.getElementsByTagName("td");
	var Cells14 = Row14.getElementsByTagName("td");
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme2",
		title:{
			text: "Pie chart according to Environment"
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			toolTipContent: "{y} - #percent %",
			yValueFormatString: "#0.#,,. Million",
			legendText: "{indexLabel}",
			dataPoints: [
				
				{  y: Cells1[1].innerText, indexLabel: Cells1[0].innerText },
				{  y: Cells2[1].innerText, indexLabel: Cells2[0].innerText },
				{  y: Cells3[1].innerText, indexLabel: Cells3[0].innerText },
				{  y: Cells4[1].innerText, indexLabel: Cells4[0].innerText },
				{  y: Cells5[1].innerText, indexLabel: Cells5[0].innerText },
				{  y: Cells6[1].innerText, indexLabel: Cells6[0].innerText },
				{  y: Cells7[1].innerText, indexLabel: Cells7[0].innerText },
				{  y: Cells8[1].innerText, indexLabel: Cells8[0].innerText },
				{  y: Cells9[1].innerText, indexLabel: Cells9[0].innerText },
				{  y: Cells10[1].innerText, indexLabel: Cells10[0].innerText },
				{  y: Cells11[1].innerText, indexLabel: Cells11[0].innerText },
				{  y: Cells12[1].innerText, indexLabel: Cells12[0].innerText },
				{  y: Cells13[1].innerText, indexLabel: Cells13[0].innerText },
				{  y: Cells14[1].innerText, indexLabel: Cells14[0].innerText }
				
				
				
				
			]
		}
		]
	});
	chart.render();
	chart={};
	var chart1 = new CanvasJS.Chart("chartContainer1", {
				title: {
					text: "Bar chart according to Environment"
				},
				data: [{
					type: "column",
					dataPoints: [
				{  y: 85, label:  Cells5[0].innerText },
				
				{  y: 47, label:  Cells8[0].innerText },
				{  y: 36, label:  Cells9[0].innerText },
				{  y: 161, label:  Cells1[0].innerText },
				{  y: 89, label:  Cells4[0].innerText },
				{  y: 79, label:  Cells6[0].innerText },
				{  y: 48, label:  Cells7[0].innerText },
				{  y: 28, label:  Cells10[0].innerText },
				{  y: 107, label:  Cells3[0].innerText },
				{  y: 17, label:  Cells12[0].innerText },
				{  y: 16, label:  Cells13[0].innerText },
				{  y: 113, label:  Cells2[0].innerText },
				{  y: 20, label:  Cells11[0].innerText },
				{  y: 17, label:  Cells12[0].innerText },
				{  y: 5, label:  Cells14[0].innerText }
						
					]
				}]
			});
			chart1.render();
			chart1={};
	

	
}
	</script>
	<script src="canvasjs.min.js"></script>
        <head>
        <link rel="stylesheet" href="http://localhost/style.css" type="css/textfile" />
        </head>
        <body>
      
        <img src="imgs/ambi/p1.jpg" style="width:240px;height:180px;">
        <img src="imgs/ambi/p2.jpg" style="width:240px;height:180px;">
		<img src="imgs/ambi/p3.jpg" style="width:240px;height:180px;">
		<img src="imgs/ambi/p4.jpg" style="width:240px;height:180px;">
		<img src="imgs/ambi/p5.jpg" style="width:240px;height:180px;">
        <h2>The hotel ratings according to Environment:</h2>
		   <div style="width: 100%; overflow: hidden;">
    <div style="width: 600px; float: left;"> 
        <table class="zui-table">
		   <thead>
        <tr>
            <th>Hotel Name</th>
            <th>Sentiment Score</th>
        </tr>
		</thead>
		<tbody>
           <tr id="e1">
            <td>""" + str(l1[0])+"""</td>
            <td>""" + str(l1[1])+ """</td>
           </tr>
           <tr id="e2">
            <td>""" + str(l2[0])+"""</td>
            <td>""" + str(l2[1])+ """</td>
           </tr>
            <tr id="e3">
            <td>""" + str(l3[0])+"""</td>
            <td>""" + str(l3[1])+ """</td>
           </tr>
            <tr id="e4">
            <td>""" + str(l4[0])+"""</td>
            <td>""" + str(l4[1])+ """</td>
           </tr>
            <tr id="e5">
            <td>""" + str(l5[0])+"""</td>
            <td>""" + str(l5[1])+ """</td>
           </tr>
            <tr id="e6">
            <td>""" + str(l6[0])+"""</td>
            <td>""" + str(l6[1])+ """</td>
           </tr>
            <tr id="e7">
            <td>""" + str(l7[0])+"""</td>
            <td>""" + str(l7[1])+ """</td>
           </tr>
            <tr id="e8">
            <td>""" + str(l8[0])+"""</td>
            <td>""" + str(l8[1])+ """</td>
           </tr>
            <tr id="e9">
            <td>""" + str(l9[0])+"""</td>
            <td>""" + str(l9[1])+ """</td>
           </tr>
            <tr id="e10">
            <td>""" + str(l10[0])+"""</td>
            <td>""" + str(l10[1])+ """</td>
           </tr>
            <tr id="e11">
            <td>""" + str(l11[0])+"""</td>
            <td>""" + str(l11[1])+ """</td>
           </tr>
            <tr id="e12">
            <td>""" + str(l12[0])+"""</td>
            <td>""" + str(l12[1])+ """</td>
           </tr>
            <tr id="e13">
            <td>""" + str(l13[0])+"""</td>
            <td>""" + str(l13[1])+ """</td>
           </tr>
            <tr id="e14">
            <td>""" + str(l14[0])+"""</td>
            <td>""" + str(l14[1])+ """</td>
           </tr>
        </table>
		 </div>
    <div id="chartContainer"  style="margin-left: 0px; height: 600px; width: 55%;"> Right </div>
</div>
		   <!-- <div id="chartContainer" style="height: 400px; width: 200px;"></div> -->
		   <br>
		   <div id="chartContainer1" style="height: 400px; width: 100%;"></div>
        </body>
		
          <a href="http://localhost/detail2.html"><h3>CHECK OUT ALL THE HOTELS !!!</h3></a>
        </html>"""
    elif asp == 'Service':
        a=ServiceRet()
        l1=list(a[0])
        l2=list(a[1])
        l3=list(a[2])
        l4=list(a[3])
        l5=list(a[4])
        l6=list(a[5])
        l7=list(a[6])
        l8=list(a[7])
        l9=list(a[8])
        l10=list(a[9])
        l11=list(a[10])
        l12=list(a[11])
        l13=list(a[12])
        l14=list(a[13])
        m=list(a[1])
        print """
         <html>
		 <!-- ====================================================
	header section -->
	<header class="top-header">
		<div class="container">
			<div class="row">
				<div class="col-xs-5 header-logo">
					<br>
					<a href="index.html"><img src="Logo.png" alt="" class="img-responsive logo"></a>
				</div>

				<div class="col-md-7">
					<nav class="navbar navbar-default">
					  <div class="container-fluid nav-bar">
					    <!-- Brand and toggle get grouped for better mobile display -->
					    <div class="navbar-header">
					     <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					        <!-- <span class="sr-only">Toggle navigation</span> -->
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					      </button>
					    </div>

					    <!-- Collect the nav links, forms, and other content for toggling -->
					    <!-- <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					      
					     <ul class="nav navbar-nav navbar-right">
					        <li><a class="menu active" href="#home" >Home</a></li>
					        <li><a class="menu" href="#about">about us</a></li>
					        <li><a class="menu" href="#service">our services </a></li>
					        <li><a class="menu" href="#team">our team</a></li>
					        <li><a class="menu" href="#contact"> contact us</a></li>
					      </ul>
					    </div><!-- /navbar-collapse -->
					  </div><!-- / .container-fluid -->
					</nav>
				</div>
			</div>
		</div>
	</header> <!-- end of header area -->
		 <style>
		   .zui-table {
    border: solid 1px #DDEEEE;
    border-collapse: collapse;
    border-spacing: 0;
    font: normal 19px Arial, sans-serif;
}
.zui-table thead th {
    background-color: #DDEFEF;
    border: solid 1px #DDEEEE;
    color: #336B6B;
    padding: 10px;
    text-align: left;
    text-shadow: 1px 1px 1px #fff;
}
.zui-table tbody td {
    border: solid 1px #DDEEEE;
    color: #333;
    padding: 10px;
    text-shadow: 1px 1px 1px #fff;
}
</style>
		 <script type="text/javascript">
window.onload = function () {
	var Row1 = document.getElementById("f1");
	var Row2 = document.getElementById("f2");
	var Row3 = document.getElementById("f3");
	var Row4 = document.getElementById("f4");
	var Row5 = document.getElementById("f5");
	var Row6 = document.getElementById("f6");
	var Row7 = document.getElementById("f7");
	var Row8 = document.getElementById("f8");
	var Row9 = document.getElementById("f9");
	var Row10 = document.getElementById("f10");
	var Row11 = document.getElementById("f11");
	var Row12 = document.getElementById("f12");
	var Row13 = document.getElementById("f13");
	var Row14 = document.getElementById("f14");
	
	var Cells1 = Row1.getElementsByTagName("td");
	var Cells2 = Row2.getElementsByTagName("td");
	var Cells3 = Row3.getElementsByTagName("td");
	var Cells4 = Row4.getElementsByTagName("td");
	var Cells5 = Row5.getElementsByTagName("td");
	var Cells6 = Row6.getElementsByTagName("td");
	var Cells7 = Row7.getElementsByTagName("td");
	var Cells8 = Row8.getElementsByTagName("td");
	var Cells9 = Row9.getElementsByTagName("td");
	var Cells10 = Row10.getElementsByTagName("td");
	var Cells11 = Row11.getElementsByTagName("td");
	var Cells12 = Row12.getElementsByTagName("td");
	var Cells13 = Row13.getElementsByTagName("td");
	var Cells14 = Row14.getElementsByTagName("td");
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme2",
		title:{
			text: "Pie chart according to Service"
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			toolTipContent: "{y} - #percent %",
			yValueFormatString: "#0.#,,. Million",
			legendText: "{indexLabel}",
			dataPoints: [
				
				{  y: Cells1[1].innerText, indexLabel: Cells1[0].innerText },
				{  y: Cells2[1].innerText, indexLabel: Cells2[0].innerText },
				{  y: Cells3[1].innerText, indexLabel: Cells3[0].innerText },
				{  y: Cells4[1].innerText, indexLabel: Cells4[0].innerText },
				{  y: Cells5[1].innerText, indexLabel: Cells5[0].innerText },
				{  y: Cells6[1].innerText, indexLabel: Cells6[0].innerText },
				{  y: Cells7[1].innerText, indexLabel: Cells7[0].innerText },
				{  y: Cells8[1].innerText, indexLabel: Cells8[0].innerText },
				{  y: Cells9[1].innerText, indexLabel: Cells9[0].innerText },
				{  y: Cells10[1].innerText, indexLabel: Cells10[0].innerText },
				{  y: Cells11[1].innerText, indexLabel: Cells11[0].innerText },
				{  y: Cells12[1].innerText, indexLabel: Cells12[0].innerText },
				{  y: Cells13[1].innerText, indexLabel: Cells13[0].innerText },
				{  y: Cells14[1].innerText, indexLabel: Cells14[0].innerText }
				
				
				
				
			]
		}
		]
	});
	chart.render();
	chart={};
	var chart1 = new CanvasJS.Chart("chartContainer1", {
				title: {
					text: "Bar chart according to Service"
				},
				data: [{
					type: "column",
					dataPoints: [
				{  y: 75, label:  Cells5[0].innerText },
				{  y: 29, label:  Cells12[0].innerText },
				{  y: 87, label:  Cells4[0].innerText },
				{  y: 59, label:  Cells6[0].innerText },
				{  y: 50, label:  Cells8[0].innerText },
				{  y: 49, label:  Cells9[0].innerText },
				{  y: 59, label:  Cells7[0].innerText },
				{  y: 20, label:  Cells13[0].innerText },
				{  y: 254, label:  Cells1[0].innerText },
				{  y: 114, label:  Cells2[0].innerText },
				{  y: 36, label:  Cells11[0].innerText },
				{  y: 48, label:  Cells10[0].innerText },
				{  y: 104, label:  Cells3[0].innerText },
				{  y: 114, label:  Cells12[0].innerText },
				{  y: 17, label:  Cells14[0].innerText }
						
					]
				}]
			});
			chart1.render();
			chart1={};
	
}
	</script>
	<script src="canvasjs.min.js"></script>
         <head>
         <link rel="stylesheet" href="http://localhost/style.css" type="css/textfile" />
         </head>
         <body>
        
         <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCQPI7dTvjrm-IhO2mngohRnsKODUo0mTW8aOhYu77A87ctzX_">
         <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRR0W9gV79g-MLbZ31iUQZoXXFpFyVpyqhxQmnXGGTbsBkdbeppHQ">
         <img src="data:image/jpeg;base64,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">
         <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQW3e9lzDq4W8eKln_mvq3K3hOQeur38rgWBgTq1ZcyKR8DCBi_Vw">
         <img src="data:image/jpeg;base64,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">
         <h2>The hotel rankings according to Service:</h2>
		    <div style="width: 100%; overflow: hidden;">
    <div style="width: 600px; float: left;"> 
         <table class="zui-table">
		   <thead>
        <tr>
            <th>Hotel Name</th>
            <th>Sentiment Score</th>
        </tr>
		</thead>
		<tbody>
           <tr id="f1">
            <td>""" + str(l1[0])+"""</td>
            <td>""" + str(l1[1])+ """</td>
           </tr>
           <tr id="f2">
            <td>""" + str(l2[0])+"""</td>
            <td>""" + str(l2[1])+ """</td>
           </tr>
            <tr id="f3">
            <td>""" + str(l3[0])+"""</td>
            <td>""" + str(l3[1])+ """</td>
           </tr>
            <tr id="f4">
            <td>""" + str(l4[0])+"""</td>
            <td>""" + str(l4[1])+ """</td>
           </tr>
            <tr id="f5">
            <td>""" + str(l5[0])+"""</td>
            <td>""" + str(l5[1])+ """</td>
           </tr>
            <tr id="f6">
            <td>""" + str(l6[0])+"""</td>
            <td>""" + str(l6[1])+ """</td>
           </tr>
            <tr id="f7">
            <td>""" + str(l7[0])+"""</td>
            <td>""" + str(l7[1])+ """</td>
           </tr>
            <tr id="f8">
            <td>""" + str(l8[0])+"""</td>
            <td>""" + str(l8[1])+ """</td>
           </tr>
            <tr id="f9">
            <td>""" + str(l9[0])+"""</td>
            <td>""" + str(l9[1])+ """</td>
           </tr>
            <tr id="f10">
            <td>""" + str(l10[0])+"""</td>
            <td>""" + str(l10[1])+ """</td>
           </tr>
            <tr id="f11">
            <td>""" + str(l11[0])+"""</td>
            <td>""" + str(l11[1])+ """</td>
           </tr>
            <tr id="f12">
            <td>""" + str(l12[0])+"""</td>
            <td>""" + str(l12[1])+ """</td>
           </tr>
            <tr id="f13">
            <td>""" + str(l13[0])+"""</td>
            <td>""" + str(l13[1])+ """</td>
           </tr>
            <tr id="f14">
            <td>""" + str(l14[0])+"""</td>
            <td>""" + str(l14[1])+ """</td>
           </tr>
           </table>
		   </div>
    <div id="chartContainer"  style="margin-left: 0px; height: 600px; width: 55%;"> Right </div>
</div>
		   <!-- <div id="chartContainer" style="height: 400px; width: 200px;"></div> -->
		   <br>
		   <div id="chartContainer1" style="height: 400px; width: 100%;"></div>
         </body>
           <a href="http://localhost/detail2.html"><h3>CHECK OUT ALL THE HOTELS !!!</h3></a>
         </html>"""

    elif asp == 'Price':
      a=PriceRet()
      l1=list(a[0])
      l2=list(a[1])
      l3=list(a[2])
      l4=list(a[3])
      l5=list(a[4])
      l6=list(a[5])
      l7=list(a[6])
      l8=list(a[7])
      l9=list(a[8])
      l10=list(a[9])
      l11=list(a[10])
      l12=list(a[11])
      l13=list(a[12])
      l14=list(a[13])
      print """
         <html>
		 <!-- ====================================================
	header section -->
	<header class="top-header">
		<div class="container">
			<div class="row">
				<div class="col-xs-5 header-logo">
					<br>
					<a href="index.html"><img src="Logo.png" alt="" class="img-responsive logo"></a>
				</div>

				<div class="col-md-7">
					<nav class="navbar navbar-default">
					  <div class="container-fluid nav-bar">
					    <!-- Brand and toggle get grouped for better mobile display -->
					    <div class="navbar-header">
					     <!-- <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					        <!-- <span class="sr-only">Toggle navigation</span> -->
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					        <span class="icon-bar"></span>
					      </button>
					    </div>

					    <!-- Collect the nav links, forms, and other content for toggling -->
					    <!-- <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
					      
					     <ul class="nav navbar-nav navbar-right">
					        <li><a class="menu active" href="#home" >Home</a></li>
					        <li><a class="menu" href="#about">about us</a></li>
					        <li><a class="menu" href="#service">our services </a></li>
					        <li><a class="menu" href="#team">our team</a></li>
					        <li><a class="menu" href="#contact"> contact us</a></li>
					      </ul>
					    </div><!-- /navbar-collapse -->
					  </div><!-- / .container-fluid -->
					</nav>
				</div>
			</div>
		</div>
	</header> <!-- end of header area -->
		 <style>
		   .zui-table {
    border: solid 1px #DDEEEE;
    border-collapse: collapse;
    border-spacing: 0;
    font: normal 19px Arial, sans-serif;
}
.zui-table thead th {
    background-color: #DDEFEF;
    border: solid 1px #DDEEEE;
    color: #336B6B;
    padding: 10px;
    text-align: left;
    text-shadow: 1px 1px 1px #fff;
}
.zui-table tbody td {
    border: solid 1px #DDEEEE;
    color: #333;
    padding: 10px;
    text-shadow: 1px 1px 1px #fff;
}
</style>
		 <script type="text/javascript">
window.onload = function () {
	var Row1 = document.getElementById("f1");
	var Row2 = document.getElementById("f2");
	var Row3 = document.getElementById("f3");
	var Row4 = document.getElementById("f4");
	var Row5 = document.getElementById("f5");
	var Row6 = document.getElementById("f6");
	var Row7 = document.getElementById("f7");
	var Row8 = document.getElementById("f8");
	var Row9 = document.getElementById("f9");
	var Row10 = document.getElementById("f10");
	var Row11 = document.getElementById("f11");
	var Row12 = document.getElementById("f12");
	var Row13 = document.getElementById("f13");
	var Row14 = document.getElementById("f14");
	
	var Cells1 = Row1.getElementsByTagName("td");
	var Cells2 = Row2.getElementsByTagName("td");
	var Cells3 = Row3.getElementsByTagName("td");
	var Cells4 = Row4.getElementsByTagName("td");
	var Cells5 = Row5.getElementsByTagName("td");
	var Cells6 = Row6.getElementsByTagName("td");
	var Cells7 = Row7.getElementsByTagName("td");
	var Cells8 = Row8.getElementsByTagName("td");
	var Cells9 = Row9.getElementsByTagName("td");
	var Cells10 = Row10.getElementsByTagName("td");
	var Cells11 = Row11.getElementsByTagName("td");
	var Cells12 = Row12.getElementsByTagName("td");
	var Cells13 = Row13.getElementsByTagName("td");
	var Cells14 = Row14.getElementsByTagName("td");
	
	var chart = new CanvasJS.Chart("chartContainer",
	{
		theme: "theme2",
		title:{
			text: "Pie chart according to Price"
		},
		data: [
		{
			type: "pie",
			showInLegend: true,
			toolTipContent: "",
			yValueFormatString: "",
			legendText: "{}",
			dataPoints: [
				
				{  y: Cells1[1].innerText, indexLabel: Cells1[0].innerText },
				{  y: Cells2[1].innerText, indexLabel: Cells2[0].innerText },
				{  y: Cells3[1].innerText, indexLabel: Cells3[0].innerText },
				{  y: Cells4[1].innerText, indexLabel: Cells4[0].innerText },
				{  y: Cells5[1].innerText, indexLabel: Cells5[0].innerText },
				{  y: Cells6[1].innerText, indexLabel: Cells6[0].innerText },
				{  y: Cells7[1].innerText, indexLabel: Cells7[0].innerText },
				{  y: Cells8[1].innerText, indexLabel: Cells8[0].innerText },
				{  y: Cells9[1].innerText, indexLabel: Cells9[0].innerText },
				{  y: Cells10[1].innerText, indexLabel: Cells10[0].innerText },
				{  y: Cells11[1].innerText, indexLabel: Cells11[0].innerText },
				{  y: Cells12[1].innerText, indexLabel: Cells12[0].innerText },
				{  y: Cells13[1].innerText, indexLabel: Cells13[0].innerText },
				{  y: Cells14[1].innerText, indexLabel: Cells14[0].innerText }
				
				
				
				
			]
		}
		]
	});
	chart.render();
	chart={};
	var chart1 = new CanvasJS.Chart("chartContainer1", {
				title: {
					text: "Bar Chart according to Price"
				},
				data: [{
					type: "column",
					dataPoints: [
				{  y: 31, label:  Cells5[0].innerText },
				{  y: -2, label:  Cells12[0].innerText },
				{  y: -3, label:  Cells13[0].innerText },
				{  y: 60, label:  Cells1[0].innerText },
				{  y: 36, label:  Cells4[0].innerText },
				{  y: 29, label:  Cells6[0].innerText },
				{  y: 51, label:  Cells2[0].innerText },
				{  y: 0, label:  Cells11[0].innerText },
				{  y: -3, label:  Cells12[0].innerText },
				{  y: 16, label:  Cells7[0].innerText },
				{  y: 13, label:  Cells8[0].innerText },
				{  y: 10, label:  Cells9[0].innerText },
				{  y: 3, label:  Cells10[0].innerText },
				{  y: 45, label:  Cells3[0].innerText },
				
				{  y: -5, label:  Cells14[0].innerText }
						
					]
				}]
			});
			chart1.render();
			chart1={};
	

}
	</script>
	<script src="canvasjs.min.js"></script>
         <head>
         <link rel="stylesheet" href="http://localhost/style.css" type="css/textfile" />
         </head>
         <body>
       
         <img src="data:image/jpeg;base64,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">
         <img src="data:image/jpeg;base64,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">
         <img src="data:image/jpeg;base64,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">
         <img src="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQZHfx80HksJo5KOn2sHrpiM6ggtPY99vWwMcIPiRnfnRfAcqXy">
         <img src="data:image/jpeg;base64,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">
         <h2>The hotel rankings according to Price:</h2>
		    <div style="width: 100%; overflow: hidden;">
    <div style="width: 600px; float: left;"> 
         <table class="zui-table">
		   <thead>
        <tr>
            <th>Hotel Name</th>
            <th>Sentiment Score</th>
        </tr>
		</thead>
		<tbody>
           <tr id="f1">
            <td>""" + str(l1[0])+"""</td>
            <td>""" + str(l1[1])+ """</td>
           </tr>
           <tr id="f2">
            <td>""" + str(l2[0])+"""</td>
            <td>""" + str(l2[1])+ """</td>
           </tr>
            <tr id="f3">
            <td>""" + str(l3[0])+"""</td>
            <td>""" + str(l3[1])+ """</td>
           </tr>
            <tr id="f4">
            <td>""" + str(l4[0])+"""</td>
            <td>""" + str(l4[1])+ """</td>
           </tr>
            <tr id="f5">
            <td>""" + str(l5[0])+"""</td>
            <td>""" + str(l5[1])+ """</td>
           </tr>
            <tr id="f6">
            <td>""" + str(l6[0])+"""</td>
            <td>""" + str(l6[1])+ """</td>
           </tr>
            <tr id="f7">
            <td>""" + str(l7[0])+"""</td>
            <td>""" + str(l7[1])+ """</td>
           </tr>
            <tr id="f8">
            <td>""" + str(l8[0])+"""</td>
            <td>""" + str(l8[1])+ """</td>
           </tr>
            <tr id="f9">
            <td>""" + str(l9[0])+"""</td>
            <td>""" + str(l9[1])+ """</td>
           </tr>
            <tr id="f10">
            <td>""" + str(l10[0])+"""</td>
            <td>""" + str(l10[1])+ """</td>
           </tr>
            <tr id="f11">
            <td>""" + str(l11[0])+"""</td>
            <td>""" + str(l11[1])+ """</td>
           </tr>
            <tr id="f12">
            <td>""" + str(l12[0])+"""</td>
            <td>""" + str(l12[1])+ """</td>
           </tr>
            <tr id="f13">
            <td>""" + str(l13[0])+"""</td>
            <td>""" + str(l13[1])+ """</td>
           </tr>
            <tr id="f14">
            <td>""" + str(l14[0])+"""</td>
            <td>""" + str(l14[1])+ """</td>
           </tr>
           </tr>
           </table>
		   </div>
    <div id="chartContainer"  style="margin-left: 0px; height: 600px; width: 55%;"> Right </div>
</div>
		   <!-- <div id="chartContainer" style="height: 400px; width: 200px;"></div> -->
		   <br>
		   <div id="chartContainer1" style="height: 400px; width: 100%;"></div>
         </body>
		 
           <a href="http://localhost/detail2.html"><h3>CHECK OUT ALL THE HOTELS !!!</h3></a>
         </html>"""
    else:
        print "Invalid choice"
  

    
