
import cv2

class Stream(object):
	def __init__(self,link,width,height):
		self.vcap = cv2.VideoCapture(link)
		self.width = width
		self.height = height
	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		ret, frame = self.vcap.read()
		if not ret:
			print("Can't receive frame....... \n Please Check your video source .....")
		frame = cv2.resize(frame,(self.width,self.height))
		ret, jpeg = cv2.imencode('.jpg', frame)
		return jpeg.tobytes()
