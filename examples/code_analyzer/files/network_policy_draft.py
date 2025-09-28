# NetworkPolicy — Draft Module (Python)

"""Centralizes all network behavior decisions for yt-dlp.
Extractors and core call into this module; they must not hand-roll
proxy parsing, TLS fingerprints, or transport selection."""

from __future__ import annotations
from typing import Literal, Optional

class NetworkPolicy:
    def __init__(self, params: dict):
        self._p = params

    def resolve_proxy(self, url: str, opts: dict) -> Optional[str]:
        """Return a validated proxy URL or None. Enforce scheme & host sanity."""
        proxy = opts.get('proxy') or self._p.get('proxy')
        if proxy and '://' not in proxy:
            # Explicitly require scheme; avoid silent http:// defaulting
            raise ValueError('Proxy must include scheme, e.g., http://host:port')
        return proxy

    def user_agent(self, site_hint: Optional[str] = None) -> str:
        ua = self._p.get('http_headers', {}).get('User-Agent')
        if ua:
            return ua
        # Allow per-site overrides; fall back to curated UA
        return self._p.get('default_ua', 'yt-dlp/NetPolicy')

    def should_impersonate(self, site_hint: Optional[str] = None) -> bool:
        # Single switch + allow per-site overrides
        if site_hint and site_hint in self._p.get('impersonate_sites', set()):
            return True
        return bool(self._p.get('impersonate', False))

    def transport(self, opts: dict) -> Literal['requests', 'curl_cffi', 'websockets']:
        if self.should_impersonate(opts.get('site_hint')):
            return 'curl_cffi'
        return opts.get('transport', self._p.get('transport', 'requests'))
