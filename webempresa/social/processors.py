from .models import Link

def contexto(request):
   
    contexto = {}
    links = Link.objects.all()
    
    for link in links:
        
        contexto[link.key] = link.url
    
    return contexto