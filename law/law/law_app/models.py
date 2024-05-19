from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Case(models.Model):
    case_id = models.BigAutoField(primary_key=True)
    case_number = models.CharField(verbose_name="номер дела", max_length=20)
    judge = models.ForeignKey('Judge', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.case_number

    class Meta:
        db_table = 'cases'


class Judge(models.Model):
    judge_id = models.BigAutoField(primary_key=True)
    judge_name = models.CharField(verbose_name="ФИО судьи", max_length=150)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.judge_name

    class Meta:
        db_table = 'judges'


class Assistant(models.Model):
    assistant_id = models.BigAutoField(primary_key=True)
    assistant_name = models.CharField(verbose_name="ФИО помощника", max_length=150)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    judge = models.ForeignKey(Judge, models.DO_NOTHING, default=1)

    def __str__(self):
        return self.assistant_name

    class Meta:
        db_table = 'assistants'


class Priority(models.Model):
    priority_id = models.BigAutoField(primary_key=True)
    priority_name = models.CharField(verbose_name="приоритет", max_length=50)

    def __str__(self):
        return self.priority_name

    class Meta:
        db_table = 'priorities'


class Query(models.Model):
    query_id = models.BigAutoField(primary_key=True)
    judge = models.ForeignKey(Judge, models.DO_NOTHING)
    case = models.ForeignKey(Case, models.DO_NOTHING)
    query_type = models.ForeignKey('QueryType', models.DO_NOTHING)
    assistant = models.ForeignKey(Assistant, models.DO_NOTHING, blank=True, null=True)
    priority = models.ForeignKey(Priority, models.DO_NOTHING)
    status = models.ForeignKey('Status', models.DO_NOTHING, default=1)
    query_comments = models.TextField(verbose_name="комментарии")
    query_creation_date = models.DateTimeField(verbose_name="дата создания", default=now)

    def __str__(self):
        return self.query_id

    class Meta:
        db_table = 'queries'
        permissions = [
            ("change_task_status", "Can change the status of tasks"),
            ("change_priority", "Can change the priority of tasks"),
            ("edit_comment", "Can edit the comments of tasks"),
            ("change_assistant", "Can change the assistant in charge of tasks"),
            ("can_create", "Can create new tasks"),
        ]


class QueryType(models.Model):
    query_type_id = models.BigAutoField(primary_key=True)
    query_type_name = models.CharField(verbose_name="тип запроса", max_length=200)

    def __str__(self):
        return self.query_type_name

    class Meta:
        db_table = 'query_types'


class Status(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_name = models.CharField(verbose_name="статус", max_length=30)

    def __str__(self):
        return self.status_name

    class Meta:
        db_table = 'statuses'