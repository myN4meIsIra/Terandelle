#logHandler
"""
handle processes of logging and data output
"""
import datetime

logFile = "./logs/log.txt"

class Logger:
    def __init__(self, terminalOutput, caller):
        self.terminalOutput = terminalOutput    # boolean value to determine whether text output should occur
        self.logFile = logFile                  # text file to load logs into
        self.caller = caller                    # what is calling the log function

    def log(self, text):
        textToLog = f"<log>{datetime.datetime.now()}<{self.caller}> {text}\n" # assemble text to log
        logFile = open(self.logFile, "a")                                   # open file in append mode
        logFile.write(textToLog)                                            # write to file
        logFile.close()                                                     # close file
        if self.terminalOutput: print(textToLog[:-1])                            # if the class is initialized w/ terminalOutput=true, print to stdout


