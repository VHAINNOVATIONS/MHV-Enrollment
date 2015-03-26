#---------------------------------------------------------------------------
# Copyright 2013 PwC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#---------------------------------------------------------------------------

## @package REG_IEMHV_Suite
## Registration Package Increase Enrollment in My HealtheVet Test (Suite)

'''
These are the Registration package Increase Enrollment in My HealtheVet
tests, implemented as Python functions.

Each test has a unique name derived from the test method name.
Each test has a unique result log with a filename derived from the testname and a datestamp.
There is a parent resultlog that is also used for pass/fail logging.
In general each test establishes a connection to the target application (VistA),
signs on as a user, provider, or programmer and then performs a set of test functions.
When testing is complete the connection is closed and a pass/fail indicate is written
to the resultlog.

Created on March 18 2015
@author: Brian Tomlin
@copyright PwC
@license http://www.apache.org/licenses/LICENSE-2.0
'''

import sys
sys.path = ['./Functional/RAS/lib'] + ['./dataFiles'] + ['./Python/vista'] + sys.path
from REG_IEMHV_Actions import REG_IEMHV_Actions
from Actions import Actions
import datetime
import TestHelper
import time



def IEMHV_T1_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='000000113')
        reg.pre_reg_tc_1_step_3to8()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T1_02(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='000000113')
        reg.pre_reg_tc_1_step_9to11()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_03(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='000000113')
        reg.pre_reg_tc_1_step_12to16()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_04(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='000000113')
        reg.pre_reg_tc_1_step_17to18()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_05(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='543236666')
        reg.pre_reg_tc_1_step_19to26()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_06(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='543236666')
        reg.pre_reg_tc_1_step_27to32()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_07(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='543236666')
        reg.pre_reg_tc_1_step_33to34()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_07_1(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_1to2(ssn='543236666')
        reg.pre_reg_tc_1_step_Delete_Reason()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T1_08(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_1_step_37to38(ssn='543236666')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T2_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_2(ssn='888776666')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T3_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_3(ssn='333224444')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T4_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_4(ssn='666551234')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T5_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_5(ssn='656454321')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T6_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_6(ssn='656451234')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T7_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_5(ssn='656771234')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T8_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_5(ssn='655447777')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T9_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_9(ssn='323123456')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T10_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_10_step_1to13(ssn='345238901')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T10_02(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_10_step_14to16(ssn='345238901')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)



def IEMHV_T11_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_11_step_1to12(ssn='354623902')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_T11_02(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_11_step_13to16(ssn='354623902')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_T11_03(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_11_step_13to16_Action_NO(ssn='354623902')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)



def IEMHV_T12_01(test_suite_details):
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_12(ssn='345678233')
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)



def IEMHV_mhvPats(test_suite_details):
    '''This clears all MHV data in the 2 node of the patient file'''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.mhv_pats(ssn='000000113')

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_prereg_logflow(test_suite_details):
    '''Use XTFCR to log flow to file.  Note a test, just creates flow diagrams. '''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)
    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.logflow(['DGPREP1'])

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details, e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_startmon(test_suite_details):
    '''This starts the Coverage Monitor'''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)
    VistA1 = None
    if test_suite_details.coverage_subset == ['*']:
      test_suite_details.coverage_subset=['DGMHV', 'DGMHVAC', 'DGMHVUTL', 'DGPREP1', 'DGRPC', 'DGRPC3', 'DGRPCE1' ]
    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        VistA1.startCoverage(test_suite_details.coverage_subset)

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details, e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        '''
        Close Vista
        '''
        VistA1.write('^\r^\r^\r')
        VistA1.write('h\r')
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)

def IEMHV_stopmon(test_suite_details):
    '''This stops the Coverage Monitor'''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)
    VistA1 = None
    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        path = (test_suite_details.result_dir + '/' + TestHelper.timeStamped('IEMHV_coverage.txt'))
        VistA1.stopCoverage(path, test_suite_details.coverage_type)

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details, e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        '''
        Close Vista
        '''
        VistA1.write('^\r^\r^\r')
        VistA1.write('h\r')
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_set_sys_date_forward(test_suite_details):
    '''This clears all MHV data in the 2 node of the patient file'''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        '''STEP 35 - Set system date to 180 days in the future'''
        reg.pre_reg_set_sys_date_forward180()
        time.sleep(10)

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)


def IEMHV_MUnit(test_suite_details):
    '''This clears all MHV data in the 2 node of the patient file'''
    testname = sys._getframe().f_code.co_name
    test_driver = TestHelper.TestDriver(testname)

    test_driver.pre_test_run(test_suite_details)

    try:
        VistA1 = test_driver.connect_VistA(test_suite_details)
        reg = REG_IEMHV_Actions(VistA1)
        reg.signon()
        reg.pre_reg_tc_MUnit()
        reg.signoff()

        test_driver.post_test_run(test_suite_details)
    except TestHelper.TestError, e:
        test_driver.exception_handling(test_suite_details,e)
    else:
        test_driver.try_else_handling(test_suite_details)
    finally:
        test_driver.finally_handling(test_suite_details)
    test_driver.end_method_handling(test_suite_details)
