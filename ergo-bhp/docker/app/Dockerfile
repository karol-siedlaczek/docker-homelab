FROM python:3.11-alpine
EXPOSE 8000
WORKDIR /opt

RUN apk add --no-cache --update git bash

ARG GIT_TOKEN
RUN git clone -b main https://oauth2:${GIT_TOKEN}@github.com/karol-siedlaczek/ergo-bhp.git
RUN pip3 install -r ergo-bhp/app/requirements.txt --no-cache-dir
COPY configuration.py /opt/ergo-bhp/app/conf/configuration.py
RUN python3 ergo-bhp/app/manage.py collectstatic --noinput
ENTRYPOINT [ "python3" ]
CMD [ "ergo-bhp/app/manage.py", "runserver", "0.0.0.0:8000"]