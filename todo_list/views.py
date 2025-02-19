from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)

from .models import ToDoItem

def index_view(request: HttpRequest) -> HttpResponse:
    """
    todo_items = [
        'item 1',
        'item 2',
    ]
    """
    todo_items = ToDoItem.objects.order_by('-id').all()  # минус - сортировка в обратную сторону
    return render(request,
                  template_name='todo_list/index.html',
                  context={'todo_items':todo_items}
                  )

class ToDoListIndexView(TemplateView):
    template_name = 'todo_list/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_items'] = ToDoItem.objects.all()
        return context


class ToDoListView(ListView):
    template_name = 'todo_list/index.html'
    model = ToDoItem

    # если ниже строку удалить, то в шаблоне в цикле необходимо записать object_list
    #context_object_name = 'todo_items'  #такое же имя как в шаблоне в цикле

    def get_context_data(self, **kwargs):
        print(ToDoItem._meta.app_label)  # выведет todo_list
        print(ToDoItem._meta.model_name) # выведет todoitem
        return super().get_context_data(**kwargs)

