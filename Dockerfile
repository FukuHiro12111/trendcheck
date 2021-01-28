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