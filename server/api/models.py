from django.db import models

LANGUAGES = [
    ('python', 'Python'),
    ('javascript', 'JavaScript'),
    ('css', 'CSS'),
    ('php', 'PHP'),
    ('cpp', 'C++'),
    ('cs', 'C#')
]


class Snippet(models.Model):
    title = models.CharField(max_length=200)
    code = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=100, choices=LANGUAGES)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} ({self.language})'