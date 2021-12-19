#!/usr/bin/python3
"""lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities "
                "INNER JOIN states ON cities.state_id = states.id "
                "WHERE states.name = '{:}'"
                "ORDER BY cities.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    print(", ".join(cit[0] for cit in query_rows))
    cur.close()
    conn.close()
