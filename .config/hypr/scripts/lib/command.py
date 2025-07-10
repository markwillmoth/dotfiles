import subprocess
from typing import List, Optional, Tuple, Union

from lib.logger import logger


def run(
    command: Union[str, List[str]], input: Optional[str] = None
) -> Tuple[str, Optional[Exception]]:
    logger.debug(f"command: {command}, input: {input}")

    result = subprocess.run(command, capture_output=True, text=True, input=input)
    if result.returncode != 0:
        output = result.stderr.strip()
        logger.error(f"command: {command}, stderr: {output}")
        return "", RuntimeError(
            f"Command '{
                ' '.join(command)}' failed:\n{output}"
        )

    output = result.stdout.strip()
    logger.info(f"command: {command}, stdout: {output}")
    return output, None
