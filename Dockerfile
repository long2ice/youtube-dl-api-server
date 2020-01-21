FROM python:3.7
RUN mkdir -p /usr/share/nginx/youtube-dl-api-server
RUN mkdir ~/.pip
RUN echo "[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple/\nformat = columns" > ~/.pip/pip.conf
WORKDIR /usr/share/nginx/youtube-dl-api-server
COPY poetry.lock pyproject.toml /usr/share/nginx/youtube-dl-api-server/
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip3 install poetry
RUN poetry install
COPY . /usr/share/nginx/youtube-dl-api-server