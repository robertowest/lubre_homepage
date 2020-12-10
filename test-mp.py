import mercadopago
import json

access_token = "TEST-1534881774722776-120914-533d8cfe4ab6b720548a020387446186-129446137"
mp = mercadopago.MP(access_token)

def index(req, **kwargs):
    preference = {
        "items": [
            {
                "title": "Test",
                "quantity": 1,
                "currency_id": "ARG",
                "unit_price": 180.25
            }
        ]
    }

    mp.create_preference(preference)
