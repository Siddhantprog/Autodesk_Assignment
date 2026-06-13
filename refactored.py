import os
import re
from pathlib import Path


def get_build_number() -> str:
    try:
        return os.environ["BuildNum"]
    except KeyError:
        raise EnvironmentError("Missing required environment variable: BuildNum")


def get_source_directory() -> Path:
    try:
        source_path = os.environ["SourcePath"]
    except KeyError:
        raise EnvironmentError("Missing required environment variable: SourcePath")

    return Path(source_path) / "develop" / "global" / "src"


def update_file(file_path: Path, pattern: str, replacement: str) -> None:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    content = file_path.read_text()

    updated_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        raise ValueError(
            f"No matching pattern found in {file_path.name}: {pattern}"
        )

    file_path.write_text(updated_content)


def update_versions() -> None:
    build_num = get_build_number()
    source_dir = get_source_directory()

    update_file(
        source_dir / "SConstruct",
        r"point\s*=\s*\d+",
        f"point={build_num}",
    )

    update_file(
        source_dir / "VERSION",
        r"ADLMSDK_VERSION_POINT\s*=\s*\d+",
        f"ADLMSDK_VERSION_POINT={build_num}",
    )


def main() -> None:
    update_versions()


if __name__ == "__main__":
    main()