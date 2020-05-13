from django.shortcuts import render, get_object_or_404
from django.views import generic

from . import models
from apps.homepage.models import Entries, Producto, Grupo

class ProductoListView(generic.ListView):
    model = Producto
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ProductoListView, self).get_context_data()

        try:
            categoria_id = self.kwargs['categoria']
        except:
            categoria_id = None

        categorias = None
        grupos = None
        productos = None

        categorias = models.Categoria.objects.all()
        grupos = Grupo.objects.filter(activo=1).filter(categoria=categorias)

        if categoria_id:
            categorias = get_object_or_404(models.Categoria, categoria_id=categoria_id)
            # productos = Producto.objects.filter(activo=1).filter(categoria=categoria)
            # Producto.objects.filter(categoria=categoria_id)[:6]
        
        context = {
            'categoria': categoria,
            'categorias': categorias,
            'grupos': grupos,
            'productos': productos,
            'pages': Entries.objects.filter(section='home').filter(active=1).order_by('ordered')
        }
        return context

class ProductoDetailView(generic.DetailView):
    model = Producto
    

# def producto_listado(request, divisionPK=None):
#     division = None
#     divisiones = models.Division.objects.all()
#     productos = Producto.objects.filter(available=True)
#     if divisionPK:
#         division = get_object_or_404(Division, slug=divisionPK)
#         productos = Producto.objects.filter(division=division)

#     context = {
#         'division': division,
#         'divisiones': divisiones,
#         'productos': productos
#     }
#     return render(request, 'tienda/producto/listado.html', context)


# def producto_detalle(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     context = {
#         'product': product,
#         'cart_product_form': cart_product_form
#     }
#     return render(request, 'tienda/producto/detalle.html', context)
