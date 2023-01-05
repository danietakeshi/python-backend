import psycopg2

#CONNECT TO DB
con = psycopg2.connect(
    host = "",
    database = "",
    user = "",
    password = "",
    port = ""
)

#OPEN CURSOR
cur = con.cursor()

cur.execute(
    """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
    """
)

rows = cur.fetchall()

for r in rows:
    print(f"table name: {r[0]}")

#CLOSE CURSOR
cur.close()
#CLOSE CONNECTION
con.close()