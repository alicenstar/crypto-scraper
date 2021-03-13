from django.http import HttpResponse
# from uuid import uuid4
# from urllib.parse import urlparse
# from django.core.validators import URLValidator
# from django.core.exceptions import ValidationError
# from django.views.decorators.http import require_POST, require_http_methods
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from main.utils import URLUtil
# from main.models import ScrapyItem

# Create your views here.

def index(request):
    return HttpResponse("New scraper app.")

# def is_valid_url(url):
#     validate = URLValidator()
#     try:
#         validate(url)
#     except ValidationError:
#         return False

#     return True


# @csrf_exempt
# @require_http_methods(['POST', 'GET'])
# def crawl(request):
#     if request.method == 'POST':
#         url = request.POST.get('url', None)

#         if not url:
#             return JsonResponse({'error': 'Missing args'})

#         if not is_valid_url(url):
#             return JsonResponse({'error': 'URL is invalid'})

#         domain = urlparse(url).netloc
#         unique_id = str(uuid4())

#         settings = {
#             'unique_id': unique_id,
#             'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
#         }

#         task