# Role Name

Adds a CODE-RADE build container service to your [Ansible Container](https://github.com/ansible/ansible-container) project. Run the following commands
to install the service:

```
# Set the working directory to your Ansible Container project root
$ cd myproject

# Install the service
$ ansible-container install AAROC.code-rade-build-containers
```

## Requirements

- [Ansible Container](https://github.com/ansible/ansible-container)
- An existing Ansible Container project. To create a project, simply run the following:
    ```
    # Create an empty project directory
    $ mkdir myproject

    # Set the working directory to the new directory
    $ cd myproject

    # Initialize the project
    $ ansible-contiainer init
    ```


## Role Variables

Variables are all in `vars/main.yml`

## Dependencies

None

## License

Apache-2.0

## Author Information

Bruce Becker | bbecker@csir.co.za
