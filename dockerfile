# ARG python_image_v="python:3.10.11"
ARG python_image_v="python:3.8"
# python3.10のイメージをダウンロード
FROM ${python_image_v}


RUN pip install pipenv 

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy