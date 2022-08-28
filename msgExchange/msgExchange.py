from threading import Thread
from dataclasses import dataclass
from collections import defaultdict
import queue


@dataclass
class TopicMessage():
    name: str

    def __init__(self, name: str):
        self.name = name


class MsgExchange(Thread):
    """ Class for Message broker """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.topicdir = defaultdict(list)
        self.topicq = queue.Queue()
        self.stoprequested = False

    def subscribe(self, topic, qid):
        try:
            self.topicdir[topic].append(qid)
        except KeyError:
            self.topicdir[topic] = qid

    def publish(self, TopicMessage):
        if self.topicdir.__contains__(TopicMessage.name):
            self.topicq.put(TopicMessage)

    def printtopics(self):
        for k, v in self.topicdir.items():
            print(k, v)

    def processmsg(self, msg):
        """ Helper function to process messages"""
        print(msg)

    def StopExchange(self):
        """ TODO  flush the queue"""
        while not self.topicq.empty():
            self.processmsg(self.topicq.get())

        self.stoprequested = True

    def run(self):
        while not self.stoprequested:
            msg = self.topicq.get()
            self.processmsg(msg)


class MsgObserver(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q


if __name__ == '__main__':
    exchange = MsgExchange('Mainexchange')
    myq = queue.Queue()

    exchange.start()
    exchange.subscribe('Hello', myq)

    for i in range(5):
        exchange.publish(TopicMessage('Hello'))

    exchange.printtopics()
    exchange.StopExchange()
