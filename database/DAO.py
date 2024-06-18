from database.DB_connect import DBConnect
from model.business import Business

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCities():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        select distinct city 
        from business b
        order by city asc
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["city"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(citta):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
        select * 
        from business b 
        where b.city = %s
        """
        cursor.execute(query, (citta, ))
        result = []
        for row in cursor:
            result.append(Business(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(citta, idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
                select b1.business_id as b1Id, b2.business_id as b2Id, b1.latitude as b1Lat, b1.longitude as b1Lon, b2.latitude as b2Lat, b2.longitude as b2Lon
                from business b1, business b2
                where b1.city = b2.city and b1.city = %s and b1.business_id != b2.business_id
                """
        cursor.execute(query, (citta, ))
        result = []
        for row in cursor:
            b1 = idMap[row["b1Id"]]
            b2 = idMap[row["b2Id"]]
            coordB1 = (row["b1Lat"], row["b1Lon"])
            coordB2 = (row["b2Lat"], row["b2Lon"])

            result.append((b1, b2, coordB1, coordB2))
        cursor.close()
        conn.close()
        return result
