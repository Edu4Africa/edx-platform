# pylint: disable=missing-docstring

import ddt
from unittest import TestCase

from track import contexts


@ddt.ddt
class TestContexts(TestCase):

    COURSE_ID = 'test/course_name/course_run'
    SPLIT_COURSE_ID = 'course-v1:test+course_name+course_run'
    ORG_ID = 'test'

    @ddt.data(
        ('http://foo.bar.com/courses/{course_id}', COURSE_ID),
        ('http://foo.bar.com/courses/{course_id}/more/stuff', COURSE_ID),
        ('http://foo.bar.com/courses/{course_id}?format=json', COURSE_ID),
        ('http://foo.bar.com/courses/{course_id}', SPLIT_COURSE_ID),
        ('http://foo.bar.com/courses/{course_id}/more/stuff', SPLIT_COURSE_ID),
        ('http://foo.bar.com/courses/{course_id}?format=json', SPLIT_COURSE_ID)
    )
    @ddt.unpack
    def test_course_id_from_url(self, url, course_id):
        self.assert_parses_course_id_from_url(url, course_id)

    def assert_parses_course_id_from_url(self, format_string, course_id):
        self.assertEquals(
            contexts.course_context_from_url(format_string.format(course_id=course_id)),
            {
                'course_id': course_id,
                'org_id': self.ORG_ID
            }
        )

    def test_no_course_id_in_url(self):
        self.assert_empty_context_for_url('http://foo.bar.com/dashboard')

    def assert_empty_context_for_url(self, url):
        self.assertEquals(
            contexts.course_context_from_url(url),
            {
                'course_id': '',
                'org_id': ''
            }
        )

    def test_malformed_course_id(self):
        self.assert_empty_context_for_url('http://foo.bar.com/courses/test')

    @ddt.data(
        ('http://foo.bar.com/x/y/z/courses/{course_id}', COURSE_ID),
        ('http://foo.bar.com/x/y/z/courses/{course_id}/more/stuff', COURSE_ID),
        ('http://foo.bar.com/x/y/z/courses/{course_id}?format=json', COURSE_ID),
        ('http://foo.bar.com/x/y/z/courses/{course_id}', SPLIT_COURSE_ID),
        ('http://foo.bar.com/x/y/z/courses/{course_id}/more/stuff', SPLIT_COURSE_ID),
        ('http://foo.bar.com/x/y/z/courses/{course_id}?format=json', SPLIT_COURSE_ID)
    )
    @ddt.unpack
    def test_course_id_later_in_url(self, url, course_id):
        self.assert_parses_course_id_from_url(url, course_id)

    def test_no_url(self):
        self.assert_empty_context_for_url(None)
