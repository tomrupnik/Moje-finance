<html>
    <head>
        <title>Izpis</title>
    </head>
    <body>
    <center>
    <h2> IZPIS STANJA </h2>
        <form action="/izpis_stanja/celotno_stanje" method="POST">
            <input type="submit" value="Izpisi celotno stanje">
        </form>
        <form action="/izpis_stanja/izpisi_stanje_mesec" method="POST">
            Izpiši stroške za mesec <input type="text" name="mesec">
        </form>
    </center>
    </body>
</html>