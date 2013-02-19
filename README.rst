smartencoding
===============

These functions are copied from the source code of Django 1.5b2.
And provides smart convertation into utf8 and other encodings.

Installation::

    pip install smartencoding

How to use::

    from smartencoding import smart_unicode, smart_unicode_with_replace
    print smart_unicode(some_string)
    print smart_unicode_with_replace(broken_string)

It's all!
