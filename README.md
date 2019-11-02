# Sirajify

### Docker
```bash
# build
docker build -t siraj:latest .
# run
docker run -d -p 80:5000 siraj:latest
```

`master` branch is automatically pushed to production, so make sure that any CI has passed before merging

### ToDo
- decide if centos or alpine is better for docker base
- simple test
- deploy to heroku?
- automate travis agent pipeline, if we really wanna go crazy
