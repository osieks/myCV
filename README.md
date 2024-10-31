Project build for learning Django framework.

Using templates and models for storing data in the default sqlite.

To see this page go to: http://mdziezok.ddns.net:8000/

to run this Dockerfile
```bash
docker build -t my-django-app .
docker run -d -p 8000:8000 --restart always my-django-app
```

or do

```bask
docker compose up --build -d
```
