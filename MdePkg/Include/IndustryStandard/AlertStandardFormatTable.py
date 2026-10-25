# /** @file
#   ACPI Alert Standard Format Description Table ASF! as described in the ASF2.0 Specification
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# 
# #ifndef _ALERT_STANDARD_FORMAT_TABLE_H_
# #define _ALERT_STANDARD_FORMAT_TABLE_H_
#
# AlertStandardFormatTable.py
#
# EfiPy2.MdePkg.IndustryStandard.AlertStandardFormatTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #include <IndustryStandard/Acpi.h>
from EfiPy2.MdePkg.IndustryStandard import Acpi, EFIPY_INDUSTRY_STRUCTURE
from EfiPy2 import *

# 
# //
# // Ensure proper structure formats
# //
# #pragma pack (1)
# 
# ///
# /// Information Record header that appears at the beginning of each record
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Reserved;
#   UINT16    RecordLength;
# } EFI_ACPI_ASF_RECORD_HEADER;
class EFI_ACPI_ASF_RECORD_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",          UINT8),
    ("Reserved",      UINT8),
    ("RecordLength",  UINT16)
  ]

# 
# ///
# /// This structure contains information that identifies the system's type
# /// and configuration
# ///
# typedef struct {
#   EFI_ACPI_ASF_RECORD_HEADER    RecordHeader;
#   UINT8                         MinWatchDogResetValue;
#   UINT8                         MinPollingInterval;
#   UINT16                        SystemID;
#   UINT32                        IANAManufactureID;
#   UINT8                         FeatureFlags;
#   UINT8                         Reserved[3];
# } EFI_ACPI_ASF_INFO;
class EFI_ACPI_ASF_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",          EFI_ACPI_ASF_RECORD_HEADER),
    ("MinWatchDogResetValue", UINT8),
    ("MinPollingInterval",    UINT8),
    ("SystemID",              UINT16),
    ("IANAManufactureID",     UINT32_BE),
    ("FeatureFlags",          UINT8),
    ("Reserved",              UINT8 * 3)
  ]

# 
# ///
# /// ASF Alert Data
# ///
# typedef struct {
#   UINT8    DeviceAddress;
#   UINT8    Command;
#   UINT8    DataMask;
#   UINT8    CompareValue;
#   UINT8    EventSenseType;
#   UINT8    EventType;
#   UINT8    EventOffset;
#   UINT8    EventSourceType;
#   UINT8    EventSeverity;
#   UINT8    SensorNumber;
#   UINT8    Entity;
#   UINT8    EntityInstance;
# } EFI_ACPI_ASF_ALERTDATA;
class EFI_ACPI_ASF_ALERTDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceAddress",     UINT8),
    ("Command",           UINT8),
    ("DataMask",          UINT8),
    ("CompareValue",      UINT8),
    ("EventSenseType",    UINT8),
    ("EventType",         UINT8),
    ("EventOffset",       UINT8),
    ("EventSourceType",   UINT8),
    ("EventSeverity",     UINT8),
    ("SensorNumber",      UINT8),
    ("Entity",            UINT8),
    ("EntityInstance",    UINT8)
  ]

# 
# ///
# /// Alert sensors definition
# ///
# typedef struct {
#   EFI_ACPI_ASF_RECORD_HEADER    RecordHeader;
#   UINT8                         AssertionEventBitMask;
#   UINT8                         DeassertionEventBitMask;
#   UINT8                         NumberOfAlerts;
#   UINT8                         ArrayElementLength;        ///< For ASF version 1.0 and later, this filed is set to 0x0C
#   ///
#   /// EFI_ACPI_ASF_ALERTDATA           DeviceArray[ANYSIZE_ARRAY];
#   ///
# } EFI_ACPI_ASF_ALRT;
class EFI_ACPI_ASF_ALRT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",            EFI_ACPI_ASF_RECORD_HEADER),
    ("AssertionEventBitMask",   UINT8),
    ("DeassertionEventBitMask", UINT8),
    ("NumberOfAlerts",          UINT8),
    ("ArrayElementLength",      UINT8),
    # ("DeviceArray",           EFI_ACPI_ASF_ALERTDATA * ANYSIZE_ARRAY)
  ]

# 
# ///
# /// Alert Control Data
# ///
# typedef struct {
#   UINT8    Function;
#   UINT8    DeviceAddress;
#   UINT8    Command;
#   UINT8    DataValue;
# } EFI_ACPI_ASF_CONTROLDATA;
class EFI_ACPI_ASF_CONTROLDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Function",      UINT8),
    ("DeviceAddress", UINT8),
    ("Command",       UINT8),
    ("DataValue",     UINT8)
  ]

# 
# ///
# /// Alert Remote Control System Actions
# ///
# typedef struct {
#   EFI_ACPI_ASF_RECORD_HEADER    RecordHeader;
#   UINT8                         NumberOfControls;
#   UINT8                         ArrayElementLength;        ///< For ASF version 1.0 and later, this filed is set to 0x4
#   UINT16                        RctlReserved;
#   ///
#   /// EFI_ACPI_ASF_CONTROLDATA;        DeviceArray[ANYSIZE_ARRAY];
#   ///
# } EFI_ACPI_ASF_RCTL;
class EFI_ACPI_ASF_RCTL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",        EFI_ACPI_ASF_RECORD_HEADER),
    ("NumberOfControls",    UINT8),
    ("ArrayElementLength",  UINT8),
    ("RctlReserved",        UINT8),
    # ("DeviceArray",       EFI_ACPI_ASF_CONTROLDATA * ANYSIZE_ARRAY)
  ]

# 
# ///
# /// Remote Control Capabilities
# ///
# typedef struct {
#   EFI_ACPI_ASF_RECORD_HEADER    RecordHeader;
#   UINT8                         RemoteControlCapabilities[7];
#   UINT8                         RMCPCompletionCode;
#   UINT32                        RMCPIANA;
#   UINT8                         RMCPSpecialCommand;
#   UINT8                         RMCPSpecialCommandParameter[2];
#   UINT8                         RMCPBootOptions[2];
#   UINT8                         RMCPOEMParameters[2];
# } EFI_ACPI_ASF_RMCP;
class EFI_ACPI_ASF_RMCP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",                EFI_ACPI_ASF_RECORD_HEADER),
    ("RemoteControlCapabilities",   UINT8 * 7),
    ("RMCPCompletionCode",          UINT8),
    ("RMCPIANA",                    UINT32_BE),
    ("RMCPSpecialCommand",          UINT8),
    ("RMCPSpecialCommandParameter", UINT8 * 2),
    ("RMCPBootOptions",             UINT8 * 2),
    ("RMCPOEMParameters",           UINT8 * 2)
  ]

# 
# ///
# /// SMBus Devices with fixed addresses
# ///
# typedef struct {
#   EFI_ACPI_ASF_RECORD_HEADER    RecordHeader;
#   UINT8                         SEEPROMAddress;
#   UINT8                         NumberOfDevices;
#   ///
#   /// UINT8                            FixedSmbusAddresses[ANYSIZE_ARRAY];
#   ///
# } EFI_ACPI_ASF_ADDR;
class EFI_ACPI_ASF_ADDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RecordHeader",        EFI_ACPI_ASF_RECORD_HEADER),
    ("SEEPROMAddress",      UINT8),
    ("NumberOfDevices",     UINT8),
    # ("FixedSmbusAddresses", UINT8 * ANYSIZE_ARRAY)
  ]

# 
# ///
# /// ASF! Description Table Header
# ///
# typedef EFI_ACPI_DESCRIPTION_HEADER EFI_ACPI_ASF_DESCRIPTION_HEADER;
EFI_ACPI_ASF_DESCRIPTION_HEADER = Acpi.EFI_ACPI_DESCRIPTION_HEADER

# 
# ///
# /// The revision stored in ASF! DESCRIPTION TABLE as BCD value
# ///
# #define EFI_ACPI_2_0_ASF_DESCRIPTION_TABLE_REVISION  0x20
EFI_ACPI_2_0_ASF_DESCRIPTION_TABLE_REVISION   = 0x20

# 
# ///
# /// "ASF!" ASF Description Table Signature
# ///
# #define EFI_ACPI_ASF_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32 ('A', 'S', 'F', '!')
EFI_ACPI_ASF_DESCRIPTION_TABLE_SIGNATURE  = SIGNATURE_32 ('A', 'S', 'F', '!')
# 
# #pragma pack ()
# 
# #endif // _ALERT_STANDARD_FORMAT_TABLE_H
# 