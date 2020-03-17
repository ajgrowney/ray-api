from django.urls import path
from .views import CheckCalendar, CheckToday, CheckReminders

urlpatterns = [
    path('calendar/today', CheckToday)
    path('calendar', CheckCalendar)
    path('reminders', CheckReminders)
]
