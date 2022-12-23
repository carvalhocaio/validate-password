FROM python:latest

# sets the working directory
WORKDIR /app

# sets Flask variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=True
ENV FLASK_RUN_HOST=0.0.0.0

# copy dependencies files
COPY Pipfile Pipfile.lock ./

# install pipenv on the container
RUN pip install -U pipenv

# install project dependencies
RUN pipenv install --system

# copy all files and directories from <src> to <dest>
COPY . .

# run application
CMD [ "flask", "run", "--port=8000"]
