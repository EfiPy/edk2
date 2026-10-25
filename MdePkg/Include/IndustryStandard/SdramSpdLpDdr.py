# /** @file
#   This file contains definitions for SPD LPDDR.
# 
#   Copyright (c) 2016, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#     - Serial Presence Detect (SPD) for LPDDR3 and LPDDR4 SDRAM Modules Document Release 2
#       http://www.jedec.org/standards-documents/docs/spd412m-2
# **/
# SdramSpdLpDdr.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdLpDdr
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _SDRAM_SPD_LPDDR_H_
# #define _SDRAM_SPD_LPDDR_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack (push, 1)
# 
# typedef union {
#   struct {
#     UINT8    BytesUsed   :  4;                       ///< Bits 3:0
#     UINT8    BytesTotal  :  3;                       ///< Bits 6:4
#     UINT8    CrcCoverage :  1;                       ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT;
class SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Minor :  4;                             ///< Bits 3:0
#     UINT8    Major :  4;                             ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_REVISION_STRUCT;
class SPD_LPDDR_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD_LPDDR_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Type :  8;                              ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT;
class SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ModuleType  :  4;                       ///< Bits 3:0
#     UINT8    HybridMedia :  3;                       ///< Bits 6:4
#     UINT8    Hybrid      :  1;                       ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_TYPE_STRUCT;
class SPD_LPDDR_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("HybridMedia", UINT8, 3),
    ("Hybrid",      UINT8, 1)
    ]

class SPD_LPDDR_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Density     :  4;                       ///< Bits 3:0
#     UINT8    BankAddress :  2;                       ///< Bits 5:4
#     UINT8    BankGroup   :  2;                       ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT;
class SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 2),
    ("BankGroup",   UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ColumnAddress :  3;                     ///< Bits 2:0
#     UINT8    RowAddress    :  3;                     ///< Bits 5:3
#     UINT8    Reserved      :  2;                     ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SDRAM_ADDRESSING_STRUCT;
class SPD_LPDDR_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SignalLoading    :  2;                  ///< Bits 1:0
#     UINT8    ChannelsPerDie   :  2;                  ///< Bits 3:2
#     UINT8    DieCount         :  3;                  ///< Bits 6:4
#     UINT8    SdramPackageType :  1;                  ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT;
class SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("ChannelsPerDie",      UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1),
    ]

class SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MaximumActivateCount  :  4;             ///< Bits 3:0
#     UINT8    MaximumActivateWindow :  2;             ///< Bits 5:4
#     UINT8    Reserved              :  2;             ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT;
class SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("Reserved",                UINT8, 2)
    ]

class SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved :  8;                          ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT;
class SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 8)
    ]

class SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved          :  5;                 ///< Bits 4:0
#     UINT8    SoftPPR           :  1;                 ///< Bits 5:5
#     UINT8    PostPackageRepair :  2;                 ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT;
class SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("SoftPPR",             UINT8, 1),
    ("PostPackageRepair",   UINT8, 2)
    ]

class SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    OperationAt1_20  :  1;                  ///< Bits 0:0
#     UINT8    EndurantAt1_20   :  1;                  ///< Bits 1:1
#     UINT8    OperationAt1_10  :  1;                  ///< Bits 2:2
#     UINT8    EndurantAt1_10   :  1;                  ///< Bits 3:3
#     UINT8    OperationAtTBD2V :  1;                  ///< Bits 4:4
#     UINT8    EndurantAtTBD2V  :  1;                  ///< Bits 5:5
#     UINT8    Reserved         :  2;                  ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT;
class SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_20",     UINT8, 1),
    ("EndurantAt1_20",      UINT8, 1),
    ("OperationAt1_10",     UINT8, 1),
    ("EndurantAt1_10",      UINT8, 1),
    ("OperationAtTBD2V",    UINT8, 1),
    ("EndurantAtTBD2V",     UINT8, 1),
    ("Reserved",            UINT8, 2)
    ]

class SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SdramDeviceWidth :  3;                  ///< Bits 2:0
#     UINT8    RankCount        :  3;                  ///< Bits 5:3
#     UINT8    Reserved         :  2;                  ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_ORGANIZATION_STRUCT;
class SPD_LPDDR_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("Reserved",            UINT8, 2)
    ]

class SPD_LPDDR_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_ORGANIZATION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    PrimaryBusWidth   :  3;                 ///< Bits 2:0
#     UINT8    BusWidthExtension :  2;                 ///< Bits 4:3
#     UINT8    NumberofChannels  :  3;                 ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT;
class SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("NumberofChannels",    UINT8, 3)
    ]

class SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved              :  7;             ///< Bits 6:0
#     UINT8    ThermalSensorPresence :  1;             ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT;
class SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ExtendedBaseModuleType :  4;            ///< Bits 3:0
#     UINT8    Reserved               :  4;            ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT;
class SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedBaseModuleType",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ChipSelectLoading                 :  3; ///< Bits 2:0
#     UINT8    CommandAddressControlClockLoading :  3; ///< Bits 5:3
#     UINT8    DataStrobeMaskLoading             :  2; ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_SIGNAL_LOADING_STRUCT;
class SPD_LPDDR_SIGNAL_LOADING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ChipSelectLoading",                   UINT8, 3),
    ("CommandAddressControlClockLoading",   UINT8, 3),
    ("DataStrobeMaskLoading",               UINT8, 2)
    ]

class SPD_LPDDR_SIGNAL_LOADING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_SIGNAL_LOADING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Fine     :  2;                          ///< Bits 1:0
#     UINT8    Medium   :  2;                          ///< Bits 3:2
#     UINT8    Reserved :  4;                          ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TIMEBASE_STRUCT;
class SPD_LPDDR_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fine",        UINT8, 2),
    ("Medium",      UINT8, 2),
    ("Reserved",    UINT8, 4)
    ]

class SPD_LPDDR_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCKmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TCK_MIN_MTB_STRUCT;
class SPD_LPDDR_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD_LPDDR_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCKmax :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TCK_MAX_MTB_STRUCT;
class SPD_LPDDR_TCK_MAX_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmax",  UINT8, 8)
    ]

class SPD_LPDDR_TCK_MAX_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MAX_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT32    Cl3       :  1;                         ///< Bits 0:0
#     UINT32    Cl6       :  1;                         ///< Bits 1:1
#     UINT32    Cl8       :  1;                         ///< Bits 2:2
#     UINT32    Cl9       :  1;                         ///< Bits 3:3
#     UINT32    Cl10      :  1;                         ///< Bits 4:4
#     UINT32    Cl11      :  1;                         ///< Bits 5:5
#     UINT32    Cl12      :  1;                         ///< Bits 6:6
#     UINT32    Cl14      :  1;                         ///< Bits 7:7
#     UINT32    Cl16      :  1;                         ///< Bits 8:8
#     UINT32    Reserved0 :  1;                         ///< Bits 9:9
#     UINT32    Cl20      :  1;                         ///< Bits 10:10
#     UINT32    Cl22      :  1;                         ///< Bits 11:11
#     UINT32    Cl24      :  1;                         ///< Bits 12:12
#     UINT32    Reserved1 :  1;                         ///< Bits 13:13
#     UINT32    Cl28      :  1;                         ///< Bits 14:14
#     UINT32    Reserved2 :  1;                         ///< Bits 15:15
#     UINT32    Cl32      :  1;                         ///< Bits 16:16
#     UINT32    Reserved3 :  1;                         ///< Bits 17:17
#     UINT32    Cl36      :  1;                         ///< Bits 18:18
#     UINT32    Reserved4 :  1;                         ///< Bits 19:19
#     UINT32    Cl40      :  1;                         ///< Bits 20:20
#     UINT32    Reserved5 :  11;                        ///< Bits 31:21
#   } Bits;
#   UINT32    Data;
#   UINT16    Data16[2];
#   UINT8     Data8[4];
# } SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT;
class SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl3",         UINT32, 1),
    ("Cl6",         UINT32, 1),
    ("Cl8",         UINT32, 1),
    ("Cl9",         UINT32, 1),
    ("Cl10",        UINT32, 1),
    ("Cl11",        UINT32, 1),
    ("Cl12",        UINT32, 1),
    ("Cl14",        UINT32, 1),
    ("Cl16",        UINT32, 1),
    ("Reserved0",   UINT32, 1),
    ("Cl20",        UINT32, 1),
    ("Cl22",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Reserved1",   UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Reserved2",   UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Reserved3",   UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Reserved4",   UINT32, 1),
    ("Cl40",        UINT32, 1),
    ("Reserved5",   UINT32, 11)
    ]

class SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("Data",    UINT32),
    ("Data16",  UINT16 * 2),
    ("Data8",   UINT8  * 4)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tAAmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TAA_MIN_MTB_STRUCT;
class SPD_LPDDR_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD_LPDDR_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ReadLatencyMode :  2;                   ///< Bits 1:0
#     UINT8    WriteLatencySet :  2;                   ///< Bits 3:2
#     UINT8    Reserved        :  4;                   ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_RW_LATENCY_OPTION_STRUCT;
class SPD_LPDDR_RW_LATENCY_OPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ReadLatencyMode", UINT8, 2),
    ("WriteLatencySet", UINT8, 2),
    ("Reserved",        UINT8, 4)
    ]

class SPD_LPDDR_RW_LATENCY_OPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_RW_LATENCY_OPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRCDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TRCD_MIN_MTB_STRUCT;
class SPD_LPDDR_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD_LPDDR_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRPab :  8;                             ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TRP_AB_MTB_STRUCT;
class SPD_LPDDR_TRP_AB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPab",   UINT8, 8)
    ]

class SPD_LPDDR_TRP_AB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_AB_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRPpb :  8;                             ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_TRP_PB_MTB_STRUCT;
class SPD_LPDDR_TRP_PB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPpb",   UINT8, 8)
    ]

class SPD_LPDDR_TRP_PB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_PB_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT16    tRFCab :  16;                           ///< Bits 15:0
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD_LPDDR_TRFC_AB_MTB_STRUCT;
class SPD_LPDDR_TRFC_AB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCab",  UINT16, 16)
    ]

class SPD_LPDDR_TRFC_AB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRFC_AB_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT16    tRFCpb :  16;                           ///< Bits 15:0
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD_LPDDR_TRFC_PB_MTB_STRUCT;
class SPD_LPDDR_TRFC_PB_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCpb",  UINT16, 16)
    ]

class SPD_LPDDR_TRFC_PB_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRFC_PB_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    BitOrderatSDRAM         :  5;           ///< Bits 4:0
#     UINT8    WiredtoUpperLowerNibble :  1;           ///< Bits 5:5
#     UINT8    PackageRankMap          :  2;           ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT;
class SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BitOrderatSDRAM",         UINT8, 5),
    ("WiredtoUpperLowerNibble", UINT8, 1),
    ("PackageRankMap",          UINT8, 2),
    ]

class SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRPpbFine :  8;                          ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TRP_PB_FTB_STRUCT;
class SPD_LPDDR_TRP_PB_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPpbFine",  INT8, 8)
    ]

class SPD_LPDDR_TRP_PB_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_PB_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRPabFine :  8;                          ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TRP_AB_FTB_STRUCT;
class SPD_LPDDR_TRP_AB_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPabFine",  INT8, 8)
    ]

class SPD_LPDDR_TRP_AB_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRP_AB_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRCDminFine :  8;                        ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TRCD_MIN_FTB_STRUCT;
class SPD_LPDDR_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD_LPDDR_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tAAminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TAA_MIN_FTB_STRUCT;
class SPD_LPDDR_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD_LPDDR_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCKmaxFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TCK_MAX_FTB_STRUCT;
class SPD_LPDDR_TCK_MAX_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmaxFine",  INT8, 8)
    ]

class SPD_LPDDR_TCK_MAX_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MAX_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCKminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD_LPDDR_TCK_MIN_FTB_STRUCT;
class SPD_LPDDR_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD_LPDDR_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     UINT16    ContinuationCount  :  7;               ///< Bits 6:0
#     UINT16    ContinuationParity :  1;               ///< Bits 7:7
#     UINT16    LastNonZeroByte    :  8;               ///< Bits 15:8
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD_LPDDR_MANUFACTURER_ID_CODE;
class SPD_LPDDR_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD_LPDDR_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2),
    ]

# 
# typedef struct {
#   UINT8    Location;                           ///< Module Manufacturing Location
# } SPD_LPDDR_MANUFACTURING_LOCATION;
class SPD_LPDDR_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",   UINT8)
    ]

# 
# typedef struct {
#   UINT8    Year;                               ///< Year represented in BCD (00h = 2000)
#   UINT8    Week;                               ///< Year represented in BCD (47h = week 47)
# } SPD_LPDDR_MANUFACTURING_DATE;
class SPD_LPDDR_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",   UINT8),
    ("Week",   UINT8)
    ]

# 
# typedef union {
#   UINT32    Data;
#   UINT16    SerialNumber16[2];
#   UINT8     SerialNumber8[4];
# } SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER;
class SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

# 
# typedef struct {
#   SPD_LPDDR_MANUFACTURER_ID_CODE          IdCode;                     ///< Module Manufacturer ID Code
#   SPD_LPDDR_MANUFACTURING_LOCATION        Location;                   ///< Module Manufacturing Location
#   SPD_LPDDR_MANUFACTURING_DATE            Date;                       ///< Module Manufacturing Year, in BCD (range: 2000-2255)
#   SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER    SerialNumber;               ///< Module Serial Number
# } SPD_LPDDR_UNIQUE_MODULE_ID;
class SPD_LPDDR_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD_LPDDR_MANUFACTURER_ID_CODE),
    ("Location",        SPD_LPDDR_MANUFACTURING_LOCATION),
    ("Date",            SPD_LPDDR_MANUFACTURING_DATE),
    ("SerialNumber",    SPD_LPDDR_MANUFACTURER_SERIAL_NUMBER)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                    ///< Bits 3:0
#     UINT8    BackThickness  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_MAXIMUM_THICKNESS;
class SPD_LPDDR_MODULE_MAXIMUM_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD_LPDDR_MODULE_MAXIMUM_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_MAXIMUM_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height           :  5;                  ///< Bits 4:0
#     UINT8    RawCardExtension :  3;                  ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_MODULE_NOMINAL_HEIGHT;
class SPD_LPDDR_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD_LPDDR_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Card      :  5;                         ///< Bits 4:0
#     UINT8    Revision  :  2;                         ///< Bits 6:5
#     UINT8    Extension :  1;                         ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD_LPDDR_REFERENCE_RAW_CARD;
class SPD_LPDDR_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD_LPDDR_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD_LPDDR_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   UINT16    Crc[1];
#   UINT8     Data8[2];
# } SPD_LPDDR_CYCLIC_REDUNDANCY_CODE;
class SPD_LPDDR_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",     UINT16 * 1),
    ("Data8",   UINT8  * 2)
    ]

# 
# typedef struct {
#   SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT               Description;              ///< 0       Number of Serial PD Bytes Written / SPD Device Size / CRC Coverage 1, 2
#   SPD_LPDDR_REVISION_STRUCT                         Revision;                 ///< 1       SPD Revision
#   SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT                 DramDeviceType;           ///< 2       DRAM Device Type
#   SPD_LPDDR_MODULE_TYPE_STRUCT                      ModuleType;               ///< 3       Module Type
#   SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT              SdramDensityAndBanks;     ///< 4       SDRAM Density and Banks
#   SPD_LPDDR_SDRAM_ADDRESSING_STRUCT                 SdramAddressing;          ///< 5       SDRAM Addressing
#   SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT               SdramPackageType;         ///< 6       SDRAM Package Type
#   SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT          SdramOptionalFeatures;    ///< 7       SDRAM Optional Features
#   SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT            ThermalAndRefreshOptions; ///< 8       SDRAM Thermal and Refresh Options
#   SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT    OtherOptionalFeatures;    ///< 9      Other SDRAM Optional Features
#   UINT8                                             Reserved0;                ///< 10      Reserved
#   SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT           ModuleNominalVoltage;     ///< 11      Module Nominal Voltage, VDD
#   SPD_LPDDR_MODULE_ORGANIZATION_STRUCT              ModuleOrganization;       ///< 12      Module Organization
#   SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT          ModuleMemoryBusWidth;     ///< 13      Module Memory Bus Width
#   SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT            ModuleThermalSensor;      ///< 14      Module Thermal Sensor
#   SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT             ExtendedModuleType;       ///< 15      Extended Module Type
#   SPD_LPDDR_SIGNAL_LOADING_STRUCT                   SignalLoading;            ///< 16      Signal Loading
#   SPD_LPDDR_TIMEBASE_STRUCT                         Timebase;                 ///< 17      Timebases
#   SPD_LPDDR_TCK_MIN_MTB_STRUCT                      tCKmin;                   ///< 18      SDRAM Minimum Cycle Time (tCKmin)
#   SPD_LPDDR_TCK_MAX_MTB_STRUCT                      tCKmax;                   ///< 19      SDRAM Maximum Cycle Time (tCKmax)
#   SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT          CasLatencies;             ///< 20-23   CAS Latencies Supported
#   SPD_LPDDR_TAA_MIN_MTB_STRUCT                      tAAmin;                   ///< 24      Minimum CAS Latency Time (tAAmin)
#   SPD_LPDDR_RW_LATENCY_OPTION_STRUCT                LatencySetOptions;        ///< 25      Read and Write Latency Set Options
#   SPD_LPDDR_TRCD_MIN_MTB_STRUCT                     tRCDmin;                  ///< 26      Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD_LPDDR_TRP_AB_MTB_STRUCT                       tRPab;                    ///< 27      Minimum Row Precharge Delay Time (tRPab), all banks
#   SPD_LPDDR_TRP_PB_MTB_STRUCT                       tRPpb;                    ///< 28      Minimum Row Precharge Delay Time (tRPpb), per bank
#   SPD_LPDDR_TRFC_AB_MTB_STRUCT                      tRFCab;                   ///< 29-30   Minimum Refresh Recovery Delay Time (tRFCab), all banks
#   SPD_LPDDR_TRFC_PB_MTB_STRUCT                      tRFCpb;                   ///< 31-32   Minimum Refresh Recovery Delay Time (tRFCpb), per bank
#   UINT8                                             Reserved1[59 - 33 + 1];   ///< 33-59   Reserved
#   SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT       BitMapping[77 - 60 + 1];  ///< 60-77   Connector to SDRAM Bit Mapping
#   UINT8                                             Reserved2[119 - 78 + 1];  ///< 78-119  Reserved
#   SPD_LPDDR_TRP_PB_FTB_STRUCT                       tRPpbFine;                ///< 120     Fine Offset for Minimum Row Precharge Delay Time (tRPpbFine), per bank
#   SPD_LPDDR_TRP_AB_FTB_STRUCT                       tRPabFine;                ///< 121     Fine Offset for Minimum Row Precharge Delay Time (tRPabFine), all ranks
#   SPD_LPDDR_TRCD_MIN_FTB_STRUCT                     tRCDminFine;              ///< 122     Fine Offset for Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD_LPDDR_TAA_MIN_FTB_STRUCT                      tAAminFine;               ///< 123     Fine Offset for Minimum CAS Latency Time (tAAmin)
#   SPD_LPDDR_TCK_MAX_FTB_STRUCT                      tCKmaxFine;               ///< 124     Fine Offset for SDRAM Maximum Cycle Time (tCKmax)
#   SPD_LPDDR_TCK_MIN_FTB_STRUCT                      tCKminFine;               ///< 125     Fine Offset for SDRAM Minimum Cycle Time (tCKmin)
#   SPD_LPDDR_CYCLIC_REDUNDANCY_CODE                  Crc;                      ///< 126-127 Cyclical Redundancy Code (CRC)
# } SPD_LPDDR_BASE_SECTION;
class SPD_LPDDR_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",                 SPD_LPDDR_DEVICE_DESCRIPTION_STRUCT           ),
    ("Revision",                    SPD_LPDDR_REVISION_STRUCT                     ),
    ("DramDeviceType",              SPD_LPDDR_DRAM_DEVICE_TYPE_STRUCT             ),
    ("ModuleType",                  SPD_LPDDR_MODULE_TYPE_STRUCT                  ),
    ("SdramDensityAndBanks",        SPD_LPDDR_SDRAM_DENSITY_BANKS_STRUCT          ),
    ("SdramAddressing",             SPD_LPDDR_SDRAM_ADDRESSING_STRUCT             ),
    ("SdramPackageType",            SPD_LPDDR_SDRAM_PACKAGE_TYPE_STRUCT           ),
    ("SdramOptionalFeatures",       SPD_LPDDR_SDRAM_OPTIONAL_FEATURES_STRUCT      ),
    ("ThermalAndRefreshOptions",    SPD_LPDDR_SDRAM_THERMAL_REFRESH_STRUCT        ),
    ("OtherOptionalFeatures",       SPD_LPDDR_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("Reserved0",                   UINT8                                         ),
    ("ModuleNominalVoltage",        SPD_LPDDR_MODULE_NOMINAL_VOLTAGE_STRUCT       ),
    ("ModuleOrganization",          SPD_LPDDR_MODULE_ORGANIZATION_STRUCT          ),
    ("ModuleMemoryBusWidth",        SPD_LPDDR_MODULE_MEMORY_BUS_WIDTH_STRUCT      ),
    ("ModuleThermalSensor",         SPD_LPDDR_MODULE_THERMAL_SENSOR_STRUCT        ),
    ("ExtendedModuleType",          SPD_LPDDR_EXTENDED_MODULE_TYPE_STRUCT         ),
    ("SignalLoading",               SPD_LPDDR_SIGNAL_LOADING_STRUCT               ),
    ("Timebase",                    SPD_LPDDR_TIMEBASE_STRUCT                     ),
    ("tCKmin",                      SPD_LPDDR_TCK_MIN_MTB_STRUCT                  ),
    ("tCKmax",                      SPD_LPDDR_TCK_MAX_MTB_STRUCT                  ),
    ("CasLatencies",                SPD_LPDDR_CAS_LATENCIES_SUPPORTED_STRUCT      ),
    ("tAAmin",                      SPD_LPDDR_TAA_MIN_MTB_STRUCT                  ),
    ("LatencySetOptions",           SPD_LPDDR_RW_LATENCY_OPTION_STRUCT            ),
    ("tRCDmin",                     SPD_LPDDR_TRCD_MIN_MTB_STRUCT                 ),
    ("tRPab",                       SPD_LPDDR_TRP_AB_MTB_STRUCT                   ),
    ("tRPpb",                       SPD_LPDDR_TRP_PB_MTB_STRUCT                   ),
    ("tRFCab",                      SPD_LPDDR_TRFC_AB_MTB_STRUCT                  ),
    ("tRFCpb",                      SPD_LPDDR_TRFC_PB_MTB_STRUCT                  ),
    ("Reserved1",                   UINT8 * (59 - 33 + 1)                         ),
    ("BitMapping",                  SPD_LPDDR_CONNECTOR_BIT_MAPPING_BYTE_STRUCT * (77 - 60 + 1)),
    ("Reserved2",                   UINT8 * (119 - 78 + 1)                        ),
    ("tRPpbFine",                   SPD_LPDDR_TRP_PB_FTB_STRUCT                   ),
    ("tRPabFine",                   SPD_LPDDR_TRP_AB_FTB_STRUCT                   ),
    ("tRCDminFine",                 SPD_LPDDR_TRCD_MIN_FTB_STRUCT                 ),
    ("tAAminFine",                  SPD_LPDDR_TAA_MIN_FTB_STRUCT                  ),
    ("tCKmaxFine",                  SPD_LPDDR_TCK_MAX_FTB_STRUCT                  ),
    ("tCKminFine",                  SPD_LPDDR_TCK_MIN_FTB_STRUCT                  ),
    ("Crc",                         SPD_LPDDR_CYCLIC_REDUNDANCY_CODE              )
    ]

# 
# typedef struct {
#   SPD_LPDDR_MODULE_NOMINAL_HEIGHT       ModuleNominalHeight;        ///< 128     Module Nominal Height
#   SPD_LPDDR_MODULE_MAXIMUM_THICKNESS    ModuleMaximumThickness;     ///< 129     Module Maximum Thickness
#   SPD_LPDDR_REFERENCE_RAW_CARD          ReferenceRawCardUsed;       ///< 130     Reference Raw Card Used
#   UINT8                                 Reserved[253 - 131 + 1];    ///< 131-253 Reserved
#   SPD_LPDDR_CYCLIC_REDUNDANCY_CODE      Crc;                        ///< 254-255 Cyclical Redundancy Code (CRC)
# } SPD_LPDDR_MODULE_LPDIMM;
class SPD_LPDDR_MODULE_LPDIMM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD_LPDDR_MODULE_NOMINAL_HEIGHT   ),
    ("ModuleMaximumThickness",  SPD_LPDDR_MODULE_MAXIMUM_THICKNESS),
    ("ReferenceRawCardUsed",    SPD_LPDDR_REFERENCE_RAW_CARD      ),
    ("Reserved",                UINT8 * (253 - 131 + 1)           ),
    ("Crc",                     SPD_LPDDR_CYCLIC_REDUNDANCY_CODE  )
    ]

# 
# typedef struct {
#   SPD_LPDDR_MODULE_LPDIMM    LpDimm;                                ///< 128-255 Unbuffered Memory Module Types
# } SPD_LPDDR_MODULE_SPECIFIC;
class SPD_LPDDR_MODULE_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LpDimm",  SPD_LPDDR_MODULE_LPDIMM)
    ]

# 
# typedef struct {
#   UINT8    ModulePartNumber[348 - 329 + 1];                                ///< 329-348 Module Part Number
# } SPD_LPDDR_MODULE_PART_NUMBER;
class SPD_LPDDR_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",  UINT8 * (348 - 329 + 1))
    ]

# 
# typedef struct {
#   UINT8    ManufacturerSpecificData[381 - 353 + 1];                                ///< 353-381 Manufacturer's Specific Data
# } SPD_LPDDR_MANUFACTURER_SPECIFIC;
class SPD_LPDDR_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",  UINT8 * (381 - 353 + 1))
    ]

# 
# typedef UINT8  SPD_LPDDR_MODULE_REVISION_CODE;                           ///< 349     Module Revision Code
# typedef UINT8  SPD_LPDDR_DRAM_STEPPING;                                  ///< 352     Dram Stepping
SPD_LPDDR_MODULE_REVISION_CODE  = UINT8
SPD_LPDDR_DRAM_STEPPING         = UINT8
# 
# typedef struct {
#   SPD_LPDDR_UNIQUE_MODULE_ID         ModuleId;                      ///< 320-328 Unique Module ID
#   SPD_LPDDR_MODULE_PART_NUMBER       ModulePartNumber;              ///< 329-348 Module Part Number
#   SPD_LPDDR_MODULE_REVISION_CODE     ModuleRevisionCode;            ///< 349     Module Revision Code
#   SPD_LPDDR_MANUFACTURER_ID_CODE     DramIdCode;                    ///< 350-351 Dram Manufacturer ID Code
#   SPD_LPDDR_DRAM_STEPPING            DramStepping;                  ///< 352     Dram Stepping
#   SPD_LPDDR_MANUFACTURER_SPECIFIC    ManufacturerSpecificData;      ///< 353-381 Manufacturer's Specific Data
#   UINT8                              Reserved[383 - 382 + 1];       ///< 382-383 Reserved
# } SPD_LPDDR_MANUFACTURING_DATA;
class SPD_LPDDR_MANUFACTURING_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleId",                    SPD_LPDDR_UNIQUE_MODULE_ID     ),
    ("ModulePartNumber",            SPD_LPDDR_MODULE_PART_NUMBER   ),
    ("ModuleRevisionCode",          SPD_LPDDR_MODULE_REVISION_CODE ),
    ("DramIdCode",                  SPD_LPDDR_MANUFACTURER_ID_CODE ),
    ("DramStepping",                SPD_LPDDR_DRAM_STEPPING        ),
    ("ManufacturerSpecificData",    SPD_LPDDR_MANUFACTURER_SPECIFIC),
    ("Reserved",                    UINT8 * (383 - 382 + 1)        )
    ]

# 
# typedef struct {
#   UINT8    Reserved[511 - 384 + 1];                                 ///< 384-511 End User Programmable
# } SPD_LPDDR_END_USER_SECTION;
class SPD_LPDDR_END_USER_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8 * (511 - 384 + 1))
    ]

# 
# ///
# /// LPDDR Serial Presence Detect structure
# ///
# typedef struct {
#   SPD_LPDDR_BASE_SECTION          Base;                             ///< 0-127   Base Configuration and DRAM Parameters
#   SPD_LPDDR_MODULE_SPECIFIC       Module;                           ///< 128-255 Module-Specific Section
#   UINT8                           Reserved[319 - 256 + 1];          ///< 256-319 Hybrid Memory Parameters
#   SPD_LPDDR_MANUFACTURING_DATA    ManufactureInfo;                  ///< 320-383 Manufacturing Information
#   SPD_LPDDR_END_USER_SECTION      EndUser;                          ///< 384-511 End User Programmable
# } SPD_LPDDR;
class SPD_LPDDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Base",            SPD_LPDDR_BASE_SECTION      ),
    ("Module",          SPD_LPDDR_MODULE_SPECIFIC   ),
    ("Reserved",        UINT8 * (319 - 256 + 1)     ),
    ("ManufactureInfo", SPD_LPDDR_MANUFACTURING_DATA),
    ("EndUser",         SPD_LPDDR_END_USER_SECTION  )
    ]

# 
# #pragma pack (pop)
# #endif
# 