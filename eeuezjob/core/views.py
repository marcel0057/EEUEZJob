from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.conf import settings

def test_supabase_api(request):
    url = "https://skigrzhriaficygtyghb.supabase.co/rest/v1/your_table"
    headers = {
        "apikey": settings.SUPABASE_API_KEY,
        "Authorization": f"Bearer {settings.SUPABASE_API_KEY}",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers)
    return JsonResponse(response.json(), safe=False)