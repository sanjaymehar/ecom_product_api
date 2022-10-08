from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.

# For fetching all Product
class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # For page caching
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

# For Creating Product
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# For Fetching single Product
class ProductRetrieve(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # For page caching  
    @method_decorator(cache_page(60*60*2))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

# For Updating Product
class ProductUpdate(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# For Deleting Product
class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 