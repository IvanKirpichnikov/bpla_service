FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /app

RUN mkdir -p ./src

COPY pyproject.toml pyproject.toml
RUN uv pip install -e . --system --no-cache

COPY ./src /app/src

CMD bpla_service_cli --config /app/config.toml --run backend
