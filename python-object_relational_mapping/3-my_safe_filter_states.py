#!/usr/bin/python3
"""List all states in a database"""
import MySQLdb
import sys


def list_states(username, password, database_name, search):
    """connects to MySQL server"""
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database_name
        )
        cursor = conn.cursor()
        query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
        cursor.execute(query, (search,))
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or executing query: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print("Usage: python3 file username password database search")
