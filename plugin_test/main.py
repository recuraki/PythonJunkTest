#!/usr/bin/python
# -*- coding: utf-8 -*-

from action_core import Action

if __name__ == "__main__":
  action = Action()
  action.hello()
  action.load_plugin()
  action.function["a"]()

