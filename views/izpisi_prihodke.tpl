<html>
    <head>
        <title>Izpis</title>
    </head>
    <body>
    <center>
    <center>
    <h2> IZPIS PRIHODKOV </h2>
        <form action="/izpisi_prihodke/vsi_prihodki" method="POST">
            <input type="submit" value="Izpisi vse prihodke">
        </form>
        <form action="/izpisi_prihodke/izpisi_prihodke_mesec" method="POST">
            Izpiši prihodke za mesec <input type="text" name="mesec">
        </form>
    </center>
    </center>
    </body>
</html>