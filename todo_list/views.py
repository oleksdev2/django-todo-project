from django.http import (
    HttpRequest,
    HttpResponse, HttpResponseRedirect,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import (
    ToDoItemCreateForm,
    ToDoItemUpdateForm,
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
    # TODO: custom qs, archived   здесь напоминалка о том, что мы в этом списке ограничим список по значению archived, когда будем изучать кастомные квэрисеты и заменим на более лучшие помошники, чем фильтр ToDoItem.objects.filter(archived=False)
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
    #model = ToDoItem
    queryset = ToDoItem.objects.filter(archived=False)  # исключаем из списка архивные (помеченные на удаление) записи

class ToDoListDoneView(ListView):
    # TODO: archived qs,
    queryset = ToDoItem.objects.filter(done=True).all()



class ToDoDetailView(DetailView):
    #model = ToDoItem
    # TODO: archived qs
    queryset = ToDoItem.objects.filter(archived=False)



class ToDoItemCreateView(CreateView):
    model = ToDoItem
    form_class = ToDoItemCreateForm
    #fields = ('title', 'description',)



class ToDoItemUpdateView(UpdateView):
    model = ToDoItem
    template_name_suffix = '_update_form'
    form_class = ToDoItemUpdateForm   # мы можем вместо этого присвоения добавить fields = ( 'title', ......) но тогда не будут применяться переопределения


class ToDoItemDeleteView(DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todo_list:list') # чтобы в момент обращения было выполнено вычисление на какой адрес перенаправлять
    # какой нам шаблон нужен, если мы не указали: ctrl+клик на DeleteView
    # и смотрим значение template_name_suffix = "_confirm_delete" -- нам нужна страничка для подтверждения удаления
    # и в urls.py запишем '<int:pk>/confirm-delete/'

    # При удалении мы хотим помечать объект как удаленный вместо полного удаления
    # Поменяем поведение, когда джанго получает успешно обработанную форму
    # Для этого нужно переопределить метод form_valid(): архивировать, а не удалять объект
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
