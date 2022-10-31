import os
import Utils

def parseCustomMode():
    for filename in os.listdir("Plugins"):
       if filename.endswith(".hpm"):
           with open(os.path.join("Plugins", filename), 'r') as f: # open in readonly mode
               instr = []
               for line in f.readlines():
                   if not line.startswith("```") and not line == ('\n'):
                       instr.append(line.rstrip())

               Utils.CustomModes[filename] = instr
               #Utils.Modes.append(Utils.Modes[-1] + 1)
