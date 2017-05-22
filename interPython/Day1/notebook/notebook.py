import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    """
    Represent a note in the notebook. Match against a
    string in searches and store tags for each note.
    """

    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional
        space-separated tags.  Automatically set the notes's
        creation date and a unique id.
        :param memo:
        :param tags:
        """
        self._memo = memo
        self._tags = tags
        self._creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self._id = last_id

    def match(self, filter):
        """
        Determine if thes note matches the filter text
        :param filter:  filter text
        :return:  True if it matches, False otherwise
        Search is case sensitive and matches both tex and tags
        """

        return filter in self._memo or filter in self._tags


class Notebook:
    """
    Represent a collection of notes that can be tagged, modified, and searchec.
    """

    def __init__(self):
        """
        initalize a notbook with an empty list.
        """
        self._notes = []

    def new_note(self, memo, tags=""):
        """
        Create a new note and add it to the list.
        :param memo:
        :param tags:
        :return: none
        """
        self._notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """
        find a note with a given id and change its memo to the given value
        :param note_id:
        :param memo:
        :return: none
        """

        note = self._find_note(note_id)
        if note:
            note._memo = memo
            return note
        return False



    def modify_tags(self, note_id, tags):
        """
        find a note with a given id and change its tag to the given value
        :param note_id:
        :param tags:
        :return: none
        """

        note = self._find_note(note_id)
        if note:
            note._tags = tags
            return note
        return False

    def search(self, filter):
        """
        Find all the notes that match the fiven filter string
        :param filter:
        :return: none
        """

        return [note for note in self._notes
                if note.match(filter)]


    def _find_note(self, note_id):
        """
        Locate the note with a given id.
        :param note_id:
        :return:
        """

        for note in self._notes:
            if str(note.id) == str(note_id):
                return note
            return None

