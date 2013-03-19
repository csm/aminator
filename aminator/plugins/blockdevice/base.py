# -*- coding: utf-8 -*-

#
#
#  Copyright 2013 Netflix, Inc.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#

"""
aminator.plugins.blockdevice.base
=================================
Base class(es) for block device manager plugins
"""
import abc
import logging

from aminator.plugins.base import BasePlugin


__all__ = ('BaseDeviceManagerPlugin',)
log = logging.getLogger(__name__)


class BaseBlockDevicePlugin(BasePlugin):
    __metaclass__ = abc.ABCMeta
    _entry_point = 'aminator.plugins.blockdevice'

    @abc.abstractmethod
    def __enter__(self):
        """
        Block device plugins are context managers
        __enter__ should return a device string after allocation
        """

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_value, trace):
        """
        exit point for block device context
        cleanup locks and such here
        """