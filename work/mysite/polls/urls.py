from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('example/', views.example, name='example'),
    path('product/', views.product, name='product'),
    path('rank/', views.rank, name='rank'),
    path('save/', views.save, name='save'),
    path('eln_result/', views.eln_result, name='eln_result'),
    path('link/', views.link, name='link'),
    path('popup/', views.link, name='popup')
]
