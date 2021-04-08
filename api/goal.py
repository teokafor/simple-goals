import json

class Goal():

    def __init__(self, title: str, description: str, date: str):
        """Primary constructor for Goal.

        Args:
            title (str): title of this goal
            description (str): a general description, or additional notes associated with this goal
            date (str): the date this goal needs to be accomplished by
        """
        self.title = title
        self.description = description
        self.date = date

    def as_json_string(self) -> str:
        """Returns this Goal as a json String literal.

        Returns:
            str: this Goal as a String in json
        """
        return json.dumps(self)