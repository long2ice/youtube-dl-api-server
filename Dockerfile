FROM arm32v7/python:3.7
RUN mkdir -p /usr/share/nginx/youtube_dl_api_server
RUN mkdir ~/.pip
RUN echo "[global]\nindex-url = https://mirrors.aliyun.com/pypi/simple/\nformat = columns" > ~/.pip/pip.conf
WORKDIR /usr/share/nginx/youtube_dl_api_server
COPY poetry.lock pyproject.toml /usr/share/nginx/youtube_dl_api_server/
RUN pip3 install poetry
ENV POETRY_VIRTUALENVS_CREATE=false
RUN poetry install
COPY . /usr/share/nginx/youtube_dl_api_server
CMD ['python','main.py']