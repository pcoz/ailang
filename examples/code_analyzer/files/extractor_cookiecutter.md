# Extractor Template (Cookiecutter-ish)

Files:
- {package}/extractor/{slug}.py
- test/test_{slug}_ie.py

{slug}.py:
----------------
from .common import InfoExtractor

class {ClassName}IE(InfoExtractor):
    _VALID_URL = r"""{valid_url}"""
    _TESTS = [
        {{
            'url': '{example_url}',
            'info_dict': {{
                'id': '{example_id}',
                # add fields as needed
            }}
        }}
    ]

    def _real_extract(self, url):
        # 1) Fetch page/API using helpers (avoid raw requests)
        # 2) Parse rich JSON where possible
        # 3) Return info dict with formats/subtitles/thumbnails
        raise NotImplementedError
----------------

Lint/Style:
- import from shared helpers: pagination, m3u8/mpd, auth, json
- no ad-hoc UA/proxy; use NetworkPolicy helpers

Tests:
- add fixture page or VCR-like recording if policy allows
- verify format selection interplay with typical flags
