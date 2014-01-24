#!/usr/bin/python
# -*- coding: utf-8 -*-
import imp
import os
import types

def load_module(module_name,basepath):
    """ 
    モジュールをロードして返す
    """
    f,n,d = imp.find_module(module_name,[basepath])
    return imp.load_module(module_name,f,n,d)

def load_plugins(basepath):
    """ Pluginをロードしてリストにして返す
    """
    plugin_list = []
    for fdn in os.listdir(basepath):
        try:
            if fdn.endswith(".py"):
                m = load_module(fdn.replace(".py",""),basepath)
                plugin_list.append(m)
            elif os.path.isdir(fdn):
                m = load_module(fdn)
                plugin_list.append(m)
        except ImportError:
            pass
    return plugin_list


class Action(object):

  function = {}

  def init(self):
    print("inited")
  def hello(self):
    print("call hello")
  def load_plugin(self):
    plugindir = "plugins"    # Pluginが入っているディレクトリ
    cwd = os.getcwd()
    moduledir = os.path.join(cwd,plugindir)
    plugins = load_plugins(moduledir)   # Pluginを読み込む
    for p in plugins:
        self.function[p.__name__] = types.MethodType(p.foo, self)
        print p.__name__

if __name__ == "__main__":
  print("core-name")
