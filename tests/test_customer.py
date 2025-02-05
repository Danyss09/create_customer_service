import unittest
from app import app

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # ✅ Prueba para verificar campos obligatorios
    def test_create_customer_missing_fields(self):
        response = self.app.post('/create_customer', json={})  # Sin datos
        self.assertEqual(response.status_code, 400)            # Espera un error 400
        self.assertIn('error', response.json)                  # Verifica que haya un mensaje de error

    # 🚀 Prueba para creación exitosa de un cliente
    def test_create_customer_success(self):
        payload = {
            "FirstName": "Juan",
            "LastName": "Pérez",
            "Email": "juan.perez@example.com",
            "PhoneNumber": "0999999999",
            "Address": "Av. Amazonas 123"
        }
        response = self.app.post('/create_customer', json=payload)
        self.assertEqual(response.status_code, 200)             # Espera un éxito 200
        self.assertIn('CustomerID', response.json)              # Verifica que se retorne un ID de cliente

    # ❌ Prueba para email duplicado (si hay validación en la BD)
    def test_create_customer_duplicate_email(self):
        payload = {
            "FirstName": "Ana",
            "LastName": "Gómez",
            "Email": "juan.perez@example.com",  # Mismo email de prueba anterior
            "PhoneNumber": "0888888888",
            "Address": "Calle 10"
        }
        response = self.app.post('/create_customer', json=payload)
        self.assertIn('error', response.json)                   # Verifica que haya un mensaje de error
        self.assertNotEqual(response.status_code, 200)          # No debe devolver un 200

if __name__ == '__main__':
    unittest.main()
