FROM python:3.11-alpine
EXPOSE 8000
RUN apk add --no-cache --update git && \
    rm -rf /var/cache/apk/*

ARG GIT_TOKEN
ARG GIT_USER
ARG GIT_REPO
ARG BRANCH

ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache
RUN git clone --depth=1 -b ${BRANCH} https://oauth2:${GIT_TOKEN}@github.com/${GIT_USER}/${GIT_REPO}.git /opt/${GIT_REPO}
RUN apk del git

WORKDIR /opt/${GIT_REPO}/app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY configuration.py conf/configuration.py
RUN python3 manage.py collectstatic --noinput

CMD ["gunicorn", "conf.wsgi:application", "-b", "0.0.0.0:8000"]