from django.urls import path

from . import views

app_name = 'scheduleApp'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('schedule-detail/',views.ScheduleDetailView.as_view(),name="schedule-detail"),
]