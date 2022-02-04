# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.0.9] - 2022-02-04
### Added
- Splunk Appinspect API check. If both repository secrets `SPLUNKBASE_USER` and `SPLUNKBASE_PASSWORD` are specified, the workflow will run Splunk Appinspect API check as well, otherwise it will be skipped.

## [0.0.8] - 2022-02-02
### Added
- Update `ucc-gen` to 5.10.2 version.

## [0.0.7] - 2022-02-02
### Added
- Provide an option to specify `ucc-gen` version as an input.

## [0.0.6] - 2022-02-02
### Added
- Use all possible tags for Splunk Appinspect CLI action.

## [0.0.5] - 2022-02-01
### Added
- Add example usage to README.md file.

### Changed
- Use specific version instead of commit's SHA for all actions.

## [0.0.4] - 2022-01-26
### Added
- Upload results after Splunk Appinspect CLI action.

## [0.0.3] - 2022-01-26
### Changed
- Specify commit's SHA for Splunk Appinspect CLI.

## [0.0.2] - 2022-01-26
### Added
- Splunk Appinspect CLI check.

## [0.0.1] - 2022-01-25
### Added
- Initial version of [workflow-splunk-addon](https://github.com/artemrys/workflow-splunk-addon).

[Unreleased]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.9...HEAD
[0.0.9]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.8...v0.0.9
[0.0.8]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.7...v0.0.8
[0.0.7]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.6...v0.0.7
[0.0.6]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.5...v0.0.6
[0.0.5]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.4...v0.0.5
[0.0.4]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.3...v0.0.4
[0.0.3]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.2...v0.0.3
[0.0.2]: https://github.com/artemrys/workflow-splunk-addon/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/artemrys/workflow-splunk-addon/releases/tag/v0.0.1
