import mysql.connector
import sys
import datetime


class DBConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                user="advent_calendar",
                password="Test123456!",
                host="192.168.188.25",
                port=3306,
                database="advent_calendar"
            )
        except mysql.connector.Error as e:
            print(f"Error connecting to MariaDB Platform: {e.msg}")
            sys.exit(1)
