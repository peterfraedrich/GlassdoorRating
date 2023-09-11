<image src="gd10.png" width="500px">

# GlassdoorRating

This repo is a small CLI tool that takes a list of companies (`companies.yaml`) and gets their GlassDoor rating. I created this as a tool for job hunting; my job tracking spreadsheet has a place for Glassdoor rating and I wanted a faster way to get them without having to manually search each company in a browser.

NOTE: Yes, there are GD API creds in this repo; they're not mine. I found them on GitHub from someone elses's repo, so go yell at them

## Installation and Usage
This is a pretty standard Poetry project. Just do the normal Poetry stuff

```
usage: main.py [-h] [-c CONFIG] [-l LIST] [-o OUTPUT]

Get company ratings from Glassdoor and others

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Path to config file
  -l LIST, --list LIST  Path to list of companies
  -o OUTPUT, --output OUTPUT
                        Output format [print, yaml, csv, txt]
```

- CONFIG : path to the config file; this defaults to `config.yaml`
- LIST : list of companies, defaults to `companies.yaml`
- OUTPUT : output format; files are generated with `output.<format>`

## TODO
Not really sure there's going to be futher iteration on this, but if I had to:
- Optional use of `stdin` for companies instead of yaml file
- Get my own API creds
- ~Tighten up the config stuff; there's some "magic params" in `scrape.py` that could be config-ized~
- Testing