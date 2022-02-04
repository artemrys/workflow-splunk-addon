# Github reusable workflow to support Splunk add-ons

This repository provides a reusable workflow to build and appinspect Splunk add-ons. It uses [`ucc-gen`](https://github.com/splunk/addonfactory-ucc-generator) and [`slim`](https://pypi.org/project/splunk-packaging-toolkit/) to create a ready to be installed add-on.

Then it uses [Splunk Appinspect CLI Github Action](https://github.com/splunk/appinspect-cli-action) to validate the generated add-on and optionally uses [Splunk Appinspect API Github Action](https://github.com/splunk/appinspect-api-action) if both `SPLUNKBASE_USER` and `SPLUNKBASE_PASSWORD` secrets are passed to the reusable workflow.

## Usage

```
name: build

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    uses: artemrys/workflow-splunk-addon/.github/workflows/reusable-build-release.yaml@v0.0.8
```

### Inputs

* [optional] `ucc_gen_version` - specify version of [`ucc-gen`](https://github.com/splunk/addonfactory-ucc-generator)

### Secrets

* [optional] `SPLUNKBASE_USER` - Splunkbase username
* [optional] `SPLUNKBASE_PASSWORD` - Splunkbase password
