class AddressInGroups:

    def __init__(self, id=None, group_id=None):
        self.id = id
        self.group_id = group_id

    def __repr__(self):
        return "%s:%s" % (
        self.id, self.group_id)