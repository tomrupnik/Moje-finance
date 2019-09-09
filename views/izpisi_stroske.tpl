<html>
    <head>
        <title>Izpis</title>
    </head>
    <body>
    <center>
    <center>
    <h2> IZPIS STROSKOV </h2>
        <form action="/izpisi_stroske/vsi_stroski" method="POST">
            <input type="submit" value="Izpisi vse stroske">
        </form>
        <form action="/izpisi_stroske/izpisi_stroske_mesec" method="POST">
            Izpiši stroške za mesec <input type="text" name="mesec">
        </form>
    </center>
    </center>
    </body>
</html>