# Generated by Django 5.0.4 on 2024-04-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_id', models.CharField(blank=True, max_length=255, null=True)),
                ('userid_di', models.CharField(blank=True, max_length=255, null=True)),
                ('registered', models.IntegerField(blank=True, null=True)),
                ('viewed', models.IntegerField(blank=True, null=True)),
                ('explored', models.IntegerField(blank=True, null=True)),
                ('certified', models.IntegerField(blank=True, null=True)),
                ('final_cc_cname_di', models.CharField(blank=True, max_length=255, null=True)),
                ('loe_di', models.CharField(blank=True, max_length=255, null=True)),
                ('yob', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('grade', models.FloatField(blank=True, null=True)),
                ('start_time_di', models.DateField(blank=True, null=True)),
                ('last_event_di', models.DateField(blank=True, null=True)),
                ('nevents', models.IntegerField(blank=True, null=True)),
                ('ndays_act', models.IntegerField(blank=True, null=True)),
                ('nplay_video', models.IntegerField(blank=True, null=True)),
                ('nchapters', models.IntegerField(blank=True, null=True)),
                ('nforum_posts', models.IntegerField(blank=True, null=True)),
                ('incomplete_flag', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courses_clean_tabla',
                'managed': False,
            },
        ),
    ]
