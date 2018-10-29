#!/bin/bash
echo "Content-type: text/html"
echo ""

urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }
QUERY_STRING=$(urldecode "${QUERY_STRING}")

# HTML/CSS PART #
cat << EOF

<!DOCTYPE html>
<html>
<head>
		<link rel="stylesheet" type="text/css" 
			href="/~Team_8/maincss.css?version=10"/>
		<link rel="shortcut icon" href="/~Team_8/favicon.ico?" type="image/x-icon">
		<title> Lottery </title>
</head>

<body>
		<table>
			<tr>
				<td>
					<img src="/~Team_8/temp_logo.png" align="left"
                        			width="100" height="100">
				<td>
				<td> 
                        		<h1> University of San Fransokyo </h1>
				</td>
			</tr>
		</table>
   		
		<div class="topnav" id="myTopnav" align="center">
                        <a 
                        href="/~Team_8/index.html">Home</a>
                        <a href="/~Team_8/prize.html">Prizes</a>
                        <a class="active" href="lottery.cgi">Lottery</a>
                        <a href="winners.cgi">Winners</a>
                </div>
                
                <div class="footer"><p><b>Team 8</b><br>
Joshua Castillo | Misak Tivriktsyan | Francisco Medina | Sevada Haghverdian | Charles Hernandez
</p></div>
                
</body>
</html>


EOF
# END HTML/CSS PART #

saveIFS=$IFS
IFS="=&"
parms=($QUERY_STRING)
firstname=${parms[1]}
year=${parms[3]}
email=${parms[5]}
phone=${parms[7]}
carrier=${parms[9]}
IFS=$saveIFS

#echo $firstname
#echo $year
#echo $email
#echo $phone


firstImg=$((1 + RANDOM % 6))
secondImg=$((1 + RANDOM % 6))
thirdImg=$((1 + RANDOM % 6))

echo "<br>"
echo "<center>"
echo '<img src='/~Team_8/$firstImg''.png' alt="RandomImage1" height="150" width="150">'
echo '<img src='/~Team_8/$secondImg''.png' alt="RandomImage2" height="150" width="150">'
echo '<img src='/~Team_8/$thirdImg''.png' alt="RandomImage3" height="150" width="150">'
echo "<br>"

#echo $firstImg
#echo $secondImg
#echo $thirdImg
echo "</center>"

if [ $firstImg -eq $secondImg ] && [ $firstImg -eq $thirdImg ] && [ $secondImg -eq $firstImg ] && [ $secondImg -eq $thirdImg ] && [ $thirdImg -eq $firstImg ] && [ $thirdImg -eq $secondImg ]; then
echo "<br>"
echo "You have won a Category A Prize! Choose your prize:"

cat << EOF
<!DOCTYPE html>
<html>

<head>
		<link rel="stylesheet" type="text/css" 
			href="/~Team_8/maincss.css?version=10"/>
		<link rel="shortcut icon" href="/~Team_8/favicon.ico" type="image/x-icon">
		<title> Lottery </title>
</head>

<body>
                
<form action="/~Team_8/cgi-bin/lottery_prize.cgi" method="get">
        <input type="hidden" name="firstname" value="${firstname}">
        <input type="radio" name="prize" value="Free Tuition For A Semester">Free Tuition For A Semester<br>
        <input type="radio" name="prize" value="Laptop Of Your Choice From USF Store">Laptop Of Your Choice From USF Store<br>
        <input type="radio" name="prize" value="Free Housing For a Semester">Free Housing For a Semester<br>
        <input type="submit" value="SUBMIT">
</form>
</body>
</html>

EOF
mail -s "You have won a Category A Prize!" $email
mail -s "You have won a Category A Prize!" $phone@$carrier

########################################################################

elif [ $firstImg -eq $secondImg ] || [ $firstImg -eq $thirdImg ] || [ $secondImg -eq $firstImg ] || [ $secondImg -eq $thirdImg ] || [ $thirdImg -eq $firstImg ] || [ $thirdImg -eq $secondImg ]; then
echo "<br>"
echo "You have won a Category B Prize! Choose your prize:"

cat << EOF
<!DOCTYPE html>
<html>

<head>
		<link rel="stylesheet" type="text/css" 
			href="/~Team_8/maincss.css?version=10"/>
		<link rel="shortcut icon" href="/~Team_8/favicon.ico" type="image/x-icon">
		<title> Lottery </title>
</head>

<body>
                
<form action="/~Team_8/cgi-bin/lottery_prize.cgi" method="get">
        <input type="hidden" name="firstname" value="${firstname}">
        <input type="radio" name="prize" value="Free Books For A Semester">Free Books For A Semester<br>
        <input type="radio" name="prize" value="Giftcard For USF Store">Giftcard For USF Store<br>
        <input type="radio" name="prize" value="Free Parking Pass">Free Parking Pass<br>
        <input type="submit" value="SUBMIT">
</form>
</body>
</html>

EOF
mail -s "You have won a Category B Prize!" $email
mail -s "You have won a Category B Prize!" $phone@$carrier

########################################################################


else
echo "<br>"
echo "You lose! Try again!"
fi

exit 0
