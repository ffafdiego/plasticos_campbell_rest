from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from productos.views import ProductViewSet,ImageViewSet
from productos import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'productos', ProductViewSet)
router.register(r'images', ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^productos/products/$', views.get_image),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += static('productos/product_images/',document_root="product_images")
urlpatterns += static('images/product_images/',document_root="product_images")
urlpatterns += staticfiles_urlpatterns()
