import sqlite3
c= sqlite3.connect('movie.db')
print(c) 
c.cursor()

c.execute("INSERT INTO MoviesINFO VALUES('Heropanti','Tiger shroff','2022','abhinai')")
c.execute("INSERT INTO MoviesINFO VALUES('shang chi','simu','2022','mervel')")
c.execute("INSERT INTO MoviesINFO VALUES('Kgf 2','Yash','2022','Prashant neil')")
c.execute("INSERT INTO MoviesINFO VALUES('Inception','Leonardo DiCaprio','2022','Christopher')")

c.commit()
c.close()