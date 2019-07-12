from django.shortcuts import render
import requests
import re

def search_page(request):
    return render(request, 'search/search.html')

def get_photo(request):
    get_url = request.GET.get('get_photo')
    url_json = requests.get(get_url).text
    pattern = r'<meta property="og:image" content="(.*)".*\/>'
    find_full_photo = re.findall(pattern, url_json)
    content = {'get_photo':find_full_photo[0]}
    return render(request, 'search/getphoto.html', content)
