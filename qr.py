import io

import qrcode

QR_VERSION = 6
MAX_SIZE = 1024


def make_qr(text: str, size: int = 512) -> bytes:
    if not text or not text.strip():
        raise ValueError("Provide some text or a URL to encode.")
    size = max(128, min(size, MAX_SIZE))
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=8,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((size, size))
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()
