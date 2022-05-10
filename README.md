Python version 3.10.4

## **Instrucciones**

- npm install
- virtualenv venv dentro del directorio **server** (server/venv)
- correr entorno virtual
- crear las variables de entorno dentro del directorio **server** (server/.env)
- npm run server:dependencies
- npm run server:migrations

## **Server Env Variables**

### **Domain Variable**

- DOMAIN (http://server-domain.com)

### **Django Secret Key Variable**

- DRF_SECRET_KEY (run in bash $ openssl rand -base64 32)

### **JWT Variables**

- TOKEN_LIFETIME (min)
- TOKEN_REFRESH_LIFETIME (min)
- ENCRYPTION_TYPE

### **Email Variables**

- EMAIL_HOST
- EMAIL_PORT
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL

### **DB Variables**

- DB_ENGINE
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT

### **AWS S3 Variables**

- S3_ACCESS_KEY
- S3_SECRET_ACCESS_KEY
- S3_STORAGE_BUCKET_NAME
- S3_REGION_NAME
- S3_ENDPOINT_URL
