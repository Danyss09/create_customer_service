from services.db_config import get_connection
import pymysql
def create_customer(first_name, last_name, email, phone_number, address):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            query = """
            INSERT INTO Customers (FirstName, LastName, Email, PhoneNumber, Address)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (first_name, last_name, email, phone_number, address))
            connection.commit()
            
            # Obtener el ID del cliente recién creado
            customer_id = cursor.lastrowid

            return {"message": "Customer created successfully!", "CustomerID": customer_id}
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()