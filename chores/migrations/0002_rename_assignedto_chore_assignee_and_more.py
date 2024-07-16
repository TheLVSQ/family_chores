# Generated by Django 4.2.14 on 2024-07-16 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore',
            old_name='assignedTo',
            new_name='assignee',
        ),
        migrations.RenameField(
            model_name='familymember',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='familymember',
            old_name='lastName',
            new_name='last_name',
        ),
        migrations.RemoveField(
            model_name='chore',
            name='schduledFor',
        ),
        migrations.AddField(
            model_name='chore',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='chore',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='chore',
            name='estimated_time',
            field=models.IntegerField(blank=True, help_text='Estimated time in minutes', null=True),
        ),
        migrations.AddField(
            model_name='chore',
            name='frequency',
            field=models.CharField(choices=[('DAILY', 'Daily'), ('EVERY_OTHER_DAY', 'Every Other Day'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('ANNUALLY', 'Annually'), ('CUSTOM', 'Custom')], default='WEEKLY', max_length=100),
        ),
        migrations.AddField(
            model_name='chore',
            name='priority',
            field=models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='MEDIUM', max_length=100),
        ),
        migrations.AddField(
            model_name='chore',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='familymember',
            name='member_type',
            field=models.CharField(choices=[('ADULT', 'Adult'), ('CHILD', 'Child')], default='CHILD', max_length=5),
        ),
        migrations.AddField(
            model_name='familymember',
            name='username',
            field=models.CharField(default='<django.db.models.fields.CharField> <django.db.models.fields.CharField>', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='chore',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chore',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
