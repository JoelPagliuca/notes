# MITMProxy
```sh
pip3 install mitmproxy
```
(`brew` doesn't come with the API completions while writing scripts)

### Using scripts
Check [`mitmexamplescript.py`](./mitmexamplescript.py) for a couple of things to get started with.
More examples with the mitmproxy [source](https://github.com/mitmproxy/mitmproxy/tree/master/examples)

To run mitm with a script
```sh
mitmproxy -s mitmexamplescript.py [arguments]
# or
mitmdump -s mitmexamplescript.py [arguments]
```

### HTTPS setup
Install and trust `~/.mitmproxy/ca-cert.pem` (created after first run)

Struggling with firefox, could be an mitm [issue](https://github.com/mitmproxy/mitmproxy/issues/156).