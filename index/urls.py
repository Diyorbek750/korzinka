from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/detail',views.product_detail,name='product_detail'),
    path('<int:pk>/addremovesaved',views.AddRemoveSavedView.as_view(),name='addremovesaved'),
    path('saveds/',views.SavedView.as_view(),name='saveds'),
    path('<str:category_name>/category',views.CategoryView.as_view(),name='category')
]
