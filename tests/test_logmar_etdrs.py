"""
Test logMar to ETDRS conversion.    
"""

import pytest
from test_eyepy.logmar_etdrs import logmar_to_etdrs

class TestLogmarToETDRS:
    def test_neg_logmar_to_etdrs(self):
        assert logmar_to_etdrs(-0.3) == 100
        
    def test_pos_logmar_to_etdrs(self):
        assert logmar_to_etdrs(0.3) == 70
        
    def test_zero_logmar_to_etdrs(self):
        assert logmar_to_etdrs(0) == 85
        