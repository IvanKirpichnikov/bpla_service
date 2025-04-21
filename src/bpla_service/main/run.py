import argparse
import asyncio
import sys
from pathlib import Path
from typing import cast, Protocol

from bpla_service.config import build_config
from bpla_service.main.build_container import build_container
from bpla_service.main.web import run_web


class Args(Protocol):
    run: str
    config_path: Path | None


def main() -> None:
    if sys.platform == "win32":
        from asyncio import WindowsSelectorEventLoopPolicy
        asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
    
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--config_path", dest="config_path", type=Path)
    arg_parser.add_argument("--run", dest="run", type=str)
    
    args = cast(Args, arg_parser.parse_args())
    
    if args.run == "backend" and args.config_path:
        config = build_config(args.config_path)
        container = build_container(config)
        run_web(config, container)
