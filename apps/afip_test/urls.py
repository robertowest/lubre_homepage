from django.conf import settings
from django.urls import path
from django.views.static import serve

from django_afip import views
from . import views as test_views

app_name = "afip_test"

urlpatterns = [
    path("invoices/pdf/<int:pk>", views.ReceiptPDFView.as_view(), name="receipt_displaypdf_view"),
    path("invoices/pdf/<int:pk>", test_views.ReceiptPDFDownloadView.as_view(), name="receipt_pdf_view"),
    path("media/<path>", serve, {"document_root": settings.MEDIA_ROOT}),
]
