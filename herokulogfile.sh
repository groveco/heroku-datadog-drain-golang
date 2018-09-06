#!/bin/sh
while true
do
heroku logs -n 1500 --app vast-cove-11097  >> heroku-dd.txt
sleep 30  
done
