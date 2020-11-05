from django.urls import path
from .views import ProductList, ProductDetail,ProductCommentList,ProductCommentDetail

urlpatterns = [
    path('api/product',ProductList.as_view()),
    path('api/product/<int:pk>',ProductDetail.as_view()),
    path('api/product_comment', ProductCommentList.as_view()),
    path('api/product_comment/<int:pk>',ProductCommentDetail.as_view()),
]