# ansible-stubs

Type annotations which help in development of Ansible plugins.

## Static typing with Python

See [Python docs](https://typing.readthedocs.io/en/latest/),
especially the [Distributing type information](https://typing.readthedocs.io/en/latest/spec/distributing.html) section.

## Note

As of July 2024, there is no type information for Ansible.

## Findings

1. [ansible-stubs](https://pypi.org/project/ansible-stubs)

   Status: Under development, [the first PR](https://github.com/pycontribs/ansible-stubs/pull/1) is open since February 2024.

2. [Request](https://github.com/python/typeshed/issues/8016) in the typeshed repo (June 2022)

   Status: Closed as not planned.

## Installation

```shell
GIT_TAG=v1.0.0
python3 -m pip install -v \
    ansible-stubs[test]@git+https://github.com/hitachienergy/ansible-stubs@$GIT_TAG
```

NOTE: The `test` package's extra is required only if you need to run [stubtest](https://mypy.readthedocs.io/en/stable/stubtest.html).

For more information, see pip docs: [Supported VCS](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Testing

```shell
python3 -m mypy.stubtest \
    ansible.module_utils.basic \
    ansible.module_utils.common.text.converters
```

## Creating type stub files

See mypy docs: [Automatic stub generation](https://mypy.readthedocs.io/en/stable/stubgen.html).

1. Generate draft stubs:

   ```shell
   stubgen -m ansible \
           -m ansible.errors \
           -m ansible.module_utils \
           -m ansible.module_utils._text \
           -m ansible.module_utils.common \
           -m ansible.module_utils.common.file \
           -m ansible.module_utils.common.text \
           -m ansible.module_utils.common.text.converters \
           -m ansible.module_utils.pycompat24 \
           -m ansible.module_utils.six \
           -m ansible.module_utils.six.moves.collections_abc \
           -v \
           && \
   stubgen -m ansible.module_utils.basic \
           --export-less --include-private -v
   ```

2. Move the generated files:

   ```shell
   mkdir -pv ansible-stubs
   # https://typing.readthedocs.io/en/latest/spec/distributing.html#partial-stub-packages
   printf "partial\n" > ansible-stubs/py.typed
   mv -v out/ansible/* ansible-stubs
   rmdir -pv out/ansible
   ```

3. Remove unneeded imports from `ansible-stubs/ansible-stubs/module_utils/basic.pyi`.

4. Install the package.

   - with Poetry (uses your active virtual environment or creates its own):

     ```shell
     poetry install --extras test --sync -v
     ```

   - with pip:

     ```shell
     # Ensure you have the plugin:
     # poetry self add -v poetry-plugin-export

     pip install --user -r <(poetry export -f requirements.txt --extras test) -v
     pip install --user --no-deps -v .
     ```

5. Run tests (they should pass):

   - with Poetry:

     ```shell
     poetry run stubtest ansible.errors \
                         ansible.module_utils._test \
                         ansible.module_utils.basic \
                         ansible.module_utils.common.text.converters
     ```

   - with pip:

     ```shell
     stubtest ansible.errors \
              ansible.module_utils._test \
              ansible.module_utils.basic \
              ansible.module_utils.common.text.converters
     ```

6. Update the generated stub files providing more precise type annotations.

7. Rerun the tests.

8. Run mypy tests:

   ```shell
   poetry run mypy ./ansible-stubs/module_utils
   ```

## Releasing a new version

1. Update the version in `pyproject.toml`.

2. Create and push a tag:

   ```shell
   TAG=v1.0.0
   git tag $TAG
   git push origin $TAG
   ```
