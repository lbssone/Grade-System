#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id: HelperFunction.py 1875 2021-02-05 02:51:13Z Tiffany $
#
# Copyright (c) 2016 Nuwa Information Co., Ltd, All Rights Reserved.
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

from django.db.models import Max, F, Sum, Avg
from django.db.models.functions import Round, Concat
from .models import Student, Grade
from django.db.models import Q, Value
from student.Exceptions import StudentExistedError, StudentNotFoundError, TestNumberTypeError, GradeNotFoundError, \
GradeExistedError, TestNumberOutOfRangeError

def getAllTestNumbers():
    allTestNumbers = set(Grade.objects.values_list('testNo', flat=True))
    return allTestNumbers

def searchStudent(name):
    students = Student.objects.annotate(full=Concat("firstName", Value(" "), "lastName")).filter(full__icontains=name)
    return students

def getTestsRank(testNumber=0):
    if testNumber:
        grades = Grade.objects.filter(testNo=testNumber).order_by(-(F('chinese') + F('english') + F('math')))
        return grades
    else:
        allTestNumbers = getAllTestNumbers()
        rankDict = {}
        for time in allTestNumbers:
            grades = Grade.objects.filter(testNo=time).order_by(-(F('chinese') + F('english') + F('math')))
            rankDict[time] = grades
        return rankDict

def getSubjectsScores():
    '''
        Returns a dictionary: {
            1: { 
                'total': {'chinese': 240, 'english': 300, 'math': 220},
                'avg': { 'chinese': 240, 'english': 290, 'math': 250 }
            },
            2: ...
        }
    '''
    allTestNumbers = getAllTestNumbers()
    subjectDict = {}
    for time in allTestNumbers:
        total = Grade.objects.filter(testNo=time) \
            .aggregate(chinese=Sum('chinese'), english=Sum('english'), math=Sum('math'))
        avg = Grade.objects.filter(testNo=time) \
            .aggregate(chinese=Round(Avg('chinese')), english=Round(Avg('english')), math=Round(Avg('math')))
        subjectDict[time] = {}
        subjectDict[time]["total"] = total
        subjectDict[time]["avg"] = avg
    return subjectDict