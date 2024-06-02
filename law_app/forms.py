from django.forms import ModelForm
from law_app.models import Case, Query, Assistant, Judge

class CreateQueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ["query_type", "case", "priority", "query_comments"]
        labels = {
            "query_type": "Тип запроса",
            "case": "Номер дела",
            "priority": "Приоритет",
            "query_comments": "Комментарии",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('id', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['case'].queryset = Case.objects.filter(judge=Judge.objects.get(user=user))


class EditQueryForm(ModelForm):
    class Meta:
        model = Query
        fields = ["query_creation_date", "query_type", "case", "priority", "assistant", "status", "query_comments"]
        labels = {
            "query_creation_date": "Дата создания",
            "query_type": "Тип запроса",
            "case": "Номер дела",
            "priority": "Приоритет",
            "assistant": "Помощник",
            "status": "Статус выполнения",
            "query_comments": "Комментарии",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['query_creation_date'].widget.attrs['readonly'] = True
        self.fields['query_creation_date'].required = False
        if user:
            if (user.groups.filter(name='judges').exists()):
                self.fields['case'].queryset = Case.objects.filter(judge=Judge.objects.get(user=user.id))
                self.fields['assistant'].widget.attrs['disabled'] = True
                self.fields['assistant'].required = False
                self.fields['status'].widget.attrs['disabled'] = True
                self.fields['status'].required = False
            elif (user.groups.filter(name='assistants').exists()):
                assist = Judge.objects.get(assistant=Assistant.objects.get(user=user.id))
                self.fields['case'].queryset = Case.objects.filter(judge=assist)
                self.fields['assistant'].queryset = Assistant.objects.filter(judge=assist)
                self.fields['query_type'].widget.attrs['disabled'] = True
                self.fields['query_type'].required = False
                self.fields['case'].widget.attrs['disabled'] = True
                self.fields['case'].required = False
                self.fields['priority'].widget.attrs['disabled'] = True
                self.fields['priority'].required = False
                self.fields['query_comments'].widget.attrs['disabled'] = True
                self.fields['query_comments'].required = False