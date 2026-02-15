MCP_TRANSPORT ?= http
MCP_PORT ?= 8000

.PHONY: dev
dev:
    @echo "Run the MCP server in development mode with auto-reloading."
    fastmcp run app/main.py --transport $(MCP_TRANSPORT) --port $(MCP_PORT) --reload

.PHONY: build
build:
    @echo "Build the Docker image for the MCP server."
    docker buildx build -t mcp:latest .

.PHONY: start
start:
    @echo "Start the MCP server using Docker. (Prod run)"
    docker run -p $(MCP_PORT):$(MCP_PORT) -e MCP_PORT=$(MCP_PORT) mcp:latest