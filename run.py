import os
import geocoder
g = geocoder.ip('me')
print(g.latlng)
from app import create_app
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

os.system("ffmpeg -i app/static/samplevideo.avi app/static/samplevideo.mp4")

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

app.config['GOOGLEMAPS_KEY'] = "AIzaSyAdDlIx5s93YoFFPbcE49FttW8ZH-ICixA"
GoogleMaps(app)
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)