FROM node:19-alpine3.16
LABEL cowsay.version=v2
RUN apk update && apk add bash
ENV PORT=8080
RUN mkdir -p /var/node
COPY src/ /var/node/
WORKDIR /var/node
RUN npm install
COPY entry-point.sh /var/node
ENTRYPOINT /var/node/entry-point.sh $PORT
