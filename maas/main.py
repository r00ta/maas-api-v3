from fastapi import FastAPI

from maas.api.v1 import APIv1
from maas.api.v2 import APIv2


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    app = FastAPI(
        title="MAAS API V3",
        name="maasapiv3",
    )

    # Register URL handlers
    APIv1.register(app.router)
    APIv2.register(app.router)
    return app
