from pathlib import Path

import django.forms
from django.conf import settings
from django.forms.renderers import DjangoTemplates as BaseDjangoTemplates


class HybridFormRenderer(BaseDjangoTemplates):
    """
    Form renderer that checks the project's own templates first, then
    falls back to Django's built-in form templates for anything not
    overridden. Lets us keep only the templates we actually customize
    (e.g. templates/django/forms/div.html, label.html) instead of a
    full copy of Django's form/widget template tree.
    """

    @property
    def engine(self):
        return self.backend(
            {
                "APP_DIRS": True,
                "DIRS": [
                    settings.BASE_DIR / "templates",
                    Path(django.forms.__file__).parent / "templates",
                ],
                "NAME": "hybridforms",
                "OPTIONS": {},
            }
        )
