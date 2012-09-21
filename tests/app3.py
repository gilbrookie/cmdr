from data import CmdrDecoratedCmds, TestCmd3, TestCmd4

CmdrDecoratedCmds.register_cmd(TestCmd3())
CmdrDecoratedCmds.register_cmd(TestCmd4())
CmdrDecoratedCmds.start()
