from django import  forms

from todo_list.models import ToDoItem


class ToDoItemCreateForm(forms.ModelForm):
    #title = forms.CharField(max_length=250) # в таком виде он тут лишний,
    #  а вот если хотим переопределить поле:
    #title = forms.CharField(max_length=250, widget=forms.Textarea())
    #  само правильно через виджет в классе Meta:

    class Meta:
        model =ToDoItem
        fields = ('title', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 5}),
        }
        help_texts = {
            'description': 'Это поле для ввода текста описания.',
        }
