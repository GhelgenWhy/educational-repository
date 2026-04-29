"""Configuration Sentry"""

import os

try:
    import sentry_sdk  # type: ignore
except ImportError:
    sentry_sdk = None


def init_sentry() -> None:
    """initialize sentry"""
    dsn = os.getenv("SENTRY_DSN")
    if not dsn or sentry_sdk is None:
        return

    sentry_sdk.init(
        dsn=dsn,
        traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", "1.0")),
        environment=os.getenv("SENTRY_ENVIRONMENT", "development"),
        send_default_pii=False,
    )


init_sentry()
