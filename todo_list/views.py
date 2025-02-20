from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
)

from .forms import ToDoItemForm
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


"""
class ToDoListIndexView(TemplateView):
    template_name = 'todo_list/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo_items'] = ToDoItem.objects.all()
        return context
"""
class ToDoListIndexView(ListView):
    template_name = 'todo_list/index.html'
    queryset = ToDoItem.objects.all()[:3]




"""  класс до создания шаблона todoitem_list.html
 get_context_data здесь только для вывода print, чтобы показать значения

class ToDoListView(ListView):
    template_name = 'todo_list/index.html'
    model = ToDoItem

    # если ниже строку удалить, то в шаблоне в цикле необходимо записать object_list
    #context_object_name = 'todo_items'  #такое же имя как в шаблоне в цикле

    def get_context_data(self, **kwargs):
        print(ToDoItem._meta.app_label)  # выведет todo_list
        print(ToDoItem._meta.model_name) # выведет todoitem
        return super().get_context_data(**kwargs)
"""
class ToDoListView(ListView):
    model = ToDoItem


class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()



class ToDoDetailView(DetailView):
    model = ToDoItem



class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemForm

    # 1ый способ: добавляем ссылку перехода после нажатия на Add на форме создания todo
    def get_success_url(self):
        return reverse(
            viewname='todo_list:detail',
            kwargs={'pk': self.object.pk},
        )