# Stage 1: Building the Node application
FROM node AS build

WORKDIR /src/app

COPY package.json index.js ./

RUN npm install


COPY . .

# Stage 2: production for the application
FROM node

WORKDIR /src/app

COPY --from=build /src/app/ ./app
COPY package.json index.js package-lock.json ./
RUN npm install --production

CMD ["node", "index.js"]
