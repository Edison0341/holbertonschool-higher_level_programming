#!/usr/bin/python3
"""List all states in a database"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """connects to MySQL server"""
    try:
        conn = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=username,
                               passwd=password,
                               db=database_name)
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        states = cur.fetchall()
        for state in states:
            print(state)

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL or executing query: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 0-select_states.py username password database")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)
