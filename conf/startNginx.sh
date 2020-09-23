#!/bin/bash
sed -i 's/AUTH_APP/'"$AUTH_APP_PORT_8888_TCP_ADDR"'/g' /etc/nginx/conf.d/default.conf
echo "D"
cat /etc/nginx/conf.d/default.conf
nginx -g "daemon off;"