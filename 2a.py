import sqlite3
c= sqlite3.connect('movie.db')
print(c) 
c.cursor()

c.execute("INSERT INTO MoviesINFO VALUES('Heropanti','Tiger shroff','2019','abhinai')")
c.execute("INSERT INTO MoviesINFO VALUES('shang chi','simu','2022','mervel')")
c.execute("INSERT INTO MoviesINFO VALUES('Kgf 2','Yash','2022','Prashant neil')")

c.commit()
c.close()