from django import forms


class StyledFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if isinstance(field.widget, forms.CheckboxInput):
                continue  # checkbox ma swoją klasę .check, nie .input
            field.widget.attrs.setdefault("class", "input")
