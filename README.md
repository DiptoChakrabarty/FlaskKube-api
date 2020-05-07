# api


This Project demoestrates how to deploy an API in docker and Kubernetes

the api has been built using Flask and supported by a mysql database 



- Send Post Request 
```sh

curl --header "Content-Type: application/json"   --request POST --data '{
"name": "CSGO",
"price": 40,
"qty": 30,
"description": "Shooter game first person"
}'  10.109.209.60:5000/productadd

```

- Send Get Request

```sh
curl 10.109.209.60:5000/products

```

- Delete Request

```sh
curl --header "Content-Type: application/json"   --request DELETE 10.109.209.60:5000/product/4

```

- Put Request for a product

```sh
 curl --header "Content-Type: application/json"   --request PUT --data '{
"name": "Splinter Cell Chaos Theory",
"price": 100,
"qty": 3,
"description": "Best Stealth game"
}'  10.109.209.60:5000/product/2

```