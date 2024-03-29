from django.shortcuts import render

# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text=request.POST['text']
    total_len=len(text)
    real_len=len(text.replace(" ", ""))
    words = text.split()
    words_len = len(words)
    return render(request, 'result.html', {'input_text':text,'total_len':total_len,'real_len': real_len, 'words_len': words_len})
