from functools import partial
from pprint import pprint
from typing import List

import click
from github import Github
from p_tqdm import p_map, t_map

from utils import extractor

REPO = "mitre/cti"
PATH = "enterprise-attack/attack-pattern"
ATTRIBUTES = ["id", "objects[0].name", "objects[0].kill_chain_phases"]


def get_files_content(folder_content: List[str]) -> List:
    """Get the files content."""

    try:
        content = t_map(lambda x: x.decoded_content, folder_content[:100])
    except Exception as e:
        print(f"There was a problem getting the file content: {e}")
        raise

    return content


@click.command()
@click.option("--repo", default=REPO, help="Repository name.")
@click.option("--path", default=PATH, help="Path to the folder.")
@click.option("--attrs", default=ATTRIBUTES, type=list, help="List of attributes.")
@click.option("--token", default=None, help="Github token to perform more requests.")
@click.option("--output", help="Filename to save the output.")
def main(repo, path, attrs, output, token):
    """Script to obtain the attributes from the files in the given folder."""

    g = Github(login_or_token=token)
    repository = g.get_repo(repo)
    folder_content = repository.get_contents(path)
    print(f"💾 Getting the content of {repo}/{path}")
    files_content = get_files_content(folder_content)

    f = partial(extractor, attributes=attrs)
    print("🛠  Extracting the required data")
    result = p_map(f, files_content)

    if output:
        with open(output + ".txt", "w") as f:
            for line in result:
                pprint(line, stream=f)
    else:
        pprint(result)


if __name__ == "__main__":
    main()
