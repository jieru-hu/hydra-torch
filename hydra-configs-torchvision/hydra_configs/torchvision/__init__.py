# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
#
# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from packaging import version
import warnings
import torchvision

CONFIGS_VERSION = "0.7.0"

if version.parse(torchvision.__version__) != version.parse(CONFIGS_VERSION):
    warnings.warn(f'Your config and library versions are mismatched. \n HYDRA-CONFIGS-TORCHVISION VERSION: {CONFIGS_VERSION}, \n TORCHVISION VERSION: {torchvision.__version__}. \n Please install the matching configs for reliable functionality.')