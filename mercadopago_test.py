import mercadopago

from django.conf import settings
from django.urls import reverse


mp = mercadopago.MP("TEST-7820321725229373-122610-f8c19c351611443dbc0d72e296501d3d-389742581")
mp.sandbox_mode(True)

# artículos vendidos
items = [
    {
        "title": "Artículo de prueba",
        "quantity": 1,
        "currency_id": "ARS",
        "unit_price": 20
    }
]

# rutas de devolución
back_urls = {
    "success": reverse('eess:payment_received'),
    "failure": reverse('eess:payment_failure'),
    "pending": reverse('eess:payment_pending')
}

# creación de preferencias
preference = {
    "items": items,
    "back_urls": back_urls
}
preferenceresult = mp.create_preference(preference)

# métodos de pago excluídos
excluded_payment_methods = [
    { "id": "master" },
    { "id": "amex" },
    { "id": "diners" },
    { "id": "naranja" },
    { "id": "nativa" },
    { "id": "shopping" },
    { "id": "cencosud" },
    { "id": "cmr_master" },
    { "id": "argencard" },
    { "id": "cordial" },
    { "id": "cordobesa" },
    { "id": "cabal" },
    { "id": "debmaster" },
    { "id": "maestro" },
    { "id": "debcabal" },
    { "id": "pagofacil" },
    { "id": "rapipago" },
    { "id": "bapropagos" },
    { "id": "cargavirtual" },
    { "id": "cobroexpress" },
    { "id": "redlink" },
    { "id": "account_money" }
]
preferenceresult['response']['payment_methods']['excluded_payment_methods'] = excluded_payment_methods
preferenceresult['response']['payment_methods']['installments'] = 1

url = preferenceresult["response"]["sandbox_init_point"]
print( url )
