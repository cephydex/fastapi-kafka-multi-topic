# FastAPI with Kafka (Single producer with multiple consumers for multiple topics) example app

# Check out code:
[Repository](https://github.com/cephydex/fastapi-kafka-multi-topic)

# How to use this repository

1. Fork/Clone repo

2. Build docker images for project

```sh
docker-compose build .
```

3. Run project in containers

```sh
docker-compose up -d
```

Navigate to: 

[kafka UI](http://localhost:7070).<br/>
[Producer service](http://localhost:7073/docs).<br/>
[Consumer 1 service](http://localhost:7071/docs).<br/>
[Consumer 2 service](http://localhost:7072/docs).<br/>
