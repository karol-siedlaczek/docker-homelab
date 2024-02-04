FROM haproxy:2.9-alpine
WORKDIR /usr/local/etc/haproxy/

COPY . ./
CMD [ "haproxy", "-f", "/usr/local/etc/haproxy/conf.d" ]