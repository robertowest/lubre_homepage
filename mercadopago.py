import mercadopago

from django.conf import settings
from django.urls import reverse


mp = mercadopago.MP("TEST-7820321725229373-122610-f8c19c351611443dbc0d72e296501d3d-389742581")
mp.sandbox_mode(True)
preference = {
    "items": [
        {
            "title": "Título del art.",
            "quantity": 1,
            "currency_id": "ARS",
            "unit_price": 20
        }
    ],
}    
preferenceresult = mp.create_preference(preference)

preferenceresult['response']['back_urls']['success'] = reverse('eess:payment_received')
preferenceresult['response']['back_urls']['failure'] = reverse('eess:payment_failure')
preferenceresult['response']['back_urls']['pending'] = reverse('eess:payment_pending')

url = preferenceresult["response"]["sandbox_init_point"]
print( url )
