from django.shortcuts import render_to_response

def index(request):
  return render_to_response('user.html', { 'vk_name': 'Ришат Шарафиев', 'vk_url': 'http://vk.com/rishatsharafiev' })