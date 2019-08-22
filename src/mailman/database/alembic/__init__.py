# Copyright (C) 2014-2019 by the Free Software Foundation, Inc.
#
# This file is part of GNU Mailman.
#
# GNU Mailman is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# GNU Mailman is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# GNU Mailman.  If not, see <https://www.gnu.org/licenses/>.

"""Alembic configuration initization."""

from alembic.config import Config
from contextlib import ExitStack
from mailman.utilities.modules import expand_path
from public import public


with ExitStack() as resources:
    cfg_path = expand_path(resources, 'python:mailman.config.alembic')
    public(alembic_cfg=Config(cfg_path))
