from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('<int:id>/', views.detail.as_view(), name="question"),
    path('postes/', views.getPoste.as_view(), name="postes" ),
    path('profiles/', views.getProfiles.as_view(), name="profiles"),
    path('profile/<int:id>/', views.updateProfile, name="profile"),
    path('poste/<int:id>/', views.setPoste.as_view(), name="poste"),
    path('user/<int:id>/', views.getUser.as_view(), name="user"),
    path('auth/', views.Auth.as_view(), name="auth"),
    path('profile/new', views.SetProfile.as_view(), name="newP"),
    path('post/create', views.CreatePost.as_view(), name="CreatePost"),
    path('LikedPosts/<int:id>', views.ApiLikedPosts.as_view(), name="LikedPosts"),

]
