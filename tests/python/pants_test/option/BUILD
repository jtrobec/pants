# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

target(
  name='option',
  dependencies=[
    ':testing'
  ],
)

python_tests(
  name='testing',
  sources=globs('*.py', exclude=[globs('*_integration.py')]),
  dependencies=[
    '3rdparty/python:mock',
    '3rdparty/python:pytest',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:deprecated',
    'src/python/pants/option',
    'src/python/pants/util:contextutil',
    'tests/python/pants_test:base_test',
  ],
)

python_tests(
  name='help_integration',
  sources=[
    'test_help_integration.py',
  ],
  dependencies=[
    'tests/python/pants_test:int-test',
  ],
)

python_tests(
  name='options_integration',
  sources=[
    'test_options_integration.py',
  ],
  dependencies=[
    'src/python/pants/util:contextutil',
    'tests/python/pants_test:int-test',
  ],
)
