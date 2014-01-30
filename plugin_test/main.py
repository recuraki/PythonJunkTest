#!/usr/bin/python
# -*- coding: utf-8 -*-

from action_core import Action

if __name__ == "__main__":
  action = Action()
  action.load_plugin()
  action.run("hello")
  action.run("walk")
  action.run("bye")


