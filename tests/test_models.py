# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from meican.models import Address


class ModelsTests(unittest.TestCase):
    def setUp(self):
        self.address_data = {
            'uniqueId': 'address_uid',
            'address': 'address',
            'pickUpLocation': 'pick_up_location',
        }

    def test_address(self):
        address = Address(self.address_data)
        self.assertEqual('address_uid address', '{}'.format(address))
