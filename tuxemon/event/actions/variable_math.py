#
# Tuxemon
# Copyright (c) 2014-2017 William Edwards <shadowapex@gmail.com>,
#                         Benjamin Bean <superman2k5@gmail.com>
#
# This file is part of Tuxemon
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Union, final

from tuxemon.event.eventaction import EventAction
from tuxemon.tools import number_or_variable

logger = logging.getLogger(__name__)


@final
@dataclass
class VariableMathAction(EventAction):
    """
    Perform a mathematical operation on the player.game_variables dictionary.

    Optionally accepts a fourth parameter to store the result, otherwise it
    is stored in ``var1``.

    Script usage:
        .. code-block::

            variable_math <var1>,<operation>,<var2>,<result>
            variable_math <var1>,<operation>,<var2>

    Script parameters:
        var1: First operand.
        operation: Operator symbol.
        var2: Second operand.
        result: Variable where to store the result. If missing, it will be
            ``var1``.

    """

    name = "variable_math"
    var1: str
    operation: str
    var2: str
    result: Union[str, None] = None

    def start(self) -> None:
        player = self.session.player

        # Read the parameters
        var = self.var1
        result = self.result
        if result is None:
            result = var
        operand1 = number_or_variable(self.session, var)
        operation = self.operation
        operand2 = number_or_variable(self.session, self.var2)

        # Perform the operation on the variable
        if operation == "+":
            player.game_variables[result] = operand1 + operand2
        elif operation == "-":
            player.game_variables[result] = operand1 - operand2
        elif operation == "*":
            player.game_variables[result] = operand1 * operand2
        elif operation == "/":
            player.game_variables[result] = operand1 / operand2
        elif operation == "=":
            player.game_variables[result] = operand2
        else:
            raise ValueError(f"invalid operation type {operation}")
