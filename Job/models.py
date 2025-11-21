from django.db import models
from django.conf import settings


class Job(models.Model):
    EMPLOYMENT_TYPES = [
        ("full_time", "Полная занятость"),
        ("part_time", "Частичная занятость"),
        ("contract", "Контракт"),
        ("internship", "Стажировка"),
        ("temporary", "Временная работа"),
    ]

    SCHEDULE_TYPES = [
        ("office", "Офис"),
        ("remote", "Удалённо"),
        ("hybrid", "Гибрид"),
    ]

    EXPERIENCE_LEVELS = [
        ("no_exp", "Без опыта"),
        ("junior", "Junior"),
        ("middle", "Middle"),
        ("senior", "Senior"),
    ]

    employer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )

    title = models.CharField(max_length=200, verbose_name="Название вакансии")
    description = models.TextField(verbose_name="Описание вакансии")

    location = models.CharField(max_length=200, verbose_name="Локация (город)")
    salary_from = models.IntegerField(null=True, blank=True, verbose_name="Зарплата от")
    salary_to = models.IntegerField(null=True, blank=True, verbose_name="Зарплата до")

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPES,
        default="full_time",
        verbose_name="Тип занятости"
    )

    schedule = models.CharField(
        max_length=20,
        choices=SCHEDULE_TYPES,
        default="office",
        verbose_name="Формат работы"
    )

    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVELS,
        default="no_exp",
        verbose_name="Требуемый опыт"
    )

    requirements = models.TextField(blank=True, verbose_name="Требования")
    responsibilities = models.TextField(blank=True, verbose_name="Обязанности")

    languages = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Знание языков (через запятую)"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"
        ordering = ['-created_at']
