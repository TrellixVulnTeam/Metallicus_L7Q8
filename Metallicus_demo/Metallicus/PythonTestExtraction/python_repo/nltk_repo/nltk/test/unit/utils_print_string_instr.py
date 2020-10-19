# -*- coding: latin-1 -*-
import unittest
b"\nfrom __future__ import absolute_import\nfrom unittest import TestCase\nfrom functools import wraps\nfrom nose.plugins.skip import SkipTest\nfrom nltk.util import py26\n\ndef skip(reason):\n    '\\n    Unconditionally skip a test.\\n    '\n\n    def decorator(test_item):\n        is_test_class = (isinstance(test_item, type) and issubclass(test_item, TestCase))\n        if (is_test_class and py26()):\n            for meth_name in (m for m in dir(test_item) if m.startswith('test_')):\n                patched_method = skip(reason)(getattr(test_item, meth_name))\n                setattr(test_item, meth_name, patched_method)\n        if (not is_test_class):\n\n            @wraps(test_item)\n            def skip_wrapper(*args, **kwargs):\n                raise SkipTest(reason)\n            skip_wrapper.__name__ = test_item.__name__\n            test_item = skip_wrapper\n        test_item.__unittest_skip__ = True\n        test_item.__unittest_skip_why__ = reason\n        return test_item\n    return decorator\n\ndef skipIf(condition, reason):\n    '\\n    Skip a test if the condition is true.\\n    '\n    if condition:\n        return skip(reason)\n    return (lambda obj: obj)\n"
if __name__ == '__main__':
	unittest.main()