from django.urls import path
from .views import CheckCalendar, CheckToday, Chores, Reminders, Reminder

urlpatterns = [
    path('calendar/today', CheckToday),
    path('calendar', CheckCalendar),
    path('chores', Chores),
    path('reminders', Reminders),
    path('reminders/<int:id>', Reminder)
]
