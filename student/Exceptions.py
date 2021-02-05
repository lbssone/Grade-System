#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id: Exceptions.py 1875 2021-02-05 02:51:13Z Tiffany $
#
# Copyright (c) 2021 Nuwa Information Co., Ltd, All Rights Reserved.
#
# Licensed under the Proprietary License,
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at our web site.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# $Author: Tiffany $
# $Date: 2021-02-05 10:51:13 +0800 (週五, 05 二月 2021) $
# $Revision: 1875 $


# Student Class Related
class StudentExistedError(Exception):
    def __init__(self, message="Student already exists."):
        self.message = message
        super().__init__(self.message)


class StudentNotFoundError(Exception):
    def __init__(self, message="Student not found."):
        self.message = message
        super().__init__(self.message)


class StudentIdTypeError(Exception):
    def __init__(self, message="Student ID should be integers."):
        self.message = message
        super().__init__(self.message)


class StudentNameTypeError(Exception):
    def __init__(self, message="Student name should contain only characters."):
        self.message = message
        super().__init__(self.message)


class PhoneLengthError(Exception):
    def __init__(self, message="Phone should be exactly 10 digits."):
        self.message = message
        super().__init__(self.message)


class PhoneTypeError(Exception):
    def __init__(self, message="Phone should be integers."):
        self.message = message
        super().__init__(self.message)


# Grade Class Related
class TestNumberTypeError(Exception):
    def __init__(self, message="Test Number should be integers."):
        self.message = message
        super().__init__(self.message)


class TestNumberOutOfRangeError(Exception):
    def __init__(self, message="No such test number"):
        self.message = message
        super().__init__(self.message)


class GradeTypeError(Exception):
    def __init__(self, message="Subject scores should be integers."):
        self.message = message
        super().__init__(self.message)


class GradeOutOfRangeError(Exception):
    def __init__(self, message="Grade should be between 0 and 100."):
        self.message = message
        super().__init__(self.message)


class GradeNotFoundError(Exception):
    def __init__(self, testNo):
        self.message = f"The student did no participated in test {testNo}. No grade to be updated."
        super().__init__(self.message)


class GradeExistedError(Exception):
    def __init__(self):
        self.message = f"Grade already exists."
        super().__init__(self.message)