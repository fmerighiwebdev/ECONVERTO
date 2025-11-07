# Usa immagine ufficiale di Node
FROM node:20-alpine

# Crea e imposta la working directory
WORKDIR /app

# Copia i file del progetto
COPY package*.json ./
RUN npm install

# Copia il resto dei file
COPY . .

# Imposta la variabile d’ambiente per la build
ENV NODE_ENV=development

# Espone la porta di Next.js
EXPOSE 3000

# Comando di avvio
CMD ["npm", "run", "dev"]
