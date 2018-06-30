from mitmproxy import http, ctx

def load(loader):
	ctx.log.info("Loaded script")

def request(flow: http.HTTPFlow) -> None:
	flow.request.headers.add('mitmproxy', 'running')

def response(flow: http.HTTPFlow) -> None:
	flow.response.headers.add('set-cookie', 'admin=true')
