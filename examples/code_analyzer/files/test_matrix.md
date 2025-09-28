# Test Matrix (Core & NetworkPolicy)

## Format selection
- sort orders: default, prefer-vp9-sort (compat), bitrate-first (custom)
- filters: height>=, vcodec=, acodec=

## Network matrix
- transports: requests, curl_cffi, websockets
- proxies: none, http, https, socks5; invalid scheme → error
- headers: UA default vs site override
- IPv4/IPv6 selection if applicable

## Post-processing
- remux combinations (mp4/mkv/webm)
- concat edge-cases (codec/profile/level mismatches)
- subtitle embedding presence/codec

## Errors mapping
- ExtractorError vs NetworkError vs PostProcessingError
- Retryable vs non-retryable classification & hints
