""" HTML widgets """

from htmltags import *
import serverhelp as srv
import tools as tools

def head(text, css=None):
    """ Generate a HTML-body environment """
    # HAS_UNIT_TESTS
    return tag_head() + title(text) + style(css) + tag_head(open=False)


def style(css):
    """ Generate a HTML-style environment """
    # HAS_UNIT_TESTS
    if css is None:
        return ''
    return tag_style() + tools.collapse_css(css) + tag_style(open=False)


def title(text):
    """ Generate a HTML-title environment """
    # HAS_UNIT_TESTS
    return tag_title() + text + tag_title(open=False)


def html(text, title=None, css=None):
    """ Generate a HTML-html environment """
    # HAS_UNIT_TESTS
    if title is None:
        title = 'Blank'
    return tag_html() + head(title, css=css) + text + tag_html(open=False)


def body(text):
    """ Generate a HTML-body environment """
    return tag_body() + text + tag_body(open=False)


def h1(text):  # pylint: disable=C0103
    """ Generate a HTML-h1 environment """
    return tag_h1() + text + tag_h1(open=False)


def div(text, style=None, options=None):
    """
    Generate a HTML-div environment

    Optionally pass in css-style or options dict.

    Example inputs:

    options = {
        'id': '1',
        'name': 'this_div'
    }

    style = {
        'color': 'blue',
        'weight': 'bold'
    }
    """
    # HAS_UNIT_TESTS
    if style is None and options is None:
        return tag_div() + text + tag_div(open=False)
    return tag_div(style=style, options=options) + text + tag_div(open=False)


def label(text):
    """ Generate a HTML-label environment """
    # HAS_UNIT_TESTS
    return tag_label() + text + tag_label(open=False)


def form(method, action, text):
    """ Generate a HTML-form environment """
    return tag_form(method, action) + text + tag_form(open=False)


def img(src):
    """
    Generate a HTML-img environment.

    src: The image URL.

    """
    return tag_img(src)


def pagePut(anchor, replies, what):
    """ Generate a HTML-page-put environment """
    if not replies:
        return ''
    elif not '/' + anchor == replies[0]:
        return ''

    for rep in replies[1:]:
        what = what.replace('?' + rep['key'], rep['val'])

    return what

# Compound widgets


def input_submit(text, submit_id, input_type='text', add_button=None, place_holder=None):
    """ Generate an input-submit form HTML-environment """
    html_input_submit = label(text)
    if place_holder is not None:
        html_input_submit += tag_input(input_type, submit_id, place_holder=place_holder)
    else:
        html_input_submit += tag_input(input_type, submit_id)
    if add_button is not None:
        html_input_submit += tag_input('submit', 'send', options={'value': add_button})
    return html_input_submit


def input_submit_meta(in_meta):
    """ Generate an input item from meta data """
    if 'placeholder' in in_meta:
        plch = in_meta['placeholder']
    else:
        plch = None
    lbl = in_meta['label']
    if 'button' in in_meta:
        btn = in_meta['button']
    else:
        btn = None
    if 'type' in in_meta:
        ipt = in_meta['type']
    else:
        ipt = 'text'
    return input_submit(lbl, in_meta['id'], input_type=ipt, add_button=btn, place_holder=plch)


def input_submit_form(meta):
    """ Generate a collection of input fields, with a button """
    form_text = ''
    form_id = meta['form_id']
    ids = []
    for item in meta['inputs']:
        ids.append(item['id'])
        form_text += input_submit_meta(item)
    return form('POST', srv.gen_post_string(form_id, ids), form_text)

def checkbox_group(meta):
    """ Generate a collection of check boxes """
    html_str = ''
    ids = []
    for item in meta['inputs']:
        this_id = item['id']
        ids.append(this_id)
        item.update({'type' : 'checkbox', 'name' : this_id})
        html_str += tag_input('checkbox', this_id, options={'value': item['value']}) + ' ' + item['text'] + "<br />"
    html_str += tag_input('submit', 'send', options={'value': meta['button_label']})
    #return html_str
    return form('POST', srv.gen_post_string(meta['form_id'], ids), html_str)
