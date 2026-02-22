from app.mcp.config import get_settings
from app.mcp.server import mcp


settings = get_settings()


if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=settings.port,
        show_banner=False,
    )
