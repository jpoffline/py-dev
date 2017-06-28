# pylint: disable=C0111
# pylint: disable=C0103

from htmlwidgets import *
import test_framework as test


def test_html():
    actual = html('test')
    expected = '<html><head><title>Blank</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_withTitle_html():
    actual = html('test', title='my title')
    expected = '<html><head><title>my title</title></head>test</html>'
    return test.exe_test(actual, expected)


def test_input_submit_form():

    an_id = 'send'
    labels = ['label_1', 'label_2']
    in_vars = ['var1', 'var2']
    expected = '<form action="/send?var1&var2" method="POST">'\
        + '<label>label_1</label><input name="var1" type="text">'\
        + '<input name="Send" type="submit">'\
        + '<label>label_2</label>'\
        + '<input name="var2" type="text">'\
        + '<input name="Send" type="submit"></form>'
    actual = input_submit_form(an_id, labels, in_vars)
    return test.exe_test(actual, expected)


def test_label():
    expected = '<label>text</label>'
    actual = label('text')
    return test.exe_test(actual, expected)


def test_noReplies_pagePut():
    reply = None

    expected = ''
    actual = pagePut('send', reply, '')
    return test.exe_test(actual, expected)


def test_wrongAnchor_pagePut():
    reply = [
        'send',
        {
            'key': 'your_name',
            'val': 'jonny'
        },
        {
            'key': 'your_age',
            'val': '29'
        }
    ]

    expected = ''
    actual = pagePut('send2', reply, '')
    return test.exe_test(actual, expected)


def test_pagePut():
    reply = [
        '/send',
        {
            'key': 'your_name',
            'val': 'jonny'
        },
        {
            'key': 'your_age',
            'val': '29'
        }
    ]

    expected = '<div>Your name: jonny, Your age: 29</div>'
    actual = pagePut(
        'send', reply, '<div>Your name: ?your_name, Your age: ?your_age</div>')
    return test.exe_test(actual, expected)


def test_plain_div():
    expected = "<div>TEXT</div>"
    actual = div("TEXT")
    return test.exe_test(actual, expected)


def test_style_div():
    expected = "<div style=\"color: blue;\">TEXT</div>"
    actual = div("TEXT", style={'color': 'blue'})
    return test.exe_test(actual, expected)


def test_stylesList_div():
    expected = "<div style=\"color: blue; weight: bold;\">TEXT</div>"
    actual = div("TEXT", style={'color': 'blue', 'weight': 'bold'})
    return test.exe_test(actual, expected)


def test_title():
    expected = '<title>TEXT</title>'
    actual = title("TEXT")
    return test.exe_test(actual, expected)


def test_head():
    expected = '<head><title>TEXT</title></head>'
    actual = head("TEXT")
    return test.exe_test(actual, expected)