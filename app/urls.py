from django.urls import path
from .views import ItemCreateView,ItemDetailView,ItemFilterView,ItemUpdateView,ItemDeleteView
# app_name=app
urlpatterns=[
    path('',ItemFilterView.as_view(),name='index'),
    
    path('detail/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', ItemCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', ItemUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='delete'),
]