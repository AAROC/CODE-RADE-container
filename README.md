# Role Name

Adds a CODE-RADE build container service to your [Ansible Container](https://github.com/ansible/ansible-container) project. To be used in conjunction with [CODE-RADE Build Containers](http://doi.org/10.5281/zenodo.572275). For galaxy info, see [`meta/main.yml`](meta/main.yml)

Run the following commands
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

Variables are all in `vars/main.yml` :

  * `modules_path` - The OS-dependent path where  `environment-modules` keeps its base configuration by default.
  * `modules` - CODE-RADE specific modulefiles `ci` and `deploy` which set up the build, test and deploy shells. These contain OS-specific variables, using `anisble_os_family`
  * `module_domains` - The domain-specific modulefile paths to which CODE-RADE can write application modulefiles. Contain :
    - astronomy
    - bioinformatics
    - compilers
    - languages
    - libraries
    - physical_sciences
    - hep
* `prerequisites`:  OS-specific dependencies that need to be in the build environment in order to execute compilation and tests. Intentionally kept small.

## Dependencies

None

## License

Apache-2.0

## Author Information

Bruce Becker | bbecker@csir.co.za | C.S.I.R. Meraka Institute
[Africa-Arabia Regional Operations Centre](https://www.africa-grid.org)
