# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass
from omegaconf import MISSING
from typing import Any


@dataclass
class LBFGSConf:
    _target_: str = "torch.optim.lbfgs.LBFGS"
    params: Any = MISSING
    lr: Any = 1
    max_iter: Any = 20
    max_eval: Any = None
    tolerance_grad: Any = 1e-07
    tolerance_change: Any = 1e-09
    history_size: Any = 100
    line_search_fn: Any = None
