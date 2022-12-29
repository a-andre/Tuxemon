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

from dataclasses import dataclass
from typing import final

from tuxemon.event.eventaction import EventAction
from tuxemon.monster import Flair


@final
@dataclass
class SetMonsterFlairAction(EventAction):
    """
    Set a monster's flair to the given value.

    Script usage:
        .. code-block::

            set_monster_flair <slot>,<category>,<flair>

    Script parameters:
        slot: Slot of the monster in the party.
        category: Category of the monster flair.
        flair: Name of the monster flair.

    """

    name = "set_monster_flair"
    slot: int
    category: str
    flair: str

    def start(self) -> None:
        monster = self.session.player.monsters[self.slot]
        if self.category in monster.flairs:
            monster.flairs[self.category] = Flair(
                self.category,
                self.flair,
            )
