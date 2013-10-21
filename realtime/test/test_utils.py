# coding=utf-8
"""
InaSAFE Disaster risk assessment tool developed by AusAid and World Bank
- **Functionality related to shake data files.**

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com'
__version__ = '0.5.0'
__date__ = '30/07/2012'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')
import os
import unittest
from datetime import date

from realtime.utils import (
    baseDataDir,
    shakemapZipDir,
    shakemapExtractDir,
    shakemapDataDir,
    reportDataDir,
    logDir,
    is_event_id,
    purgeWorkingData)

# Clear away working dirs so we can be sure they
# are actually created
purgeWorkingData()
# The logger is intiailsed in utils.py by init
import logging
LOGGER = logging.getLogger('InaSAFE')


class Test(unittest.TestCase):

    def test_baseDataDir(self):
        """Test we can get the realtime data dir"""
        myDir = baseDataDir()
        myExpectedDir = '/tmp/inasafe/realtime'
        assert os.path.exists(myExpectedDir)
        self.assertEqual(myDir, myExpectedDir)

    def test_shakemapZipDir(self):
        """Test we can get the shakemap zip dir"""
        myDir = shakemapZipDir()
        myExpectedDir = '/tmp/inasafe/realtime/shakemaps-zipped'
        assert os.path.exists(myExpectedDir)
        self.assertEqual(myDir, myExpectedDir)

    def test_shakemapExtractDir(self):
        """Test we can get the shakemap extracted data dir"""
        myDir = shakemapExtractDir()
        myExpectedDir = '/tmp/inasafe/realtime/shakemaps-extracted'
        assert os.path.exists(myExpectedDir)
        self.assertEqual(myDir, myExpectedDir)

    def test_shakemapDataDir(self):
        """Test we can get the shakemap post processed data dir"""
        myDir = shakemapDataDir()
        myExpectedDir = '/tmp/inasafe/realtime/shakemaps-processed'
        assert os.path.exists(myExpectedDir)
        self.assertEqual(myDir, myExpectedDir)

    def test_reportDataDir(self):
        """Test we can get the report data dir"""
        myDir = reportDataDir()
        myExpectedDir = '/tmp/inasafe/realtime/reports'
        assert os.path.exists(myExpectedDir)
        self.assertEqual(myDir, myExpectedDir)

    def test_Logging(self):
        myPath = os.path.join(logDir(), 'realtime.log')
        myCurrentDate = date.today()
        myDateString = myCurrentDate.strftime('%d-%m-%Y-%s')
        myMessage = 'Testing logger %s' % myDateString
        LOGGER.info(myMessage)
        myFile = open(myPath, 'rt')
        myLines = myFile.readlines()
        if myMessage not in myLines:
            assert 'Error, expected log message not shown in logs'
        myFile.close()

    def test_is_event_id(self):
        """Test to check if a event is in server
        """
        assert is_event_id('20130110041009'), 'should be event id'
        assert not is_event_id('20130110041090'), 'should not be event id'
        assert not is_event_id('2013'), 'should not be event id'
        assert not is_event_id('AAA'), 'should not be event id'

if __name__ == '__main__':
    unittest.main()
