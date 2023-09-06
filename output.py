import yaml
import csv


class Renderer:
    @classmethod
    def Render(cls, data: dict) -> None:
        return None


class Print(Renderer):

    def Render(cls, data: dict) -> None:
        for k, v in data.items():
            print(f'--> {k} = {v}')
        return


class YAML(Renderer):

    def Render(cls, data: dict) -> None:
        with open('output.yaml', 'w+') as f:
            d = yaml.dump(data)
            f.write(d)
        return


class CSV(Renderer):

    def Render(self, data: dict) -> None:
        with open('output.csv', 'w+') as f:
            file = csv.DictWriter(f, ['company', 'rating'], dialect="excel")
            file.writeheader()
            d = [{'company': k, 'rating': v} for k, v in data.items()]
            file.writerows(d)
        return


def OutputFactory(method: str):
    if method == 'print':
        return Print()
    elif method == 'yaml':
        return YAML()
    elif method == 'csv':
        return CSV()
    else:
        return Renderer
