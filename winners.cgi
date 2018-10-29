#! /bin/bash
echo "Content-type: text/html"
echo ""

firstname=$(grep ":" "/home/Team_8/public_html/winners.txt" | cut -d: -f1)
#echo $firstname

prize=$(grep ":" "/home/Team_8/public_html/winners.txt" | cut -d: -f2)
#echo $prize

urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }
#prize=$(urldecode "${prize}")
echo "<html>"
echo "<head>"
echo "        <link rel="stylesheet" type="text/css" href="/~Team_8/maincss.css?version=4"/>"
echo "        <link rel="shortcut icon" href="/~Team_8/favicon.ico" type="image/x-icon">"
echo "        <title> Winners Page </title>"

echo "<script>"
echo "function myFunction() {"
echo "    var str = document.getElementById(\"prize\").innerHTML;" 
echo "    var res = str.replace(/\+/g, \" \");"
echo "    document.getElementById(\"prize\").innerHTML = res;"
echo "}"
echo "</script>"

echo "</head>"

echo "<body onload=\"myFunction()\">"

echo "		<table>"
echo "                        <tr>"
echo "                                <td>"
echo "                                        <img src="/~Team_8/temp_logo.png" align="left""
echo "                                                width="100" height="100">"
echo "                                <td>"
echo "                                <td>"
echo "                                        <h1> University of San Fransokyo </h1>"
echo "                                </td>"
echo "                        </tr>"
echo "                </table>"

echo "        	<div class="topnav" id="myTopnav" align="center">"
echo "                        <a href="/~Team_8/index.html">Home</a>"
echo "                        <a href="/~Team_8/prize.html">Prizes</a>"
echo "                        <a href="lottery.cgi">Lottery</a>"
echo "                        <a class="active""
echo "				href="winners.cgi">Winners</a>"
echo "                </div>"
                
echo "  <center>"
echo "  <br>"
echo "	<h2> List of Previous Winners </h2>"
echo "  <br>"

echo "<table border ="1" cellpadding="12">"
echo " <tr><th>First Name</th>"
for name in $firstname 
do
  echo "<tr><td>$name</td></tr>"
  echo " "
done
echo "</table>"

echo "<table border ="1" cellpadding="12" id ="prize">"
echo " <tr><th>Prize</th>"
for name in $prize 
do
  echo "<tr><td>$name</td></tr>"
done
echo "</table>"
echo " </center>"
 
 
echo "    <div class="footer"><p><b>Team 8</b><br>"
echo "   Joshua Castillo | Misak Tivriktsyan | Francisco Medina | Sevada Haghverdian | Charles Hernandez"
echo "   </p></div>"
   
echo "</body>"
echo "<html>"
exit 0

