from django.urls import path
from escola import views

urlpatterns = [
    path('', views.AlunoList.as_view(), name='aluno_list'),
    path('aluno/create/', views.AlunoCreate.as_view(), name='aluno_create'),
    path('aluno/<int:pk>', views.AlunoDetailView.as_view(), name='aluno_detail'),
    path('aluno/<int:pk>/update/', views.AlunoUpdate.as_view(), name='aluno_update'),
    path('aluno/<int:pk>/delete/', views.AlunoDelete.as_view(), name='aluno_delete'),
]