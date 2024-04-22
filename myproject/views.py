from django.http import HttpResponse

def home(request):
    # HTML 문자열 직접 반환
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Todolist 시작!</title>
    </head>
    <body>
        <h1>Todolist 시작!</h1>
        <form action="/todos/">
            <button type="submit">시작</button>
        </form>
    </body>
    </html>
    """
    return HttpResponse(html)
