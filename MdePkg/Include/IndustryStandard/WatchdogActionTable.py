# /** @file
#   ACPI Watchdog Action Table (WADT) as defined at
#   Microsoft Hardware Watchdog Timers Design Specification.
# 
#   Copyright (c) 2008 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
#
# WatchdogActionTable.py
#
# EfiPy2.MdePkg.IndustryStandard.WatchdogActionTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _WATCHDOG_ACTION_TABLE_H_
# #define _WATCHDOG_ACTION_TABLE_H_
# 
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import *
from EfiPy2.MdePkg.IndustryStandard import Acpi

# 
# //
# // Ensure proper structure formats
# //
# #pragma pack(1)
# ///
# /// Watchdog Action Table definition.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         WatchdogHeaderLength;
#   UINT16                         PCISegment;
#   UINT8                          PCIBusNumber;
#   UINT8                          PCIDeviceNumber;
#   UINT8                          PCIFunctionNumber;
#   UINT8                          Reserved_45[3];
#   UINT32                         TimerPeriod;
#   UINT32                         MaxCount;
#   UINT32                         MinCount;
#   UINT8                          WatchdogFlags;
#   UINT8                          Reserved_61[3];
#   UINT32                         NumberWatchdogInstructionEntries;
# } EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE;
class EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                            Acpi.EFI_ACPI_DESCRIPTION_HEADER),
    ("WatchdogHeaderLength",              UINT32),
    ("PCISegment",                        UINT16),
    ("PCIBusNumber",                      UINT8),
    ("PCIDeviceNumber",                   UINT8),
    ("PCIFunctionNumber",                 UINT8),
    ("Reserved_45",                       UINT8 * 3),
    ("TimerPeriod",                       UINT32),
    ("MaxCount",                          UINT32),
    ("MinCount",                          UINT32),
    ("WatchdogFlags",                     UINT8),
    ("Reserved_61",                       UINT8 * 3),
    ("NumberWatchdogInstructionEntries",  UINT32)
  ]

# 
# ///
# /// Watchdog Instruction Entries
# ///
# typedef struct {
#   UINT8                                     WatchdogAction;
#   UINT8                                     InstructionFlags;
#   UINT8                                     Reserved_2[2];
#   EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE    RegisterRegion;
#   UINT32                                    Value;
#   UINT32                                    Mask;
# } EFI_ACPI_WATCHDOG_ACTION_1_0_WATCHDOG_ACTION_INSTRUCTION_ENTRY;
class EFI_ACPI_WATCHDOG_ACTION_1_0_WATCHDOG_ACTION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("WatchdogAction",    UINT8),
    ("InstructionFlags",  UINT8),
    ("Reserved_2",        UINT8 * 2),
    ("RegisterRegion",    Acpi.EFI_ACPI_2_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",             UINT32),
    ("Mask",              UINT32)
  ]

# 
# #pragma pack()
# 
# ///
# /// WDAT Revision (defined in spec)
# ///
# #define EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE_REVISION  0x01
EFI_ACPI_WATCHDOG_ACTION_1_0_TABLE_REVISION  = 0x01

# 
# //
# // WDAT 1.0 Flags
# //
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ENABLED                 0x1
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_STOPPED_IN_SLEEP_STATE  0x80
EFI_ACPI_WDAT_1_0_WATCHDOG_ENABLED                 = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_STOPPED_IN_SLEEP_STATE  = 0x80

# 
# //
# // WDAT 1.0 Watchdog Actions
# //
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_RESET                           0x1
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_CURRENT_COUNTDOWN_PERIOD  0x4
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_COUNTDOWN_PERIOD          0x5
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_COUNTDOWN_PERIOD            0x6
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_RUNNING_STATE             0x8
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_RUNNING_STATE               0x9
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_STOPPED_STATE             0xA
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_STOPPED_STATE               0xB
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_REBOOT                    0x10
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_REBOOT                      0x11
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_SHUTDOWN                  0x12
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_SHUTDOWN                    0x13
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_WATCHDOG_STATUS           0x20
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_WATCHDOG_STATUS             0x21
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_RESET                           = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_CURRENT_COUNTDOWN_PERIOD  = 0x4
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_COUNTDOWN_PERIOD          = 0x5
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_COUNTDOWN_PERIOD            = 0x6
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_RUNNING_STATE             = 0x8
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_RUNNING_STATE               = 0x9
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_STOPPED_STATE             = 0xA
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_STOPPED_STATE               = 0xB
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_REBOOT                    = 0x10
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_REBOOT                      = 0x11
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_SHUTDOWN                  = 0x12
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_SHUTDOWN                    = 0x13
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_QUERY_WATCHDOG_STATUS           = 0x20
EFI_ACPI_WDAT_1_0_WATCHDOG_ACTION_SET_WATCHDOG_STATUS             = 0x21

# 
# //
# // WDAT 1.0 Watchdog Action Entry Instruction Flags
# //
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_VALUE         0x0
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_COUNTDOWN     0x1
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_VALUE        0x2
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_COUNTDOWN    0x3
# #define EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_PRESERVE_REGISTER  0x80
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_VALUE         = 0x0
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_READ_COUNTDOWN     = 0x1
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_VALUE        = 0x2
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_WRITE_COUNTDOWN    = 0x3
EFI_ACPI_WDAT_1_0_WATCHDOG_INSTRUCTION_PRESERVE_REGISTER  = 0x80
# 
# #endif
# 