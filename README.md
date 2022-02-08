<br/>
<div align="center">

A curated list of awesome Snyk community contributions

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License](https://badgen.net/badge/License/CC%20BY-SA%204.0/green)](http://creativecommons.org/licenses/by-sa/4.0/)

_List inspired by the [awesome](https://github.com/sindresorhus/awesome) list thing._

</div>
<br/>

# Contents

<!-- doctoc: generated with `doctoc --github --notitle`>
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [The List](#the-list)
  - [Tools Powered by Snyk](#tools-powered-by-snyk)
  - [Snyk CLI, Plugins, Extensions, Filters](#snyk-cli-plugins-extensions-filters)
  - [SDKs](#sdks)
    - [Python](#python)
    - [JavaScript / TypeScript](#javascript--typescript)
    - [Snyk API Helpers](#snyk-api-helpers)
  - [IDE Plugins](#ide-plugins)
  - [Integration tooling](#integration-tooling)
    - [CI/CD](#cicd)
      - [CircleCI](#circleci)
      - [CodeShip](#codeship)
      - [GitHub Actions](#github-actions)
    - [Container Registries](#container-registries)
      - [Artifactory CR](#artifactory-cr)
    - [Issue & Project Management](#issue--project-management)
      - [Jira](#jira)
    - [Monitoring & Observability](#monitoring--observability)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# The List

## Tools Powered by Snyk

- [Snyk Advisor](https://snyk.io/advisor) - Find the best package for your next project
- [is-website-vulnerable](https://github.com/lirantal/is-website-vulnerable) - finds publicly known security vulnerabilities in a website's frontend JavaScript libraries
- [Security Report](https://www.npmjs.com/package/security-report) - a CLi to responsibly disclose a security issue to the [Snyk's security team](https://snyk.io/vulnerability-disclosure/)


## Snyk CLI, Plugins, Extensions, Filters

Useful in for running snyk locally and for automating CI/CD workflows

- [Snyk CLI](https://github.com/snyk/snyk) - The Snyk CLI
- [Snyk asdf plugin](https://github.com/nirfuchs/asdf-snyk) - asdf plugin for Snyk. Easily manage multiple versions of Snyk CLI in your runtime environment
- [Snyker](https://github.com/asos/snyker) - An opinionated CLI wrapper around Snyk for purging vulnerabilities from Node projects.
- [snyk-to-html](https://github.com/snyk/snyk-to-html) - Create template-based HTML artifacts from Snyk CLI JSON output; useful for generating build artifacts
- [snyk-issues-to-html](https://github.com/snyk-labs/snyk-issues-to-html) - This command line utility uses the Snyk API to export the list of all reported issues for a Snyk organization to a static HTML page.
- [snyk-disallow](https://github.com/snyk-tech-services/snyk-disallow) - Create and manage a list of unwanted dependencies against which you can test your application with Snyk
- [snyk-filter](https://github.com/snyk-tech-services/snyk-filter) - Filter CLI test results and/or fail CI builds using custom criteria
- [snyk-licenses-texts](https://github.com/snyk-tech-services/snyk-licenses-texts) - Generate a Snyk organization-level report showing licenses and copyright attribution for all dependencies in use
- [snyk-delta](https://github.com/snyk-tech-services/snyk-delta) - Prevent new vulns feature for CLI projects,  comparing the the delta between your current test and an existing snapshot. Particularly useful when running CLI-based scans, like in your local environment, git hooks, etc.\
- [snyk-cli-with-longformprojectname](https://github.com/snyk-tech-services/snyk-cli-with-longformprojectname) - It contains --longformprojectname option, allowing project versions to be appended to the project name.  Addressing very specific needs primarily around maven projects.  This project is continuously updated and in sync with github.com/snyk/snyk
- [snyk-scm-refresh](https://github.com/snyk-tech-services/snyk-scm-refresh) - Keeps Snyk projects in sync with their associated Github or Github Enterprise repos
- [helm-snyk](https://github.com/snyk-labs/helm-snyk) - Check for vulnerabilities in container images referenced in your helm charts
- [Snyk User Sync Tool](https://github.com/snyk-tech-services/snyk-user-sync-tool) - sync user org memberships from an external source into Snyk
- [Snyk History Scanner](https://github.com/cjheppell/snyk-history-scanner/) - A very thin wrapper around the Snyk CLI tool to make it possible to monitor specific versioned releases of software
- [snyk2spdx](https://www.npmjs.com/package/snyk2spdx) - Convert Snyk CLI output to [SPDX](https://spdx.dev/) format
- [snyk-cleanup-archived-github-repositories](https://github.com/Financial-Times/snyk-cleanup-archived-repositories) - Remove archived repositories from Snyk
- [snyk-watcher-lambda](https://github.com/granular-oss/snyk-watcher-lambda) - snyk-watcher is triggered via a Gitlab System Hook which calls an AWS Lambda via AWS API Gateway. Keeps Snyk projects in sync with their associated Gitlab Enterprise repos

## SDKs

### Python

- [PySnyk](https://github.com/snyk-labs/pysnyk) - A Python client for the Snyk API
- [python-snyk-test](https://github.com/avishayil/python-snyk-test) - A tool that wraps pysnyk library for easier usage from command line interfaces.

### JavaScript / TypeScript

- [dep-graph](https://github.com/snyk/dep-graph) - TypeScript package for representing a dependency graph for use with the [Snyk dep-graph testing API](https://snyk.docs.apiary.io/#reference/test/dep-graph/test-dep-graph)
https://github.com/snyk-tech-services/snyk-api-ts-client


### Snyk API Helpers

- [API Import](https://github.com/snyk-tech-services/snyk-api-import) by Snyk Tech Services team
- [Snyk Request Manager](https://github.com/snyk-tech-services/snyk-request-manager) by Snyk Tech Services team
- [Collection of Snyk admin scripts](https://github.com/binkhq/snyk-tools) by [Bink](https://bink.com)

## IDE Plugins

- [InteliJ Snyk plugin](https://plugins.jetbrains.com/plugin/10972-snyk-vulnerability-scanning) - Detect and fix security issues in your project
- [Eclipse Snyk plugin](https://marketplace.eclipse.org/content/snyk-vuln-scanner)
- [Vuln Cost](https://marketplace.visualstudio.com/items?itemName=snyk-security.vscode-vuln-cost) - Security Scanner to find and fix vulnerabilities in JavaScript and TypeScript.
- [VS Code Snyk](https://marketplace.visualstudio.com/items?itemName=pmbenjamin.vscode-snyk) - A Snyk plugin for Visual Studio Code
- [PyCharm Security plugin](https://github.com/tonybaloney/pycharm-security) - [Anthony Shaw](https://twitter.com/anthonypjshaw) author of PyCharm Security plugin [added support for Snyk](https://twitter.com/anthonypjshaw/status/1233535013897097216) for versions >= 1.13.0 of the plugin.


## Integration tooling

### CI/CD

- [Snyk CI/CD Integration Examples](https://github.com/snyk-labs/snyk-cicd-integration-examples)

#### CircleCI
- [Circle CI Snyk Orb](https://circleci.com/orbs/registry/orb/snyk/snyk) - This orb uses Snyk to find, fix and monitor known vulnerabilities in your app dependencies and docker image

#### CodeShip

- [Snyk in Codeship](https://documentation.codeship.com/general/integrations/snyk)

#### GitHub Actions

- [Propagate Python Fix](https://github.com/snyk-tech-services/github-actions-snyk-propagate-python-fix) - Propagates fixes injected into requirements.txt into requirements.in
- [Prevent job from CircleCI](https://github.com/snyk-tech-services/github-actions-snyk-prevent-job-from-circleci) - Sample gradle project with CircleCI pipeline saving the test output for snyk to pick up in github action
- [Test PNPM projects](https://github.com/snyk-tech-services/github-actions-pnpm-snyk) - Allows PNPM projects to be scanned in a similar manner NPM projects on Snyk.

### Container Registries

#### Artifactory CR

[Snyk CR Monitor](https://github.com/snyk-tech-services/snyk-cr-monitor) - Monitor container images in on-premise Artifactory container registries with Snyk

### Issue & Project Management

#### Jira

https://github.com/snyk-tech-services/jira-tickets-for-new-vulns

### Monitoring & Observability

- [Lunarway's Prometheus exporter for Snyk](https://github.com/lunarway/snyk_exporter) - Prometheus exporter for Snyk
- [prometheus_snyk_exporter](https://github.com/dnanexus/prometheus_snyk_exporter) - Gathers security vulnerability metrics from snyk.io for use in Prometheus monitoring
https://github.com/snyk-tech-services/backstage-plugin-snyk



# License

[![License](https://badgen.net/badge/License/CC%20BY-SA%204.0/green)](http://creativecommons.org/licenses/by-sa/4.0/)

This work is licensed under a Creative Commons Attribution-ShareAlike 4.0 International License.
