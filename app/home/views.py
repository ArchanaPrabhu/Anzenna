from flask import abort,flash,redirect,url_for,render_template, Flask
from flask_login import current_user,login_required
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
from . import home
import os


os.system("ffmpeg -i '{input}' '{output}.mp4'".format(input = '../static/sample_video.avi', output = 'samplevideo.mp4'))


		
@home.route('/')
def homepage():
    return render_template('destino/index.html', title ='Home')

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('destino/index.html', title='Dashboard')

@home.route('/dashboard')
@login_required
def dashboard():
    return render_template('destino/index.html', title='Dashboard')


@home.route('/googlemaps', methods=['GET', 'POST'])
def googlemaps():
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    return render_template('destino/choice.html', title='Google Maps', mymap=mymap )
