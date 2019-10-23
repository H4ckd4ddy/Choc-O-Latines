# Crypteur

In french, the term "crypter" is incorrect, we have to use "chiffrer".
So we just make a little Twitter bot to remind that to all peoples who use incorrect term :)

##### Usage :
```
git clone https://github.com/ProTechTion/Crypteur.git
cd Crypteur
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
-d protechtion/crypteur
```

##### With docker-compose :
```
version: '3'
services:
  crypteur:
    image: protechtion/crypteur
    environment:
      CONSUMER_API:
      CONSUMER_API_SECRET:
      ACCES_TOKEN:
      ACCES_TOKEN_SECRET:
```
