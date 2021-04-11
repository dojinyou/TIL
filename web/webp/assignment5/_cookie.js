const http = require('http');

http
	.createServer((req, res) => {
		console.log(req.url, req.headers.cookie);
		res.writeHead(200, { 'Set-Cookie': ['class=AdvWeb', 'credits=3'] });
		res.write('Cookie Testing');
		res.end('.......');
	})
	.listen(2000, () => {
		console.log('2000번 포트에서 대기중...');
	});
