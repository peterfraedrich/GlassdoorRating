#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
import yaml
import scraper
import output


def parse_args() -> Namespace:
    args = ArgumentParser(description='Get company ratings from Glassdoor and others')
    args.add_argument('-c', '--config', help='Path to config file', default='config.yaml')
    args.add_argument('-l', '--list', help='Path to list of companies', default='companies.yaml')
    args.add_argument('-o', '--output', help='Output format [print, yaml, csv]', default='print')
    return args.parse_args()


def load_file(path: str) -> dict:
    with open(path, 'r') as f:
        d = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return d


def main() -> None:
    args = parse_args()
    config = load_file(args.config)
    companies = load_file(args.list)
    rating_scraper = scraper.ScraperFactory(config['rating_source'])
    ouptut_renderer = output.OutputFactory(args.output.lower())
    results = {}
    for c in companies:
        if '*' in c:
            results[c] = 'n/a'
            continue
        conf = config[config['rating_source']]
        results[c] = rating_scraper.get_rating(c, conf['url'], conf['query_key'])
        print(f'--> {c} = {results[c]}')
    print(results)
    ouptut_renderer.Render(results)
    return


if __name__ == '__main__':
    main()
