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
curl -H "username:Ram" http://localhost
```
