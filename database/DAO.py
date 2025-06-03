from database.DB_connect import DBConnect
from model.arco import Arco
from model.ordine import Ordine
from model.store import Store


class DAO():
    @staticmethod
    def getStores():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.*
                    from stores s """

        cursor.execute(query)

        for row in cursor:
            result.append(Store(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getOrdiniStore(store):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select o.*
                    from orders o 
                    where o.store_id = %s"""

        cursor.execute(query, (store, ))

        for row in cursor:
            result.append(Ordine(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(store, k):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select o.*
                    from orders o 
                    where o.store_id = %s"""

        cursor.execute(query, (store, k))

        for row in cursor:
            result.append(Arco(**row))

        cursor.close()
        conn.close()
        return result

