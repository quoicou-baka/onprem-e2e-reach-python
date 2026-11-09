"""Reachability fixture for the Aikido Box e2e checks: calls the vulnerable PyYAML full_load."""
import sys

import yaml


def load_config(path):
    with open(path) as handle:
        return yaml.full_load(handle)


if __name__ == "__main__":
    print(load_config(sys.argv[1]))
