from django.urls import path

from booking import views


app_name = 'booking'


urlpatterns = [
    path('list/', views.BookingListView.as_view(),
    	name='list'),
    path('reserve/', views.ReserveTable.as_view(),
    	name='reserve'),
]