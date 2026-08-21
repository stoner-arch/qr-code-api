# QR Code Generator API

Generate a QR code PNG from any text or URL.

## Endpoints

- `GET /api/qr?text=<text>&size=<128-1024>` — returns a PNG image (default size 512)
- `GET /api/quota` — tier + remaining calls

## Auth

`X-API-Key` header (demo keys: `demo-free`, `demo-pro`) or RapidAPI proxy secret.

## Workflow

```bash
# from the repo root
python -m pytest
git add . && git commit -m "msg" && git push
```

Push to GitHub `main` → Render auto-deploys.
