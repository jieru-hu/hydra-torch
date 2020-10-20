# Copyright (c) 2020, Facebook, Inc. and its affiliates. All Rights Reserved
# SPDX-License-Identifier: MIT
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from omegaconf import MISSING
from typing import Any


@dataclass
class LambdaLRConf:
    _target_: str = "torch.optim.lr_scheduler.LambdaLR"
    optimizer: Any = MISSING
    lr_lambda: Any = MISSING
    last_epoch: Any = -1


@dataclass
class MultiplicativeLRConf:
    _target_: str = "torch.optim.lr_scheduler.MultiplicativeLR"
    optimizer: Any = MISSING
    lr_lambda: Any = MISSING
    last_epoch: Any = -1


@dataclass
class StepLRConf:
    _target_: str = "torch.optim.lr_scheduler.StepLR"
    optimizer: Any = MISSING
    step_size: Any = MISSING
    gamma: Any = 0.1
    last_epoch: Any = -1


@dataclass
class MultiStepLRConf:
    _target_: str = "torch.optim.lr_scheduler.MultiStepLR"
    optimizer: Any = MISSING
    milestones: Any = MISSING
    gamma: Any = 0.1
    last_epoch: Any = -1


@dataclass
class ExponentialLRConf:
    _target_: str = "torch.optim.lr_scheduler.ExponentialLR"
    optimizer: Any = MISSING
    gamma: Any = MISSING
    last_epoch: Any = -1


@dataclass
class CosineAnnealingLRConf:
    _target_: str = "torch.optim.lr_scheduler.CosineAnnealingLR"
    optimizer: Any = MISSING
    T_max: Any = MISSING
    eta_min: Any = 0
    last_epoch: Any = -1


@dataclass
class ReduceLROnPlateauConf:
    _target_: str = "torch.optim.lr_scheduler.ReduceLROnPlateau"
    optimizer: Any = MISSING
    mode: str = 'min'
    factor: Any = 0.1
    patience: Any = 10
    verbose: Any = False
    threshold: Any = 0.0001
    threshold_mode: str = 'rel'
    cooldown: Any = 0
    min_lr: Any = 0
    eps: Any = 1e-08


@dataclass
class CyclicLRConf:
    _target_: str = "torch.optim.lr_scheduler.CyclicLR"
    optimizer: Any = MISSING
    base_lr: Any = MISSING
    max_lr: Any = MISSING
    step_size_up: Any = 2000
    step_size_down: Any = None
    mode: str = 'triangular'
    gamma: Any = 1.0
    scale_fn: Any = None
    scale_mode: str = 'cycle'
    cycle_momentum: Any = True
    base_momentum: Any = 0.8
    max_momentum: Any = 0.9
    last_epoch: Any = -1


@dataclass
class CosineAnnealingWarmRestartsConf:
    _target_: str = "torch.optim.lr_scheduler.CosineAnnealingWarmRestarts"
    optimizer: Any = MISSING
    T_0: Any = MISSING
    T_mult: Any = 1
    eta_min: Any = 0
    last_epoch: Any = -1


@dataclass
class OneCycleLRConf:
    _target_: str = "torch.optim.lr_scheduler.OneCycleLR"
    optimizer: Any = MISSING
    max_lr: Any = MISSING
    total_steps: Any = None
    epochs: Any = None
    steps_per_epoch: Any = None
    pct_start: Any = 0.3
    anneal_strategy: str = 'cos'
    cycle_momentum: Any = True
    base_momentum: Any = 0.85
    max_momentum: Any = 0.95
    div_factor: Any = 25.0
    final_div_factor: Any = 10000.0
    last_epoch: Any = -1
