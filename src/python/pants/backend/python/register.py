# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.backend.python.pants_requirement import pants_requirement
from pants.backend.python.python_artifact import PythonArtifact
from pants.backend.python.python_requirement import PythonRequirement
from pants.backend.python.python_requirements import python_requirements
from pants.backend.python.targets.python_binary import PythonBinary
from pants.backend.python.targets.python_library import PythonLibrary
from pants.backend.python.targets.python_requirement_library import PythonRequirementLibrary
from pants.backend.python.targets.python_tests import PythonTests
from pants.backend.python.tasks.pytest_run import PytestRun
from pants.backend.python.tasks.python_binary_create import PythonBinaryCreate
from pants.backend.python.tasks.python_repl import PythonRepl
from pants.backend.python.tasks.python_run import PythonRun
from pants.backend.python.tasks.setup_py import SetupPy
from pants.base.deprecated import deprecated
from pants.build_graph.build_file_aliases import BuildFileAliases
from pants.build_graph.target import Target
from pants.goal.task_registrar import TaskRegistrar as task


class PythonTestSuite(Target):
  """Deprecated. Use target() instead."""

  @deprecated('0.0.64', 'Replace python_test_suite(...) with target(...) in your BUILD files. '
                        'Replace uses of PythonTestSuite with Target in your code.')
  def __init__(self, *args, **kwargs):
    raise RuntimeError('For {}: python_test_suite(...) targets no longer work. Replace with '
                       'target(...) in your BUILD files.'.format(kwargs['address'].spec))


def build_file_aliases():
  return BuildFileAliases(
    targets={
      'python_binary': PythonBinary,
      'python_library': PythonLibrary,
      'python_requirement_library': PythonRequirementLibrary,
      'python_test_suite': PythonTestSuite,
      'python_tests': PythonTests,
    },
    objects={
      'python_requirement': PythonRequirement,
      'python_artifact': PythonArtifact,
      'setup_py': PythonArtifact,
    },
    context_aware_object_factories={
      'python_requirements': BuildFileAliases.curry_context(python_requirements),
      'pants_requirement': BuildFileAliases.curry_context(pants_requirement),
    }
  )


def register_goals():
  task(name='python-binary-create', action=PythonBinaryCreate).install('binary')
  task(name='pytest', action=PytestRun).install('test')
  task(name='py', action=PythonRun).install('run')
  task(name='py', action=PythonRepl).install('repl')
  task(name='setup-py', action=SetupPy).install()
