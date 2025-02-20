from django import  forms

from todo_list.models import ToDoItem


class ToDoItemForm(forms.ModelForm):
    title = forms.CharField(max_length=250)

    class Meta:
        model =ToDoItem
        fields = ('title',)