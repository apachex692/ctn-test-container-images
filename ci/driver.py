# Author: Apache X692
# Created on: 06/12/2024
from os import path, getenv
from subprocess import run as shell_run


def main():
    DOCKER_USERNAME = getenv("DOCKER_USERNAME")

    if path.exists("./.build"):
        with open("./.build", 'r') as file_handle:
            build_dirs = tuple(
                map(lambda x: x.strip(), file_handle.readlines())
            )
    else:
        exit(1)

    print("Building:", build_dirs)

    for directory in build_dirs:
        if directory == '':
            continue

        shell_run(
            [
                "docker", "build", "--tag",
                f"{DOCKER_USERNAME}/{directory}:latest", directory
            ], check=True
        )
        shell_run(
            [
                "docker", "push",
                f"{DOCKER_USERNAME}/{directory}:latest"
            ], check=True
        )


if __name__ == "__main__":
    main()
