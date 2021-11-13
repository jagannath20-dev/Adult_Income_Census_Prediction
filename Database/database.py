from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


class Connector:
    def __init__(self):
        """
        :DESC: Creates connection with Database when backend thread runs.
        """
        self.Client_id = 'INKAkfJyEfFAyEIeORtlYYtG'
        self.Client_secret = 'FaRNXX31z4CTxb.uxO1PUkO8L4i-9wgaHyHfzbvhZ1r5yScuXJXcaihoFZyEUohHqzWRrMWvf61lPDZeznUreh221-xow1,LzLPtSuoR_cT9rxmgKns18+vGj+i,oR0,'
        cloud_config = {
            'secure_connect_bundle': 'secure-connect-adultincomecensusprediction.zip'}
        auth_provider = PlainTextAuthProvider(
            self.Client_id, self.Client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()

    def master(self):
        """
        :DESC: Creates table if not existed into database
        :return:
        """
        self.session.execute("use adultincomecensusprediction")
        self.session.execute("select release_version from system.local")
        self.session.execute(
            "CREATE TABLE Data(id uuid PRIMARY KEY ,Age int,Sex text,Capital Gain int,Capital Loss int,Hours-Per-Week int,Country text,Employment Type text);")

    def addData(self, result):
        """
        :param result: Gets data from user and puts it into database
        :return:
        """

        column = "id,Age,Sex,Capital-Gain,Capital-Loss,Hours-Per-Week,Country,Employment-Type"
        value = "{0},{1},'{2}',{3},{4},{5},{6},'{7}'".format('id', result['Age'], result['Sex'],
                                                             result['Capital-Gain'], result['Capital-Loss'],
                                                             result['Hours-Per-Week'], result['Country'],
                                                             result['Employment-Type'])
        custom = "INSERT INTO Data({}) VALUES({});".format(column, value)

        self.session.execute("USE adultincomcensus")

        output = self.session.execute(custom)

    def getData(self):
        """
        :DESC: Retrieves Data from Database
        :return:
        """
        self.session.execute("use adultincomecensus")
        row = self.session.execute("SELECT * FROM Data;")
        collection = []
        for i in row:
            collection.append(tuple(i))
        return tuple(collection)
