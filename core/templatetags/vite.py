import json

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def vite_hmr_client():
    if not settings.DEBUG:
        return ""

    return format_html(
        '<script type="module" src="http://localhost:5173/@vite/client"></script>'
    )


@register.simple_tag
def vite_asset(entry):
    if settings.DEBUG:
        return format_html(
            '<script type="module" src="http://localhost:5173/{}"></script>',
            entry,
        )

    manifest_path = (
        settings.BASE_DIR / "assets" / "dist" / ".vite" / "manifest.json"
    )

    with manifest_path.open(encoding="utf-8") as manifest_file:
        manifest = json.load(manifest_file)

    asset = manifest[entry]
    tags = []

    for css_file in asset.get("css", []):
        tags.append(
            format_html(
                '<link rel="stylesheet" href="{}">',
                static(f"dist/{css_file}"),
            )
        )

    tags.append(
        format_html(
            '<script type="module" src="{}"></script>',
            static(f"dist/{asset['file']}"),
        )
    )

    return mark_safe("".join(str(tag) for tag in tags))
