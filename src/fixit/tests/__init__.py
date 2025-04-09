# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyrefly: ignore  # missing-module-attribute
from fixit.config import collect_rules

# pyrefly: ignore  # missing-module-attribute
from fixit.ftypes import Config, QualifiedRule

# pyrefly: ignore  # missing-module-attribute
from fixit.testing import add_lint_rule_tests_to_module
from .config import ConfigTest
from .engine import EngineTest
from .ftypes import TypesTest
from .rule import RuleTest, RunnerTest
from .smoke import SmokeTest

add_lint_rule_tests_to_module(
    globals(),
    collect_rules(
        Config(
            enable=[
                QualifiedRule("fixit.rules"),
                QualifiedRule("fixit.upgrade"),
            ],
            python_version=None,
        )
    ),
)
