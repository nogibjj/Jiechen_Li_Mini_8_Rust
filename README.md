[![CI](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-ruff-template/actions/workflows/cicd.yml)

## 706-Data-Engineering-Template

### Repo Information

This  template is from [706_Data_Engineering_ Mini_Project]("https://github.com/carrieli15/706-Data-Engineering-Template.git"). I use <font color=#008000>GREEN</font> words to indicate the changes by adding Rust configuration:

- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The ``Dockerfile`` within this folder specifies how the container should be built, and other settings in this directory may control development environment configurations. <font color=#008000>Add Rust to path</font>.
                For the ``devcontainer.json``, <font color=#008000>to add Rust-specific settings, including the Rust extension for VS Code</font>.

- ``workflows`` includes GitHub Actions, which contain configuration files for setting up automated build, test, and deployment pipelines for your project. <font color=#008000>Adjust the steps to accommodate commands for Rust</font>.

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git. <font color=#008000>Add ``target/``, which is the directory containing Rust build artifacts, and ``Cargo.lock`` ensures consistent dependency versions</font>.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks. <font color=#008000>Add ``target/``Add commands for Rust build, test, format, lint, and run</font>.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file.

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project. <font color=#008000>Add libraries for Python and Rust</font>.

- ``test_main.py`` is a test file for main.py that can successfully run in IDEs.

### Build Rust Environment in Python Environment

**The structure of Rust project created by Cargo in this repo**:

rust_project/
│
├── src/
│   └── main.rs              # primary Rust code file
├── test/
│    └── test_main.rs
├── Cargo.toml               # configuration file that lists project's dependencies
├── Cargo.lock
└── .gitignore

**To set up Rust and Cargo**:

1. *Install Rust using rustup*:
Rust provides a tool called rustup to manage Rust versions and associated tools for the platform.

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

This command will download a script and start the installation. We can accept the default installation options by pressing "1".

2. *Source the shell profile*:
Once the installation is complete, we'll be prompted to run a command to update our shell profile:

```
source $HOME/.cargo/env
```

Alternatively, we can open a new terminal window, and it should recognize the cargo command.

3. *Verify Installation*:
Check if both Rust and Cargo are installed:

```
rustc --version
cargo --version
```

4. *Navigate to the "rust_project" directory and initialize a new Rust project*:

```
cd rust_project
cargo init
```

Now, we set up with a Rust environment in ``rust_project`` directory.

### Results

**Rust Result**:<br/>
<img decoding="async" src="./rs_result.png" width="85%">  

**Python Result**: <br/>
<img decoding="async" src="./py_result.png" width="85%">  

**Visualaization**: <br/>
<img decoding="async" src="./Figure_1.png" width="85%">  

<!-- <img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/1#issue-1885098942" width="50%">

<img decoding="async" src="https://github.com/carrieli15/706-Data-Engineering-Template/issues/2#issue-1885099594" width="50%">-->

<img decoding="async" src="/Users/castnut/Desktop/706_Data_Engineering/Mini_Project/Figure_1.png" width="50%">

![img](./rs_result.png)

### Reference

[Online Converting Tool for Python and Rust]("https://thepythoncode.com/assistant/code-converter/rust/")
