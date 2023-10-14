import yaml
import sys


class ListLoader:
    list_source: str

    def __init__(self, list_source: str):
        self.list_source = list_source
        return

    def Load(self) -> list:
        fn = self._pick_loader()
        return fn()

    def _pick_loader(self) -> object:
        if '.yaml' in self.list_source or '.yml' in self.list_source:
            return self._yaml
        if 'stdin' in self.list_source:
            return self._stdin
        return 'err'

    def _yaml(self) -> list:
        with open(self.list_source, 'r') as f:
            d = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return d

    def _stdin(self) -> list:
        lines = []
        for line in sys.stdin:
            lines.append(line.replace('\n', ''))
        print(lines)
        return lines