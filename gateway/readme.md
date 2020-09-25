### Start the API gateway

```
docker build -t apigate . && docker container run -it --rm --name api_gw -p7200:80 apigate

```
