from app.mcp.config import get_settings
from app.mcp.server import mcp

settings = get_settings()

if __name__ == "__main__":
    transport_kwargs = {}
    if settings.transport in ("http", "streamable-http"):
        transport_kwargs["host"] = "0.0.0.0"
        transport_kwargs["port"] = settings.port

    mcp.run(
        transport=settings.transport,
        show_banner=False,
        **transport_kwargs,
    )
