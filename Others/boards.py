# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 15:25:08 2021

@author: krish
"""

from trello.base import TrelloBase
from trello.compat import force_str


class Boards(TrelloBase):
    
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return u'<Board %s>' % self.name



b = Boards('python_trial')
print(b)