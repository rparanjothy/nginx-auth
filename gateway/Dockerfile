
FROM nginx:1.12-alpine
COPY apigateway.conf /etc/nginx/conf.d/default.conf
ADD error.html /usr/share/nginx/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

