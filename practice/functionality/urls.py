
from django.urls import path, include
from .views import CustomerAPIView, Customerget, CustomerUpdate, Customergetall, UserViewSet, UserCustomView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet),
router.register(r'customer',UserCustomView, basename='customer_set'),


urlpatterns = [
    path('api/', include(router.urls)),
    path('member/', CustomerAPIView.as_view(),name='member'),
    path('member-get/<int:pk>',Customerget.as_view(), name='mamber-get'),
    path('member-update/<int:pk>', CustomerUpdate.as_view(), name= 'member-update'),
    path('member-get/', Customergetall.as_view(), name = 'get-customer'),
]