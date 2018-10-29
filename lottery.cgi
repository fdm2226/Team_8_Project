#! /bin/bash
echo "Content-type: text/html"
echo ""

cat << EOF
<head>
  <title>Lottery Page</title>
	<link rel="stylesheet" type="text/css" href="/~Team_8/maincss.css?version4"/>
	<link rel="shortcut icon" href="/~Team_8/favicon.ico" type="image/x-icon">
 
<script type="text/javascript">
  function openselect()
  {
  if (document.myform.phone.value.length !=0)
  {
    document.myform.carrier.disabled = false;
  }
  else
  {
  document.myform.carrier.disabled = true;
  }
  }
  </script>
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
  			<a href="/~Team_8/index.html">Home</a>
			<a href="/~Team_8/prize.html">Prizes</a>
  			<a class="active" 
				href="lottery.cgi">Lottery</a>
  			<a href="winners.cgi">Winners</a>
		</div>

<br>
<center>
<h2>Please enter your information:</h2>
<form id="myform" name="myform" action="/~Team_8/cgi-bin/lottery_spin.cgi" method="get">
<table>
<tr>
<td>First Name:</td><td><input type="text" name="firstname" value="" required></td>
</tr>
<tr>
<td>Year:</td>
<td><select name="year" required> 
<option value="Freshman">Freshman</option>
<option value="Sophomore">Sophomore</option>
<option value="Junior">Junior</option>
<option value="Senior">Senior</option>
<option value="Graduate">Graduate</option>
</select></td>
</tr>
<tr>
<td>Email Address:</td><td><input type="text" name="email" value="" required></td>
</tr>
<tr>
<td>Cell Phone Number:</td><td><input type="text" name="phone" id="phone" onchange="openselect()"></td>
</tr>
<tr>
<td>Carrier:</td><td>

<select name="carrier" id="carrier" disabled="disabled"> 
<option value="message.alltel.com">Alltel</option>
<option value="txt.att.net">AT&T</option>
<option value="myboostmobile.com">Boost Mobile</option>
<option value="sms.mycricket.com">Cricket</option>
<option value="mymetropcs.com">Metro PCS</option>
<option value="messaging.sprintpcs.com">Sprint</option>
<option value="vtext.com">Straight Talk</option>
<option value="tmomail.net">T-Mobile</option>
<option value="email.uscc.net">US Cellular</option>
<option value="vtext.com">Verizon</option>
<option value="test.wireless.alltel.com">Virgin Mobile</option>
</select></td>
</tr>
<tr>
<td></td>
<td><input type="submit" value="SPIN TO WIN"></td>
</tr>
</table>
</form>
</center>

<div class="footer"><p><b>Team 8</b><br>
Joshua Castillo | Misak Tivriktsyan | Francisco Medina | Sevada Haghverdian | Charles Hernandez
</p></div>
</body>
EOF

exit 0
