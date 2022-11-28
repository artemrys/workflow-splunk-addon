import yaml
import requests


def versiontuple(version: str) -> tuple:
    return tuple(map(int, (version.split("."))))


def get_latest_ucc_gen_version_from_pypi() -> str:
    response = requests.get("https://pypi.org/pypi/splunk-add-on-ucc-framework/json")
    response_json = response.json()
    latest_version = response_json["info"]["version"]
    return latest_version


def get_current_ucc_gen_version_from_workflow_file() -> str:
    with open(".github/workflows/reusable-build-release.yaml") as workflow_file:
        content = yaml.safe_load(workflow_file.read())
    # By YAML 1.1 spec, "on" is considered as a True.
    # More details here: https://github.com/yaml/pyyaml/issues/376.
    # It can be changed in the future if I introduce a custom resolver.
    current_version = content[True]["workflow_call"]["inputs"]["ucc_gen_version"][
        "default"
    ]
    return current_version


def main():
    current_version = get_current_ucc_gen_version_from_workflow_file()
    print(f"Current version is {current_version}")
    latest_version = get_latest_ucc_gen_version_from_pypi()
    print(f"Latest version is {latest_version}")
    if versiontuple(latest_version) > versiontuple(current_version):
        print("Latest version is bigger than current version")
        with open("current_version.txt", "w") as current_version_file:
            current_version_adj = current_version.replace(".", "\.")
            current_version_file.write(current_version_adj)
        with open("latest_version.txt", "w") as latest_version_file:
            latest_version_adj = latest_version.replace(".", "\.")
            latest_version_file.write(latest_version_adj)


if __name__ == "__main__":
    main()
