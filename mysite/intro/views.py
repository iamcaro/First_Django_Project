from django.http import HttpResponse

# Create your views here.
data = {
    "Name": "Carolina",
    "Track": "Backend (Python)",
    "Message": "Thanks for your hard work. I'm learning a lot!"
}

def index(request):
    return HttpResponse("Hello, my name is %s and my track is %s. Message to my instructors: %s" % (data["Name"], data["Track"], data["Message"]))