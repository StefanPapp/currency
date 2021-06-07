# README
We have created a python module. 

docker build . -t stefanpapp/currencyconverter
docker run -it stefanpapp/currencyconverter:latest /bin/bash
docker run stefanpapp/currencyconverter:latest python -m currency_converter -i EUR -o USD -a 10


# Distribute
docker push stefanpapp/currencyconverter