## Raspi-sensors
This project uses three different sensors to monitor the temperature, humidity, magnetic field and presence of objects nearby.
The following are the software, tools and devices used:
- Raspberry Pi 3 model-B
- Python 2.7
- Flask for python
- HTML
- Skeleton 
- uWSGI 
- Python virtual envirnoment

## The sensors used are:
- DHT11 for temperature and humidity.
- REED switch for magnetic field
- HSCR04 for proximity
These sensors all give a digital ouptput.


## Basic Working:
The sensor outputs are put onto a local server using the Flask Application. Flask is an extension of python. Flask is a microframework for Python based on Werkzeug and Jinja 2.
The seperate test codes for each sensor are in the sensor code folder and the main flask app is in the `__init__.py` file. The web page is designed using HTML and the style and other accessories are added using the Skeleton CSS.
The static files, that is the images and the CSS files are in the `static` folder while the HTML files are in the `templates` folder.
The same format MUST BE MAINTAINED because the flask application will look for the HTML and CSS files in the `templates` and `static` folder respectively.

## Improvements that can be made to the project:
- Addition of dynamic graphs. High charts provides good graphs for this application.
- Setting up a SQLite database so that data from sensors can be stored and used later.
- Using Heroku to deploy your app onto it so that it is viewable on other networks also.
