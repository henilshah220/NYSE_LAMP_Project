<?php

?>
<html>
<head>
    <title>SQL SELECT Statement</title>
</head>
<body style="background-color:lightblack;">
<table align="center" border="1">
<?php
    $cnx = new mysqli('127.0.0.1', 'root', 'henil202', 'demo');

    if ($cnx->connect_error)
        die('Connection failed: ' . $cnx->connect_error);
    $TS="border: double 5px ; border-spacing: 1px ";
$THS="background-color: #d3eef1; color: ##191919 ; padding: 10px";
$TDS="padding: 10px";
$out="";	
	$out.="<table border=2 >";
	$out.="<th style ='$THS'>Exchange</th><th style ='$THS'>Symbol</th><th style ='$THS'>Company</th><th style ='$THS'>Volume</th><th style ='$THS'>Price</th><th style ='$THS'>Change</th>";
    
    $query = 'SELECT * FROM cs288';
    $cursor = $cnx->query($query);
    while ($row = $cursor->fetch_assoc()) {
        $out.= '<tr>';
        $out.='<td>' . $row['exchange'] . '</td><td>' . $row['symbol'] . '</td><td>' . $row['company'] . '</td><td>' . $row['volume'] . '</td><td>' . $row['price'] . '</td><td>' . $row['change1']  .'</td>';
        $out.= '</tr>';
    }
    echo $out;
        
        
    $cnx->close();
?>
</table>
</body>
</html>
