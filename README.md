# Choc-O-Latine

Expliquons au monde le nom des bonnes choses :)

##### Usage :
```
git clone https://github.com/H4ckd4ddy/Choc-O-Latine.git
cd Choc-O-Latine
pip3 install -r requirements.txt
CONSUMER_API=[your consumer API]
CONSUMER_API_SECRET=[your consumer API secret]
ACCES_TOKEN=[your token]
ACCES_TOKEN_SECRET=[your token secret]
python3 crypteur.py
```

##### With docker :
```
docker run \
--env CONSUMER_API=my_consumer \
--env CONSUMER_API_SECRET=my_consumer_secret \
--env ACCES_TOKEN=my_token \
--env ACCES_TOKEN_SECRET=my_token_secret \
-d hackdaddy/Choc-O-Latine
```

##### With docker-compose :
```
version: '3'
services:
  Choc-O-Latine:
    image: hackdaddy/Choc-O-Latine
    environment:
      CONSUMER_API:
      CONSUMER_API_SECRET:
      ACCES_TOKEN:
      ACCES_TOKEN_SECRET:
```
