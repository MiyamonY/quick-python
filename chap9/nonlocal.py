# /usr/bin/env python
# -*- coding:utf-8 -*-

g_var = 0
nl_var = 0
print("top_level -> g_var : {0} nl_var:{1}".format(g_var, nl_var))

def test():
    nl_var = 2
    print("in_test->g_var:{0} nl_var:{1}".format(g_var, nl_var))

    def inner_test():
        global g_var
        nonlocal nl_var
        g_var = 1
        nl_var = 4
        print("in inner_test->g_var{0} nl_var{1}".format(g_var, nl_var))

    inner_test()

    print("in_test->g_var:{0} nl_var:{1}".format(g_var, nl_var))

test()
print("top_level -> g_var : {0} nl_var:{1}".format(g_var, nl_var))
    
