from django.urls import path
from .views import Chores, Reminders, Reminder

urlpatterns = [
    path('chores', Chores),
    path('reminders', Reminders),
    path('reminders/<int:id>', Reminder)
]
