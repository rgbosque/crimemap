import psycopg2
import datetime
from config import config


class DBHelper():

    def connect(self):
        params = config()
        conn = psycopg2.connect(**params)
        return conn

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES (%s);"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()

    def add_crime(self, category, date, latitude, longitude, description):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes(category, date, latitude, longitude, description, created, updated) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            with connection.cursor() as cursor:
                cursor.execute(query, (category, date, latitude,
                                       longitude, description, date, date))
                connection.commit()
        except Exception as e:
            print (e)
        finally:
            connection.close()

    def get_all_crimes(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                named_crimes = []
                for crime in cursor:
                    named_crime = {
                        'latitude': float(crime[1]),
                        'longitude': float(crime[2]),
                        'date': datetime.datetime.strftime(crime[3], '%Y-%m-%d'),
                        'category': crime[4],
                        'description': crime[5]
                    }
                    named_crimes.append(named_crime)
            return named_crimes
        finally:
            connection.close()
