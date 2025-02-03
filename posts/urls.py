from django.urls import path
from . import views
urlpatterns =[
    path('', views.index, name='index'),
    path('sol/<str:pk>',views.sol,name='sol'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit-solution/', views.submit_solution, name='submit_solution'),
    path('chat/', views.chat, name='chat'),

]