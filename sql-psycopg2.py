import psycopg2

# connect to database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records from artist table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - Select only 'Name' column from table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - Select only 'Queen' from table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query 4 - Select by ArtistId
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - Select only albums by artist with specific artist ID
cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# fetch results - multiple
results = cursor.fetchall()

# fetch results - single
# results = cursor.fetchone()

# close database connection
connection.close()

for result in results:
    print(result)
