from django import template,models

register = template.Library()

@register.simple_tag
def fonction_modele(client):
    return client.get_animaux()
