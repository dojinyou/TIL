const express = require('express');
const path = require('path');

const app = express();

app.set('port', process.env.PORT || 2000);
app.get('/', (req, res) => {
	// res.sendFile(path.join(__dirname, './index.html'));
	res.send('Hello Expresss!');
});

app.listen(app.get('port'), () => {
	console.log(`App listening at http://localhost:${app.get('port')}`);
});
