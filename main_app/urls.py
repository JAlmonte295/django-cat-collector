from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cat_index, name='cat-index'),
    # new route below
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy-create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy-detail'),
    path('toys/', views.ToyList.as_view(), name='toy-index'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy-delete'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy-update'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.associated_toy, name='assoc-toy'),
    path('cats/<int:cat_id>/unassoc_toy/<int:toy_id>/', views.unassociated_toy, name='unassoc-toy'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),

]