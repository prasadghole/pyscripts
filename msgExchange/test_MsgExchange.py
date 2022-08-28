from msgExchange import MsgExchange
from msgExchange import TopicMessage

import queue


def test_subscirbe_init():
    exchange = MsgExchange('Mainexchange')
    myq = queue.Queue()
    exchange.subscribe('Hello', myq)
    assert(exchange.topicdir.__contains__('Hello'))

def test_publish_init():
    exchange = MsgExchange('Mainexchange')
    myq = queue.Queue()
    exchange.subscribe('Hello', myq)
    assert(exchange.topicdir.__contains__('Hello'))
    exchange.publish(TopicMessage('Hello'))
