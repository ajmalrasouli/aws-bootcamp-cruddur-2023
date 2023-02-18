FROM python:3.10-slim-buster

# Inside Container
# make a new folder inside container
WORKDIR /backend-flask

# Outside Container -> Inside Container
# this conains the libraries want to install to run the app
COPY requirements.txt requirements.txt

# Inside Container
RUN pip3 install -r requirements.txt

# cd backend-flask
# export FRONTEND_URL="*"
# export BACKEND_URL="*"
# python3 -m flask run --host=0.0.0.0 --port=4567
# cd ..
# make sure to unlock the port on the port tab
#open the link for 4567 in your browser
# append to the url to /api/activities/home
# you should get back json



# Outside Container -> Inside Container
# . means everything in the current directory
# first period . - /backend-flask (outside container)
# second period . /backend-flask (inside container)
COPY . .

# Set env var (Env Vars)
# inside container and will remain
ENV FLASK_ENV=development
# unset=BACKEND_URL
# unset=FRONTEND_URL

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

# docker build -t  backend-flask ./backend-flask
# docker ps
# docker images
# Run the Container

# docker run --rm -p 4567:4567 -it backend-flask

# docker run --rm -p 4567:4567 -it -e FRONTEND_URL='*' -e BACKEND_URL='*' backend-flask