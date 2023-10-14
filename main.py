#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
import yaml
import scraper
import loader
import output


def parse_args() -> Namespace:
    args = ArgumentParser(description='Get company ratings from Glassdoor and others')
    args.add_argument('-c', '--config', help='Path to config file', default='config.yaml')
    args.add_argument('-l', '--list', help='Path to list of companies [myfile.yaml, stdin]', default='companies.yaml')
    args.add_argument('-o', '--output', help='Output format [print, yaml, csv, txt]', default='print')
    return args.parse_args()


def load_file(path: str) -> dict:
    with open(path, 'r') as f:
        d = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return d


def main() -> None:
    args = parse_args()
    config = load_file(args.config)
    companies = loader.ListLoader(args.list).Load()
    rating_scraper = scraper.ScraperFactory(config['rating_source'], config)
    ouptut_renderer = output.OutputFactory(args.output.lower())
    results = {}
    for c in companies:
        if '*' in c:
            # I use the * to denote staffing agenies or other companies I dont want to rate
            results[c] = 'n/a'
            continue
        results[c] = rating_scraper.get_rating(c)
        # print(f'--> {c} = {results[c]}')
    print(results)
    ouptut_renderer.Render(results)
    return


if __name__ == '__main__':
    main()
