import yaml
from pathlib import Path

if __name__ == "__main__":
    conf = yaml.safe_load(Path('yamlFiles/sample2.yaml').read_text())
    print(conf)

