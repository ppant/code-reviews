# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:17:16 2021

@author: Pradeep
"""

import hashlib
shard_key = 'ABCDEF'
print(hashlib.md5(shard_key.encode()).hexdigest()[-6:])