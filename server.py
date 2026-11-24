import argparse

from sc_kpm import ScServer
from search_module import SearchModule


def main(args: dict) -> None:
    server = ScServer(
        f"{args['protocol']}://{args['host']}:{args['port']}"
    )

    with server.connect():
        server.add_modules(SearchModule())
        with server.register_modules():
            server.serve()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", default="ws", help="SC-server protocol")
    parser.add_argument("--host", default="localhost", help="SC-server host")
    parser.add_argument("--port", type=int, default=8090, help="SC-server port")
    main(vars(parser.parse_args()))
