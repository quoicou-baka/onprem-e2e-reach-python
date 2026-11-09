# onprem-e2e-reach-python

Fixture for the Aikido Box reachability check (Python worker). `app.py` calls `yaml.full_load` from a vulnerable PyYAML pin; `requests` is pinned but never imported.
