from django.urls import path
from .views import *

urlpatterns = [
    path('account/', AccountView.as_view()),

    path('account/services/', ServiceListCreateView.as_view()),
    path('account/services/<int:pk>/', ServiceRetrieveUpdateDeleteView.as_view()),

    path('account/reviews/', ReviewListView.as_view()),

    # path('account/<int:user_id>/', AccountView.as_view()),
    # path('account/<int:user_id>/reviews/<int:review_id>/', AccountView.as_view()),
]
