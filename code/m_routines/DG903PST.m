DG903PST ;ALB/JCH - DG*5.3*903 POST INSTALL ; 11/10/14 9:51am
 ;;5.3;Registration;**903**;Aug 13, 1993;Build 53
 ;
 ; Submitted to OSEHRA 04/02/2015 by HP
 ; All entry points authored by James Harris 2014-2015
 ;
 Q
POST  ; Add entry 315 in INCONSISTENT DATA ELEMENTS file (#38.6)
 ;
 D PCHK
 D MHVACTWP
 Q
 ;
PCHK  ; File new INCONSISTENT DATA ELEMENTS (#38.6) file entry for missing MHV enrollment status
 N DIE,X,Y,DR,DA,DIC,DGFILE,DGIENS,DGFIELD,DGWROOT,DGTXT
 Q:$D(^DGIN(38.6,315))  ; Rule #315 already exists. Can't overwrite different rule, but rule #'s are hard coded in DGRPC*
 S DIE="^DGIN(38.6,",DA=315,DR=".01////MHV ENROLLMENT STATUS MISSING;2////MHV ENROLLMENT STATUS MISSING;3////0;4////0;5////1" D ^DIE
 N DIE,X,Y,DR,DA,DIC
 S DGFILE="38.6",DGIENS="315,",DGFIELD=50,DGWROOT="DGTXT",DGMROOT="DGMSG",DGMSG=""
 S DGTXT(1)="This check ensures a patient has been asked about their enrollment, or "
 S DGTXT(2)="interest in enrollment, in My HealtheVet"
 D WP^DIE(DGFILE,DGIENS,DGFIELD,,DGWROOT,DGMROOT)
 Q 
 ;
MHVACTWP  ; File word processing action display text into MHV SOCIALIZATION ACTIONS (#390.02) file
 N DGACDATA,DGACTIEN,DGACTXT
 F DGACTIEN=1:1:14 S DGACDATA=$T(@DGACTIEN) S DGACTXT=$P(DGACDATA,";",3) D
 .Q:DGACTXT=""
 .N DIE,X,Y,DR,DA,DIC,DGTXTAR,MARX
 .S DGFILE=390.02,DGIENS=DGACTIEN_",",DGFIELD=3,DGWROOT="DGTXTAR",DGMROOT="DGMSG"
 .D TXT^DGMHV(DGACTXT,80)
 .M DGTXTAR=MARX
 .D WP^DIE(DGFILE,DGIENS,DGFIELD,,DGWROOT,DGMROOT)
 .W !,"IEN: ",DGACTIEN,!," TEXT:",$P(DGACDATA,";",3)
 Q
1 ;HELPED PATIENT CREATE ACCOUNT SOCIALIZATION;Helped patient to create a MHV account.
2 ;REFERRED PATIENT TO THE MHV OFFICE SOCIALIZATION;Referred patient to the MHV office/station for assistance with enrollment.
3 ;SCHEDULED FUTURE APPOINTMENT SOCIALIZATION;Scheduled future appointment for patient to enroll at MHV office/station.
4 ;GAVE PATIENT MHV ENROLLMENT INSTRUCTIONS SOCIALIZATION;Gave patient MHV enrollment instructions to complete at a MHV kiosk/computer.
5 ;REFERRED TO COORDINATOR SECURE MESSAGING;Referred patient to MHV coordinator for assistance.
6 ;PATIENT SIGNED AUTHENTICATION FORM AUTHENTICATION;Patient signed MHV authentication form.
7 ;PATIENT COULD NOT AUTHENTICATE (DEFERRED) AUTHENTICATION;Patient could not authenticate. Advised to do so at next appt.
8 ;CLERK COULD NOT AUTHENTICATE (REFERRED) AUTHENTICATION;Clerk did not have authentication form. Referred to another staff member.
9 ;MHV PORTAL ISSUE PREVENTED AUTHENTICATION AUTHENTICATION;MHV admin portal issue prevented patient authentication. Referred to MHV Help Desk or MHV coordinator.
10 ;CAREGIVER NOT PRESENT;AUTHENTICATION;Caregiver not present and Veteran needs caregiver to sign form.
11 ;VETERAN DID NOT HAVE PHOTO ID AUTHENTICATION;Veteran did not have a form of photo ID to authenticate. Advised patient to bring ID to next appointment.
12 ;GAVE PATIENT SECURE MESSAGING INSTRUCTIONS SECURE MESSAGING;Gave patient instructions to set up their secure messaging at home or at kiosk.
13 ;PROVIDED MHV HELP DESK NUMBER AUTHENTICATION SECURE MESSAGING ENROLLMENT SOCIALIZATION;Patient had a MHV account issue. Provided MHV Help Desk toll free #1-877-327-0022, Mon-Fri, 8 a.m.-8 p.m. (EST)
14 ;HELPED SET UP SECURE MESSAGING SECURE MESSAGING;Helped patient set up their secure messaging account.