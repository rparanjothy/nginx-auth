## Start the Auth app

```
pushd auth-api && \

docker build -t auth_app . && \
docker container run -it --rm --name auth_app1 -p8888:8888 --network bridge auth_app

```

### Start the API app which uses the Auth App

```
docker build -t api_app . && \
docker container run -it --rm --name api_app1 -p80:80 --link auth_app1:auth_app --network bridge api_app

```

### See the redirects

```
# Success
curl -i -H "username:Ram" http://localhost

$ curl -i -H "username:Ram" http://localhost
HTTP/1.1 200 OK
Server: nginx/1.12.2
Date: Wed, 23 Sep 2020 04:51:55 GMT
Content-Type: application/json
Content-Length: 27
Last-Modified: Wed, 23 Sep 2020 01:10:56 GMT
Connection: keep-alive
ETag: "5f6aa0a0-1b"
Accept-Ranges: bytes

{
  "msg": "Welcome!"
}



# Unauth'ed user
curl -i  http://localhost



$ curl -i http://localhost
HTTP/1.1 401 Unauthorized
Server: nginx/1.12.2
Date: Wed, 23 Sep 2020 04:52:20 GMT
Content-Type: application/json
Content-Length: 23
Connection: keep-alive

{"msg":"Unauthorized!"}


```

```

```
