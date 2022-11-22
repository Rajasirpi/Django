from django.urls import include, path
from rest_framework import routers
from . import views

# created routers
# router = routers.DefaultRouter()
# router.register(r'Restaurant', views.RestaurantViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/restaurants', views.get_post_data.as_view()),
    path('api/restaurants/<int:pk>', views.edit_delete_data.as_view()),
    # path('api/genrestaurants', views.get_postApi.as_view()),
    # path('api/genrestaurants/<int:pk>', views.edit_deleteApi.as_view()),
]