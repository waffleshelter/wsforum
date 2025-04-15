FROM nginx:stable-alpine

WORKDIR /frontend

COPY . /usr/share/nginx/html
COPY /css /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000
CMD [ "nginx", "-g", "daemon off;" ]