from django.urls import path

from Authuser.views import get_join_count, join_waitlist


urlpatterns = [
    path('join/', join_waitlist, name='join-waitlist'),
    path("count/", get_join_count),
]