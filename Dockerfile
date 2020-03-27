FROM python:3
ENV ALLOWED_HOST=localhost
ENV DEBUG=False
WORKDIR /usr/src/app
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY ./mathtrainer ./mathtrainer
COPY ./docker/run.sh ./mathtrainer/run.sh
WORKDIR /usr/src/app/mathtrainer
RUN python3 manage.py collectstatic --no-input
CMD ["/bin/sh", "run.sh"]
