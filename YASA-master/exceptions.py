#******************************************************************************
# * Copyright (c) 2019, XtremeDV. All rights reserved.
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# * http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *
# * Author: Jude Zhang, Email: zhajio.1988@gmail.com
# *******************************************************************************
# Copyright (c) 2014-2018, Lars Asplund lars.anders.asplund@gmail.com

"""
Contains exceptions which are globally known
"""

class CompileError(Exception):
    """
    An error occured when compiling a HDL file
    """

class TestcaseUnknown(Exception):
    def __init__(self, testCase):
        super(TestcaseUnknown, self).__init__()
        self.errorinfo = '%s is unknown!' % testCase

    def __str__(self):
        return self.errorinfo

class buildUnknown(TestcaseUnknown):
    def __init__(self, build):
        super(buildUnknown, self).__init__(build)

class groupUnknown(TestcaseUnknown):
    def __init__(self, group):
        super(groupUnknown, self).__init__(group)
