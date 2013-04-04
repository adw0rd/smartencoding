smartencoding
===============

These functions are copied from the source code of Django 1.5b2.
And provides smart functions for convertation into utf8 and other encodings without Django.
For example, I use in the Flask.

.. image:: https://secure.travis-ci.org/adw0rd/smartencoding.png
    :target: http://travis-ci.org/adw0rd/smartencoding


Installation::

    pip install smartencoding

How to use::

    from smartencoding import smart_unicode, smart_unicode_with_replace
    print smart_unicode(some_string)
    print smart_unicode_with_replace(broken_string)

See also:

* https://pypi.python.org/pypi/Unidecode
* https://pypi.python.org/pypi/chardet

