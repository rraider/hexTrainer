FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install -r requirements.txt
WORKDIR /usr/src/app/mathtrainer
CMD ["python3", "manage.py", "runserver"]