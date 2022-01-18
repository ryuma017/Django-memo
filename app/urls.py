from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('new_memo', views.MemoCreateView.as_view(), name='new_memo'),
    path('delete_memo/<int:pk>', views.MemoDeleteView.as_view(), name='delete_memo'),
    path('edit_memo/<int:pk>', views.MemoEditView.as_view(), name='edit_memo'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('contact/success', views.ContactSuccessView.as_view(), name='contact_success'),
]
