# CODE-RADE Build Container

[![Build Status](https://travis-ci.org/AAROC/CODE-RADE-container.svg?branch=master)](https://travis-ci.org/AAROC/CODE-RADE-container) [![Maintainability](https://api.codeclimate.com/v1/badges/1e0a914e6a4a8be5522b/maintainability)](https://codeclimate.com/github/AAROC/CODE-RADE-container/maintainability) [![DOI](https://zenodo.org/badge/89260996.svg)](https://zenodo.org/badge/latestdoi/89260996)

A somewhat OS-independent role to build [CODE-RADE](https://github.com/AAROC/CODE-RADE) slaves for use in a continuous integration environment, using [Ansible-Container](https://docs.ansible.com/ansible-container).


## Tools

This role ensures that an image corresponding to the EGI execution environment is built so that applications can be built against it.
The image is used in the continuous integration environment in order to build applications which are subsequently delivered to a CVMFS repository.

Included in the image are:

  - a generic user to execute the builds - `jenkins`
  - build tools (compilers, testing programs and libraries, _etc_)
  - a consistent SSH installation built from source to be the same across images

The ssh service is used by the Jenkins server to start the connection to the master, it listens on port 2222, which can be tweaked in the variables.
The bare minimum of libraries and dependencies are installed, so as to make the image itself lightweight and ensure that unmet dependencies are not requested in the production environment.

## Building

Adds a CODE-RADE build container service to your [Ansible Container](https://github.com/ansible/ansible-container) project. To be used in conjunction with [CODE-RADE Build Containers](http://doi.org/10.5281/zenodo.572275). For galaxy info, see [`meta/main.yml`](meta/main.yml)

Run the following commands  
to install the service:

```
# Set the working directory to your Ansible Container project root
$ cd myproject

# Install the service
$ ansible-container install AAROC.code-rade-build-containers
```

## Testing

The role is tested with [molecule](https://molecule.readthedocs.io) across a few well-known scenarios - Docker environments, virtualised environments and cloud installations.
Testing is done with [TestInfra](https://testinfra.readthedocs.io) and checks whether the image is valid for the continuous integration environment:

  - build user exists
  - SSH daemon exists, is properly configured and responds on the required port
  - build, deploy and module directories are present and belong to the correct user

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
    - chemistry
* `prerequisites`:  OS-specific dependencies that need to be in the build environment in order to execute compilation and tests. Intentionally kept small.

## Dependencies

None

## License

Apache-2.0

## Author Information

Bruce Becker | bbecker@csir.co.za | C.S.I.R. Meraka Institute
[Africa-Arabia Regional Operations Centre](https://www.africa-grid.org)
Bruce Becker | bruce.becker@egi.eu | [EGI Foundation](https://egi.eu)

# Citing

If you use this role in an academic or research context, please cite :
Bruce Becker. (2017). AAROC/CODE-RADE-container: DevOps for CODE-RADE - Build Container role [Data set]. Zenodo. http://doi.org/10.5281/zenodo.572278
