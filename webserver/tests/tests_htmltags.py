""" Unit tests for htmltags """
# pylint: disable=C0111
# pylint: disable=C0103

import htmltags
import test_framework as test


def test_tag_html():
    actual = htmltags.tag_html()
    expected = '<html>'
    return test.exe_test(actual, expected)


def test_withmeta_tag():
    actual = htmltags.tag('html', meta='thing')
    expected = '<html thing>'
    return test.exe_test(actual, expected)


def test_withoutmeta_tag():
    actual = htmltags.tag('html')
    expected = '<html>'
    return test.exe_test(actual, expected)


def test_empty_tag_form():
    actual = htmltags.tag_form()
    expected = '<form action="" method="">'
    return test.exe_test(actual, expected)


def test_full_tag_form():
    actual = htmltags.tag_form('METHOD', 'ACTION')
    expected = '<form action="ACTION" method="METHOD">'
    return test.exe_test(actual, expected)


def test_close_tag_form():
    actual = htmltags.tag_form(open=False)
    expected = '</form>'
    return test.exe_test(actual, expected)


def test_tag_h1():
    actual = htmltags.tag_h1()
    expected = '<h1>'
    return test.exe_test(actual, expected)


def test_h2_tag_h_general():
    actual = htmltags.tag_h_general(2)
    expected = '<h2>'
    return test.exe_test(actual, expected)


def test_h5_tag_h_general():
    actual = htmltags.tag_h_general(5)
    expected = '<h5>'
    return test.exe_test(actual, expected)


def test_tag_div():
    actual = htmltags.tag_div()
    expected = '<div>'
    return test.exe_test(actual, expected)


def test_close_tag_div():
    actual = htmltags.tag_div(open=False)
    expected = '</div>'
    return test.exe_test(actual, expected)


def test_style_tag_div():
    actual = htmltags.tag_div(style={'thing': 'value'})
    expected = '<div style=\"thing: value;\">'
    return test.exe_test(actual, expected)


def test_styleOnly_options_to_str():
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    actual = htmltags.options_to_str(style=style)
    expected = 'style=\"color: blue; weight: bold;\"'
    return test.exe_test(actual, expected)


def test_optionsOnly_options_to_str():
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.options_to_str(options=opts)
    expected = 'id=\"1\" name=\"jp\"'
    return test.exe_test(actual, expected)


def test_optionsAndStyle_options_to_str():
    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    opts = {
        'id': '1',
        'name': 'jp'
    }
    actual = htmltags.options_to_str(style=style, options=opts)
    expected = 'style=\"color: blue; weight: bold;\" id=\"1\" name=\"jp\"'
    return test.exe_test(actual, expected)


def test_tag_input():
    actual = htmltags.tag_input('T', 'N')
    expected = '<input name=\"N\" type=\"T\">'
    return test.exe_test(actual, expected)