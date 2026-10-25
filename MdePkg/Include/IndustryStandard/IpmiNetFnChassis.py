# /** @file
#   IPMI 2.0 definitions from the IPMI Specification Version 2.0, Revision 1.1.
# 
#   This file contains all NetFn Chassis commands, including:
#     Chassis Commands (Chapter 28)
# 
#   See IPMI specification, Appendix G, Command Assignments
#   and Appendix H, Sub-function Assignments.
# 
#   Copyright (c) 1999 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# 
# IpmiNetFnChassis.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnChassis
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _IPMI_NET_FN_CHASSIS_H_
# #define _IPMI_NET_FN_CHASSIS_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack (1)
# //
# // Net function definition for Chassis command
# //
# #define IPMI_NETFN_CHASSIS  0x00
IPMI_NETFN_CHASSIS  = 0x00

# 
# //
# //  Below is Definitions for Chassis commands (Chapter 28)
# //
# 
# //
# //  Definitions for Get Chassis Capabilities command
# //
# #define IPMI_CHASSIS_GET_CAPABILITIES  0x00
IPMI_CHASSIS_GET_CAPABILITIES  = 0x00

# 
# //
# //  Constants and Structure definitions for "Get Chassis Capabilities" command to follow here
# //
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    CapabilitiesFlags;
#   UINT8    ChassisFruInfoDeviceAddress;
#   UINT8    ChassisSDRDeviceAddress;
#   UINT8    ChassisSELDeviceAddress;
#   UINT8    ChassisSystemManagementDeviceAddress;
#   UINT8    ChassisBridgeDeviceAddress;
# } IPMI_GET_CHASSIS_CAPABILITIES_RESPONSE;
class IPMI_GET_CHASSIS_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",                      UINT8),
    ("CapabilitiesFlags",                   UINT8),
    ("ChassisFruInfoDeviceAddress",         UINT8),
    ("ChassisSDRDeviceAddress",             UINT8),
    ("ChassisSELDeviceAddress",             UINT8),
    ("ChassisSystemManagementDeviceAddress",UINT8),
    ("ChassisBridgeDeviceAddress",          UINT8)
    ]

# 
# //
# //  Definitions for Get Chassis Status command
# //
# #define IPMI_CHASSIS_GET_STATUS  0x01
IPMI_CHASSIS_GET_STATUS  = 0x01

# 
# //
# //  Constants and Structure definitions for "Get Chassis Status" command to follow here
# //
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    CurrentPowerState;
#   UINT8    LastPowerEvent;
#   UINT8    MiscChassisState;
#   UINT8    FrontPanelButtonCapabilities;
# } IPMI_GET_CHASSIS_STATUS_RESPONSE;
class IPMI_GET_CHASSIS_STATUS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",                  UINT8),
    ("CurrentPowerState",               UINT8),
    ("LastPowerEvent",                  UINT8),
    ("MiscChassisState",                UINT8),
    ("FrontPanelButtonCapabilities",    UINT8)
    ]

# 
# //
# //  Definitions for Chassis Control command
# //
# #define IPMI_CHASSIS_CONTROL  0x02
IPMI_CHASSIS_CONTROL  = 0x02

# 
# //
# //  Constants and Structure definitions for "Chassis Control" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChassisControl : 4;
#     UINT8    Reserved       : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL;
class IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChassisControl",  UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL    ChassisControl;
# } IPMI_CHASSIS_CONTROL_REQUEST;
class IPMI_CHASSIS_CONTROL_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChassisControl",  IPMI_CHASSIS_CONTROL_CHASSIS_CONTROL)
    ]

# 
# //
# //  Definitions for Chassis Reset command
# //
# #define IPMI_CHASSIS_RESET  0x03
IPMI_CHASSIS_RESET  = 0x03

# 
# //
# //  Constants and Structure definitions for "Chassis Reset" command to follow here
# //
# 
# //
# //  Definitions for Chassis Identify command
# //
# #define IPMI_CHASSIS_IDENTIFY  0x04
IPMI_CHASSIS_IDENTIFY  = 0x04

# 
# //
# //  Constants and Structure definitions for "Chassis Identify" command to follow here
# //
# 
# //
# //  Definitions for Set Chassis Capabilities command
# //
# #define IPMI_CHASSIS_SET_CAPABILITIES  0x05
IPMI_CHASSIS_SET_CAPABILITIES  = 0x05

# 
# //
# //  Constants and Structure definitions for "Set Chassis Capabilities" command to follow here
# //
# 
# //
# //  Definitions for Set Power Restore Policy command
# //
# #define IPMI_CHASSIS_SET_POWER_RESTORE_POLICY  0x06
IPMI_CHASSIS_SET_POWER_RESTORE_POLICY  = 0x06

# 
# //
# //  Constants and Structure definitions for "Set Power Restore Policy" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    PowerRestorePolicy : 3;
#     UINT8    Reserved           : 5;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_POWER_RESTORE_POLICY;
class IPMI_POWER_RESTORE_POLICY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerRestorePolicy",  UINT8, 3),
    ("Reserved",            UINT8, 5)
    ]

class IPMI_POWER_RESTORE_POLICY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_POWER_RESTORE_POLICY_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_POWER_RESTORE_POLICY    PowerRestorePolicy;
# } IPMI_SET_POWER_RESTORE_POLICY_REQUEST;
class IPMI_SET_POWER_RESTORE_POLICY_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerRestorePolicy",  IPMI_POWER_RESTORE_POLICY)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    PowerRestorePolicySupport;
# } IPMI_SET_POWER_RESTORE_POLICY_RESPONSE;
class IPMI_SET_POWER_RESTORE_POLICY_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("PowerRestorePolicySupport",   UINT8)
    ]

# 
# //
# //  Definitions for Get System Restart Cause command
# //
# #define IPMI_CHASSIS_GET_SYSTEM_RESTART_CAUSE  0x07
IPMI_CHASSIS_GET_SYSTEM_RESTART_CAUSE  = 0x07

# 
# //
# //  Constants and Structure definitions for "Get System Restart Cause" command to follow here
# //
# #define IPMI_SYSTEM_RESTART_CAUSE_UNKNOWN                    0x0
# #define IPMI_SYSTEM_RESTART_CAUSE_CHASSIS_CONTROL_COMMAND    0x1
# #define IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_RESET           0x2
# #define IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_POWERUP         0x3
# #define IPMI_SYSTEM_RESTART_CAUSE_WATCHDOG_EXPIRE            0x4
# #define IPMI_SYSTEM_RESTART_CAUSE_OEM                        0x5
# #define IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_ALWAYS_RESTORE  0x6
# #define IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_RESTORE_PREV    0x7
# #define IPMI_SYSTEM_RESTART_CAUSE_PEF_RESET                  0x8
# #define IPMI_SYSTEM_RESTART_CAUSE_PEF_POWERCYCLE             0x9
# #define IPMI_SYSTEM_RESTART_CAUSE_SOFT_RESET                 0xA
# #define IPMI_SYSTEM_RESTART_CAUSE_RTC_POWERUP                0xB
IPMI_SYSTEM_RESTART_CAUSE_UNKNOWN                    = 0x0
IPMI_SYSTEM_RESTART_CAUSE_CHASSIS_CONTROL_COMMAND    = 0x1
IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_RESET           = 0x2
IPMI_SYSTEM_RESTART_CAUSE_PUSHBUTTON_POWERUP         = 0x3
IPMI_SYSTEM_RESTART_CAUSE_WATCHDOG_EXPIRE            = 0x4
IPMI_SYSTEM_RESTART_CAUSE_OEM                        = 0x5
IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_ALWAYS_RESTORE  = 0x6
IPMI_SYSTEM_RESTART_CAUSE_AUTO_POWER_RESTORE_PREV    = 0x7
IPMI_SYSTEM_RESTART_CAUSE_PEF_RESET                  = 0x8
IPMI_SYSTEM_RESTART_CAUSE_PEF_POWERCYCLE             = 0x9
IPMI_SYSTEM_RESTART_CAUSE_SOFT_RESET                 = 0xA
IPMI_SYSTEM_RESTART_CAUSE_RTC_POWERUP                = 0xB

# 
# typedef union {
#   struct {
#     UINT8    Cause    : 4;
#     UINT8    Reserved : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SYSTEM_RESTART_CAUSE;
class IPMI_SYSTEM_RESTART_CAUSE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cause",       UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_SYSTEM_RESTART_CAUSE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_RESTART_CAUSE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                        CompletionCode;
#   IPMI_SYSTEM_RESTART_CAUSE    RestartCause;
#   UINT8                        ChannelNumber;
# } IPMI_GET_SYSTEM_RESTART_CAUSE_RESPONSE;
class IPMI_GET_SYSTEM_RESTART_CAUSE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("RestartCause",    IPMI_SYSTEM_RESTART_CAUSE),
    ("ChannelNumber",   UINT8)
    ]

# 
# //
# //  Definitions for Set System BOOT options command
# //
# #define IPMI_CHASSIS_SET_SYSTEM_BOOT_OPTIONS  0x08
IPMI_CHASSIS_SET_SYSTEM_BOOT_OPTIONS  = 0x08

# 
# //
# //  Constants and Structure definitions for "Set System boot options" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ParameterSelector    : 7;
#     UINT8    MarkParameterInvalid : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID;
class IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("MarkParameterInvalid",UINT8, 1),
    ]

class IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID    ParameterValid;
#   UINT8                                    ParameterData[0];
# } IPMI_SET_BOOT_OPTIONS_REQUEST;
class IPMI_SET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterValid",  IPMI_SET_BOOT_OPTIONS_PARAMETER_VALID),
    ("ParameterData",   UINT8 * 0)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode : 8;
# } IPMI_SET_BOOT_OPTIONS_RESPONSE;
class IPMI_SET_BOOT_OPTIONS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8, 8)
    ]

# 
# //
# //  Definitions for Get System Boot options command
# //
# #define IPMI_CHASSIS_GET_SYSTEM_BOOT_OPTIONS  0x09
IPMI_CHASSIS_GET_SYSTEM_BOOT_OPTIONS  = 0x09

# 
# //
# //  Constants and Structure definitions for "Get System boot options" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ParameterSelector : 7;
#     UINT8    Reserved          : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR;
class IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR    ParameterSelector;
#   UINT8                                       SetSelector;
#   UINT8                                       BlockSelector;
# } IPMI_GET_BOOT_OPTIONS_REQUEST;
class IPMI_GET_BOOT_OPTIONS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   IPMI_GET_BOOT_OPTIONS_PARAMETER_SELECTOR),
    ("SetSelector",         UINT8),
    ("BlockSelector",       UINT8)
    ]

# 
# typedef struct {
#   UINT8    Parameter;
#   UINT8    Valid;
#   UINT8    Data1;
#   UINT8    Data2;
#   UINT8    Data3;
#   UINT8    Data4;
#   UINT8    Data5;
# } IPMI_GET_THE_SYSTEM_BOOT_OPTIONS;
class IPMI_GET_THE_SYSTEM_BOOT_OPTIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Parameter",   UINT8),
    ("Valid",       UINT8),
    ("Data1",       UINT8),
    ("Data2",       UINT8),
    ("Data3",       UINT8),
    ("Data4",       UINT8),
    ("Data5",       UINT8)
    ]

# 
# typedef struct {
#   UINT8     ParameterVersion;
#   UINT8     ParameterValid;
#   UINT8     ChannelNumber;
#   UINT32    SessionId;
#   UINT32    TimeStamp;
#   UINT8     Reserved[3];
# } IPMI_BOOT_INITIATOR;
class IPMI_BOOT_INITIATOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterVersion",    UINT8 ),
    ("ParameterValid",      UINT8 ),
    ("ChannelNumber",       UINT8 ),
    ("SessionId",           UINT32),
    ("TimeStamp",           UINT32),
    ("Reserved",            UINT8 * 3)
    ]

# 
# //
# // Definitions for boot option parameter selector
# //
# #define IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SET_IN_PROGRESS             0x0
# #define IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SELECTOR  0x1
# #define IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SCAN      0x2
# #define IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_BMC_BOOT_FLAG               0x3
# #define IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INFO_ACK                        0x4
# #define IPMI_BOOT_OPTIONS_PARAMETER_BOOT_FLAGS                           0x5
# #define IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_INFO                  0x6
# #define IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_MAILBOX               0x7
# #define IPMI_BOOT_OPTIONS_PARAMETER_OEM_BEGIN                            0x60
# #define IPMI_BOOT_OPTIONS_PARAMETER_OEM_END                              0x7F
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SET_IN_PROGRESS             = 0x0
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SELECTOR  = 0x1
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_SERVICE_PARTITION_SCAN      = 0x2
IPMI_BOOT_OPTIONS_PARAMETER_SELECTOR_BMC_BOOT_FLAG               = 0x3
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INFO_ACK                        = 0x4
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_FLAGS                           = 0x5
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_INFO                  = 0x6
IPMI_BOOT_OPTIONS_PARAMETER_BOOT_INITIATOR_MAILBOX               = 0x7
IPMI_BOOT_OPTIONS_PARAMETER_OEM_BEGIN                            = 0x60
IPMI_BOOT_OPTIONS_PARAMETER_OEM_END                              = 0x7F

# 
# //
# // Response Parameters for IPMI Get Boot Options
# //
# typedef union {
#   struct {
#     UINT8    SetInProgress : 2;
#     UINT8    Reserved      : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetInProgress",   UINT8, 2),
    ("Reserved",        UINT8, 6),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    ServicePartitionSelector;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionSelector",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ServicePartitionDiscovered  : 1;
#     UINT8    ServicePartitionScanRequest : 1;
#     UINT8    Reserved                    : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ServicePartitionDiscovered",  UINT8, 1),
    ("ServicePartitionScanRequest", UINT8, 1),
    ("Reserved",                    UINT8, 6)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    BmcBootFlagValid : 5;
#     UINT8    Reserved         : 3;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BmcBootFlagValid",    UINT8, 5),
    ("Reserved",            UINT8, 3)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    WriteMask;
#   UINT8    BootInitiatorAcknowledgeData;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WriteMask",                       UINT8),
    ("BootInitiatorAcknowledgeData",    UINT8)
    ]

# 
# //
# //  Definitions for the 'Boot device selector' field of Boot Option Parameters #5
# //
# #define IPMI_BOOT_DEVICE_SELECTOR_NO_OVERRIDE           0x0
# #define IPMI_BOOT_DEVICE_SELECTOR_PXE                   0x1
# #define IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE             0x2
# #define IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE_SAFE_MODE   0x3
# #define IPMI_BOOT_DEVICE_SELECTOR_DIAGNOSTIC_PARTITION  0x4
# #define IPMI_BOOT_DEVICE_SELECTOR_CD_DVD                0x5
# #define IPMI_BOOT_DEVICE_SELECTOR_BIOS_SETUP            0x6
# #define IPMI_BOOT_DEVICE_SELECTOR_REMOTE_FLOPPY         0x7
# #define IPMI_BOOT_DEVICE_SELECTOR_REMOTE_CD_DVD         0x8
# #define IPMI_BOOT_DEVICE_SELECTOR_PRIMARY_REMOTE_MEDIA  0x9
# #define IPMI_BOOT_DEVICE_SELECTOR_REMOTE_HARDDRIVE      0xB
# #define IPMI_BOOT_DEVICE_SELECTOR_FLOPPY                0xF
IPMI_BOOT_DEVICE_SELECTOR_NO_OVERRIDE           = 0x0
IPMI_BOOT_DEVICE_SELECTOR_PXE                   = 0x1
IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE             = 0x2
IPMI_BOOT_DEVICE_SELECTOR_HARDDRIVE_SAFE_MODE   = 0x3
IPMI_BOOT_DEVICE_SELECTOR_DIAGNOSTIC_PARTITION  = 0x4
IPMI_BOOT_DEVICE_SELECTOR_CD_DVD                = 0x5
IPMI_BOOT_DEVICE_SELECTOR_BIOS_SETUP            = 0x6
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_FLOPPY         = 0x7
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_CD_DVD         = 0x8
IPMI_BOOT_DEVICE_SELECTOR_PRIMARY_REMOTE_MEDIA  = 0x9
IPMI_BOOT_DEVICE_SELECTOR_REMOTE_HARDDRIVE      = 0xB
IPMI_BOOT_DEVICE_SELECTOR_FLOPPY                = 0xF

# 
# #define BOOT_OPTION_HANDLED_BY_BIOS  0x01
BOOT_OPTION_HANDLED_BY_BIOS  = 0x01

# 
# //
# //  Constant definitions for the 'BIOS Mux Control Override' field of Boot Option Parameters #5
# //
# #define BIOS_MUX_CONTROL_OVERRIDE_RECOMMEND_SETTING  0x00
# #define BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_BMC       0x01
# #define BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_SYSTEM    0x02
BIOS_MUX_CONTROL_OVERRIDE_RECOMMEND_SETTING  = 0x00
BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_BMC       = 0x01
BIOS_MUX_CONTROL_OVERRIDE_FORCE_TO_SYSTEM    = 0x02

# 
# typedef union {
#   struct {
#     UINT8    Reserved          : 5;
#     UINT8    BiosBootType      : 1;
#     UINT8    PersistentOptions : 1;
#     UINT8    BootFlagValid     : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("BiosBootType",        UINT8, 1),
    ("PersistentOptions",   UINT8, 1),
    ("BootFlagValid",       UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    LockReset          : 1;
#     UINT8    ScreenBlank        : 1;
#     UINT8    BootDeviceSelector : 4;
#     UINT8    LockKeyboard       : 1;
#     UINT8    CmosClear          : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LockReset",           UINT8, 1),
    ("ScreenBlank",         UINT8, 1),
    ("BootDeviceSelector",  UINT8, 4),
    ("LockKeyboard",        UINT8, 1),
    ("CmosClear",           UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ConsoleRedirection     : 2;
#     UINT8    LockSleep              : 1;
#     UINT8    UserPasswordBypass     : 1;
#     UINT8    ForceProgressEventTrap : 1;
#     UINT8    BiosVerbosity          : 2;
#     UINT8    LockPower              : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ConsoleRedirection",      UINT8, 2),
    ("LockSleep",               UINT8, 1),
    ("UserPasswordBypass",      UINT8, 1),
    ("ForceProgressEventTrap",  UINT8, 1),
    ("BiosVerbosity",           UINT8, 2),
    ("LockPower",               UINT8, 1)
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    BiosMuxControlOverride : 3;
#     UINT8    BiosSharedModeOverride : 1;
#     UINT8    Reserved               : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BiosMuxControlOverride",  UINT8, 3),
    ("BiosSharedModeOverride",  UINT8, 1),
    ("Reserved",                UINT8, 4),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DeviceInstanceSelector : 5;
#     UINT8    Reserved               : 3;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceInstanceSelector",  UINT8, 5),
    ("Reserved",                UINT8, 3),
    ]

class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1    Data1;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2    Data2;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3    Data3;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4    Data4;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5    Data5;
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Data1", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_1),
    ("Data2", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_2),
    ("Data3", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_3),
    ("Data4", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_4),
    ("Data5", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5_DATA_5)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChannelNumber : 4;
#     UINT8    Reserved      : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BOOT_OPTIONS_CHANNEL_NUMBER;
class IPMI_BOOT_OPTIONS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Reserved",        UINT8, 4),
    ]

class IPMI_BOOT_OPTIONS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BOOT_OPTIONS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_BOOT_OPTIONS_CHANNEL_NUMBER    ChannelNumber;
#   UINT8                               SessionId[4];
#   UINT8                               BootInfoTimeStamp[4];
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",       IPMI_BOOT_OPTIONS_CHANNEL_NUMBER),
    ("SessionId",           UINT8 * 4),
    ("BootInfoTimeStamp",   UINT8 * 4)
    ]

# 
# typedef struct {
#   UINT8    SetSelector;
#   UINT8    BlockData[16];
# } IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetSelector", UINT8),
    ("BlockData",   UINT8 * 16)
    ]

# 
# typedef union {
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0    Parm0;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1    Parm1;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2    Parm2;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3    Parm3;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4    Parm4;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5    Parm5;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6    Parm6;
#   IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7    Parm7;
# } IPMI_BOOT_OPTIONS_PARAMETERS;
class IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Parm0", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_0),
    ("Parm1", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_1),
    ("Parm2", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_2),
    ("Parm3", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_3),
    ("Parm4", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_4),
    ("Parm5", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_5),
    ("Parm6", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_6),
    ("Parm7", IPMI_BOOT_OPTIONS_RESPONSE_PARAMETER_7)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ParameterVersion : 4;
#     UINT8    Reserved         : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION;
class IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterVersion",    UINT8, 4),
    ("Reserved",            UINT8, 4)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ParameterSelector : 7;
#     UINT8    ParameterValid    : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID;
class IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ParameterSelector",   UINT8, 7),
    ("ParameterValid",      UINT8, 1)
    ]

class IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                      CompletionCode;
#   IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION    ParameterVersion;
#   IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID      ParameterValid;
#   UINT8                                      ParameterData[0];
# } IPMI_GET_BOOT_OPTIONS_RESPONSE;
class IPMI_GET_BOOT_OPTIONS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8                                  ),
    ("ParameterVersion", IPMI_GET_BOOT_OPTIONS_PARAMETER_VERSION),
    ("ParameterValid",   IPMI_GET_BOOT_OPTIONS_PARAMETER_VALID  ),
    ("ParameterData",    UINT8 * 0                              )
    ]

# 
# //
# //  Definitions for Set front panel button enables command
# //
# #define IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES  0x0A
IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES  = 0x0A

# 
# //
# //  Constants and Structure definitions for "Set front panel button enables" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    DisablePoweroffButton            : 1;
#     UINT8    DisableResetButton               : 1;
#     UINT8    DisableDiagnosticInterruptButton : 1;
#     UINT8    DisableStandbyButton             : 1;
#     UINT8    Reserved                         : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_FRONT_PANEL_BUTTON_ENABLES;
class IPMI_FRONT_PANEL_BUTTON_ENABLES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DisablePoweroffButton",               UINT8, 1),
    ("DisableResetButton",                  UINT8, 1),
    ("DisableDiagnosticInterruptButton",    UINT8, 1),
    ("DisableStandbyButton",                UINT8, 1),
    ("Reserved",                            UINT8, 4)
    ]

class IPMI_FRONT_PANEL_BUTTON_ENABLES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_FRONT_PANEL_BUTTON_ENABLES_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_FRONT_PANEL_BUTTON_ENABLES    FrontPanelButtonEnables;
# } IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES_REQUEST;
class IPMI_CHASSIS_SET_FRONT_PANEL_BUTTON_ENABLES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontPanelButtonEnables", IPMI_FRONT_PANEL_BUTTON_ENABLES)
    ]

# 
# //
# //  Definitions for Set Power Cycle Interval command
# //
# #define IPMI_CHASSIS_SET_POWER_CYCLE_INTERVALS  0x0B
IPMI_CHASSIS_SET_POWER_CYCLE_INTERVALS  = 0x0B

# 
# //
# //  Constants and Structure definitions for "Set Power Cycle Interval" command to follow here
# //
# 
# //
# //  Definitions for Get POH Counter command
# //
# #define IPMI_CHASSIS_GET_POH_COUNTER  0x0F
IPMI_CHASSIS_GET_POH_COUNTER  = 0x0F

# 
# //
# //  Constants and Structure definitions for "Get POH Counter" command to follow here
# //
# #pragma pack()
# #endif
# 