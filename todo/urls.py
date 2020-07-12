from django.urls import path
from .views import CheckCalendar, CheckToday, Reminders, Reminder

urlpatterns = [
    path('calendar/today', CheckToday),
    path('calendar', CheckCalendar),
    path('reminders', Reminders),
    path('reminders/<int:id>', Reminder)
]
