#!/usr/bin/env python
# -*- coding: utf-8 -*- 

s = '\xED\x95\x9C\xEA\xB8\x80'
#s = '한글'
print s.decode('utf-8').encode('utf-8')
