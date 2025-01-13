set shell := ["powershell.exe", "-c"]

backend:
    uav_service_cli --config_path=./config.toml --run=backend
postgresql:
    docker compose up postgresql
