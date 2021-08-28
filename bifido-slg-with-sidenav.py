# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 23:06:44 2020

@author: Ryzen
"""

import csv

#replace the name with your actual csv file name
file_name = "master.csv" 
f1 = open(file_name)
csv_file = csv.reader(f1)

def slr(line):
    slrtable=""
    file_name1 = "CSV/"+line[0]+"/JSL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            if line1[0].isalnum():
                slrtable = slrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
                idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            if line1[0].isalnum():
                slrtable = slrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
                idx += 1
            
    return slrtable

def dlr(line):
    dlrtable=""
    file_name1 = "CSV/"+line[0]+"/JDL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            dlrtable = dlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            if line1[0].isalnum():
                dlrtable = dlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td></tr>"
                idx += 1
            
    return dlrtable

def tlr(line):
    tlrtable=""
    file_name1 = "CSV/"+line[0]+"/JTL.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            tlrtable = tlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/reactions/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td><td><a href='"+line[8]+"/reactions/"+line1[2]+"' target='blank'><center><u><font color='black'>"+line1[2]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            tlrtable = tlrtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#reaction/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td><td><a href='https://vmh.life/#reaction/"+line1[2]+"' target='blank'><center><u><font color='black'>"+line1[2]+"</font></u></center></a></td></tr>"
            idx += 1
    
    return tlrtable

def slg(line):
    slgtable=""
    file_name1 = "CSV/"+line[0]+"/SGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            slgtable = slgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            slgtable = slgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td></tr>"
            idx += 1

    return slgtable

def dlg(line):
    dlgtable=""
    file_name1 = "CSV/"+line[0]+"/DGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            dlgtable = dlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            dlgtable = dlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td></tr>"
            idx += 1

    return dlgtable

def tlg(line):
    tlgtable=""
    file_name1 = "CSV/"+line[0]+"/TGD.csv" 
    f2 = open(file_name1)
    csv_file1 = csv.reader(f2)
    idx = 1
    if (line[10]=="bigg"):
        for line1 in csv_file1:
            tlgtable = tlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='"+line[8]+"/genes/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td><td><a href='"+line[8]+"/genes/"+line1[2]+"' target='blank'><center><u><font color='black'>"+line1[2]+"</font></u></center></a></td></tr>"
            idx += 1
    elif (line[10]=="vmh"):
        for line1 in csv_file1:
            tlgtable = tlgtable+"<tr><td><center><font color='black'>"+str(idx)+"</font></center></td><td><a href='https://vmh.life/#microbegene/"+line1[0]+"' target='blank'><center><u><font color='black'>"+line1[0]+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[1]+"' target='blank'><center><u><font color='black'>"+line1[1]+"</font></u></center></a></td><td><a href='https://vmh.life/#microbegene/"+line1[2]+"' target='blank'><center><u><font color='black'>"+line1[2]+"</font></u></center></a></td></tr>"
            idx += 1

    return tlgtable

html = """

    <!doctype html>
<html lang="en">
<head>
  
    <title>CASTLE | {organism1:}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link href="https://fonts.googleapis.com/css?family=Muli:400,700|Hepta+Slab:400,700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="../fonts/icomoon/style.css">
    <link rel="shortcut icon" type="image/x-icon" href="../img/logo.png">	

    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <link rel="stylesheet" href="../css/bootstrap-datepicker.css">
    <link rel="stylesheet" href="../css/jquery.fancybox.min.css">
    <link rel="stylesheet" href="../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../css/owl.theme.default.min.css">
    <link rel="stylesheet" href="../fonts/flaticon/font/flaticon.css">
    <link rel="stylesheet" href="../css/aos.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-csv/0.71/jquery.csv-0.71.min.js"></script>
	<script src="https://www.w3schools.com/lib/w3data.js"></script>
    <!-- MAIN CSS -->
    <link rel="stylesheet" href="../css/style.css">
    <link rel="stylesheet" href="../css/syntheticlethals.css">

<script>
	$(document).scroll(function() {{
	  var y = $(this).scrollTop();
	  if (y > 300) {{
		$('.sidenav').fadeIn();
	  }} else {{
		$('.sidenav').fadeOut();
	  }}
	}});
</script>
  </head>

<body>


    <header>
        <div class="header-area ">
            <div id="sticky-header" class="main-header-area white-bg">
                <div class="container-fluid p-0">
                    <div class="row align-items-center justify-content-between no-gutters">
                        <div class="col-xl-2 col-lg-2">
                            <div class="logo-img">
                                <a href="../index.html">
                                    <img src="../img/logo.png" alt="">
                                </a>
                            </div>
                        </div>
                        <div class="col-xl-4 col-lg-4">
                            <div class="main-menu  d-none d-lg-block">
                                <nav>
                                    <ul id="navigation">
                                        <li><a class="active" href="../index.html">home</a></li>
                                        <li><a href="../about.html">About</a></li>
                                        <li><a href="../contact.html">Contact</a></li>
                                    </ul>
                                </nav>
                            </div>
                        </div>
                        <div class="col-12">
                            <div class="mobile_menu d-block d-lg-none"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
    	<!-- breadcam_area_start -->
    <div class="breadcam_area bradcam_bg overlay2">
        <div class="bradcam_text">
            <h2><mark>{organism1:}</mark></h2>
        </div>
    </div>
    <!-- breadcam_area_end -->
    
      <div class="site-section">
		<div class="col-lg-4 sidenav">
			<h4>Jump to Sections</h4>
			<a href="#downloads">Download Files</a>
			<a href="#slr">Single Lethal Reactions</a>
			<a href="#dlr">Double Lethal Reactions</a>		  
			<a href="#tlr">Triple Lethal Reactions</a>
			<a href="#slg">Single Lethal Genes</a>
        	<a href="#dlg">Double Lethal Genes</a>
			<a href="#tlg">Triple Lethal Genes</a>
        </div>
            <div id="downloads" class="container">			
                    <br>
                   <br>
                    <table class="minimalistBlack" border="0" align="center">
                        <tr><td><center><a href="#slr"><font color="maroon"><u>Single lethal reactions</u>
                            <br> (Jsl)</font></a></center></td>
                            <td> <p><a href="../CSV/{organism:}/JSL.csv" download="{organism:}_Jsl.csv"><center><abbr title='Download the Jsl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                        
                        </tr>
                        <tr><td><center><a href="#dlr"><font color="maroon"><u>Double lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JDL.csv" download="{organism:}_Jdl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#tlr"><font color="maroon"><u>Triple lethal reactions</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/JTL.csv" download="{organism:}_Jtl.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#slg"><font color="maroon"><u>Single lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/SGD.csv" download="{organism:}_Sgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#dlg"><font color="maroon"><u>Double lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/DGD.csv" download="{organism:}_Dgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                        <tr><td><center><a href="#tlg"><font color="maroon"><u>Triple lethal genes</u>
                            <br> (Jdl)</font></a></center> </td>
                              <td> <p><a href="../CSV/{organism:}/TGD.csv" download="{organism:}_Tgd.csv"><center><abbr title='Download the Jdl CSV file'><img src='../img/elements/csv.jpg' height='35' width='35'></abbr></a></p></td>
                          
                        </tr>
                    
                    </table>
               
               <br>
			   	<p style = 'line-height: 10px'>
					<img src = '../img/elements/model_link.PNG' width=20 height=20 style='vertical-align: middle' />
                    <font size=4>Model Link:<a href="{link:}" target="blank"> <font color="black"><u>{link:}</u></font></a>
				</font></p>
                        <br>
             <br><br>
             
            </div>
			
            <div class="site-section">
				<div id="slr" class="container">
                    <div>
					<div>
				   <center> 
			   <br><br>
			   <h2>Single Lethal Reactions</h2>
			   <br>
					<table width="50%" align="center">{slrtable:}</table>
					</center>
					</div>
				</div>
					
          </div>
		  
		  <div id="dlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{dlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>
          
		  <div id="tlr" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Reactions</h2>
			   <br>
                <table width="65%" align="center">{tlrtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="slg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Single Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{slgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="dlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Double Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{dlgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>

		  <div id="tlg" class="container">
              <div>
                <div>
               <center> 
			   <br><br>
			   <h2>Triple Lethal Genes</h2>
			   <br>
                <table width="65%" align="center">{tlgtable:}</table>
                </center>
                </div>
            </div>
                
          </div>          
  
    <footer class="footer footer_bg">
        <div class="footer_copy_right">
            <p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved by CASTLE | This template is made with <i class="fa fa-heart-o" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        </div>
    </footer>
          </div> <!-- END .site-section -->

</body>
</html>
    
"""

for line in csv_file:
    if 'Bifidobacteria' in str(line[0]):
        try:
            full_html = html.format(organism = line[0], organism1 = ' '.join([i for i in line[0].split('_')]), gr = line[7],hp = line[9],link = line[8],
                                    slrtable=slr(line), dlrtable=dlr(line), tlrtable=tlr(line),
                                    slgtable=slg(line), dlgtable=dlg(line), tlgtable=tlg(line))
            filename='Synthetic_lethal/'+line[0]+'.html'
            print(filename)
            f = open(filename,'w')
            f.write(full_html)
            f.close()
        except FileNotFoundError:
            continue;
        
    print(line[0])
    
#    break;
    
f1.close()