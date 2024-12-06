FROM python:3.11-alpine AS build

WORKDIR /app/

COPY ./requirements.txt ./
RUN pip install --no-cache-dir --prefix=/install/ -r ./requirements.txt

COPY ./ ./

FROM python:3.11-alpine

WORKDIR /app/

COPY --from=build /install/ /usr/local/

COPY ./ ./

EXPOSE 5000

CMD ["python", "app.py"]
