class Testy112:
    @staticmethod
    def StworzTesty(f):
        import sys
        import os
        import importlib
        sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../skrypty"))
        p = os.path.abspath(os.path.dirname(os.path.abspath(__file__))).split(os.sep)
        importlib.import_module("StworzTesty").StworzTesty(112,os.path.join(p[-2],p[-1]),f)