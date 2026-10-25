# /** @file
#   This file contains definitions for SPD DDR4.
# 
#   Copyright (c) 2016, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#     - Serial Presence Detect (SPD) for DDR4 SDRAM Modules Document Release 4
#       http://www.jedec.org/standards-documents/docs/spd412l-4
# **/
# SdramSpdDdr4.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdDdr4
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _SDRAM_SPD_DDR4_H_
# #define _SDRAM_SPD_DDR4_H_
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
# } SPD4_DEVICE_DESCRIPTION_STRUCT;
class SPD4_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD4_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Minor :  4;                             ///< Bits 3:0
#     UINT8    Major :  4;                             ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_REVISION_STRUCT;
class SPD4_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD4_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Type :  8;                              ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_DRAM_DEVICE_TYPE_STRUCT;
class SPD4_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD4_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_DRAM_DEVICE_TYPE_STRUCT_Bits),
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
# } SPD4_MODULE_TYPE_STRUCT;
class SPD4_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("HybridMedia", UINT8, 3),
    ("Hybrid",      UINT8, 1)
    ]

class SPD4_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_TYPE_STRUCT_Bits),
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
# } SPD4_SDRAM_DENSITY_BANKS_STRUCT;
class SPD4_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 2),
    ("BankGroup",   UINT8, 2)
    ]

class SPD4_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_DENSITY_BANKS_STRUCT_Bits),
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
# } SPD4_SDRAM_ADDRESSING_STRUCT;
class SPD4_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD4_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SignalLoading    :  2;                  ///< Bits 1:0
#     UINT8    Reserved         :  2;                  ///< Bits 3:2
#     UINT8    DieCount         :  3;                  ///< Bits 6:4
#     UINT8    SdramPackageType :  1;                  ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT;
class SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("Reserved",            UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1),
    ]

class SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
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
# } SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT;
class SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("Reserved",                UINT8, 2)
    ]

class SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved :  8;                          ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_SDRAM_THERMAL_REFRESH_STRUCT;
class SPD4_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 8)
    ]

class SPD4_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
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
# } SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT;
class SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT8, 5),
    ("SoftPPR",             UINT8, 1),
    ("PostPackageRepair",   UINT8, 2)
    ]

class SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SignalLoading    :  2;                  ///< Bits 1:0
#     UINT8    DRAMDensityRatio :  2;                  ///< Bits 3:2
#     UINT8    DieCount         :  3;                  ///< Bits 6:4
#     UINT8    SdramPackageType :  1;                  ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT;
class SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",       UINT8, 2),
    ("DRAMDensityRatio",    UINT8, 2),
    ("DieCount",            UINT8, 3),
    ("SdramPackageType",    UINT8, 1)
    ]

class SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    OperationAt1_20 :  1;                   ///< Bits 0:0
#     UINT8    EndurantAt1_20  :  1;                   ///< Bits 1:1
#     UINT8    Reserved        :  6;                   ///< Bits 7:2
#   } Bits;
#   UINT8    Data;
# } SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT;
class SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_20",     UINT8, 1),
    ("EndurantAt1_20",      UINT8, 1),
    ("Reserved",            UINT8, 6)
    ]

class SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SdramDeviceWidth :  3;                  ///< Bits 2:0
#     UINT8    RankCount        :  3;                  ///< Bits 5:3
#     UINT8    RankMix          :  1;                  ///< Bits 6:6
#     UINT8    Reserved         :  1;                  ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_MODULE_ORGANIZATION_STRUCT;
class SPD4_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("RankMix",             UINT8, 1),
    ("Reserved",            UINT8, 1)
    ]

class SPD4_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_ORGANIZATION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    PrimaryBusWidth   :  3;                 ///< Bits 2:0
#     UINT8    BusWidthExtension :  2;                 ///< Bits 4:3
#     UINT8    Reserved          :  3;                 ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT;
class SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("Reserved",            UINT8, 3)
    ]

class SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved              :  7;             ///< Bits 6:0
#     UINT8    ThermalSensorPresence :  1;             ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_MODULE_THERMAL_SENSOR_STRUCT;
class SPD4_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD4_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ExtendedBaseModuleType :  4;            ///< Bits 3:0
#     UINT8    Reserved               :  4;            ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_EXTENDED_MODULE_TYPE_STRUCT;
class SPD4_EXTENDED_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedBaseModuleType",  UINT8, 4),
    ("Reserved",                UINT8, 4)
    ]

class SPD4_EXTENDED_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_EXTENDED_MODULE_TYPE_STRUCT_Bits),
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
# } SPD4_TIMEBASE_STRUCT;
class SPD4_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fine",        UINT8, 2),
    ("Medium",      UINT8, 2),
    ("Reserved",    UINT8, 4)
    ]

class SPD4_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCKmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TCK_MIN_MTB_STRUCT;
class SPD4_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD4_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCKmax :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TCK_MAX_MTB_STRUCT;
class SPD4_TCK_MAX_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmax",  UINT8, 8)
    ]

class SPD4_TCK_MAX_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MAX_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT32    Cl7      :  1;                         ///< Bits 0:0
#     UINT32    Cl8      :  1;                         ///< Bits 1:1
#     UINT32    Cl9      :  1;                         ///< Bits 2:2
#     UINT32    Cl10     :  1;                         ///< Bits 3:3
#     UINT32    Cl11     :  1;                         ///< Bits 4:4
#     UINT32    Cl12     :  1;                         ///< Bits 5:5
#     UINT32    Cl13     :  1;                         ///< Bits 6:6
#     UINT32    Cl14     :  1;                         ///< Bits 7:7
#     UINT32    Cl15     :  1;                         ///< Bits 8:8
#     UINT32    Cl16     :  1;                         ///< Bits 9:9
#     UINT32    Cl17     :  1;                         ///< Bits 10:10
#     UINT32    Cl18     :  1;                         ///< Bits 11:11
#     UINT32    Cl19     :  1;                         ///< Bits 12:12
#     UINT32    Cl20     :  1;                         ///< Bits 13:13
#     UINT32    Cl21     :  1;                         ///< Bits 14:14
#     UINT32    Cl22     :  1;                         ///< Bits 15:15
#     UINT32    Cl23     :  1;                         ///< Bits 16:16
#     UINT32    Cl24     :  1;                         ///< Bits 17:17
#     UINT32    Cl25     :  1;                         ///< Bits 18:18
#     UINT32    Cl26     :  1;                         ///< Bits 19:19
#     UINT32    Cl27     :  1;                         ///< Bits 20:20
#     UINT32    Cl28     :  1;                         ///< Bits 21:21
#     UINT32    Cl29     :  1;                         ///< Bits 22:22
#     UINT32    Cl30     :  1;                         ///< Bits 23:23
#     UINT32    Cl31     :  1;                         ///< Bits 24:24
#     UINT32    Cl32     :  1;                         ///< Bits 25:25
#     UINT32    Cl33     :  1;                         ///< Bits 26:26
#     UINT32    Cl34     :  1;                         ///< Bits 27:27
#     UINT32    Cl35     :  1;                         ///< Bits 28:28
#     UINT32    Cl36     :  1;                         ///< Bits 29:29
#     UINT32    Reserved :  1;                         ///< Bits 30:30
#     UINT32    ClRange  :  1;                         ///< Bits 31:31
#   } Bits;
#   struct {
#     UINT32    Cl23     :  1;                         ///< Bits 0:0
#     UINT32    Cl24     :  1;                         ///< Bits 1:1
#     UINT32    Cl25     :  1;                         ///< Bits 2:2
#     UINT32    Cl26     :  1;                         ///< Bits 3:3
#     UINT32    Cl27     :  1;                         ///< Bits 4:4
#     UINT32    Cl28     :  1;                         ///< Bits 5:5
#     UINT32    Cl29     :  1;                         ///< Bits 6:6
#     UINT32    Cl30     :  1;                         ///< Bits 7:7
#     UINT32    Cl31     :  1;                         ///< Bits 8:8
#     UINT32    Cl32     :  1;                         ///< Bits 9:9
#     UINT32    Cl33     :  1;                         ///< Bits 10:10
#     UINT32    Cl34     :  1;                         ///< Bits 11:11
#     UINT32    Cl35     :  1;                         ///< Bits 12:12
#     UINT32    Cl36     :  1;                         ///< Bits 13:13
#     UINT32    Cl37     :  1;                         ///< Bits 14:14
#     UINT32    Cl38     :  1;                         ///< Bits 15:15
#     UINT32    Cl39     :  1;                         ///< Bits 16:16
#     UINT32    Cl40     :  1;                         ///< Bits 17:17
#     UINT32    Cl41     :  1;                         ///< Bits 18:18
#     UINT32    Cl42     :  1;                         ///< Bits 19:19
#     UINT32    Cl43     :  1;                         ///< Bits 20:20
#     UINT32    Cl44     :  1;                         ///< Bits 21:21
#     UINT32    Cl45     :  1;                         ///< Bits 22:22
#     UINT32    Cl46     :  1;                         ///< Bits 23:23
#     UINT32    Cl47     :  1;                         ///< Bits 24:24
#     UINT32    Cl48     :  1;                         ///< Bits 25:25
#     UINT32    Cl49     :  1;                         ///< Bits 26:26
#     UINT32    Cl50     :  1;                         ///< Bits 27:27
#     UINT32    Cl51     :  1;                         ///< Bits 28:28
#     UINT32    Cl52     :  1;                         ///< Bits 29:29
#     UINT32    Reserved :  1;                         ///< Bits 30:30
#     UINT32    ClRange  :  1;                         ///< Bits 31:31
#   } HighRangeBits;
#   UINT32    Data;
#   UINT16    Data16[2];
#   UINT8     Data8[4];
# } SPD4_CAS_LATENCIES_SUPPORTED_STRUCT;
class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl7",         UINT32, 1),
    ("Cl8",         UINT32, 1),
    ("Cl9",         UINT32, 1),
    ("Cl10",        UINT32, 1),
    ("Cl11",        UINT32, 1),
    ("Cl12",        UINT32, 1),
    ("Cl13",        UINT32, 1),
    ("Cl14",        UINT32, 1),
    ("Cl15",        UINT32, 1),
    ("Cl16",        UINT32, 1),
    ("Cl17",        UINT32, 1),
    ("Cl18",        UINT32, 1),
    ("Cl19",        UINT32, 1),
    ("Cl20",        UINT32, 1),
    ("Cl21",        UINT32, 1),
    ("Cl22",        UINT32, 1),
    ("Cl23",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Cl25",        UINT32, 1),
    ("Cl26",        UINT32, 1),
    ("Cl27",        UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Cl29",        UINT32, 1),
    ("Cl30",        UINT32, 1),
    ("Cl31",        UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Cl33",        UINT32, 1),
    ("Cl34",        UINT32, 1),
    ("Cl35",        UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Reserved",    UINT32, 1),
    ("ClRange",     UINT32, 1)
    ]

class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_HighRangeBits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl23",        UINT32, 1),
    ("Cl24",        UINT32, 1),
    ("Cl25",        UINT32, 1),
    ("Cl26",        UINT32, 1),
    ("Cl27",        UINT32, 1),
    ("Cl28",        UINT32, 1),
    ("Cl29",        UINT32, 1),
    ("Cl30",        UINT32, 1),
    ("Cl31",        UINT32, 1),
    ("Cl32",        UINT32, 1),
    ("Cl33",        UINT32, 1),
    ("Cl34",        UINT32, 1),
    ("Cl35",        UINT32, 1),
    ("Cl36",        UINT32, 1),
    ("Cl37",        UINT32, 1),
    ("Cl38",        UINT32, 1),
    ("Cl39",        UINT32, 1),
    ("Cl40",        UINT32, 1),
    ("Cl41",        UINT32, 1),
    ("Cl42",        UINT32, 1),
    ("Cl43",        UINT32, 1),
    ("Cl44",        UINT32, 1),
    ("Cl45",        UINT32, 1),
    ("Cl46",        UINT32, 1),
    ("Cl47",        UINT32, 1),
    ("Cl48",        UINT32, 1),
    ("Cl49",        UINT32, 1),
    ("Cl50",        UINT32, 1),
    ("Cl51",        UINT32, 1),
    ("Cl52",        UINT32, 1),
    ("Reserved",    UINT32, 1),
    ("ClRange",     UINT32, 1)
    ]

class SPD4_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("HighRangeBits",   SPD4_CAS_LATENCIES_SUPPORTED_STRUCT_HighRangeBits),
    ("Data",            UINT32),
    ("Data16",          UINT16 * 2),
    ("Data8",           UINT8  * 4)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tAAmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TAA_MIN_MTB_STRUCT;
class SPD4_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD4_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRCDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TRCD_MIN_MTB_STRUCT;
class SPD4_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD4_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRPmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TRP_MIN_MTB_STRUCT;
class SPD4_TRP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPmin",  UINT8, 8)
    ]

class SPD4_TRP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRASminUpper :  4;                      ///< Bits 3:0
#     UINT8    tRCminUpper  :  4;                      ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_TRAS_TRC_MIN_MTB_STRUCT;
class SPD4_TRAS_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASminUpper",    UINT8, 4),
    ("tRCminUpper",     UINT8, 4)
    ]

class SPD4_TRAS_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRAS_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRASmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TRAS_MIN_MTB_STRUCT;
class SPD4_TRAS_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASmin", UINT8, 8)
    ]

class SPD4_TRAS_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRAS_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRCmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TRC_MIN_MTB_STRUCT;
class SPD4_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCmin",  UINT8, 8)
    ]

class SPD4_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT16    tRFCmin :  16;                          ///< Bits 15:0
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD4_TRFC_MIN_MTB_STRUCT;
class SPD4_TRFC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCmin", UINT16, 16)
    ]

class SPD4_TRFC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRFC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tFAWminUpper :  4;                      ///< Bits 3:0
#     UINT8    Reserved     :  4;                      ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_TFAW_MIN_MTB_UPPER_STRUCT;
class SPD4_TFAW_MIN_MTB_UPPER_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWminUpper",    UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class SPD4_TFAW_MIN_MTB_UPPER_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TFAW_MIN_MTB_UPPER_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tFAWmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TFAW_MIN_MTB_STRUCT;
class SPD4_TFAW_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWmin", UINT8, 8)
    ]

class SPD4_TFAW_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TFAW_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRRDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TRRD_MIN_MTB_STRUCT;
class SPD4_TRRD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDmin", UINT8, 8)
    ]

class SPD4_TRRD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRRD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCCDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TCCD_MIN_MTB_STRUCT;
class SPD4_TCCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCCDmin", UINT8, 8)
    ]

class SPD4_TCCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWRminMostSignificantNibble :  4;       ///< Bits 3:0
#     UINT8    Reserved                    :  4;       ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_TWR_UPPER_NIBBLE_STRUCT;
class SPD4_TWR_UPPER_NIBBLE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRminMostSignificantNibble", UINT8, 4),
    ("Reserved",                    UINT8, 4)
    ]

class SPD4_TWR_UPPER_NIBBLE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWR_UPPER_NIBBLE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWRmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TWR_MIN_MTB_STRUCT;
class SPD4_TWR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRmin",  UINT8, 8)
    ]

class SPD4_TWR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWTR_SminMostSignificantNibble :  4;    ///< Bits 3:0
#     UINT8    tWTR_LminMostSignificantNibble :  4;    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_TWTR_UPPER_NIBBLE_STRUCT;
class SPD4_TWTR_UPPER_NIBBLE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTR_SminMostSignificantNibble", UINT8, 4),
    ("tWTR_LminMostSignificantNibble", UINT8, 4)
    ]

class SPD4_TWTR_UPPER_NIBBLE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWTR_UPPER_NIBBLE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWTRmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_TWTR_MIN_MTB_STRUCT;
class SPD4_TWTR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTRmin", UINT8, 8)
    ]

class SPD4_TWTR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TWTR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    BitOrderatSDRAM         :  5;           ///< Bits 4:0
#     UINT8    WiredtoUpperLowerNibble :  1;           ///< Bits 5:5
#     UINT8    PackageRankMap          :  2;           ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT;
class SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BitOrderatSDRAM",         UINT8, 5),
    ("WiredtoUpperLowerNibble", UINT8, 1),
    ("PackageRankMap",          UINT8, 2),
    ]

class SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCCDminFine :  8;                        ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TCCD_MIN_FTB_STRUCT;
class SPD4_TCCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCCDminFine", INT8, 8)
    ]

class SPD4_TCCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRRDminFine :  8;                        ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TRRD_MIN_FTB_STRUCT;
class SPD4_TRRD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDminFine", INT8, 8)
    ]

class SPD4_TRRD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRRD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRCminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TRC_MIN_FTB_STRUCT;
class SPD4_TRC_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCminFine",  INT8, 8)
    ]

class SPD4_TRC_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRC_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRPminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TRP_MIN_FTB_STRUCT;
class SPD4_TRP_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPminFine",  INT8, 8)
    ]

class SPD4_TRP_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRP_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRCDminFine :  8;                        ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TRCD_MIN_FTB_STRUCT;
class SPD4_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD4_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tAAminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TAA_MIN_FTB_STRUCT;
class SPD4_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD4_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCKmaxFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TCK_MAX_FTB_STRUCT;
class SPD4_TCK_MAX_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmaxFine",  INT8, 8)
    ]

class SPD4_TCK_MAX_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MAX_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCKminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD4_TCK_MIN_FTB_STRUCT;
class SPD4_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD4_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height           :  5;                  ///< Bits 4:0
#     UINT8    RawCardExtension :  3;                  ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD4_UNBUF_MODULE_NOMINAL_HEIGHT;
class SPD4_UNBUF_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                    ///< Bits 3:0
#     UINT8    BackThickness  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_UNBUF_MODULE_NOMINAL_THICKNESS;
class SPD4_UNBUF_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_UNBUF_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_MODULE_NOMINAL_THICKNESS_Bits),
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
# } SPD4_UNBUF_REFERENCE_RAW_CARD;
class SPD4_UNBUF_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1),
    ]

class SPD4_UNBUF_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MappingRank1 :  1;                      ///< Bits 0:0
#     UINT8    Reserved     :  7;                      ///< Bits 7:1
#   } Bits;
#   UINT8    Data;
# } SPD4_UNBUF_ADDRESS_MAPPING;
class SPD4_UNBUF_ADDRESS_MAPPING_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MappingRank1",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_UNBUF_ADDRESS_MAPPING (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_UNBUF_ADDRESS_MAPPING_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height   :  5;                          ///< Bits 4:0
#     UINT8    Reserved :  3;                          ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_MODULE_NOMINAL_HEIGHT;
class SPD4_RDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                    ///< Bits 3:0
#     UINT8    BackThickness  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_MODULE_NOMINAL_THICKNESS;
class SPD4_RDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_RDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_NOMINAL_THICKNESS_Bits),
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
# } SPD4_RDIMM_REFERENCE_RAW_CARD;
class SPD4_RDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_RDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RegisterCount :  2;                     ///< Bits 1:0
#     UINT8    DramRowCount  :  2;                     ///< Bits 3:2
#     UINT8    RegisterType  :  4;                     ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_MODULE_ATTRIBUTES;
class SPD4_RDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD4_RDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    HeatSpreaderThermalCharacteristics :  7; ///< Bits 6:0
#     UINT8    HeatSpreaderSolution               :  1; ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION;
class SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
    ("Data",    UINT8)
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
# } SPD4_MANUFACTURER_ID_CODE;
class SPD4_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD4_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RegisterRevisionNumber;           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_REGISTER_REVISION_NUMBER;
class SPD4_RDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD4_RDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Rank1Mapping :  1;                     ///< Bits 0:0
#     UINT8    Reserved     :  7;                     ///< Bits 7:1
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM;
class SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank1Mapping",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Cke            :  2;                   ///< Bits 1:0
#     UINT8    Odt            :  2;                   ///< Bits 3:2
#     UINT8    CommandAddress :  2;                   ///< Bits 5:4
#     UINT8    ChipSelect     :  2;                   ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS;
class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cke",             UINT8, 2),
    ("Odt",             UINT8, 2),
    ("CommandAddress",  UINT8, 2),
    ("ChipSelect",      UINT8, 2)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Y0Y2                     :  2;         ///< Bits 1:0
#     UINT8    Y1Y3                     :  2;         ///< Bits 3:2
#     UINT8    Reserved0                :  2;         ///< Bits 5:4
#     UINT8    RcdOutputSlewRateControl :  1;         ///< Bits 6:6
#     UINT8    Reserved1                :  1;         ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK;
class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Y0Y2",                        UINT8, 2),
    ("Y1Y3",                        UINT8, 2),
    ("Reserved0",                   UINT8, 2),
    ("RcdOutputSlewRateControl",    UINT8, 1),
    ("Reserved1",                   UINT8, 1)
    ]

class SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height   :  5;                         ///< Bits 4:0
#     UINT8    Reserved :  3;                         ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT;
class SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                   ///< Bits 3:0
#     UINT8    BackThickness  :  4;                   ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS;
class SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Card      :  5;                        ///< Bits 4:0
#     UINT8    Revision  :  2;                        ///< Bits 6:5
#     UINT8    Extension :  1;                        ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_REFERENCE_RAW_CARD;
class SPD4_LRDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_LRDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RegisterCount :  2;                    ///< Bits 1:0
#     UINT8    DramRowCount  :  2;                    ///< Bits 3:2
#     UINT8    RegisterType  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_MODULE_ATTRIBUTES;
class SPD4_LRDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD4_LRDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    HeatSpreaderThermalCharacteristics :  7; ///< Bits 6:0
#     UINT8    HeatSpreaderSolution               :  1; ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION;
class SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RegisterRevisionNumber;                ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_REGISTER_REVISION_NUMBER;
class SPD4_LRDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD4_LRDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Rank1Mapping :  1;                     ///< Bits 0:0
#     UINT8    Reserved     :  7;                     ///< Bits 7:1
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM;
class SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank1Mapping",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Cke            :  2;                   ///< Bits 1:0
#     UINT8    Odt            :  2;                   ///< Bits 3:2
#     UINT8    CommandAddress :  2;                   ///< Bits 5:4
#     UINT8    ChipSelect     :  2;                   ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS;
class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cke",             UINT8, 2),
    ("Odt",             UINT8, 2),
    ("CommandAddress",  UINT8, 2),
    ("ChipSelect",      UINT8, 2)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Y0Y2                     :  2;         ///< Bits 1:0
#     UINT8    Y1Y3                     :  2;         ///< Bits 3:2
#     UINT8    Reserved0                :  2;         ///< Bits 5:4
#     UINT8    RcdOutputSlewRateControl :  1;         ///< Bits 6:6
#     UINT8    Reserved1                :  1;         ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK;
class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Y0Y2",                        UINT8, 2),
    ("Y1Y3",                        UINT8, 2),
    ("Reserved0",                   UINT8, 2),
    ("RcdOutputSlewRateControl",    UINT8, 1),
    ("Reserved1",                   UINT8, 1)
    ]

class SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef struct {
#   UINT8    DataBufferRevisionNumber;
# } SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER;
class SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferRevisionNumber",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DramVrefDQForPackageRank0 :  6;        ///< Bits 5:0
#     UINT8    Reserved                  :  2;        ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK;
class SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DramVrefDQForPackageRank0",   UINT8, 6),
    ("Reserved",                    UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef struct {
#   UINT8    DataBufferVrefDQforDramInterface;
# } SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE;
class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferVrefDQforDramInterface",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DramInterfaceMdqDriveStrength           :  4; ///< Bits 3:0
#     UINT8    DramInterfaceMdqReadTerminationStrength :  4; ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE;
class SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DramInterfaceMdqDriveStrength",           UINT8, 4),
    ("DramInterfaceMdqReadTerminationStrength", UINT8, 4)
    ]

class SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DataRateLe1866 :  2;                         ///< Bits 1:0
#     UINT8    DataRateLe2400 :  2;                         ///< Bits 3:2
#     UINT8    DataRateLe3200 :  2;                         ///< Bits 5:4
#     UINT8    Reserved       :  2;                         ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DRAM_DRIVE_STRENGTH;
class SPD4_LRDIMM_DRAM_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataRateLe1866",  UINT8, 2),
    ("DataRateLe2400",  UINT8, 2),
    ("DataRateLe3200",  UINT8, 2),
    ("Reserved",        UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Rtt_Nom  :  3;                               ///< Bits 2:0
#     UINT8    Rtt_WR   :  3;                               ///< Bits 5:3
#     UINT8    Reserved :  2;                               ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE;
class SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rtt_Nom",     UINT8, 3),
    ("Rtt_WR",      UINT8, 3),
    ("Reserved",    UINT8, 2)
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    PackageRanks0_1 :  3;                        ///< Bits 2:0
#     UINT8    PackageRanks2_3 :  3;                        ///< Bits 5:3
#     UINT8    Reserved        :  2;                        ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE;
class SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PackageRanks0_1", UINT8, 3),
    ("PackageRanks2_3", UINT8, 3),
    ("Reserved",        UINT8, 2),
    ]

class SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Rank0      :  1;                             ///< Bits 0:0
#     UINT8    Rank1      :  1;                             ///< Bits 1:1
#     UINT8    Rank2      :  1;                             ///< Bits 2:2
#     UINT8    Rank3      :  1;                             ///< Bits 3:3
#     UINT8    DataBuffer :  1;                             ///< Bits 4:4
#     UINT8    Reserved   :  3;                             ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE;
class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rank0",       UINT8, 1),
    ("Rank1",       UINT8, 1),
    ("Rank2",       UINT8, 1),
    ("Rank3",       UINT8, 1),
    ("DataBuffer",  UINT8, 1),
    ("Reserved",    UINT8, 3)
    ]

class SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DataBufferGainAdjustment :  1;               ///< Bits 0:0
#     UINT8    DataBufferDfe            :  1;               ///< Bits 1:1
#     UINT8    Reserved                 :  6;               ///< Bits 7:2
#   } Bits;
#   UINT8    Data;
# } SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION;
class SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DataBufferGainAdjustment",    UINT8, 1),
    ("DataBufferDfe",               UINT8, 1),
    ("Reserved",                    UINT8, 6)
    ]

class SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef UINT16 SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER;
SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER = UINT16

# 
# typedef union {
#   struct {
#     UINT16    ContinuationCount  :  7;               ///< Bits 6:0
#     UINT16    ContinuationParity :  1;               ///< Bits 7:7
#     UINT16    LastNonZeroByte    :  8;               ///< Bits 15:8
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE;
class SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef UINT16 SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER;
# 
# typedef UINT8 SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE;
SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER     = UINT16
SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE  = UINT8
# 
# typedef union {
#   struct {
#     UINT8    Card      :  5;                         ///< Bits 4:0
#     UINT8    Revision  :  2;                         ///< Bits 6:5
#     UINT8    Extension :  1;                         ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD4_NVDIMM_REFERENCE_RAW_CARD;
class SPD4_NVDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD4_NVDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved  :  4;                         ///< Bits 3:0
#     UINT8    Extension :  4;                         ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD4_NVDIMM_MODULE_CHARACTERISTICS;
class SPD4_NVDIMM_MODULE_CHARACTERISTICS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8, 4),
    ("Extension",   UINT8, 4)
    ]

class SPD4_NVDIMM_MODULE_CHARACTERISTICS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_MODULE_CHARACTERISTICS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef struct {
#   UINT8    Reserved;
#   UINT8    MediaType;
# } SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES;
class SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",    UINT8),
    ("MediaType",   UINT8)
    ]

# 
# typedef UINT8 SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME;
SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME = UINT8

# 
# typedef union {
#   struct {
#     UINT16    FunctionInterface :  5;                ///< Bits 4:0
#     UINT16    FunctionClass     :  5;                ///< Bits 9:5
#     UINT16    BlockOffset       :  4;                ///< Bits 13:10
#     UINT16    Reserved          :  1;                ///< Bits 14:14
#     UINT16    Implemented       :  1;                ///< Bits 15:15
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR;
class SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FunctionInterface",   UINT16, 5),
    ("FunctionClass",       UINT16, 5),
    ("BlockOffset",         UINT16, 4),
    ("Reserved",            UINT16, 1),
    ("Implemented",         UINT16, 1)
    ]

class SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef struct {
#   UINT8    Year;                               ///< Year represented in BCD (00h = 2000)
#   UINT8    Week;                               ///< Year represented in BCD (47h = week 47)
# } SPD4_MANUFACTURING_DATE;
class SPD4_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",    UINT8),
    ("Week",    UINT8)
    ]

# 
# typedef union {
#   UINT32    Data;
#   UINT16    SerialNumber16[2];
#   UINT8     SerialNumber8[4];
# } SPD4_MANUFACTURER_SERIAL_NUMBER;
class SPD4_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

# 
# typedef struct {
#   UINT8    Location;                           ///< Module Manufacturing Location
# } SPD4_MANUFACTURING_LOCATION;
class SPD4_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",    UINT8)
    ]

# 
# typedef struct {
#   SPD4_MANUFACTURER_ID_CODE          IdCode;                     ///< Module Manufacturer ID Code
#   SPD4_MANUFACTURING_LOCATION        Location;                   ///< Module Manufacturing Location
#   SPD4_MANUFACTURING_DATE            Date;                       ///< Module Manufacturing Year, in BCD (range: 2000-2255)
#   SPD4_MANUFACTURER_SERIAL_NUMBER    SerialNumber;               ///< Module Serial Number
# } SPD4_UNIQUE_MODULE_ID;
class SPD4_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD4_MANUFACTURER_ID_CODE      ),
    ("Location",        SPD4_MANUFACTURING_LOCATION    ),
    ("Date",            SPD4_MANUFACTURING_DATE        ),
    ("SerialNumber",    SPD4_MANUFACTURER_SERIAL_NUMBER)
    ]

# 
# typedef union {
#   UINT16    Crc[1];
#   UINT8     Data8[2];
# } SPD4_CYCLIC_REDUNDANCY_CODE;
class SPD4_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",    UINT16 * 1),
    ("Data8",  UINT8  * 2)
    ]

# 
# typedef struct {
#   SPD4_DEVICE_DESCRIPTION_STRUCT               Description;               ///< 0       Number of Serial PD Bytes Written / SPD Device Size / CRC Coverage 1, 2
#   SPD4_REVISION_STRUCT                         Revision;                  ///< 1       SPD Revision
#   SPD4_DRAM_DEVICE_TYPE_STRUCT                 DramDeviceType;            ///< 2       DRAM Device Type
#   SPD4_MODULE_TYPE_STRUCT                      ModuleType;                ///< 3       Module Type
#   SPD4_SDRAM_DENSITY_BANKS_STRUCT              SdramDensityAndBanks;      ///< 4       SDRAM Density and Banks
#   SPD4_SDRAM_ADDRESSING_STRUCT                 SdramAddressing;           ///< 5       SDRAM Addressing
#   SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT       PrimarySdramPackageType;   ///< 6       Primary SDRAM Package Type
#   SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT          SdramOptionalFeatures;     ///< 7       SDRAM Optional Features
#   SPD4_SDRAM_THERMAL_REFRESH_STRUCT            ThermalAndRefreshOptions;  ///< 8       SDRAM Thermal and Refresh Options
#   SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT    OtherOptionalFeatures;     ///< 9       Other SDRAM Optional Features
#   SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT     SecondarySdramPackageType; ///< 10      Secondary SDRAM Package Type
#   SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT           ModuleNominalVoltage;      ///< 11      Module Nominal Voltage, VDD
#   SPD4_MODULE_ORGANIZATION_STRUCT              ModuleOrganization;        ///< 12      Module Organization
#   SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT          ModuleMemoryBusWidth;      ///< 13      Module Memory Bus Width
#   SPD4_MODULE_THERMAL_SENSOR_STRUCT            ModuleThermalSensor;       ///< 14      Module Thermal Sensor
#   SPD4_EXTENDED_MODULE_TYPE_STRUCT             ExtendedModuleType;        ///< 15      Extended Module Type
#   UINT8                                        Reserved0;                 ///< 16      Reserved
#   SPD4_TIMEBASE_STRUCT                         Timebase;                  ///< 17      Timebases
#   SPD4_TCK_MIN_MTB_STRUCT                      tCKmin;                    ///< 18      SDRAM Minimum Cycle Time (tCKmin)
#   SPD4_TCK_MAX_MTB_STRUCT                      tCKmax;                    ///< 19      SDRAM Maximum Cycle Time (tCKmax)
#   SPD4_CAS_LATENCIES_SUPPORTED_STRUCT          CasLatencies;              ///< 20-23   CAS Latencies Supported
#   SPD4_TAA_MIN_MTB_STRUCT                      tAAmin;                    ///< 24      Minimum CAS Latency Time (tAAmin)
#   SPD4_TRCD_MIN_MTB_STRUCT                     tRCDmin;                   ///< 25      Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD4_TRP_MIN_MTB_STRUCT                      tRPmin;                    ///< 26      Minimum Row Precharge Delay Time (tRPmin)
#   SPD4_TRAS_TRC_MIN_MTB_STRUCT                 tRASMintRCMinUpper;        ///< 27      Upper Nibbles for tRAS and tRC
#   SPD4_TRAS_MIN_MTB_STRUCT                     tRASmin;                   ///< 28      Minimum Active to Precharge Delay Time (tRASmin), Least Significant Byte
#   SPD4_TRC_MIN_MTB_STRUCT                      tRCmin;                    ///< 29      Minimum Active to Active/Refresh Delay Time (tRCmin), Least Significant Byte
#   SPD4_TRFC_MIN_MTB_STRUCT                     tRFC1min;                  ///< 30-31   Minimum Refresh Recovery Delay Time (tRFC1min)
#   SPD4_TRFC_MIN_MTB_STRUCT                     tRFC2min;                  ///< 32-33   Minimum Refresh Recovery Delay Time (tRFC2min)
#   SPD4_TRFC_MIN_MTB_STRUCT                     tRFC4min;                  ///< 34-35   Minimum Refresh Recovery Delay Time (tRFC4min)
#   SPD4_TFAW_MIN_MTB_UPPER_STRUCT               tFAWMinUpper;              ///< 36      Upper Nibble for tFAW
#   SPD4_TFAW_MIN_MTB_STRUCT                     tFAWmin;                   ///< 37      Minimum Four Activate Window Delay Time (tFAWmin)
#   SPD4_TRRD_MIN_MTB_STRUCT                     tRRD_Smin;                 ///< 38      Minimum Activate to Activate Delay Time (tRRD_Smin), different bank group
#   SPD4_TRRD_MIN_MTB_STRUCT                     tRRD_Lmin;                 ///< 39      Minimum Activate to Activate Delay Time (tRRD_Lmin), same bank group
#   SPD4_TCCD_MIN_MTB_STRUCT                     tCCD_Lmin;                 ///< 40      Minimum CAS to CAS Delay Time (tCCD_Lmin), Same Bank Group
#   SPD4_TWR_UPPER_NIBBLE_STRUCT                 tWRUpperNibble;            ///< 41      Upper Nibble for tWRmin
#   SPD4_TWR_MIN_MTB_STRUCT                      tWRmin;                    ///< 42      Minimum Write Recovery Time (tWRmin)
#   SPD4_TWTR_UPPER_NIBBLE_STRUCT                tWTRUpperNibble;           ///< 43      Upper Nibbles for tWTRmin
#   SPD4_TWTR_MIN_MTB_STRUCT                     tWTR_Smin;                 ///< 44      Minimum Write to Read Time (tWTR_Smin), Different Bank Group
#   SPD4_TWTR_MIN_MTB_STRUCT                     tWTR_Lmin;                 ///< 45      Minimum Write to Read Time (tWTR_Lmin), Same Bank Group
#   UINT8                                        Reserved1[59 - 46 + 1];    ///< 46-59   Reserved
#   SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT       BitMapping[77 - 60 + 1];   ///< 60-77   Connector to SDRAM Bit Mapping
#   UINT8                                        Reserved2[116 - 78 + 1];   ///< 78-116  Reserved
#   SPD4_TCCD_MIN_FTB_STRUCT                     tCCD_LminFine;             ///< 117     Fine Offset for Minimum CAS to CAS Delay Time (tCCD_Lmin), same bank group
#   SPD4_TRRD_MIN_FTB_STRUCT                     tRRD_LminFine;             ///< 118     Fine Offset for Minimum Activate to Activate Delay Time (tRRD_Lmin), different bank group
#   SPD4_TRRD_MIN_FTB_STRUCT                     tRRD_SminFine;             ///< 119     Fine Offset for Minimum Activate to Activate Delay Time (tRRD_Smin), same bank group
#   SPD4_TRC_MIN_FTB_STRUCT                      tRCminFine;                ///< 120     Fine Offset for Minimum Active to Active/Refresh Delay Time (tRCmin)
#   SPD4_TRP_MIN_FTB_STRUCT                      tRPminFine;                ///< 121     Fine Offset for Minimum Row Precharge Delay Time (tRPabmin)
#   SPD4_TRCD_MIN_FTB_STRUCT                     tRCDminFine;               ///< 122     Fine Offset for Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD4_TAA_MIN_FTB_STRUCT                      tAAminFine;                ///< 123     Fine Offset for Minimum CAS Latency Time (tAAmin)
#   SPD4_TCK_MAX_FTB_STRUCT                      tCKmaxFine;                ///< 124     Fine Offset for SDRAM Minimum Cycle Time (tCKmax)
#   SPD4_TCK_MIN_FTB_STRUCT                      tCKminFine;                ///< 125     Fine Offset for SDRAM Maximum Cycle Time (tCKmin)
#   SPD4_CYCLIC_REDUNDANCY_CODE                  Crc;                       ///< 126-127 Cyclical Redundancy Code (CRC)
# } SPD4_BASE_SECTION;
class SPD4_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",                 SPD4_DEVICE_DESCRIPTION_STRUCT           ),
    ("Revision",                    SPD4_REVISION_STRUCT                     ),
    ("DramDeviceType",              SPD4_DRAM_DEVICE_TYPE_STRUCT             ),
    ("ModuleType",                  SPD4_MODULE_TYPE_STRUCT                  ),
    ("SdramDensityAndBanks",        SPD4_SDRAM_DENSITY_BANKS_STRUCT          ),
    ("SdramAddressing",             SPD4_SDRAM_ADDRESSING_STRUCT             ),
    ("PrimarySdramPackageType",     SPD4_PRIMARY_SDRAM_PACKAGE_TYPE_STRUCT   ),
    ("SdramOptionalFeatures",       SPD4_SDRAM_OPTIONAL_FEATURES_STRUCT      ),
    ("ThermalAndRefreshOptions",    SPD4_SDRAM_THERMAL_REFRESH_STRUCT        ),
    ("OtherOptionalFeatures",       SPD4_OTHER_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("SecondarySdramPackageType",   SPD4_SECONDARY_SDRAM_PACKAGE_TYPE_STRUCT ),
    ("ModuleNominalVoltage",        SPD4_MODULE_NOMINAL_VOLTAGE_STRUCT       ),
    ("ModuleOrganization",          SPD4_MODULE_ORGANIZATION_STRUCT          ),
    ("ModuleMemoryBusWidth",        SPD4_MODULE_MEMORY_BUS_WIDTH_STRUCT      ),
    ("ModuleThermalSensor",         SPD4_MODULE_THERMAL_SENSOR_STRUCT        ),
    ("ExtendedModuleType",          SPD4_EXTENDED_MODULE_TYPE_STRUCT         ),
    ("Reserved0",                   UINT8                                    ),
    ("Timebase",                    SPD4_TIMEBASE_STRUCT                     ),
    ("tCKmin",                      SPD4_TCK_MIN_MTB_STRUCT                  ),
    ("tCKmax",                      SPD4_TCK_MAX_MTB_STRUCT                  ),
    ("CasLatencies",                SPD4_CAS_LATENCIES_SUPPORTED_STRUCT      ),
    ("tAAmin",                      SPD4_TAA_MIN_MTB_STRUCT                  ),
    ("tRCDmin",                     SPD4_TRCD_MIN_MTB_STRUCT                 ),
    ("tRPmin",                      SPD4_TRP_MIN_MTB_STRUCT                  ),
    ("tRASMintRCMinUpper",          SPD4_TRAS_TRC_MIN_MTB_STRUCT             ),
    ("tRASmin",                     SPD4_TRAS_MIN_MTB_STRUCT                 ),
    ("tRCmin",                      SPD4_TRC_MIN_MTB_STRUCT                  ),
    ("tRFC1min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tRFC2min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tRFC4min",                    SPD4_TRFC_MIN_MTB_STRUCT                 ),
    ("tFAWMinUpper",                SPD4_TFAW_MIN_MTB_UPPER_STRUCT           ),
    ("tFAWmin",                     SPD4_TFAW_MIN_MTB_STRUCT                 ),
    ("tRRD_Smin",                   SPD4_TRRD_MIN_MTB_STRUCT                 ),
    ("tRRD_Lmin",                   SPD4_TRRD_MIN_MTB_STRUCT                 ),
    ("tCCD_Lmin",                   SPD4_TCCD_MIN_MTB_STRUCT                 ),
    ("tWRUpperNibble",              SPD4_TWR_UPPER_NIBBLE_STRUCT             ),
    ("tWRmin",                      SPD4_TWR_MIN_MTB_STRUCT                  ),
    ("tWTRUpperNibble",             SPD4_TWTR_UPPER_NIBBLE_STRUCT            ),
    ("tWTR_Smin",                   SPD4_TWTR_MIN_MTB_STRUCT                 ),
    ("tWTR_Lmin",                   SPD4_TWTR_MIN_MTB_STRUCT                 ),
    ("Reserved1",                   UINT8 * (59 - 46 + 1)                    ),
    ("BitMapping",                  SPD4_CONNECTOR_BIT_MAPPING_BYTE_STRUCT * (77 - 60 + 1)),
    ("Reserved2",                   UINT8 * (116 - 78 + 1)                   ),
    ("tCCD_LminFine",               SPD4_TCCD_MIN_FTB_STRUCT                 ),
    ("tRRD_LminFine",               SPD4_TRRD_MIN_FTB_STRUCT                 ),
    ("tRRD_SminFine",               SPD4_TRRD_MIN_FTB_STRUCT                 ),
    ("tRCminFine",                  SPD4_TRC_MIN_FTB_STRUCT                  ),
    ("tRPminFine",                  SPD4_TRP_MIN_FTB_STRUCT                  ),
    ("tRCDminFine",                 SPD4_TRCD_MIN_FTB_STRUCT                 ),
    ("tAAminFine",                  SPD4_TAA_MIN_FTB_STRUCT                  ),
    ("tCKmaxFine",                  SPD4_TCK_MAX_FTB_STRUCT                  ),
    ("tCKminFine",                  SPD4_TCK_MIN_FTB_STRUCT                  ),
    ("Crc",                         SPD4_CYCLIC_REDUNDANCY_CODE              )
    ]

# 
# typedef struct {
#   SPD4_UNBUF_MODULE_NOMINAL_HEIGHT       ModuleNominalHeight;     ///< 128     Module Nominal Height
#   SPD4_UNBUF_MODULE_NOMINAL_THICKNESS    ModuleMaximumThickness;  ///< 129     Module Maximum Thickness
#   SPD4_UNBUF_REFERENCE_RAW_CARD          ReferenceRawCardUsed;    ///< 130     Reference Raw Card Used
#   SPD4_UNBUF_ADDRESS_MAPPING             AddressMappingEdgeConn;  ///< 131     Address Mapping from Edge Connector to DRAM
#   UINT8                                  Reserved[253 - 132 + 1]; ///< 132-253 Reserved
#   SPD4_CYCLIC_REDUNDANCY_CODE            Crc;                     ///< 254-255 Cyclical Redundancy Code (CRC)
# } SPD4_MODULE_UNBUFFERED;
class SPD4_MODULE_UNBUFFERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD4_UNBUF_MODULE_NOMINAL_HEIGHT   ),
    ("ModuleMaximumThickness",  SPD4_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",    SPD4_UNBUF_REFERENCE_RAW_CARD      ),
    ("AddressMappingEdgeConn",  SPD4_UNBUF_ADDRESS_MAPPING         ),
    ("Reserved",                UINT8 * (253 - 132 + 1)            ),
    ("Crc",                     SPD4_CYCLIC_REDUNDANCY_CODE        )
    ]

# 
# typedef struct {
#   SPD4_RDIMM_MODULE_NOMINAL_HEIGHT                                         ModuleNominalHeight;                                 ///< 128     Module Nominal Height
#   SPD4_RDIMM_MODULE_NOMINAL_THICKNESS                                      ModuleMaximumThickness;                              ///< 129     Module Maximum Thickness
#   SPD4_RDIMM_REFERENCE_RAW_CARD                                            ReferenceRawCardUsed;                                ///< 130     Reference Raw Card Used
#   SPD4_RDIMM_MODULE_ATTRIBUTES                                             DimmModuleAttributes;                                ///< 131     DIMM Module Attributes
#   SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION                                DimmThermalHeatSpreaderSolution;                     ///< 132     RDIMM Thermal Heat Spreader Solution
#   SPD4_MANUFACTURER_ID_CODE                                                RegisterManufacturerIdCode;                          ///< 133-134 Register Manufacturer ID Code
#   SPD4_RDIMM_REGISTER_REVISION_NUMBER                                      RegisterRevisionNumber;                              ///< 135     Register Revision Number
#   SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                         AddressMappingFromRegisterToDRAM;                    ///< 136     Address Mapping from Register to DRAM
#   SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS    RegisterOutputDriveStrengthForControlCommandAddress; ///< 137 Register Output Drive Strength for Control and Command Address
#   SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                      RegisterOutputDriveStrengthForClock;                 ///< 138     Register Output Drive Strength for Clock
#   UINT8                                                                    Reserved[253 - 139 + 1];                             ///< 253-139 Reserved
#   SPD4_CYCLIC_REDUNDANCY_CODE                                              Crc;                                                 ///< 254-255 Cyclical Redundancy Code (CRC)
# } SPD4_MODULE_REGISTERED;
class SPD4_MODULE_REGISTERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                                 SPD4_RDIMM_MODULE_NOMINAL_HEIGHT                                     ),
    ("ModuleMaximumThickness",                              SPD4_RDIMM_MODULE_NOMINAL_THICKNESS                                  ),
    ("ReferenceRawCardUsed",                                SPD4_RDIMM_REFERENCE_RAW_CARD                                        ),
    ("DimmModuleAttributes",                                SPD4_RDIMM_MODULE_ATTRIBUTES                                         ),
    ("DimmThermalHeatSpreaderSolution",                     SPD4_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION                            ),
    ("RegisterManufacturerIdCode",                          SPD4_MANUFACTURER_ID_CODE                                            ),
    ("RegisterRevisionNumber",                              SPD4_RDIMM_REGISTER_REVISION_NUMBER                                  ),
    ("AddressMappingFromRegisterToDRAM",                    SPD4_RDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                     ),
    ("RegisterOutputDriveStrengthForControlCommandAddress", SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS),
    ("RegisterOutputDriveStrengthForClock",                 SPD4_RDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                  ),
    ("Reserved",                                            UINT8 * (253 - 139 + 1)                                              ),
    ("Crc",                                                 SPD4_CYCLIC_REDUNDANCY_CODE                                          )
    ]

# 
# typedef struct {
#   SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT                                         ModuleNominalHeight;                                 ///< 128     Module Nominal Height
#   SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS                                      ModuleMaximumThickness;                              ///< 129     Module Maximum Thickness
#   SPD4_LRDIMM_REFERENCE_RAW_CARD                                            ReferenceRawCardUsed;                                ///< 130     Reference Raw Card Used
#   SPD4_LRDIMM_MODULE_ATTRIBUTES                                             DimmModuleAttributes;                                ///< 131     DIMM Module Attributes
#   SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION                                ThermalHeatSpreaderSolution;                         ///< 132     RDIMM Thermal Heat Spreader Solution
#   SPD4_MANUFACTURER_ID_CODE                                                 RegisterManufacturerIdCode;                          ///< 133-134 Register Manufacturer ID Code
#   SPD4_LRDIMM_REGISTER_REVISION_NUMBER                                      RegisterRevisionNumber;                              ///< 135     Register Revision Number
#   SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                         AddressMappingFromRegisterToDram;                    ///< 136 Address Mapping from Register to DRAM
#   SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS    RegisterOutputDriveStrengthForControlCommandAddress; ///< 137 Register Output Drive Strength for Control and Command Address
#   SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                      RegisterOutputDriveStrengthForClock;                 ///< 138 Register Output Drive Strength for Clock
#   SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER                                   DataBufferRevisionNumber;                            ///< 139     Data Buffer Revision Number
#   SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                                  DramVrefDQForPackageRank0;                           ///< 140     DRAM VrefDQ for Package Rank 0
#   SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                                  DramVrefDQForPackageRank1;                           ///< 141     DRAM VrefDQ for Package Rank 1
#   SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                                  DramVrefDQForPackageRank2;                           ///< 142     DRAM VrefDQ for Package Rank 2
#   SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                                  DramVrefDQForPackageRank3;                           ///< 143     DRAM VrefDQ for Package Rank 3
#   SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE                         DataBufferVrefDQForDramInterface;                    ///< 144     Data Buffer VrefDQ for DRAM Interface
#   SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE              DataBufferMdqDriveStrengthRttForDataRateLe1866;      ///< 145     Data Buffer MDQ Drive Strength and RTT for data rate <= 1866
#   SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE              DataBufferMdqDriveStrengthRttForDataRateLe2400;      ///< 146     Data Buffer MDQ Drive Strength and RTT for data rate <=2400
#   SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE              DataBufferMdqDriveStrengthRttForDataRateLe3200;      ///< 147     Data Buffer MDQ Drive Strength and RTT for data rate <=3200
#   SPD4_LRDIMM_DRAM_DRIVE_STRENGTH                                           DramDriveStrength;                                   ///< 148     DRAM Drive Strength
#   SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                         DramOdtRttWrRttNomForDataRateLe1866;                 ///< 149     DRAM ODT (RTT_WR and RTT_NOM) for data rate <= 1866
#   SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                         DramOdtRttWrRttNomForDataRateLe2400;                 ///< 150     DRAM ODT (RTT_WR and RTT_NOM) for data rate <= 2400
#   SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                         DramOdtRttWrRttNomForDataRateLe3200;                 ///< 151     DRAM ODT (RTT_WR and RTT_NOM) for data rate <= 3200
#   SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                               DramOdtRttParkForDataRateLe1866;                     ///< 152     DRAM ODT (RTT_PARK) for data rate <= 1866
#   SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                               DramOdtRttParkForDataRateLe2400;                     ///< 153     DRAM ODT (RTT_PARK) for data rate <= 2400
#   SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                               DramOdtRttParkForDataRateLe3200;                     ///< 154     DRAM ODT (RTT_PARK) for data rate <= 3200
#   SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE                   DataBufferVrefDQForDramInterfaceRange;               ///< 155     Data Buffer VrefDQ for DRAM Interface Range
#   SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION                 DataBufferDqDecisionFeedbackEqualization;            ///< 156     Data Buffer DQ Decision Feedback Equalization
#   UINT8                                                                     Reserved[253 - 157 + 1];                             ///< 253-132 Reserved
#   SPD4_CYCLIC_REDUNDANCY_CODE                                               Crc;                                                 ///< 254-255 Cyclical Redundancy Code (CRC)
# } SPD4_MODULE_LOADREDUCED;
class SPD4_MODULE_LOADREDUCED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                                 SPD4_LRDIMM_MODULE_NOMINAL_HEIGHT                                     ),
    ("ModuleMaximumThickness",                              SPD4_LRDIMM_MODULE_NOMINAL_THICKNESS                                  ),
    ("ReferenceRawCardUsed",                                SPD4_LRDIMM_REFERENCE_RAW_CARD                                        ),
    ("DimmModuleAttributes",                                SPD4_LRDIMM_MODULE_ATTRIBUTES                                         ),
    ("ThermalHeatSpreaderSolution",                         SPD4_LRDIMM_THERMAL_HEAT_SPREADER_SOLUTION                            ),
    ("RegisterManufacturerIdCode",                          SPD4_MANUFACTURER_ID_CODE                                             ),
    ("RegisterRevisionNumber",                              SPD4_LRDIMM_REGISTER_REVISION_NUMBER                                  ),
    ("AddressMappingFromRegisterToDram",                    SPD4_LRDIMM_ADDRESS_MAPPING_FROM_REGISTER_TO_DRAM                     ),
    ("RegisterOutputDriveStrengthForControlCommandAddress", SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CONTROL_COMMAND_ADDRESS),
    ("RegisterOutputDriveStrengthForClock",                 SPD4_LRDIMM_REGISTER_OUTPUT_DRIVE_STRENGTH_FOR_CLOCK                  ),
    ("DataBufferRevisionNumber",                            SPD4_LRDIMM_DATA_BUFFER_REVISION_NUMBER                               ),
    ("DramVrefDQForPackageRank0",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank1",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank2",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DramVrefDQForPackageRank3",                           SPD4_LRDIMM_DRAM_VREFDQ_FOR_PACKAGE_RANK                              ),
    ("DataBufferVrefDQForDramInterface",                    SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE                     ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe1866",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe2400",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DataBufferMdqDriveStrengthRttForDataRateLe3200",      SPD4_LRDIMM_DATA_BUFFER_MDQ_DRIVE_STRENGTH_RTT_FOR_DATA_RATE          ),
    ("DramDriveStrength",                                   SPD4_LRDIMM_DRAM_DRIVE_STRENGTH                                       ),
    ("DramOdtRttWrRttNomForDataRateLe1866",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttWrRttNomForDataRateLe2400",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttWrRttNomForDataRateLe3200",                 SPD4_LRDIMM_DRAM_ODT_RTT_WR_RTT_NOM_FOR_DATA_RATE                     ),
    ("DramOdtRttParkForDataRateLe1866",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DramOdtRttParkForDataRateLe2400",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DramOdtRttParkForDataRateLe3200",                     SPD4_LRDIMM_DRAM_ODT_RTT_PARK_FOR_DATA_RATE                           ),
    ("DataBufferVrefDQForDramInterfaceRange",               SPD4_LRDIMM_DATA_BUFFER_VREFDQ_FOR_DRAM_INTERFACE_RANGE               ),
    ("DataBufferDqDecisionFeedbackEqualization",            SPD4_LRDIMM_DATA_BUFFER_DQ_DECISION_FEEDBACK_EQUALIZATION             ),
    ("Reserved",                                            UINT8 * (253 - 157 + 1)                                               ),
    ("Crc",                                                 SPD4_CYCLIC_REDUNDANCY_CODE                                           )
    ]

# 
# typedef struct {
#   UINT8                                                         Reserved0[191 - 128 + 1];                   ///< 128-191  Reserved
#   SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER                         ModuleProductIdentifier;                    ///< 192-193  Module Product Identifier
#   SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE         SubsystemControllerManufacturerIdCode;      ///< 194-195  Subsystem Controller Manufacturer's ID Code
#   SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER                   SubsystemControllerIdentifier;              ///< 196-197  Subsystem Controller Identifier
#   SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE                SubsystemControllerRevisionCode;            ///< 198      Subsystem Controller Revision Code
#   SPD4_NVDIMM_REFERENCE_RAW_CARD                                ReferenceRawCardUsed;                       ///< 199      Reference Raw Card Used
#   SPD4_NVDIMM_MODULE_CHARACTERISTICS                            ModuleCharacteristics;                      ///< 200      Module Characteristics
#   SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES                         HybridModuleMediaTypes;                     ///< 201-202  Hybrid Module Media Types
#   SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME    MaximumNonVolatileMemoryInitializationTime; ///< 203 Maximum Non-Volatile Memory Initialization Time
#   SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR                     FunctionInterfaceDescriptors[8];            ///< 204-219  Function Interface Descriptors
#   UINT8                                                         Reserved[253 - 220 + 1];                    ///< 220-253  Reserved
#   SPD4_CYCLIC_REDUNDANCY_CODE                                   Crc;                                        ///< 254-255  Cyclical Redundancy Code (CRC)
# } SPD4_MODULE_NVDIMM;
class SPD4_MODULE_NVDIMM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved0",                                   UINT8 * (191 - 128 + 1)                                   ),
    ("ModuleProductIdentifier",                     SPD4_NVDIMM_MODULE_PRODUCT_IDENTIFIER                     ),
    ("SubsystemControllerManufacturerIdCode",       SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_MANUFACTURER_ID_CODE     ),
    ("SubsystemControllerIdentifier",               SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_IDENTIFIER               ),
    ("SubsystemControllerRevisionCode",             SPD4_NVDIMM_SUBSYSTEM_CONTROLLER_REVISION_CODE            ),
    ("ReferenceRawCardUsed",                        SPD4_NVDIMM_REFERENCE_RAW_CARD                            ),
    ("ModuleCharacteristics",                       SPD4_NVDIMM_MODULE_CHARACTERISTICS                        ),
    ("HybridModuleMediaTypes",                      SPD4_NVDIMM_HYBRID_MODULE_MEDIA_TYPES                     ),
    ("MaximumNonVolatileMemoryInitializationTime",  SPD4_NVDIMM_MAXIMUM_NONVOLATILE_MEMORY_INITIALIZATION_TIME),
    ("FunctionInterfaceDescriptors",                SPD4_NVDIMM_FUNCTION_INTERFACE_DESCRIPTOR * 8             ),
    ("Reserved",                                    UINT8 * (253 - 220 + 1)                                   ),
    ("Crc",                                         SPD4_CYCLIC_REDUNDANCY_CODE                               )
    ]

# 
# typedef union {
#   SPD4_MODULE_UNBUFFERED     Unbuffered;                        ///< 128-255 Unbuffered Memory Module Types
#   SPD4_MODULE_REGISTERED     Registered;                        ///< 128-255 Registered Memory Module Types
#   SPD4_MODULE_LOADREDUCED    LoadReduced;                       ///< 128-255 Load Reduced Memory Module Types
#   SPD4_MODULE_NVDIMM         NonVolatile;                       ///< 128-255 Non-Volatile (NVDIMM-N) Hybrid Memory Parameters
# } SPD4_MODULE_SPECIFIC;
class SPD4_MODULE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unbuffered",  SPD4_MODULE_UNBUFFERED),
    ("Registered",  SPD4_MODULE_REGISTERED),
    ("LoadReduced", SPD4_MODULE_LOADREDUCED),
    ("NonVolatile", SPD4_MODULE_NVDIMM)
    ]

# 
# typedef struct {
#   UINT8    ModulePartNumber[348 - 329 + 1];                            ///< 329-348 Module Part Number
# } SPD4_MODULE_PART_NUMBER;
class SPD4_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",   UINT8 * (348 - 329 + 1))
    ]

# 
# typedef struct {
#   UINT8    ManufacturerSpecificData[381 - 353 + 1];                            ///< 353-381 Manufacturer's Specific Data
# } SPD4_MANUFACTURER_SPECIFIC;
class SPD4_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",   UINT8 * (381 - 353 + 1))
    ]

# 
# typedef UINT8 SPD4_MODULE_REVISION_CODE;                        ///< 349     Module Revision Code
# typedef UINT8 SPD4_DRAM_STEPPING;                               ///< 352     Dram Stepping\
SPD4_MODULE_REVISION_CODE   = UINT8
SPD4_DRAM_STEPPING          = UINT8

# 
# typedef struct {
#   SPD4_UNIQUE_MODULE_ID         ModuleId;                       ///< 320-328 Unique Module ID
#   SPD4_MODULE_PART_NUMBER       ModulePartNumber;               ///< 329-348 Module Part Number
#   SPD4_MODULE_REVISION_CODE     ModuleRevisionCode;             ///< 349     Module Revision Code
#   SPD4_MANUFACTURER_ID_CODE     DramIdCode;                     ///< 350-351 Dram Manufacturer ID Code
#   SPD4_DRAM_STEPPING            DramStepping;                   ///< 352     Dram Stepping
#   SPD4_MANUFACTURER_SPECIFIC    ManufacturerSpecificData;       ///< 353-381 Manufacturer's Specific Data
#   UINT8                         Reserved[2];                    ///< 382-383 Reserved
# } SPD4_MANUFACTURING_DATA;
class SPD4_MANUFACTURING_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleId",                    SPD4_UNIQUE_MODULE_ID     ),
    ("ModulePartNumber",            SPD4_MODULE_PART_NUMBER   ),
    ("ModuleRevisionCode",          SPD4_MODULE_REVISION_CODE ),
    ("DramIdCode",                  SPD4_MANUFACTURER_ID_CODE ),
    ("DramStepping",                SPD4_DRAM_STEPPING        ),
    ("ManufacturerSpecificData",    SPD4_MANUFACTURER_SPECIFIC),
    ("Reserved",                    UINT8 * 2                 )
    ]

# 
# typedef struct {
#   UINT8    Reserved[511 - 384 + 1];                             ///< 384-511 Unbuffered Memory Module Types
# } SPD4_END_USER_SECTION;
class SPD4_END_USER_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",   UINT8 * (511 - 384 + 1))
    ]

# 
# ///
# /// DDR4 Serial Presence Detect structure
# ///
# typedef struct {
#   SPD4_BASE_SECTION          Base;                              ///< 0-127   Base Configuration and DRAM Parameters
#   SPD4_MODULE_SPECIFIC       Module;                            ///< 128-255 Module-Specific Section
#   UINT8                      Reserved[319 - 256 + 1];           ///< 256-319 Reserved
#   SPD4_MANUFACTURING_DATA    ManufactureInfo;                   ///< 320-383 Manufacturing Information
#   SPD4_END_USER_SECTION      EndUser;                           ///< 384-511 End User Programmable
# } SPD_DDR4;
class SPD_DDR4 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Base",            SPD4_BASE_SECTION),
    ("Module",          SPD4_MODULE_SPECIFIC),
    ("Reserved",        UINT8 * (319 - 256 + 1)),
    ("ManufactureInfo", SPD4_MANUFACTURING_DATA),
    ("EndUser",         SPD4_END_USER_SECTION)
    ]

# 
# #pragma pack (pop)
# #endif
# 