from __Init_CMD__ import InitUI
class EXAMPLE(InitUI): 
      def __init__(self) -> None:
            super(EXAMPLE,self).__init__()
            self._COMMAND_["PRINT"] = lambda: PRINT()
            def PRINT():
               self.SHELL_COMMAND = "-HELLO WORLD !"
               self._COMMAND_["print"]("(45, 255, 134")
              
            self.BackGroundMenu.show()
            sys.exit(self.app.exec_())
              
 
__import__("ctypes").windll.user32.ShowWindow(__import__("ctypes").windll.kernel32.GetConsoleWindow(),0)
EXAMPLE()
          
  
