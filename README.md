# py-conventional-commits

## Summary

Package for check conventional commits written only in python

## Description

The goal of this project is to validate commit messages using the Conventional Commits specification. The Conventional Commits specification is a set of rules that standardizes commit messages in software projects, making it easier to read and interpret changes made to the codebase. The specification can be found at https://www.conventionalcommits.org/en/v1.0.0/#specification.

Commit message validation will be performed using a Python script that will be automatically executed by the commit-msg Git Hook whenever a new commit is made. The script will check whether the commit message follows the pattern defined by the Conventional Commits specification and, if it does not comply, it will prevent the commit and display an error message indicating the issue.

The project will use Python's re library to create regular expressions that define the pattern of a valid commit message. In addition, a configuration file will be created to allow developers to customize some of the validation rules according to the specific needs of the project.

## Features

- Validate commit messages using the Conventional Commits specification.
- Prevent commits if the message does not comply with the specification.
- Display an error message indicating the issue with the commit message.
- Allow customization of validation rules via a configuration file.
- Automatically executed by the commit-msg Git Hook.

## Benefits

- Standardize commit messages across the project, making it easier to read and interpret changes made to the codebase.
- Improve the overall quality of commit messages, leading to better communication and collaboration among developers.
- Depend exclusively on Python, specifically on 0 other packages.

## Installation

Global installation

```bash
sudo pip3 install -U py-conventional-commits
```

### Python project

You can add it to your local project using one of these:

```bash
pip install -U py-conventional-commits
```

for Poetry >= 1.2.0:

```bash
poetry add py-conventional-commits --group dev
```

for Poetry < 1.2.0:

```bash
poetry add py-conventional-commits --dev
```
