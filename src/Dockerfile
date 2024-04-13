FROM python:latest

WORKDIR /src/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8000

COPY . ./src
# CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000",  "--reload" ]