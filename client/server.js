import express from 'express';

import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);

const __dirname = path.dirname(__filename);

const app = express();

app.use(express.static(__dirname));

app.get('/', (req, res) => {
   res.sendFile(__dirname + '/index.html', { contentType: 'text/html' });
});

app.listen(3333, () => {
   console.log('Server runing on port 3333');
});
