#!/usr/bin/env python

# This amulet test deploys a sub-class named yaml file in this directory.

import os
import unittest
import yaml
import amulet


class GangliaBundleTest(unittest.TestCase):
    """ Create a class for testing the charm in the unit test framework. """

    bundle_name = None

    @classmethod
    def setUpClass(cls):
        """ Set up an amulet deployment using the bundle. """
        if not cls.bundle_name:
            return
        d = amulet.Deployment()
        bundle_path = os.path.join(os.path.dirname(__file__), cls.bundle_name)
        with open(bundle_path, 'r') as bundle_file:
            contents = yaml.safe_load(bundle_file)
            d.load(contents)
        seconds_to_wait = os.environ.get('AMULET_SETUP_TIMEOUT', 600)
        d.setup(seconds_to_wait)
        d.sentry.wait(seconds_to_wait)
        cls.d = d

    def test_deployed(self):
        """ Test to see if the bundle deployed successfully. """
        self.assertTrue(self.d.deployed)
