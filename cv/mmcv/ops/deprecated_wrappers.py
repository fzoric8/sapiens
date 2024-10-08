# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

# This file is for backward compatibility.
# Module wrappers for empty tensor have been moved to mmcv.cnn.bricks.
import warnings

from ..cnn.bricks.wrappers import Conv2d, ConvTranspose2d, Linear, MaxPool2d


class Conv2d_deprecated(Conv2d):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            'Importing Conv2d wrapper from "mmcv.ops" will be deprecated in'
            ' the future. Please import them from "mmcv.cnn" instead',
            DeprecationWarning)


class ConvTranspose2d_deprecated(ConvTranspose2d):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            'Importing ConvTranspose2d wrapper from "mmcv.ops" will be '
            'deprecated in the future. Please import them from "mmcv.cnn" '
            'instead', DeprecationWarning)


class MaxPool2d_deprecated(MaxPool2d):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            'Importing MaxPool2d wrapper from "mmcv.ops" will be deprecated in'
            ' the future. Please import them from "mmcv.cnn" instead',
            DeprecationWarning)


class Linear_deprecated(Linear):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warnings.warn(
            'Importing Linear wrapper from "mmcv.ops" will be deprecated in'
            ' the future. Please import them from "mmcv.cnn" instead',
            DeprecationWarning)
