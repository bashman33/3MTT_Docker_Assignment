# Stage 1: Build
FROM python:3.11-alpine3.19 as build

WORKDIR /app
COPY . . 

# Stage 2: Runtime
FROM python:3.11-alpine3.19 as runtime

WORKDIR /app
COPY --from=build /app /app

CMD ["python", "odd_even.py"]