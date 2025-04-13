# README: template 

## Table of Contents 

- [README: template](#readme-template)
- [Table of Contents](#table-of-contents)
- [How to Use the Python Template with Copier](#how-to-use-the-python-template-with-copier)
    - [Prerequisites](#prerequisites)
    - [Steps to Use the Template](#steps-to-use-the-template)
    - [Example `copier.yml`](#example-copieryml)

## How to Use the Python Template with Copier

This template can be used with the `copier` tool to scaffold a new Python project. 
Follow the steps below to use the template:

### Prerequisites
1. Install `copier` if you haven't already:
    ```bash
    python --version     # >=3.11.0,<4.0.0
    pipx --version       # >=1.1.0
    pipx install copier  # ending with the success message
    which copier         # /home/$USER/.local/bin/copier
    copier --version     # >=9.6.0
    ```

2. Ensure you have access to the template directory or repository.

### Steps to Use the Template
1. Navigate to the directory where you want to create your new project:
    ```bash
    cd /{project_path}
    ```

2. Run the `copier` command, specifying the path to the template:
    ```bash
    copier /home/$USER/__templates/python_template .
    ```

    Alternatively, if the template is hosted in a Git repository, you can use the repository URL:
    ```bash
    copier gh:username/repository_name .
    ```

3. Follow the interactive prompts to configure your new project. The prompts are defined in the `copier.yml` file of the template.

### Example `copier.yml`

> [!Important]
> The variables used for the project are defined in `copier.yml` in the root folder
> For more documentation see: [https://copier.readthedocs.io](https://copier.readthedocs.io/en/stable/#installation)
