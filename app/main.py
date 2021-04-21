import sys
from pprint import pprint
from typing import Any, Dict

from github import Github
from p_tqdm import t_map

from utils import extractor

REPO = "mitre/cti"
PATH = "enterprise-attack/attack-pattern"
ATTRIBUTES = ["id", "objects[0].name", "objects[0].kill_chain_phases"]


def extractor_constructor(file_content: Any, attributes=ATTRIBUTES) -> Dict:

    try:
        the_content = file_content.decoded_content
    except Exception as e:
        print(f"There was a problem getting the file content: {e}")
        raise
    return extractor(the_content, attributes)


def main():
    g = Github()
    repo = g.get_repo(REPO)
    folder_content = repo.get_contents(PATH)
    folder_content = folder_content[:10]
    result = t_map(extractor_constructor, folder_content)

    return result


if __name__ == "__main__":
    print(f"💾 Getting the content of {REPO}/{PATH}", file=sys.stderr)
    pprint(main())
