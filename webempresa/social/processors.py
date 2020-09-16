from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url #diccionario con las redes sociales link
    return ctx