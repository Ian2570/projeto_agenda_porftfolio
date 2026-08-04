from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('contact/<int:contact_id>', views.contact, name='contact'),
    path('contact/<int:contact_id>/update', views.update, name='update'),
    path('contact/create', views.create, name='create'),
    path('contact/<int:contact_id>/delete', views.delete, name='delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
