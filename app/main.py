from pprint import pprint
from typing import Any, Dict

from github import Github
from p_tqdm import t_map
from utils import extractor

REPO = "mitre/cti"
PATH = "enterprise-attack/attack-pattern"
ATTRIBUTES = ["id", "objects[0].name", "objects[0].kill_chain_phases"]
TOKEN = "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"


def extractor_constructor(file_content: Any, attributes=ATTRIBUTES) -> Dict:

    try:
        the_content = file_content.decoded_content
    except Exception as e:
        print(f"There was a problem getting the file content: {e}")
        raise
    return extractor(the_content, attributes)


def main():
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    folder_content = repo.get_contents(PATH)
    result = t_map(extractor_constructor, folder_content)

    return result


if __name__ == "__main__":
    print(f"💾 Getting the content of {REPO}/{PATH}")
    pprint(main())
