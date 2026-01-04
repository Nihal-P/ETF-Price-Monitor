# Source used: 
    # https://www.docker.com/blog/how-to-dockerize-react-app/
    # https://create-react-app.dev/docs/deployment/#static-server

# minimal node image
FROM node:18-alpine


WORKDIR /app

COPY package*.json ./

# install dependencies
RUN npm install

COPY . .

RUN npm run build

# better for production than npm start
RUN npm install -g serve

EXPOSE 3000

CMD ["serve", "-s", "build", "-l", "3000"]