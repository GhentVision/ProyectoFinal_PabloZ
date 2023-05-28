from django.urls import path
from blog_learning import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('filtrar-fecha/', views.filtrar_por_fecha, name='filtrar_por_fecha'),
    path('blog-detalle/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('blog-crear/', views.crear_post, name='crear_post'),
    path('blog-editar/<int:post_id>/', views.editar_post, name='editar_post'),
    path('blog-eliminar/<int:post_id>/', views.eliminar_post, name='eliminar_post'),
    path('about/', views.about, name='about'),
]