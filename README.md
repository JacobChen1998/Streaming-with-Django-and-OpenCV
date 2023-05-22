<h1> Streaming with Django and OpenCV </h1>

This is a simple example to demonstrate how to stram your source on your website.
Here we use two packages : [Django](https://www.djangoproject.com/) and [OpenCV](https://opencv.org/)


## Prerequisites 
- Python > 3.6

## Quick start with anaconda 

#### 0. Clone and into project 
```
    cd Streaming-with-Django-and-OpenCV/
```



#### 1. Environment create
```
$    conda create --name django-stream python=3.8
```

#### 2. Environment activate
```
$    conda activate django-stream
```

#### 3. Packages install
```
$    pip install -r requirements.txt
```

#### 4. Replace playing source in [cfg.py](https://github.com/JacobChen1998/Streaming-with-Django-and-OpenCV/blob/main/cfg.py)
```
   stream_link =  <your source>
```

#### 5. Run the server
```
$   python manage.py runserver
```

### 6. Go to 127.0.0.1:8000 with your browser than enjoy!


## Support source type:

###### :white_check_mark: webcam (stream_link=0)

###### :white_check_mark: RTSP source (stream_link="rtsp://.........")

###### :white_check_mark: .mp4

###### :white_check_mark: .3gp

###### :white_check_mark: .avi

###### :white_check_mark: .MOV


## :warning: Notice :warning:
The local video can not play is normal, you must make your video openable with browser detectly first.

This [http.server](https://docs.python.org/3/library/http.server.html) document can help you.
