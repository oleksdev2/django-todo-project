from django.contrib import admin

from todo_list.models import ToDoItem


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", 'description', 'visible', "done"  # добавлено поле visible для считывания значения archived
    list_display_links = "id", "title"

    # получаем значение visible из поля archived
    def visible(self, obj: ToDoItem) -> bool:
        return not obj.archived

    # Как нам объяснить джанго, что visible - это булеан?
    # Надо добавить новое свойство:
    visible.boolean = True  # так мы подскажем джанго, что это булеан поле
    # после этого в админке будут галочки вместо слова "True"