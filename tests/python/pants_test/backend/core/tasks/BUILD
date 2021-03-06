# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

target(
  name='tasks',
  dependencies=[
    ':dependees',
    ':filter',
    ':markdown_to_html',
    ':target_filter_task_mixin',
  ],
)

python_tests(
  name='cache_cleanup',
  sources=['test_cache_cleanup.py'],
  dependencies=[
    'src/python/pants/backend/jvm/tasks/jvm_compile:zinc',
    'src/python/pants/util:dirutil',
    'tests/python/pants_test:int-test',
    'src/python/pants/util:contextutil',
  ]
)

python_tests(
  name='cloc',
  sources=['test_cloc.py'],
  coverage=['pants.backend.core.tasks.cloc'],
  dependencies=[
    'src/python/pants/backend/core/tasks:cloc',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/base:build_environment',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)

python_tests(
  name = 'dependees',
  sources = ['test_dependees.py'],
  dependencies = [
    'src/python/pants/backend/codegen/targets:java',
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/backend/core/tasks:dependees',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/jvm/targets:jvm',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/build_graph',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)

python_tests(
  name = 'filter',
  sources = ['test_filter.py'],
  dependencies = [
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/backend/core/tasks:filter',
    'src/python/pants/backend/jvm/targets:java',
    'src/python/pants/backend/python/targets:python',
    'src/python/pants/base:exceptions',
    'src/python/pants/build_graph',
    'tests/python/pants_test/tasks:task_test_base',
  ],
)

python_tests(
  name = 'markdown_to_html',
  sources = ['test_markdown_to_html.py'],
  dependencies = [
    '3rdparty/python:beautifulsoup4',
    '3rdparty/python:mock',
    'src/python/pants/backend/core/targets:common',
    'src/python/pants/backend/core/tasks:markdown_to_html',
    'src/python/pants/base:exceptions',
    'tests/python/pants_test/tasks:task_test_base',
  ],
  coverage=[
    'pants.backend.core.tasks.markdown_to_html',
  ]
)

python_tests(
  name='markdown_to_html_integration',
  sources=['test_markdown_to_html_integration.py'],
  dependencies=[
    'src/python/pants/base:build_environment',
    'src/python/pants/util:dirutil',
    'tests/python/pants_test:int-test',
  ],
  coverage=[
    'pants.backend.core.tasks.markdown_to_html',
  ]
)

python_tests(
  name='paths',
  sources=['test_paths.py'],
  dependencies=[
    'src/python/pants/backend/core/tasks:paths',
    'src/python/pants/base:exceptions',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)

python_tests(
  name='target_filter_task_mixin',
  sources=['test_target_filter_task_mixin.py'],
  dependencies=[
    'src/python/pants/backend/core/tasks:target_filter_task_mixin',
    'src/python/pants/build_graph',
    'tests/python/pants_test/tasks:task_test_base',
  ]
)
