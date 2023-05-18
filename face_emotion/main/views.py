from django.shortcuts import render
import cv2

# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def stream_video(request):
    cap = cv2.VideoCapture(0)  # Open the default camera
    if not cap.isOpened():
        return render(request, 'stream_error.html')
    
    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            break
        
        # Perform any processing or analysis on the frame using OpenCV
        # You can also stream the processed frame to the user
        
        _, jpeg = cv2.imencode('.jpg', frame)  # Encode the frame as JPEG
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')

    cap.release()
    
def streamView(request):
    return StreamingHttpResponse(stream_video(request), content_type='multipart/x-mixed-replace; boundary=frame')

def uploadView(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        # Process the uploaded image using OpenCV
        # You can save it to disk or perform any other operations
    return render(request, 'upload.html')