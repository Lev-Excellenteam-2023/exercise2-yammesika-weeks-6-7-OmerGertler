# Omer Gertler


class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_title, message_body, urgent=False):
        """Send a message to a recipient.

        Note: I added 'read' key to the message_details dictionary to enable marking messages
                as read or not. This key is useful in the "read_inbox" method.
                The default 'read' value for a new message is False.
                In addition, I added 'title' to the details to enable
                searching in the title (look at the exercise requirements). (Omer Gertler).
        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_title: The title of the message.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': message_title,
            'body': message_body,
            'sender': sender,
            'read': False
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """ Return the n first unread messages in the user's post-box.

        If n is not specified, return all unread messages in the box.
        :param str username: The username's name.
        :param int n: The number of the required first unread messages (assume positive number).
        :return: List of the first n unread messages.
        :rtype: list
        """
        user_box = self.boxes[username]
        read_box = []
        if n is None or n > len(user_box):
            n = len(user_box)
        for i in range(n):
            msg = user_box[i]
            if msg['read'] is False:
                read_box.append(msg)
                msg['read'] = True
                # next call the loop won't iterate this post:
                user_box.append(user_box.pop(msg))
        return read_box

    def search_inbox(self, username, string):
        """ Return all messages that contain 'string' in the message's body or title.

        :param str username: The username's name to search in his post-box.
        :param str string: The string for looking for.
        :return: All the messages that contain the string.
        :rtype: list
        """
        res = []
        for msg in self.boxes[username]:
            if string in msg.message_body or string in msg.message_title:
                res.append(msg)
        return res
