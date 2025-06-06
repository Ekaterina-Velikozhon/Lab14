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
        query = """SELECT distinct * from orders o where o.store_id=%s"""

        cursor.execute(query, (store, ))

        for row in cursor:
            result.append(Ordine(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(store, k, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select DISTINCT o1.order_id as ordine1, o2.order_id as ordine2, count(oi.quantity+ oi2.quantity) as peso
                from orders o1, orders o2, order_items oi, order_items oi2 
                where o1.store_id=%s
                and o1.store_id=o2.store_id 
                and o1.order_date > o2.order_date
                and oi.order_id = o1.order_id
                and oi2.order_id  = o2.order_id
                and DATEDIFF(o1.order_Date, o2.order_date) < %s
                group by o1.order_id, o2.order_id """

        cursor.execute(query, (store, k))

        for row in cursor:
            result.append(Arco(idMap[row["ordine1"]], idMap[row["ordine2"]], row["peso"]))

        cursor.close()
        conn.close()
        return result

