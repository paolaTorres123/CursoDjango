from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="about">Acerca de </a></li>
    <li><a href="portfolio">Portafolio</a></li>
    <li><a href="contact">Contacto</a></li>
</ul>
"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esta es la portada</p>
    """)

def about(request):
    return HttpResponse("""
        <h1>Mi WEB personal</h1>
        <h2>Acerca de</h2>
        <p>Me llamo paola torres macias</p>
    """)

def portfolio(request):
    return HttpResponse("""
        <h2>Portafolio</h2>
        <p>Este es el portafolio</p>
    """)

def contact(request):
    return HttpResponse("""
        <h2>Contacto</h2>
        <p>Me llamo paola torres macias</br> 4851294408</p>
    """)
