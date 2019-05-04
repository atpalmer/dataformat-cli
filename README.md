# dataformat-cli

## Usage

```
Usage: dataformat [OPTIONS]

Options:
  -i, --in [json|yaml|toml]   Format of data written to STDOUT
  -o, --out [json|yaml|toml]  Format of data read from STDIN
  --help                      Show this message and exit.
```

## Usage Samples
```
$ dataformat -o yaml < mydata.json > mydata.yaml
$ dataformat -i yaml -o toml < mydata.yaml > mydata.toml
$ curl -s httpbin.org/get | dataformat -o yaml
args: {}
headers: {Accept: '*/*', Host: httpbin.org, User-Agent: curl/7.58.0}
origin: 127.0.0.1
url: https://httpbin.org/get
```
