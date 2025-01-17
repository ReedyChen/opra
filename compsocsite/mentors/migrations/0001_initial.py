# Generated by Django 2.2 on 2019-11-25 06:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mentors.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=4)),
                ('number', models.CharField(default='1000', max_length=4)),
                ('name', models.CharField(default='none', max_length=50)),
                ('instructor', models.CharField(default='none', max_length=50)),
                ('time_slots', models.CharField(default='[]', max_length=500)),
                ('feature_cumlative_GPA', models.IntegerField(default=0)),
                ('feature_has_taken', models.IntegerField(default=0)),
                ('feature_course_GPA', models.IntegerField(default=0)),
                ('feature_mentor_exp', models.IntegerField(default=0)),
                ('mentor_cap', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Instrcutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied', models.BooleanField(default=False)),
                ('RIN', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)])),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('GPA', mentors.models.MinMaxFloat(default=0)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('recommender', models.CharField(default='', max_length=50)),
                ('compensation', models.CharField(choices=[('n', 'No Preference'), ('p', 'Pay ($14/hour) '), ('c', 'Credit')], default='n', max_length=1)),
                ('studnet_status', models.CharField(choices=[('i', 'International'), ('d', 'Domestic')], default='i', max_length=1)),
                ('employed_paid_before', models.BooleanField(default=False)),
                ('mentored_non_cs_bf', models.BooleanField(default=False)),
                ('time_slots', models.CharField(default='[]', max_length=1000)),
                ('other_times', models.CharField(default='', max_length=1000)),
                ('relevant_info', models.CharField(default='', max_length=1000)),
                ('course_pref', models.CharField(max_length=10000)),
                ('mentored_course', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='mentors.Course')),
            ],
        ),
        migrations.CreateModel(
            name='KeyValuePair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=240)),
                ('value', models.CharField(db_index=True, max_length=240)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.Dict')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_grade', models.CharField(choices=[('a', 'A'), ('a-', 'A-'), ('b+', 'B+'), ('b', 'B'), ('b-', 'B-'), ('c+', 'C+'), ('c', 'C'), ('c-', 'C-'), ('d+', 'D+'), ('d', 'D'), ('f', 'F'), ('p', 'Progressing'), ('n', 'Not Taken')], default='n', max_length=1)),
                ('have_taken', models.BooleanField(default=False)),
                ('mentor_exp', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentors.Mentor')),
            ],
        ),
    ]
