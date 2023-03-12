from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from streamapp.camera import Stream
from cfg import *

def index(request):
	return render(request, 'streamapp/home.html')

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

stream1 = Stream(stream_link,width,height)
def webstramfunc(request):
	return StreamingHttpResponse(gen(stream1),
					content_type='multipart/x-mixed-replace; boundary=frame')
					