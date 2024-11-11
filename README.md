# aws-s3-browser

## Dist
Build dist from the [forked repository](https://github.com/emmaliaocode/DjangoS3Browser).
```bash
git clone https://github.com/emmaliaocode/DjangoS3Browser
cd DjangoS3Browser
python setup.py sdist
cp -r dist ./../aws-s3-browser/
```
Use dist in the project.
```bash
cd aws-s3-browser
pipenv install dist/djangos3browser-0.3.tar.gz
```

## Static files
Collect the static files to `STATIC_ROOT` which is set in `settings.py`.
```
python manage.py collectstatic
```
`STATIC_URL` is the URL to use when referring to static files located in `STATIC_ROOT` (e.g., /static/ or [http://www.example.com/static](http://www.example.com/static)).

## Build image
Build Docker image.
```bash
docker build . -t aws-s3-browser:1.0.0
```

## Usage
Run in a Docker container.
```bash
docker run -itd -p 8000:8000 \
-e BUCKET_NAME=[S3_BUCKET_NAME] \
-e AWS_ACCESS_KEY_ID=[YOUR_AWS_ACCESS_KEY_ID] \
-e AWS_SECRET_ACCESS_KEY=[YOUR_AWS_SECRET_ACCESS_KEY] \
--name=aws-s3-browser \
aws-s3-browser:0.1.5
```
- `BUCKET_NAME`: Bucket name for the browser to connect to.
- `AWS_ACCESS_KEY_ID` is optional.
- `AWS_SECRET_ACCESS_KEY` is optional.
