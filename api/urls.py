from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  path("all_recipe/",views.get_recipes,name = "all_recipe"),
  path("recipe/<str:pk>/",views.get_indi_recipe,name = "individual recipe"),
  path("create_recipe",views.create_recipe,name = "Create"),
  path("delete/<str:pk>/",views.delete_recipe,name = "Delete"),
  path("update/<str:pk>/",views.update_recipe,name = "Update"),
  path("search/<str:pk>/",views.search,name = "search"),
  path("add_review/<str:pk>/",views.add_review,name = "Add review"),
  path("get_recipe_review/<str:pk>/",views.get_recipe_reviews,name = "Get Reviews"),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path("delete_review/<str:pk>/",views.delete_review,name = "Delete Review")
]