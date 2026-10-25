# /** @file
#   IPMI 2.0 definitions from the IPMI Specification Version 2.0, Revision 1.1.
# 
#   This file contains all NetFn App commands, including:
#     IPM Device "Global" Commands (Chapter 20)
#     Firmware Firewall & Command Discovery Commands (Chapter 21)
#     BMC Watchdog Timer Commands (Chapter 27)
#     IPMI Messaging Support Commands (Chapter 22)
#     RMCP+ Support and Payload Commands (Chapter 24)
# 
#   See IPMI specification, Appendix G, Command Assignments
#   and Appendix H, Sub-function Assignments.
# 
#   Copyright (c) 1999 - 2018, Intel Corporation. All rights reserved.<BR>
#   Copyright (C) 2023 Advanced Micro Devices, Inc. All rights reserved.<BR>
#   Copyright (c) 2023, Ampere Computing LLC. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
#
# IpmiNetFnApp.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnApp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _IPMI_NET_FN_APP_H_
# #define _IPMI_NET_FN_APP_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack(1)
# //
# // Net function definition for App command
# //
# #define IPMI_NETFN_APP  0x06
IPMI_NETFN_APP  = 0x06

# 
# //
# //  Below is Definitions for IPM Device "Global" Commands  (Chapter 20)
# //
# 
# //
# //  Definitions for Get Device ID command
# //
# #define IPMI_APP_GET_DEVICE_ID  0x1
IPMI_APP_GET_DEVICE_ID = 0x1

# 
# //
# //  Constants and Structure definitions for "Get Device ID" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    DeviceRevision : 4;
#     UINT8    Reserved       : 3;
#     UINT8    DeviceSdr      : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_DEVICE_ID_DEVICE_REV;
class IPMI_GET_DEVICE_ID_DEVICE_REV_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceRevision",          UINT8, 4),
    ("Reserved",                UINT8, 3),
    ("DeviceSdr",               UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_DEVICE_REV (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_DEVICE_REV_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MajorFirmwareRev : 7;
#     UINT8    UpdateMode       : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_DEVICE_ID_FIRMWARE_REV_1;
class IPMI_GET_DEVICE_ID_FIRMWARE_REV_1_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MajorFirmwareRev",    UINT8, 7),
    ("UpdateMode",          UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_FIRMWARE_REV_1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_FIRMWARE_REV_1_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SensorDeviceSupport  : 1;
#     UINT8    SdrRepositorySupport : 1;
#     UINT8    SelDeviceSupport     : 1;
#     UINT8    FruInventorySupport  : 1;
#     UINT8    IpmbMessageReceiver  : 1;
#     UINT8    IpmbMessageGenerator : 1;
#     UINT8    BridgeSupport        : 1;
#     UINT8    ChassisSupport       : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_DEVICE_ID_DEVICE_SUPPORT;
class IPMI_GET_DEVICE_ID_DEVICE_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SensorDeviceSupport",     UINT8, 1),
    ("SdrRepositorySupport",    UINT8, 1),
    ("SelDeviceSupport",        UINT8, 1),
    ("FruInventorySupport",     UINT8, 1),
    ("IpmbMessageReceiver",     UINT8, 1),
    ("IpmbMessageGenerator",    UINT8, 1),
    ("BridgeSupport",           UINT8, 1),
    ("ChassisSupport",          UINT8, 1)
    ]

class IPMI_GET_DEVICE_ID_DEVICE_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_DEVICE_ID_DEVICE_SUPPORT_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                CompletionCode;
#   UINT8                                DeviceId;
#   IPMI_GET_DEVICE_ID_DEVICE_REV        DeviceRevision;
#   IPMI_GET_DEVICE_ID_FIRMWARE_REV_1    FirmwareRev1;
#   UINT8                                MinorFirmwareRev;
#   UINT8                                SpecificationVersion;
#   IPMI_GET_DEVICE_ID_DEVICE_SUPPORT    DeviceSupport;
#   UINT8                                ManufacturerId[3];
#   UINT16                               ProductId;
#   UINT32                               AuxFirmwareRevInfo;
# } IPMI_GET_DEVICE_ID_RESPONSE;
class IPMI_GET_DEVICE_ID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",      UINT8                            ),
    ("DeviceId",            UINT8                            ),
    ("DeviceRevision",      IPMI_GET_DEVICE_ID_DEVICE_REV    ),
    ("FirmwareRev1",        IPMI_GET_DEVICE_ID_FIRMWARE_REV_1),
    ("MinorFirmwareRev",    UINT8                            ),
    ("SpecificationVersion",UINT8                            ),
    ("DeviceSupport",       IPMI_GET_DEVICE_ID_DEVICE_SUPPORT),
    ("ManufacturerId",      UINT8 * 3                        ),
    ("ProductId",           UINT16                           ),
    ("AuxFirmwareRevInfo",  UINT32                           )
    ]

# 
# //
# //  Definitions for Cold Reset command
# //
# #define IPMI_APP_COLD_RESET  0x2
IPMI_APP_COLD_RESET  = 0x2

# 
# //
# //  Constants and Structure definitions for "Cold Reset" command to follow here
# //
# 
# //
# //  Definitions for Warm Reset command
# //
# #define IPMI_APP_WARM_RESET  0x3
IPMI_APP_WARM_RESET  = 0x3

# 
# //
# //  Constants and Structure definitions for "Warm Reset" command to follow here
# //
# 
# //
# //  Definitions for Get Self Results command
# //
# #define IPMI_APP_GET_SELFTEST_RESULTS  0x4
IPMI_APP_GET_SELFTEST_RESULTS  = 0x4

# 
# //
# //  Constants and Structure definitions for "Get Self Test Results" command to follow here
# //
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    Result;
#   UINT8    Param;
# } IPMI_SELF_TEST_RESULT_RESPONSE;
class IPMI_SELF_TEST_RESULT_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Result",          UINT8),
    ("Param",           UINT8)
  ]

# 
# #define IPMI_APP_SELFTEST_NO_ERROR              0x55
# #define IPMI_APP_SELFTEST_NOT_IMPLEMENTED       0x56
# #define IPMI_APP_SELFTEST_ERROR                 0x57
# #define IPMI_APP_SELFTEST_FATAL_HW_ERROR        0x58
# #define IPMI_APP_SELFTEST_INACCESSIBLE_SEL      0x80
# #define IPMI_APP_SELFTEST_INACCESSIBLE_SDR      0x40
# #define IPMI_APP_SELFTEST_INACCESSIBLE_FRU      0x20
# #define IPMI_APP_SELFTEST_IPMB_SIGNAL_FAIL      0x10
# #define IPMI_APP_SELFTEST_SDR_REPOSITORY_EMPTY  0x08
# #define IPMI_APP_SELFTEST_FRU_CORRUPT           0x04
# #define IPMI_APP_SELFTEST_FW_BOOTBLOCK_CORRUPT  0x02
# #define IPMI_APP_SELFTEST_FW_CORRUPT            0x01
IPMI_APP_SELFTEST_NO_ERROR             = 0x55
IPMI_APP_SELFTEST_NOT_IMPLEMENTED      = 0x56
IPMI_APP_SELFTEST_ERROR                = 0x57
IPMI_APP_SELFTEST_FATAL_HW_ERROR       = 0x58
IPMI_APP_SELFTEST_INACCESSIBLE_SEL     = 0x80
IPMI_APP_SELFTEST_INACCESSIBLE_SDR     = 0x40
IPMI_APP_SELFTEST_INACCESSIBLE_FRU     = 0x20
IPMI_APP_SELFTEST_IPMB_SIGNAL_FAIL     = 0x10
IPMI_APP_SELFTEST_SDR_REPOSITORY_EMPTY = 0x08
IPMI_APP_SELFTEST_FRU_CORRUPT          = 0x04
IPMI_APP_SELFTEST_FW_BOOTBLOCK_CORRUPT = 0x02
IPMI_APP_SELFTEST_FW_CORRUPT           = 0x01

# 
# //
# //  Definitions for Manufacturing Test ON command
# //
# #define IPMI_APP_MANUFACTURING_TEST_ON  0x5
IPMI_APP_MANUFACTURING_TEST_ON = 0x5

# 
# //
# //  Constants and Structure definitions for "Manufacturing Test ON" command to follow here
# //
# 
# //
# //  Definitions for Set ACPI Power State command
# //
# #define IPMI_APP_SET_ACPI_POWERSTATE  0x6
IPMI_APP_SET_ACPI_POWERSTATE = 0x6

# 
# //
# //  Constants and Structure definitions for "Set ACPI Power State" command to follow here
# //
# 
# //
# //  Definitions for System Power State
# //
# // Working
# #define IPMI_SYSTEM_POWER_STATE_S0_G0  0x0
# #define IPMI_SYSTEM_POWER_STATE_S1     0x1
# #define IPMI_SYSTEM_POWER_STATE_S2     0x2
# #define IPMI_SYSTEM_POWER_STATE_S3     0x3
# #define IPMI_SYSTEM_POWER_STATE_S4     0x4
IPMI_SYSTEM_POWER_STATE_S0_G0  = 0x0
IPMI_SYSTEM_POWER_STATE_S1     = 0x1
IPMI_SYSTEM_POWER_STATE_S2     = 0x2
IPMI_SYSTEM_POWER_STATE_S3     = 0x3
IPMI_SYSTEM_POWER_STATE_S4     = 0x4
# // Soft off
# #define IPMI_SYSTEM_POWER_STATE_S5_G2  0x5
IPMI_SYSTEM_POWER_STATE_S5_G2  = 0x5
# // Sent when message source cannot differentiate between S4 and S5
# #define IPMI_SYSTEM_POWER_STATE_S4_S5  0x6
IPMI_SYSTEM_POWER_STATE_S4_S5  = 0x6
# // Mechanical off
# #define IPMI_SYSTEM_POWER_STATE_G3  0x7
IPMI_SYSTEM_POWER_STATE_G3  = 0x7
# // Sleeping - cannot differentiate between S1-S3
# #define IPMI_SYSTEM_POWER_STATE_SLEEPING  0x8
IPMI_SYSTEM_POWER_STATE_SLEEPING  = 0x8
# // Sleeping - cannot differentiate between S1-S4
# #define IPMI_SYSTEM_POWER_STATE_G1_SLEEPING  0x9
IPMI_SYSTEM_POWER_STATE_G1_SLEEPING  = 0x9
# // S5 entered by override
# #define IPMI_SYSTEM_POWER_STATE_OVERRIDE    0xA
# #define IPMI_SYSTEM_POWER_STATE_LEGACY_ON   0x20
# #define IPMI_SYSTEM_POWER_STATE_LEGACY_OFF  0x21
# #define IPMI_SYSTEM_POWER_STATE_UNKNOWN     0x2A
# #define IPMI_SYSTEM_POWER_STATE_NO_CHANGE   0x7F
IPMI_SYSTEM_POWER_STATE_OVERRIDE    = 0xA
IPMI_SYSTEM_POWER_STATE_LEGACY_ON   = 0x20
IPMI_SYSTEM_POWER_STATE_LEGACY_OFF  = 0x21
IPMI_SYSTEM_POWER_STATE_UNKNOWN     = 0x2A
IPMI_SYSTEM_POWER_STATE_NO_CHANGE   = 0x7F

# 
# //
# //  Definitions for Device Power State
# //
# #define IPMI_DEVICE_POWER_STATE_D0         0x0
# #define IPMI_DEVICE_POWER_STATE_D1         0x1
# #define IPMI_DEVICE_POWER_STATE_D2         0x2
# #define IPMI_DEVICE_POWER_STATE_D3         0x3
# #define IPMI_DEVICE_POWER_STATE_UNKNOWN    0x2A
# #define IPMI_DEVICE_POWER_STATE_NO_CHANGE  0x7F
IPMI_DEVICE_POWER_STATE_D0         = 0x0
IPMI_DEVICE_POWER_STATE_D1         = 0x1
IPMI_DEVICE_POWER_STATE_D2         = 0x2
IPMI_DEVICE_POWER_STATE_D3         = 0x3
IPMI_DEVICE_POWER_STATE_UNKNOWN    = 0x2A
IPMI_DEVICE_POWER_STATE_NO_CHANGE  = 0x7F

# 
# typedef union {
#   struct {
#     UINT8    PowerState  : 7;
#     UINT8    StateChange : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_ACPI_POWER_STATE;
class IPMI_ACPI_POWER_STATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PowerState",  UINT8, 7),
    ("StateChange", UINT8, 1)
    ]

class IPMI_ACPI_POWER_STATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_ACPI_POWER_STATE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_ACPI_POWER_STATE    SystemPowerState;
#   IPMI_ACPI_POWER_STATE    DevicePowerState;
# } IPMI_SET_ACPI_POWER_STATE_REQUEST;
class IPMI_SET_ACPI_POWER_STATE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemPowerState",   IPMI_ACPI_POWER_STATE),
    ("DevicePowerState",   IPMI_ACPI_POWER_STATE)
    ]

# 
# //
# //  Definitions for Get ACPI Power State command
# //
# #define IPMI_APP_GET_ACPI_POWERSTATE  0x7
IPMI_APP_GET_ACPI_POWERSTATE  = 0x7

# 
# //
# //  Constants and Structure definitions for "Get ACPI Power State" command to follow here
# //
# 
# //
# //  Definitions for Get Device GUID command
# //
# #define IPMI_APP_GET_DEVICE_GUID  0x8
IPMI_APP_GET_DEVICE_GUID  = 0x8

# 
# //
# //  Constants and Structure definitions for "Get Device GUID" command to follow here
# //
# //
# //  Message structure definition for "Get Device Guid" IPMI command
# //
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    Guid[16];
# } IPMI_GET_DEVICE_GUID_RESPONSE;
class IPMI_GET_DEVICE_GUID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("Guid",            UINT8 * 16)
  ]

# 
# //
# //  Below is Definitions for BMC Watchdog Timer Commands (Chapter 27)
# //
# 
# //
# //  Definitions for Reset WatchDog Timer command
# //
# #define IPMI_APP_RESET_WATCHDOG_TIMER  0x22
IPMI_APP_RESET_WATCHDOG_TIMER  = 0x22

# 
# //
# //  Definitions for Set WatchDog Timer command
# //
# #define IPMI_APP_SET_WATCHDOG_TIMER  0x24
IPMI_APP_SET_WATCHDOG_TIMER  = 0x24

# 
# //
# //  Constants and Structure definitions for "Set WatchDog Timer" command to follow here
# //
# 
# //
# // Definitions for watchdog timer use
# //
# #define IPMI_WATCHDOG_TIMER_BIOS_FRB2  0x1
# #define IPMI_WATCHDOG_TIMER_BIOS_POST  0x2
# #define IPMI_WATCHDOG_TIMER_OS_LOADER  0x3
# #define IPMI_WATCHDOG_TIMER_SMS        0x4
# #define IPMI_WATCHDOG_TIMER_OEM        0x5
IPMI_WATCHDOG_TIMER_BIOS_FRB2  = 0x1
IPMI_WATCHDOG_TIMER_BIOS_POST  = 0x2
IPMI_WATCHDOG_TIMER_OS_LOADER  = 0x3
IPMI_WATCHDOG_TIMER_SMS        = 0x4
IPMI_WATCHDOG_TIMER_OEM        = 0x5

# 
# //
# //  Structure definition for timer Use
# //
# typedef union {
#   struct {
#     UINT8    TimerUse                  : 3;
#     UINT8    Reserved                  : 3;
#     UINT8    TimerRunning              : 1;
#     UINT8    TimerUseExpirationFlagLog : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_WATCHDOG_TIMER_USE;
class IPMI_WATCHDOG_TIMER_USE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                    UINT8, 3),
    ("Reserved",                    UINT8, 3),
    ("TimerRunning",                UINT8, 1),
    ("TimerUseExpirationFlagLog",   UINT8, 1)
    ]

class IPMI_WATCHDOG_TIMER_USE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_WATCHDOG_TIMER_USE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# //
# //  Definitions for watchdog timeout action
# //
# #define IPMI_WATCHDOG_TIMER_ACTION_NO_ACTION    0x0
# #define IPMI_WATCHDOG_TIMER_ACTION_HARD_RESET   0x1
# #define IPMI_WATCHDOG_TIMER_ACTION_POWER_DONW   0x2
# #define IPMI_WATCHDOG_TIMER_ACTION_POWER_CYCLE  0x3
IPMI_WATCHDOG_TIMER_ACTION_NO_ACTION    = 0x0
IPMI_WATCHDOG_TIMER_ACTION_HARD_RESET   = 0x1
IPMI_WATCHDOG_TIMER_ACTION_POWER_DONW   = 0x2
IPMI_WATCHDOG_TIMER_ACTION_POWER_CYCLE  = 0x3

# 
# //
# //  Definitions for watchdog pre-timeout interrupt
# //
# #define IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NONE       0x0
# #define IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_SMI        0x1
# #define IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NMI        0x2
# #define IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_MESSAGING  0x3
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NONE       = 0x0
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_SMI        = 0x1
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_NMI        = 0x2
IPMI_WATCHDOG_PRE_TIMEOUT_INTERRUPT_MESSAGING  = 0x3

# 
# //
# //  Structure definitions for Timer Actions
# //
# typedef union {
#   struct {
#     UINT8    TimeoutAction       : 3;
#     UINT8    Reserved1           : 1;
#     UINT8    PreTimeoutInterrupt : 3;
#     UINT8    Reserved2           : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_WATCHDOG_TIMER_ACTIONS;
class IPMI_WATCHDOG_TIMER_ACTIONS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimeoutAction",       UINT8, 3),
    ("Reserved1",           UINT8, 1),
    ("PreTimeoutInterrupt", UINT8, 3),
    ("Reserved2",           UINT8, 1)
    ]

class IPMI_WATCHDOG_TIMER_ACTIONS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_WATCHDOG_TIMER_ACTIONS_Bits),
    ("Uint8",   UINT8)
    ]

# 
# //
# //  Bit definitions for Timer use expiration flags
# //
# #define IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_FRB2  BIT1
# #define IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_POST  BIT2
# #define IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OS_LOAD    BIT3
# #define IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_SMS_OS     BIT4
# #define IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OEM        BIT5
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_FRB2  = BIT1
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_BIOS_POST  = BIT2
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OS_LOAD    = BIT3
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_SMS_OS     = BIT4
IPMI_WATCHDOG_TIMER_EXPIRATION_FLAG_OEM        = BIT5

# 
# typedef struct {
#   IPMI_WATCHDOG_TIMER_USE        TimerUse;
#   IPMI_WATCHDOG_TIMER_ACTIONS    TimerActions;
#   UINT8                          PretimeoutInterval;
#   UINT8                          TimerUseExpirationFlagsClear;
#   UINT16                         InitialCountdownValue;
# } IPMI_SET_WATCHDOG_TIMER_REQUEST;
class IPMI_SET_WATCHDOG_TIMER_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TimerUse",                        IPMI_WATCHDOG_TIMER_USE    ),
    ("TimerActions",                    IPMI_WATCHDOG_TIMER_ACTIONS),
    ("PretimeoutInterval",              UINT8                      ),
    ("TimerUseExpirationFlagsClear",    UINT8                      ),
    ("InitialCountdownValue",           UINT16                     )
    ]

# 
# //
# //  Definitions for Get WatchDog Timer command
# //
# #define IPMI_APP_GET_WATCHDOG_TIMER  0x25
IPMI_APP_GET_WATCHDOG_TIMER  = 0x25

# 
# //
# //  Constants and Structure definitions for "Get WatchDog Timer" command to follow here
# //
# typedef struct {
#   UINT8                          CompletionCode;
#   IPMI_WATCHDOG_TIMER_USE        TimerUse;
#   IPMI_WATCHDOG_TIMER_ACTIONS    TimerActions;
#   UINT8                          PretimeoutInterval;
#   UINT8                          TimerUseExpirationFlagsClear;
#   UINT16                         InitialCountdownValue;
#   UINT16                         PresentCountdownValue;
# } IPMI_GET_WATCHDOG_TIMER_RESPONSE;
class IPMI_GET_WATCHDOG_TIMER_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",              UINT8),
    ("TimerUse",                    IPMI_WATCHDOG_TIMER_USE),
    ("TimerActions",                IPMI_WATCHDOG_TIMER_ACTIONS),
    ("PretimeoutInterval",          UINT8),
    ("TimerUseExpirationFlagsClear",UINT8),
    ("InitialCountdownValue",       UINT16),
    ("PresentCountdownValue",       UINT16)
  ]

# 
# //
# //  Below is Definitions for IPMI Messaging Support Commands (Chapter 22)
# //
# 
# //
# //  Definitions for Set BMC Global Enables command
# //
# #define IPMI_APP_SET_BMC_GLOBAL_ENABLES  0x2E
IPMI_APP_SET_BMC_GLOBAL_ENABLES  = 0x2E

# 
# //
# //  Constants and Structure definitions for "Set BMC Global Enables " command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ReceiveMessageQueueInterrupt    : 1;
#     UINT8    EventMessageBufferFullInterrupt : 1;
#     UINT8    EventMessageBuffer              : 1;
#     UINT8    SystemEventLogging              : 1;
#     UINT8    Reserved                        : 1;
#     UINT8    Oem0Enable                      : 1;
#     UINT8    Oem1Enable                      : 1;
#     UINT8    Oem2Enable                      : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_BMC_GLOBAL_ENABLES;
class IPMI_BMC_GLOBAL_ENABLES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReceiveMessageQueueInterrupt",    UINT8, 1),
    ("EventMessageBufferFullInterrupt", UINT8, 1),
    ("EventMessageBuffer",              UINT8, 1),
    ("SystemEventLogging",              UINT8, 1),
    ("Reserved",                        UINT8, 1),
    ("Oem0Enable",                      UINT8, 1),
    ("Oem1Enable",                      UINT8, 1),
    ("Oem2Enable",                      UINT8, 1)
    ]

class IPMI_BMC_GLOBAL_ENABLES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_BMC_GLOBAL_ENABLES_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_BMC_GLOBAL_ENABLES    SetEnables;
# } IPMI_SET_BMC_GLOBAL_ENABLES_REQUEST;
class IPMI_SET_BMC_GLOBAL_ENABLES_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SetEnables",  IPMI_BMC_GLOBAL_ENABLES)
    ]

# 
# //
# //  Definitions for Get BMC Global Enables command
# //
# #define IPMI_APP_GET_BMC_GLOBAL_ENABLES  0x2F
IPMI_APP_GET_BMC_GLOBAL_ENABLES  = 0x2F

# 
# //
# //  Constants and Structure definitions for "Get BMC Global Enables " command to follow here
# //
# typedef struct {
#   UINT8                      CompletionCode;
#   IPMI_BMC_GLOBAL_ENABLES    GetEnables;
# } IPMI_GET_BMC_GLOBAL_ENABLES_RESPONSE;
class IPMI_GET_BMC_GLOBAL_ENABLES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("GetEnables",      IPMI_BMC_GLOBAL_ENABLES)
    ]

# 
# //
# //  Definitions for Clear Message Flags command
# //
# #define IPMI_APP_CLEAR_MESSAGE_FLAGS  0x30
IPMI_APP_CLEAR_MESSAGE_FLAGS = 0x30

# 
# //
# //  Constants and Structure definitions for "Clear Message Flags" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ReceiveMessageQueue         : 1;
#     UINT8    EventMessageBuffer          : 1;
#     UINT8    Reserved1                   : 1;
#     UINT8    WatchdogPerTimeoutInterrupt : 1;
#     UINT8    Reserved2                   : 1;
#     UINT8    Oem0                        : 1;
#     UINT8    Oem1                        : 1;
#     UINT8    Oem2                        : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_MESSAGE_FLAGS;
class IPMI_MESSAGE_FLAGS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReceiveMessageQueue",         UINT8, 1),
    ("EventMessageBuffer",          UINT8, 1),
    ("Reserved1",                   UINT8, 1),
    ("WatchdogPerTimeoutInterrupt", UINT8, 1),
    ("Reserved2",                   UINT8, 1),
    ("Oem0",                        UINT8, 1),
    ("Oem1",                        UINT8, 1),
    ("Oem2",                        UINT8, 1),
    ]

class IPMI_MESSAGE_FLAGS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_MESSAGE_FLAGS_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_MESSAGE_FLAGS    ClearFlags;
# } IPMI_CLEAR_MESSAGE_FLAGS_REQUEST;
class IPMI_CLEAR_MESSAGE_FLAGS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ClearFlags",  IPMI_MESSAGE_FLAGS)
    ]

# 
# //
# //  Definitions for Get Message Flags command
# //
# #define IPMI_APP_GET_MESSAGE_FLAGS  0x31
IPMI_APP_GET_MESSAGE_FLAGS  = 0x31

# 
# //
# //  Constants and Structure definitions for "Get Message Flags" command to follow here
# //
# typedef struct {
#   UINT8                 CompletionCode;
#   IPMI_MESSAGE_FLAGS    GetFlags;
# } IPMI_GET_MESSAGE_FLAGS_RESPONSE;
class IPMI_GET_MESSAGE_FLAGS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("GetFlags",        IPMI_MESSAGE_FLAGS)
    ]

# 
# //
# //  Definitions for Enable Message Channel Receive command
# //
# #define IPMI_APP_ENABLE_MESSAGE_CHANNEL_RECEIVE  0x32
IPMI_APP_ENABLE_MESSAGE_CHANNEL_RECEIVE  = 0x32

# 
# //
# //  Constants and Structure definitions for "Enable Message Channel Receive" command to follow here
# //
# 
# //
# //  Definitions for Get Message command
# //
# #define IPMI_APP_GET_MESSAGE  0x33
IPMI_APP_GET_MESSAGE  = 0x33

# 
# //
# //  Constants and Structure definitions for "Get Message" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChannelNumber          : 4;
#     UINT8    InferredPrivilegeLevel : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_MESSAGE_CHANNEL_NUMBER;
class IPMI_GET_MESSAGE_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",           UINT8, 4),
    ("InferredPrivilegeLevel",  UINT8, 4)
    ]

class IPMI_GET_MESSAGE_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_MESSAGE_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                              CompletionCode;
#   IPMI_GET_MESSAGE_CHANNEL_NUMBER    ChannelNumber;
#   UINT8                              MessageData[0];
# } IPMI_GET_MESSAGE_RESPONSE;
class IPMI_GET_MESSAGE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ChannelNumber",   IPMI_GET_MESSAGE_CHANNEL_NUMBER),
    ("MessageData",     UINT8 * 0)
    ]

# 
# //
# //  Definitions for Send Message command
# //
# #define IPMI_APP_SEND_MESSAGE  0x34
IPMI_APP_SEND_MESSAGE  = 0x34

# 
# //
# //  Constants and Structure definitions for "Send Message" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChannelNumber  : 4;
#     UINT8    Authentication : 1;
#     UINT8    Encryption     : 1;
#     UINT8    Tracking       : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SEND_MESSAGE_CHANNEL_NUMBER;
class IPMI_SEND_MESSAGE_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   UINT8, 4),
    ("Authentication",  UINT8, 1),
    ("Encryption",      UINT8, 1),
    ("Tracking",        UINT8, 2)
    ]

class IPMI_SEND_MESSAGE_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SEND_MESSAGE_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                               CompletionCode;
#   IPMI_SEND_MESSAGE_CHANNEL_NUMBER    ChannelNumber;
#   UINT8                               MessageData[0];
# } IPMI_SEND_MESSAGE_REQUEST;
class IPMI_SEND_MESSAGE_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ChannelNumber",   IPMI_SEND_MESSAGE_CHANNEL_NUMBER),
    ("MessageData",     UINT8 * 0)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    ResponseData[0];
# } IPMI_SEND_MESSAGE_RESPONSE;
class IPMI_SEND_MESSAGE_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("ResponseData",    UINT8 * 0)
    ]

# 
# //
# //  Definitions for Read Event Message Buffer command
# //
# #define IPMI_APP_READ_EVENT_MSG_BUFFER  0x35
IPMI_APP_READ_EVENT_MSG_BUFFER  = 0x35

# 
# //
# //  Constants and Structure definitions for "Read Event Message Buffer" command to follow here
# //
# 
# //
# //  Definitions for Get BT Interface Capabilities command
# //
# #define IPMI_APP_GET_BT_INTERFACE_CAPABILITY  0x36
IPMI_APP_GET_BT_INTERFACE_CAPABILITY  = 0x36

# 
# //
# //  Constants and Structure definitions for "Get BT Interface Capabilities" command to follow here
# //
# 
# //
# //  Definitions for Get System GUID command
# //
# #define IPMI_APP_GET_SYSTEM_GUID  0x37
IPMI_APP_GET_SYSTEM_GUID  = 0x37

# 
# typedef struct {
#   UINT8       CompletionCode;
#   EFI_GUID    SystemUuid;
# } IPMI_GET_SYSTEM_UUID_RESPONSE;
class IPMI_GET_SYSTEM_UUID_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("SystemUuid",      EFI_GUID)
    ]

# 
# //
# //  Constants and Structure definitions for "Get System GUID" command to follow here
# //
# 
# //
# //  Definitions for Get Channel Authentication Capabilities command
# //
# #define IPMI_APP_GET_CHANNEL_AUTHENTICATION_CAPABILITIES  0x38
IPMI_APP_GET_CHANNEL_AUTHENTICATION_CAPABILITIES  = 0x38

# 
# //
# //  Constants and Structure definitions for "Get Channel Authentication Capabilities" command to follow here
# //
# 
# //
# //  Definitions for Get Session Challenge command
# //
# #define IPMI_APP_GET_SESSION_CHALLENGE  0x39
IPMI_APP_GET_SESSION_CHALLENGE  = 0x39

# 
# //
# //  Constants and Structure definitions for "Get Session Challenge" command to follow here
# //
# 
# //
# //  Definitions for Activate Session command
# //
# #define IPMI_APP_ACTIVATE_SESSION  0x3A
IPMI_APP_ACTIVATE_SESSION  = 0x3A

# 
# //
# //  Constants and Structure definitions for "Activate Session" command to follow here
# //
# 
# //
# //  Definitions for Set Session Privelege Level command
# //
# #define IPMI_APP_SET_SESSION_PRIVELEGE_LEVEL  0x3B
IPMI_APP_SET_SESSION_PRIVELEGE_LEVEL  = 0x3B

# 
# //
# //  Constants and Structure definitions for "Set Session Privelege Level" command to follow here
# //
# 
# //
# //  Definitions for Close Session command
# //
# #define IPMI_APP_CLOSE_SESSION  0x3C
IPMI_APP_CLOSE_SESSION  = 0x3C

# 
# //
# //  Constants and Structure definitions for "Close Session" command to follow here
# //
# 
# //
# //  Definitions for Get Session Info command
# //
# #define IPMI_APP_GET_SESSION_INFO  0x3D
IPMI_APP_GET_SESSION_INFO  = 0x3D

# 
# //
# //  Constants and Structure definitions for "Get Session Info" command to follow here
# //
# 
# //
# //  Definitions for Get Auth Code command
# //
# #define IPMI_APP_GET_AUTHCODE  0x3F
IPMI_APP_GET_AUTHCODE  = 0x3F

# 
# //
# //  Constants and Structure definitions for "Get AuthCode" command to follow here
# //
# 
# //
# //  Definitions for Set Channel Access command
# //
# #define IPMI_APP_SET_CHANNEL_ACCESS  0x40
IPMI_APP_SET_CHANNEL_ACCESS  = 0x40
# 
# //
# //  Constants and Structure definitions for "Set Channel Access" command to follow here
# //
# 
# //
# //  Definitions for Get Channel Access command
# //
# #define IPMI_APP_GET_CHANNEL_ACCESS  0x41
IPMI_APP_GET_CHANNEL_ACCESS  = 0x41

# 
# //
# //  Constants and Structure definitions for "Get Channel Access" command to follow here
# //
# 
# //
# //  Definitions for channel access memory type in Get Channel Access command request
# //
# #define IPMI_CHANNEL_ACCESS_MEMORY_TYPE_NON_VOLATILE              0x1
# #define IPMI_CHANNEL_ACCESS_MEMORY_TYPE_PRESENT_VOLATILE_SETTING  0x2
IPMI_CHANNEL_ACCESS_MEMORY_TYPE_NON_VOLATILE              = 0x1
IPMI_CHANNEL_ACCESS_MEMORY_TYPE_PRESENT_VOLATILE_SETTING  = 0x2

# 
# //
# //  Definitions for channel access modes in Get Channel Access command response
# //
# #define IPMI_CHANNEL_ACCESS_MODES_DISABLED          0x0
# #define IPMI_CHANNEL_ACCESS_MODES_PRE_BOOT_ONLY     0x1
# #define IPMI_CHANNEL_ACCESS_MODES_ALWAYS_AVAILABLE  0x2
# #define IPMI_CHANNEL_ACCESS_MODES_SHARED            0x3
IPMI_CHANNEL_ACCESS_MODES_DISABLED          = 0x0
IPMI_CHANNEL_ACCESS_MODES_PRE_BOOT_ONLY     = 0x1
IPMI_CHANNEL_ACCESS_MODES_ALWAYS_AVAILABLE  = 0x2
IPMI_CHANNEL_ACCESS_MODES_SHARED            = 0x3

# 
# typedef union {
#   struct {
#     UINT8    ChannelNo : 4;
#     UINT8    Reserved  : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER;
class IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved   : 6;
#     UINT8    MemoryType : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_CHANNEL_ACCESS_TYPE;
class IPMI_GET_CHANNEL_ACCESS_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 6),
    ("MemoryType",  UINT8, 2)
    ]

class IPMI_GET_CHANNEL_ACCESS_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER    ChannelNumber;
#   IPMI_GET_CHANNEL_ACCESS_TYPE              AccessType;
# } IPMI_GET_CHANNEL_ACCESS_REQUEST;
class IPMI_GET_CHANNEL_ACCESS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_GET_CHANNEL_ACCESS_CHANNEL_NUMBER),
    ("AccessType",      IPMI_GET_CHANNEL_ACCESS_TYPE)
    ]

# 
# typedef union {
#   struct {
#     UINT8    AccessMode           : 3;
#     UINT8    UserLevelAuthEnabled : 1;
#     UINT8    MessageAuthEnable    : 1;
#     UINT8    Alert                : 1;
#     UINT8    Reserved             : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS;
class IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AccessMode",              UINT8, 3),
    ("UserLevelAuthEnabled",    UINT8, 1),
    ("MessageAuthEnable",       UINT8, 1),
    ("Alert",                   UINT8, 1),
    ("Reserved",                UINT8, 2)
    ]

class IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChannelPriviledgeLimit : 4;
#     UINT8    Reserved               : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT;
class IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelPriviledgeLimit",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                      CompletionCode;
#   IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS     ChannelAccess;
#   IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT    PrivilegeLimit;
# } IPMI_GET_CHANNEL_ACCESS_RESPONSE;
class IPMI_GET_CHANNEL_ACCESS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",   UINT8),
    ("ChannelAccess",    IPMI_GET_CHANNEL_ACCESS_CHANNEL_ACCESS),
    ("PrivilegeLimit",   IPMI_GET_CHANNEL_ACCESS_PRIVILEGE_LIMIT)
    ]

# 
# //
# //  Definitions for Get Channel Info command
# //
# #define IPMI_APP_GET_CHANNEL_INFO  0x42
IPMI_APP_GET_CHANNEL_INFO  = 0x42

# 
# //
# //  Constants and Structure definitions for "Get Channel Info" command to follow here
# //
# 
# //
# //  Definitions for channel media type
# //
# // IPMB (I2C)
# #define IPMI_CHANNEL_MEDIA_TYPE_IPMB  0x1
IPMI_CHANNEL_MEDIA_TYPE_IPMB  = 0x1
# // ICMB v1.0
# #define IPMI_CHANNEL_MEDIA_TYPE_ICMB_1_0  0x2
IPMI_CHANNEL_MEDIA_TYPE_ICMB_1_0  = 0x2
# // ICMB v0.9
# #define IPMI_CHANNEL_MEDIA_TYPE_ICMB_0_9  0x3
IPMI_CHANNEL_MEDIA_TYPE_ICMB_0_9  = 0x3
# // 802.3 LAN
# #define IPMI_CHANNEL_MEDIA_TYPE_802_3_LAN  0x4
IPMI_CHANNEL_MEDIA_TYPE_802_3_LAN  = 0x4
# // Asynch. Serial/Modem (RS-232)
# #define IPMI_CHANNEL_MEDIA_TYPE_RS_232  0x5
IPMI_CHANNEL_MEDIA_TYPE_RS_232  = 0x5
# // Other LAN
# #define IPMI_CHANNEL_MEDIA_TYPE_OTHER_LAN  0x6
IPMI_CHANNEL_MEDIA_TYPE_OTHER_LAN  = 0x6
# // PCI SMBus
# #define IPMI_CHANNEL_MEDIA_TYPE_PCI_SM_BUS  0x7
IPMI_CHANNEL_MEDIA_TYPE_PCI_SM_BUS  = 0x7
# // SMBus v1.0/1.1
# #define IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V1  0x8
IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V1  = 0x8
# // SMBus v2.0
# #define IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V2  0x9
IPMI_CHANNEL_MEDIA_TYPE_SM_BUS_V2  = 0x9
# // USB 1.x
# #define IPMI_CHANNEL_MEDIA_TYPE_USB1  0xA
IPMI_CHANNEL_MEDIA_TYPE_USB1  = 0xA
# // USB 2.x
# #define IPMI_CHANNEL_MEDIA_TYPE_USB2  0xB
IPMI_CHANNEL_MEDIA_TYPE_USB2  = 0xB
# // System Interface (KCS, SMIC, or BT)
# #define IPMI_CHANNEL_MEDIA_TYPE_SYSTEM_INTERFACE  0xC
IPMI_CHANNEL_MEDIA_TYPE_SYSTEM_INTERFACE  = 0xC
# // OEM
# #define IPMI_CHANNEL_MEDIA_TYPE_OEM_START  0x60
IPMI_CHANNEL_MEDIA_TYPE_OEM_START  = 0x60
# #define IPMI_CHANNEL_MEDIA_TYPE_OEM_END    0x7F
IPMI_CHANNEL_MEDIA_TYPE_OEM_END    = 0x7F

# 
# //
# //  Definitions for channel protocol type
# //
# // Not available
# #define IPMI_CHANNEL_PROTOCOL_TYPE_NA  0x00
IPMI_CHANNEL_PROTOCOL_TYPE_NA  = 0x00
# // IPMB-1.0
# #define IPMI_CHANNEL_PROTOCOL_TYPE_IPMB_1_0  0x01
IPMI_CHANNEL_PROTOCOL_TYPE_IPMB_1_0  = 0x01
# // ICMB-1.0
# #define IPMI_CHANNEL_PROTOCOL_TYPE_ICMB_1_0  0x02
IPMI_CHANNEL_PROTOCOL_TYPE_ICMB_1_0  = 0x02
# // Reserved
# #define IPMI_CHANNEL_PROTOCOL_TYPE_RESERVED  0x03
IPMI_CHANNEL_PROTOCOL_TYPE_RESERVED  = 0x03
# // IPMI SMBUS
# #define IPMI_CHANNEL_PROTOCOL_TYPE_IPMI_SMBUS  0x04
IPMI_CHANNEL_PROTOCOL_TYPE_IPMI_SMBUS  = 0x04
# // KCS
# #define IPMI_CHANNEL_PROTOCOL_TYPE_KCS  0x05
IPMI_CHANNEL_PROTOCOL_TYPE_KCS  = 0x05
# // SMIC
# #define IPMI_CHANNEL_PROTOCOL_TYPE_SMIC  0x06
IPMI_CHANNEL_PROTOCOL_TYPE_SMIC  = 0x06
# // BT-10
# #define IPMI_CHANNEL_PROTOCOL_TYPE_BT_10  0x07
IPMI_CHANNEL_PROTOCOL_TYPE_BT_10  = 0x07
# // BT-15
# #define IPMI_CHANNEL_PROTOCOL_TYPE_BT_15  0x08
IPMI_CHANNEL_PROTOCOL_TYPE_BT_15  = 0x08
# // TMode
# #define IPMI_CHANNEL_PROTOCOL_TYPE_TMODE  0x09
IPMI_CHANNEL_PROTOCOL_TYPE_TMODE  = 0x09

# 
# typedef union {
#   struct {
#     UINT8    ChannelNo : 4;
#     UINT8    Reserved  : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_INFO_CHANNEL_NUMBER;
class IPMI_CHANNEL_INFO_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_CHANNEL_INFO_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChannelMediumType : 7;
#     UINT8    Reserved          : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_INFO_MEDIUM_TYPE;
class IPMI_CHANNEL_INFO_MEDIUM_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelMediumType",   UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class IPMI_CHANNEL_INFO_MEDIUM_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_MEDIUM_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChannelProtocolType : 5;
#     UINT8    Reserved            : 3;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_INFO_PROTOCOL_TYPE;
class IPMI_CHANNEL_INFO_PROTOCOL_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelProtocolType", UINT8, 5),
    ("Reserved",            UINT8, 3)
    ]

class IPMI_CHANNEL_INFO_PROTOCOL_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_PROTOCOL_TYPE_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ActiveSessionCount : 6;
#     UINT8    SessionSupport     : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_CHANNEL_INFO_SESSION_SUPPORT;
class IPMI_CHANNEL_INFO_SESSION_SUPPORT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActiveSessionCount",  UINT8, 6),
    ("SessionSupport",      UINT8, 2)
    ]

class IPMI_CHANNEL_INFO_SESSION_SUPPORT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_CHANNEL_INFO_SESSION_SUPPORT_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                CompletionCode;
#   IPMI_CHANNEL_INFO_CHANNEL_NUMBER     ChannelNumber;
#   IPMI_CHANNEL_INFO_MEDIUM_TYPE        MediumType;
#   IPMI_CHANNEL_INFO_PROTOCOL_TYPE      ProtocolType;
#   IPMI_CHANNEL_INFO_SESSION_SUPPORT    SessionSupport;
#   UINT8                                VendorId[3];
#   UINT16                               AuxChannelInfo;
# } IPMI_GET_CHANNEL_INFO_RESPONSE;
class IPMI_GET_CHANNEL_INFO_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8                            ),
    ("ChannelNumber",   IPMI_CHANNEL_INFO_CHANNEL_NUMBER ),
    ("MediumType",      IPMI_CHANNEL_INFO_MEDIUM_TYPE    ),
    ("ProtocolType",    IPMI_CHANNEL_INFO_PROTOCOL_TYPE  ),
    ("SessionSupport",  IPMI_CHANNEL_INFO_SESSION_SUPPORT),
    ("VendorId",        UINT8 * 3                        ),
    ("AuxChannelInfo",  UINT16                           )
    ]

# 
# typedef struct {
#   IPMI_CHANNEL_INFO_CHANNEL_NUMBER    ChannelNumber;
# } IPMI_GET_CHANNEL_INFO_REQUEST;
class IPMI_GET_CHANNEL_INFO_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_CHANNEL_INFO_CHANNEL_NUMBER )
    ]

# 
# //
# //  Constants and Structure definitions for "Get Channel Info" command to follow here
# //
# 
# //
# //  Definitions for Set User Access command
# //
# #define IPMI_APP_SET_USER_ACCESS  0x43
IPMI_APP_SET_USER_ACCESS  = 0x43

# 
# //
# //  Constants and Structure definitions for "Set User Access" command to follow here
# //
# 
# //
# //  Definitions for Get User Access command
# //
# #define IPMI_APP_GET_USER_ACCESS  0x44
IPMI_APP_GET_USER_ACCESS  = 0x44

# 
# //
# //  Constants and Structure definitions for "Get User Access" command to follow here
# //
# typedef union {
#   struct {
#     UINT8    ChannelNo : 4;
#     UINT8    Reserved  : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_USER_ACCESS_CHANNEL_NUMBER;
class IPMI_GET_USER_ACCESS_CHANNEL_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNo",   UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class IPMI_GET_USER_ACCESS_CHANNEL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CHANNEL_NUMBER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    UserId   : 6;
#     UINT8    Reserved : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_USER_ID;
class IPMI_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",      UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_GET_USER_ACCESS_CHANNEL_NUMBER    ChannelNumber;
#   IPMI_USER_ID                           UserId;
# } IPMI_GET_USER_ACCESS_REQUEST;
class IPMI_GET_USER_ACCESS_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChannelNumber",   IPMI_GET_USER_ACCESS_CHANNEL_NUMBER),
    ("UserId",          IPMI_USER_ID)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MaxUserId : 6;
#     UINT8    Reserved  : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_USER_ACCESS_MAX_USER_ID;
class IPMI_GET_USER_ACCESS_MAX_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaxUserId",   UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_MAX_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_MAX_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    CurrentUserId      : 6;
#     UINT8    UserIdEnableStatus : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_USER_ACCESS_CURRENT_USER;
class IPMI_GET_USER_ACCESS_CURRENT_USER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CurrentUserId",       UINT8, 6),
    ("UserIdEnableStatus",  UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_CURRENT_USER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CURRENT_USER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FixedUserId : 6;
#     UINT8    Reserved    : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_USER_ACCESS_FIXED_NAME_USER;
class IPMI_GET_USER_ACCESS_FIXED_NAME_USER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FixedUserId", UINT8, 6),
    ("Reserved",    UINT8, 2)
    ]

class IPMI_GET_USER_ACCESS_FIXED_NAME_USER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_FIXED_NAME_USER_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    UserPrivilegeLimit          : 4;
#     UINT8    EnableIpmiMessaging         : 1;
#     UINT8    EnableUserLinkAuthetication : 1;
#     UINT8    UserAccessAvailable         : 1;
#     UINT8    Reserved                    : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_USER_ACCESS_CHANNEL_ACCESS;
class IPMI_GET_USER_ACCESS_CHANNEL_ACCESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserPrivilegeLimit",          UINT8, 4),
    ("EnableIpmiMessaging",         UINT8, 1),
    ("EnableUserLinkAuthetication", UINT8, 1),
    ("UserAccessAvailable",         UINT8, 1),
    ("Reserved",                    UINT8, 1)
    ]

class IPMI_GET_USER_ACCESS_CHANNEL_ACCESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_USER_ACCESS_CHANNEL_ACCESS_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                   CompletionCode;
#   IPMI_GET_USER_ACCESS_MAX_USER_ID        MaxUserId;
#   IPMI_GET_USER_ACCESS_CURRENT_USER       CurrentUser;
#   IPMI_GET_USER_ACCESS_FIXED_NAME_USER    FixedNameUser;
#   IPMI_GET_USER_ACCESS_CHANNEL_ACCESS     ChannelAccess;
# } IPMI_GET_USER_ACCESS_RESPONSE;
class IPMI_GET_USER_ACCESS_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCod",   UINT8                               ),
    ("MaxUserId",       IPMI_GET_USER_ACCESS_MAX_USER_ID    ),
    ("CurrentUser",     IPMI_GET_USER_ACCESS_CURRENT_USER   ),
    ("FixedNameUser",   IPMI_GET_USER_ACCESS_FIXED_NAME_USER),
    ("ChannelAccess",   IPMI_GET_USER_ACCESS_CHANNEL_ACCESS )
    ]

# 
# //
# //  Definitions for Set User Name command
# //
# #define IPMI_APP_SET_USER_NAME  0x45
IPMI_APP_SET_USER_NAME  = 0x45

# 
# //
# //  Constants and Structure definitions for "Set User Name" command to follow here
# //
# typedef struct {
#   IPMI_USER_ID    UserId;
#   UINT8           UserName[16];
# } IPMI_SET_USER_NAME_REQUEST;
class IPMI_SET_USER_NAME_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",   IPMI_USER_ID),
    ("UserName", UINT8 * 16)
    ]

# 
# //
# //  Definitions for Get User Name command
# //
# #define IPMI_APP_GET_USER_NAME  0x46
IPMI_APP_GET_USER_NAME  = 0x46

# 
# //
# //  Constants and Structure definitions for "Get User Name" command to follow here
# //
# typedef struct {
#   IPMI_USER_ID    UserId;
# } IPMI_GET_USER_NAME_REQUEST;
class IPMI_GET_USER_NAME_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",   IPMI_USER_ID)
    ]

# 
# typedef struct {
#   UINT8    CompletionCode;
#   UINT8    UserName[16];
# } IPMI_GET_USER_NAME_RESPONSE;
class IPMI_GET_USER_NAME_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8),
    ("UserName",        UINT8 * 16)
    ]

# 
# //
# //  Definitions for Set User Password command
# //
# #define IPMI_APP_SET_USER_PASSWORD  0x47
IPMI_APP_SET_USER_PASSWORD  = 0x47

# 
# //
# //  Constants and Structure definitions for "Set User Password" command to follow here
# //
# 
# //
# //  Definitions for Set User password command operation type
# //
# #define IPMI_SET_USER_PASSWORD_OPERATION_TYPE_DISABLE_USER   0x0
# #define IPMI_SET_USER_PASSWORD_OPERATION_TYPE_ENABLE_USER    0x1
# #define IPMI_SET_USER_PASSWORD_OPERATION_TYPE_SET_PASSWORD   0x2
# #define IPMI_SET_USER_PASSWORD_OPERATION_TYPE_TEST_PASSWORD  0x3
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_DISABLE_USER   = 0x0
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_ENABLE_USER    = 0x1
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_SET_PASSWORD   = 0x2
IPMI_SET_USER_PASSWORD_OPERATION_TYPE_TEST_PASSWORD  = 0x3

# 
# //
# //  Definitions for Set user password command password size
# //
# #define IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_16  0x0
# #define IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_20  0x1
IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_16  = 0x0
IPMI_SET_USER_PASSWORD_PASSWORD_SIZE_20  = 0x1

# 
# typedef union {
#   struct {
#     UINT8    UserId       : 6;
#     UINT8    Reserved     : 1;
#     UINT8    PasswordSize : 1;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SET_USER_PASSWORD_USER_ID;
class IPMI_SET_USER_PASSWORD_USER_ID_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",          UINT8, 6),
    ("Reserved",        UINT8, 1),
    ("PasswordSize",    UINT8, 1),
    ]

class IPMI_SET_USER_PASSWORD_USER_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_USER_PASSWORD_USER_ID_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Operation : 2;
#     UINT8    Reserved  : 6;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SET_USER_PASSWORD_OPERATION;
class IPMI_SET_USER_PASSWORD_OPERATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Operation",   UINT8, 6),
    ("Reserved",    UINT8, 1)
    ]

class IPMI_SET_USER_PASSWORD_OPERATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SET_USER_PASSWORD_OPERATION_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   IPMI_SET_USER_PASSWORD_USER_ID      UserId;
#   IPMI_SET_USER_PASSWORD_OPERATION    Operation;
#   UINT8                               PasswordData[0]; // 16 or 20 bytes, depending on the 'PasswordSize' field
# } IPMI_SET_USER_PASSWORD_REQUEST;
class IPMI_SET_USER_PASSWORD_REQUEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UserId",          IPMI_SET_USER_PASSWORD_USER_ID),
    ("Operation",       IPMI_SET_USER_PASSWORD_OPERATION),
    ("PasswordData",    UINT8 * 0)
    ]

# 
# //
# //  Below is Definitions for RMCP+ Support and Payload Commands (Chapter 24)
# //
# 
# //
# //  Definitions for Activate Payload command
# //
# #define IPMI_APP_ACTIVATE_PAYLOAD  0x48
IPMI_APP_ACTIVATE_PAYLOAD  = 0x48

# 
# //
# //  Constants and Structure definitions for "Activate Payload" command to follow here
# //
# 
# //
# //  Definitions for De-Activate Payload command
# //
# #define IPMI_APP_DEACTIVATE_PAYLOAD  0x49
IPMI_APP_DEACTIVATE_PAYLOAD  = 0x49

# 
# //
# //  Constants and Structure definitions for "DeActivate Payload" command to follow here
# //
# 
# //
# //  Definitions for Get Payload activation Status command
# //
# #define IPMI_APP_GET_PAYLOAD_ACTIVATION_STATUS  0x4a
IPMI_APP_GET_PAYLOAD_ACTIVATION_STATUS  = 0x4a

# 
# //
# //  Constants and Structure definitions for "Get Payload activation Status" command to follow here
# //
# 
# //
# //  Definitions for Get Payload Instance Info command
# //
# #define IPMI_APP_GET_PAYLOAD_INSTANCE_INFO  0x4b
IPMI_APP_GET_PAYLOAD_INSTANCE_INFO  = 0x4b

# 
# //
# //  Constants and Structure definitions for "Get Payload Instance Info" command to follow here
# //
# 
# //
# //  Definitions for Set User Payload Access command
# //
# #define IPMI_APP_SET_USER_PAYLOAD_ACCESS  0x4C
IPMI_APP_SET_USER_PAYLOAD_ACCESS  = 0x4C

# 
# //
# //  Constants and Structure definitions for "Set User Payload Access" command to follow here
# //
# 
# //
# //  Definitions for Get User Payload Access command
# //
# #define IPMI_APP_GET_USER_PAYLOAD_ACCESS  0x4D
IPMI_APP_GET_USER_PAYLOAD_ACCESS  = 0x4D

# 
# //
# //  Constants and Structure definitions for "Get User Payload Access" command to follow here
# //
# 
# //
# //  Definitions for Get Channel Payload Support command
# //
# #define IPMI_APP_GET_CHANNEL_PAYLOAD_SUPPORT  0x4E
IPMI_APP_GET_CHANNEL_PAYLOAD_SUPPORT  = 0x4E

# 
# //
# //  Constants and Structure definitions for "Get Channel Payload Support" command to follow here
# //
# 
# //
# //  Definitions for Get Channel Payload Version command
# //
# #define IPMI_APP_GET_CHANNEL_PAYLOAD_VERSION  0x4F
IPMI_APP_GET_CHANNEL_PAYLOAD_VERSION  = 0x4F

# 
# //
# //  Constants and Structure definitions for "Get Channel Payload Version" command to follow here
# //
# 
# //
# //  Definitions for Get Channel OEM Payload Info command
# //
# #define IPMI_APP_GET_CHANNEL_OEM_PAYLOAD_INFO  0x50
IPMI_APP_GET_CHANNEL_OEM_PAYLOAD_INFO  = 0x50

# 
# //
# //  Constants and Structure definitions for "Get Channel OEM Payload Info" command to follow here
# //
# 
# //
# //  Definitions for  Master Write-Read command
# //
# #define IPMI_APP_MASTER_WRITE_READ  0x52
IPMI_APP_MASTER_WRITE_READ  = 0x52

# 
# //
# //  Constants and Structure definitions for "Master Write Read" command to follow here
# //
# 
# //
# //  Definitions for  Get Channel Cipher Suites command
# //
# #define IPMI_APP_GET_CHANNEL_CIPHER_SUITES  0x54
IPMI_APP_GET_CHANNEL_CIPHER_SUITES  = 0x54

# 
# //
# //  Constants and Structure definitions for "Get Channel Cipher Suites" command to follow here
# //
# 
# //
# //  Below is Definitions for RMCP+ Support and Payload Commands (Chapter 24, Section 3)
# //
# 
# //
# //  Definitions for  Suspend-Resume Payload Encryption command
# //
# #define IPMI_APP_SUSPEND_RESUME_PAYLOAD_ENCRYPTION  0x55
IPMI_APP_SUSPEND_RESUME_PAYLOAD_ENCRYPTION  = 0x55

# 
# //
# //  Constants and Structure definitions for "Suspend-Resume Payload Encryption" command to follow here
# //
# 
# //
# //  Below is Definitions for IPMI Messaging Support Commands (Chapter 22, Section 25 and 9)
# //
# 
# //
# //  Definitions for  Set Channel Security Keys command
# //
# #define IPMI_APP_SET_CHANNEL_SECURITY_KEYS  0x56
IPMI_APP_SET_CHANNEL_SECURITY_KEYS  = 0x56

# 
# //
# //  Constants and Structure definitions for "Set Channel Security Keys" command to follow here
# //
# 
# //
# //  Definitions for  Get System Interface Capabilities command
# //
# #define IPMI_APP_GET_SYSTEM_INTERFACE_CAPABILITIES  0x57
IPMI_APP_GET_SYSTEM_INTERFACE_CAPABILITIES  = 0x57

# 
# //
# //  Constants and Structure definitions for "Get System Interface Capabilities" command to follow here
# //
# 
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SSIF  0x0
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_KCS   0x1
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SMIC  0x2
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SSIF  = 0x0
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_KCS   = 0x1
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_INTERFACE_TYPE_SMIC  = 0x2

# 
# typedef union {
#   struct {
#     UINT8    InterfaceType : 4;
#     UINT8    Reserved      : 4;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST;
class IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InterfaceType",   UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_REQUEST_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Version            : 3;
#     UINT8    PecSupport         : 1;
#     UINT8    Reserved           : 2;
#     UINT8    TransactionSupport : 2;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES;
class IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",             UINT8, 3),
    ("PecSupport",          UINT8, 1),
    ("Reserved",            UINT8, 2),
    ("TransactionSupport",  UINT8, 2)
    ]

class IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SystemInterfaceVersion : 3;
#     UINT8    Reserved               : 5;
#   } Bits;
#   UINT8    Uint8;
# } IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES;
class IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SystemInterfaceVersion",  UINT8, 3),
    ("Reserved",                UINT8, 5)
    ]

class IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_Bits),
    ("Uint8",   UINT8)
    ]

# 
# typedef struct {
#   UINT8                                      CompletionCode;
#   UINT8                                      Reserved;
#   IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES    InterfaceCap;
#   UINT8                                      InputMsgSize;
#   UINT8                                      OutputMsgSize;
# } IPMI_GET_SYSTEM_INTERFACE_SSIF_CAPABILITIES_RESPONSE;
class IPMI_GET_SYSTEM_INTERFACE_SSIF_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCod",   UINT8                                  ),
    ("Reserved",        UINT8                                  ),
    ("InterfaceCap",    IPMI_SYSTEM_INTERFACE_SSIF_CAPABILITIES),
    ("InputMsgSize",    UINT8                                  ),
    ("OutputMsgSize",   UINT8                                  )
    ]

# 
# typedef struct {
#   UINT8                                          CompletionCode;
#   UINT8                                          Reserved;
#   IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES    InterfaceCap;
#   UINT8                                          InputMaxMsgSize;
# } IPMI_GET_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_RESPONSE;
class IPMI_GET_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CompletionCode",  UINT8                                      ),
    ("Reserved",        UINT8                                      ),
    ("InterfaceCap",    IPMI_SYSTEM_INTERFACE_KCS_SMIC_CAPABILITIES),
    ("InputMaxMsgSize", UINT8                                      )
    ]

# 
# //
# //  Definitions for Get System Interface Capabilities command SSIF transaction support
# //
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_SINGLE_PARTITION_RW             0x0
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW              0x1
# #define IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW_WITH_MIDDLE  0x2
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_SINGLE_PARTITION_RW             = 0x0
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW              = 0x1
IPMI_GET_SYSTEM_INTERFACE_CAPABILITIES_SSIF_TRANSACTION_SUPPORT_MULTI_PARTITION_RW_WITH_MIDDLE  = 0x2

# 
# #pragma pack()
# #endif
# 