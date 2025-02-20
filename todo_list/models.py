from django.db import models
from django.urls import reverse


class ToDoItem(models.Model):

    class Meta:
        ordering = ('-id',)
        verbose_name = "Элемент ToDo"
        verbose_name_plural = "Элементы ToDo"

    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)

    # 2ый более правильный способ: добавляем ссылку перехода после нажатия на Add на форме создания todo
    def get_absolute_url(self):
        return reverse(
            viewname='todo_list:detail',  # ToDoItem будет доступен по todo_list:detail
            kwargs={'pk': self.pk},       # по его primary key
        )

    def __str__(self):
        return self.title