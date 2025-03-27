# dbHandler
"""
handle calling and writing database information
@todo incorperate requester, company, name, email
"""

from logHandler import Logger
Log = Logger(True, "dbHandler")

import json

class DBHandler:
    def __init__(self):
        self.fill = None    # filler var, since I don't know what to do with it yet @todo do somethign with

    # push
    """
        push object data to db file (as a JSON)
        @object: object to push to db
        @dbFileToWriteTo: file to write to
        return 1 on success
    """
    def push(self, object, dbFileToWriteTo):

        # @todo:make the push function add a new person to the existing json db without breaking things. It's a list format: [{person},{person},{person}]

        previousContent = self.pull(f"db/{dbFileToWriteTo}")
        newContent = previousContent
        Log.log(f"previous content of {dbFileToWriteTo}: {previousContent}")
        newContent.append(object.__dict__)
        Log.log(f"updated content: {newContent}")

        with open(f"db/{dbFileToWriteTo}", "w") as db:
            json.dump(previousContent, db, indent=4)

        return 1

    # pull
    """
        pull json data from file
        @dbToPull: file to pull from
        return json of data
    """
    def pull(self, dbToPull):
        try:
            with open(f"db/{dbToPull}", "r") as db:                       # open db in read mode
                dbJSON = json.load(db)                          # load db
            Log.log("data pull from db")
            return dbJSON                                       # return db
        except FileNotFoundError:                               # if file is not found, return empty json
            Log.log(f"alert: {dbToPull} does not exist, and we tried to pull from it")
            return []
        except Exception as e:
            Log.log(f"Error!!! {e}")                            # if error occurs, log it
            return []

