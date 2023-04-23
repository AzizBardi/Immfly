from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('file', models.URLField(blank=True)),
                ('type', models.CharField(choices=[('video', 'Video'), ('pdf', 'PDF'), ('text', 'Text')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubtitleLanguage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.URLField(blank=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.content')),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('picture', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('contents', models.ManyToManyField(blank=True, to='media.content')),
                ('subchannels', models.ManyToManyField(blank=True, to='media.channel')),
            ],
        ),
        migrations.CreateModel(
            name='AudioLanguage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('file', models.URLField(blank=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.content')),
            ],
        ),
    ]
