# スクレイピングアプリ
- Yahooニュース
- Qiita

# 使用技術 
- フロント
 - HTML 
 - CSS(bootstrap4)
 - JavaScript(jquery)
- サーバーサイド
 - Python(Django)
- 環境構築
 - docker


# 環境構築

## Dockerfile

```Dockerfile:Dockerfile
FROM python:3.7
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1

# Pythonが標準入出力をバッファリングすることを防ぐ。ターミナル(コンテナログなど)直接送信され、
# 出力をリアルタイムに確認できる。これにより、Pythonアプリケーションがクラッシュした場合に備えて、
# 部分的な出力がどこかのバッファーに保持されたり、書き込まれたりすることがなくなる。
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```

## docker-compose.yml

```docker-compose.yml:docker-compose.yml
version: "3"

services:
  db:
    image: postgres
    ports:
      - "5432"
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=password
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

## setting.py

```setting.py:setting.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'db',
        'POST': 5432,
    }
}
```

## bash

```bash:bash
$ docker-compose run web django-admin.py startproject project .
$ docker-compose up -d
$ docker-compose run web python manage.py startapp news
```

## マイグレーション

```bash:bash
$ docker-compose run web python3 manage.py makemigrations
$ docker-compose run web python3 manage.py migrate
```
