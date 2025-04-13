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

2. Run the `copier` command, use the repository URL:
    ```bash
    copier gh:42sol-eu/python_template .
    ```
    
    Alternatively, if you have a local copy run the `copier` command, specifying the path to the template:
    ```bash
    copier /home/$USER/__templates/python_template .
    ```

3. Follow the interactive prompts to configure your new project. The prompts are defined in the `copier.yml` file of the template.

### Example `copier.yml`

> [!Important]
> The variables used for the project are defined in `copier.yml` in the root folder
> For more documentation see: [https://copier.readthedocs.io](https://copier.readthedocs.io/en/stable/#installation)


## Contributing

> [!Note] Template
> We welcome contributions to improve this template! If you have ideas, bug fixes, or enhancements, feel free to submit a pull request on GitHub or GitLab. 
> Here's how you can contribute:
> 1. **Ensure that you have read the necessary documentation** and **that your system is set up correctly**. 
> 2. **Fork the Repository**: Create a copy of the repository in your own GitHub/GitLab account.
> 3. **Create a Branch**: Make a new branch for your changes. Use a descriptive name, such as `feature/add-new-feature` or `fix/bug-description`.
> 4. **Make Your Changes**: Implement your changes in the new branch. Ensure your code follows the project's style guidelines and is well-documented.
> 5. **Test Your Changes**: Verify that your changes work as expected and do not introduce new issues.
> 6. **Submit a Pull Request**: Open a pull request to the main repository. Provide a clear description of your changes, including the problem they solve or the feature they add.
> 7. **Be patient until we answer** or **give us an additional ping** via the provided.
> 
> We appreciate your contributions and will review your pull request as soon as possible. Thank you for helping us improve this template!
