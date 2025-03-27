# wikipedia
"""
pull data from wikipedia
"""
import wikipedia

class WikipediaClass:

    def __init__(self):
        pass

    #
    def wikipediaDefine(self, query):
        query = str(query)
        print("query: {0}".format(query))

        if query == '' or query == []:
            return 0
        try:
            text = wikipedia.summary(str(query))

            return text

        except Exception as e:
            return(f"failure finding information about {query} because of {e}, could you try again?")