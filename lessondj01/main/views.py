from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("""
                        <h1>You're at the main index.</h1>
                        <p><a href='/data/'>Перейти на страницу DATA</a></p>
                        <p><a href='/test/'>Перейти на страницу TEST</a></p>
                        """
                        )

def data(request):
    return HttpResponse("<h1>Вторая страница DATA</h1>")

def test(request):
    return HttpResponse("<h1>Третья страница TEST</h1>")