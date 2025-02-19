from django.apps import AppConfig


class TodoListConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_list'
    verbose_name = "Список ToDo"
    #label = 'todo_list'  # в видео 3 объяснение где-то с 40 минуты