ZZDGMHV1 ;VAINNOV/BNT - Increate Enrollment in MyHealtheVet unit test ; 12/9/03 3:22pm
 ;;5.3;Registration;**903**;Aug 13, 1993;Build 53
 ;
 ; Submitted to OSEHRA 04/02/2015 by HP
 ; All entry points authored by Brian Tomlin 2014-2015
 ;
 ; makes it easy to run tests simply by running this routine and
 ; insures that XTMUNIT will be run only where it is present
 I $T(EN^XTMUNIT)'="" D EN^XTMUNIT("ZZDGMHV1",1)
 Q
 ;
STARTUP ; optional entry point
 ; if present executed before any other entry point any variables
 ; or other work that needs to be done for any or all tests in the
 ; routine.  This is run only once at the beginning.
 Q
 ;
SHUTDOWN ; optional entry point
 ; if present executed after all other processing is complete to remove
 ; any variables, or undo work done in STARTUP.
 Q
 ;
SETUP ; optional entry point
 ; if present it will be executed before each test entry to set up
 ; variables, etc.
 Q
 ;
TEARDOWN ; optional entry point
 ; if present it will be exceuted after each test entry to clean up
 ; variables, etc.
 Q
 ;
CHKTXT; Unit test TXT tag in DGMHV routine to verify that it properly splits the text
 ;
 TSTART
 N TXT,LEN
 S LEN=40
 S TXT="THIS IS A LONG LINE OF TEXT. THIS IS A LONG LINE OF TEXT. THIS IS A LONG LINE OF TEXT. THIS IS A LONG LINE OF TEXT. THIS IS A LONG LINE OF TEXT."
 D TXT^DGMHV(TXT,LEN)
 ; Verify tha the MARX(1) is equal to the the words in the first 40 character limit.
 D CHKEQ^XTMUNIT("THIS IS A LONG LINE OF TEXT. THIS IS A",MARX(1),"Return of text doesn't match")
 TROLLBACK
 Q
 ;
CHKLKUPACT ; Test LKUPACT tag in DGMHVAC routine and verify correct MHV SOCIALIZATION ACTIONS is returned
 ;
 TSTART
 N ACT,ACT0
 S ACT=0 F  S ACT=$O(^DGMHV(390.02,ACT)) Q:'ACT  S ACT0=$G(^DGMHV(390.02,ACT,0)) D
 . D CHKEQ^XTMUNIT(ACT0,$$LKUPACT^DGMHVAC(ACT),"Return of MHV SOCIALIZATION ACTION doesn't match")
 . W !,"Expected:  ",ACT0,!,"Actual:  ",ACT0
 . W !,"----------------------------------------------",!
 TROLLBACK
 Q
 ;
CHKCONSTAT ; Test CONSTAT tag in DGMHVUTL routine and verify that the Condensed patient MHV status is covered
 ;
 TSTART
 N DFN,DGFLDNO
 S DGFLDNO(1)=1,DGFLDNO(2)=1,DGFLDNO(3)=1
 S DFN=0 F  S DFN=$O(^DPT(DFN)) Q:'DFN  I $D(^DPT(DFN,2))!($D(^DPT(DFN,1))) D CONSTAT^DGMHVUTL(DFN,.DGFLDNO)
 TROLLBACK
 Q
 ;
XTROU ;
 ;;ZZDGMHV1
 ; Entry points for tests are specified as the third semi-colon piece,
 ; a description of what it tests is optional as the fourth semi-colon
 ; piece on a line. The first line without a third piece terminates the
 ; search for TAGs to be used as entry points
XTENT ;
 ;;CHKTXT;Unit Test to check the TXT^DGMHV API.
 ;;CHKLKUPACT;Unit Test to check the LKUPACT^DGMHVAC API for MHV SOCIALIZATIONS ACTIONS
 ;;CHKCONSTAT;Unit Test to check that the condense patient status is displayed for each patient
 Q