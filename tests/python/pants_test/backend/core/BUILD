# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

target(
  name='core',
  dependencies=[
    ':wrapped_globs',
    'tests/python/pants_test/backend/core/tasks',
  ],
)

python_tests(
  name = 'wrapped_globs',
  sources = ['test_wrapped_globs.py'],
  dependencies = [
    'src/python/pants/backend/core',
    'tests/python/pants_test:base_test',
  ]
)
