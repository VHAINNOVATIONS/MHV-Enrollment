#---------------------------------------------------------------------------
# Copyright 2015 HP
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

## @package REG_IEMHV_Test
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
@copyright HP
@license http://www.apache.org/licenses/LICENSE-2.0

'''

import sys
sys.path = ['./RAS/lib'] + ['./dataFiles'] + ['../Python/vista'] + sys.path
import REG_IEMHV_suite
import TestHelper

def main():
    test_suite_driver = TestHelper.TestSuiteDriver(__file__)
    test_suite_details = test_suite_driver.generate_test_suite_details()

    try:
        test_suite_driver.pre_test_suite_run(test_suite_details)

        # Begin Tests
        REG_IEMHV_suite.IEMHV_startmon(test_suite_details)
        REG_IEMHV_suite.IEMHV_mhvPats(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_02(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_03(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_04(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_05(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_06(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_07(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_07_1(test_suite_details)
        REG_IEMHV_suite.IEMHV_T1_08(test_suite_details)
        REG_IEMHV_suite.IEMHV_T2_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T3_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T4_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T5_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T6_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T7_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T8_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T9_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T10_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T10_02(test_suite_details)
        REG_IEMHV_suite.IEMHV_T11_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_T11_02(test_suite_details)
        REG_IEMHV_suite.IEMHV_T11_03(test_suite_details)
        # Reset the patient data before test case 12
        REG_IEMHV_suite.IEMHV_mhvPats(test_suite_details)
        REG_IEMHV_suite.IEMHV_T12_01(test_suite_details)
        REG_IEMHV_suite.IEMHV_MUnit(test_suite_details)
        REG_IEMHV_suite.IEMHV_prereg_logflow(test_suite_details)
        REG_IEMHV_suite.IEMHV_stopmon(test_suite_details)
        # End Tests

        test_suite_driver.post_test_suite_run(test_suite_details)
    except Exception, e:
        test_suite_driver.exception_handling(test_suite_details, e)
    else:
        test_suite_driver.try_else_handling(test_suite_details)
    finally:
        test_suite_driver.finally_handling(test_suite_details)

    test_suite_driver.end_method_handling(test_suite_details)

if __name__ == '__main__':
  main()
