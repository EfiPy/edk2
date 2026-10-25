# /** @file
#   This file contains definitions for SPD DDR3.
# 
#   Copyright (c) 2016, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#     - Serial Presence Detect (SPD) for DDR3 SDRAM Modules Document Release 6
#       http://www.jedec.org/sites/default/files/docs/4_01_02_11R21A.pdf
# **/
# SdramSpdDdr3.py
#
# EfiPy2.MdePkg.IndustryStandard.SdramSpdDdr3
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _SDRAM_SPD_DDR3_H_
# #define _SDRAM_SPD_DDR3_H_
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
# } SPD3_DEVICE_DESCRIPTION_STRUCT;
class SPD3_DEVICE_DESCRIPTION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BytesUsed",   UINT8, 4),
    ("BytesTotal",  UINT8, 3),
    ("CrcCoverage", UINT8, 1)
    ]

class SPD3_DEVICE_DESCRIPTION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_DEVICE_DESCRIPTION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Minor :  4;                             ///< Bits 3:0
#     UINT8    Major :  4;                             ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_REVISION_STRUCT;
class SPD3_REVISION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Minor",   UINT8, 4),
    ("Major",   UINT8, 4)
    ]

class SPD3_REVISION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_REVISION_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Type :  8;                              ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_DRAM_DEVICE_TYPE_STRUCT;
class SPD3_DRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",    UINT8, 8)
    ]

class SPD3_DRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_DRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ModuleType :  4;                        ///< Bits 3:0
#     UINT8    Reserved   :  4;                        ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_MODULE_TYPE_STRUCT;
class SPD3_MODULE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleType",  UINT8, 4),
    ("Reserved",    UINT8, 4)
    ]

class SPD3_MODULE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Density     :  4;                       ///< Bits 3:0
#     UINT8    BankAddress :  3;                       ///< Bits 6:4
#     UINT8    Reserved    :  1;                       ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_SDRAM_DENSITY_BANKS_STRUCT;
class SPD3_SDRAM_DENSITY_BANKS_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Density",     UINT8, 4),
    ("BankAddress", UINT8, 3),
    ("Reserved",    UINT8, 1)
    ]

class SPD3_SDRAM_DENSITY_BANKS_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_DENSITY_BANKS_STRUCT_Bits),
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
# } SPD3_SDRAM_ADDRESSING_STRUCT;
class SPD3_SDRAM_ADDRESSING_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ColumnAddress",   UINT8, 3),
    ("RowAddress",      UINT8, 3),
    ("Reserved",        UINT8, 2)
    ]

class SPD3_SDRAM_ADDRESSING_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_ADDRESSING_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    OperationAt1_50 :  1;                   ///< Bits 0:0
#     UINT8    OperationAt1_35 :  1;                   ///< Bits 1:1
#     UINT8    OperationAt1_25 :  1;                   ///< Bits 2:2
#     UINT8    Reserved        :  5;                   ///< Bits 7:3
#   } Bits;
#   UINT8    Data;
# } SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT;
class SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OperationAt1_50",     UINT8, 1),
    ("OperationAt1_35",     UINT8, 1),
    ("OperationAt1_25",     UINT8, 1),
    ("Reserved",            UINT8, 5)
    ]

class SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT_Bits),
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
# } SPD3_MODULE_ORGANIZATION_STRUCT;
class SPD3_MODULE_ORGANIZATION_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SdramDeviceWidth",    UINT8, 3),
    ("RankCount",           UINT8, 3),
    ("Reserved",            UINT8, 2)
    ]

class SPD3_MODULE_ORGANIZATION_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_ORGANIZATION_STRUCT_Bits),
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
# } SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT;
class SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PrimaryBusWidth",     UINT8, 3),
    ("BusWidthExtension",   UINT8, 2),
    ("Reserved",            UINT8, 3)
    ]

class SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Divisor  :  4;                          ///< Bits 3:0
#     UINT8    Dividend :  4;                          ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_FINE_TIMEBASE_STRUCT;
class SPD3_FINE_TIMEBASE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Divisor",     UINT8, 4),
    ("Dividend",    UINT8, 4)
    ]

class SPD3_FINE_TIMEBASE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_FINE_TIMEBASE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Dividend :  8;                          ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT;
class SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Dividend",    UINT8, 8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Divisor :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT;
class SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Divisor",     UINT8, 8)
    ]

class SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef struct {
#   SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT    Dividend; ///< Medium Timebase (MTB) Dividend
#   SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT     Divisor;  ///< Medium Timebase (MTB) Divisor
# } SPD3_MEDIUM_TIMEBASE;
class SPD3_MEDIUM_TIMEBASE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Dividend",    SPD3_MEDIUM_TIMEBASE_DIVIDEND_STRUCT),
    ("Divisor",     SPD3_MEDIUM_TIMEBASE_DIVISOR_STRUCT)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tCKmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TCK_MIN_MTB_STRUCT;
class SPD3_TCK_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKmin",  UINT8, 8)
    ]

class SPD3_TCK_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TCK_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT16    Cl4      :  1;                         ///< Bits 0:0
#     UINT16    Cl5      :  1;                         ///< Bits 1:1
#     UINT16    Cl6      :  1;                         ///< Bits 2:2
#     UINT16    Cl7      :  1;                         ///< Bits 3:3
#     UINT16    Cl8      :  1;                         ///< Bits 4:4
#     UINT16    Cl9      :  1;                         ///< Bits 5:5
#     UINT16    Cl10     :  1;                         ///< Bits 6:6
#     UINT16    Cl11     :  1;                         ///< Bits 7:7
#     UINT16    Cl12     :  1;                         ///< Bits 8:8
#     UINT16    Cl13     :  1;                         ///< Bits 9:9
#     UINT16    Cl14     :  1;                         ///< Bits 10:10
#     UINT16    Cl15     :  1;                         ///< Bits 11:11
#     UINT16    Cl16     :  1;                         ///< Bits 12:12
#     UINT16    Cl17     :  1;                         ///< Bits 13:13
#     UINT16    Cl18     :  1;                         ///< Bits 14:14
#     UINT16    Reserved :  1;                         ///< Bits 15:15
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD3_CAS_LATENCIES_SUPPORTED_STRUCT;
class SPD3_CAS_LATENCIES_SUPPORTED_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cl4",         UINT16, 1),
    ("Cl5",         UINT16, 1),
    ("Cl6",         UINT16, 1),
    ("Cl7",         UINT16, 1),
    ("Cl8",         UINT16, 1),
    ("Cl9",         UINT16, 1),
    ("Cl10",        UINT16, 1),
    ("Cl11",        UINT16, 1),
    ("Cl12",        UINT16, 1),
    ("Cl13",        UINT16, 1),
    ("Cl14",        UINT16, 1),
    ("Cl15",        UINT16, 1),
    ("Cl16",        UINT16, 1),
    ("Cl17",        UINT16, 1),
    ("Cl18",        UINT16, 1),
    ("Reserved",    UINT16, 1)
    ]

class SPD3_CAS_LATENCIES_SUPPORTED_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            SPD3_CAS_LATENCIES_SUPPORTED_STRUCT_Bits),
    ("Data",            UINT16),
    ("Data8",           UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tAAmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TAA_MIN_MTB_STRUCT;
class SPD3_TAA_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAmin",  UINT8, 8)
    ]

class SPD3_TAA_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TAA_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWRmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TWR_MIN_MTB_STRUCT;
class SPD3_TWR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWRmin",  UINT8, 8)
    ]

class SPD3_TWR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TWR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRCDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRCD_MIN_MTB_STRUCT;
class SPD3_TRCD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDmin", UINT8, 8)
    ]

class SPD3_TRCD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRCD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRRDmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRRD_MIN_MTB_STRUCT;
class SPD3_TRRD_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRRDmin", UINT8, 8)
    ]

class SPD3_TRRD_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRRD_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRPmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRP_MIN_MTB_STRUCT;
class SPD3_TRP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPmin",  UINT8, 8)
    ]

class SPD3_TRP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRASminUpper :  4;                      ///< Bits 3:0
#     UINT8    tRCminUpper  :  4;                      ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_TRAS_TRC_MIN_MTB_STRUCT;
class SPD3_TRAS_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASminUpper",    UINT8, 4),
    ("tRCminUpper",     UINT8, 4)
    ]

class SPD3_TRAS_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRAS_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRASmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRAS_MIN_MTB_STRUCT;
class SPD3_TRAS_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRASmin", UINT8, 8)
    ]

class SPD3_TRAS_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRAS_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRCmin :  8;                            ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRC_MIN_MTB_STRUCT;
class SPD3_TRC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCmin",  UINT8, 8)
    ]

class SPD3_TRC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT16    tRFCmin :  16;                          ///< Bits 15:0
#   } Bits;
#   UINT16    Data;
#   UINT8     Data8[2];
# } SPD3_TRFC_MIN_MTB_STRUCT;
class SPD3_TRFC_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRFCmin", UINT16, 16)
    ]

class SPD3_TRFC_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRFC_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tWTRmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TWTR_MIN_MTB_STRUCT;
class SPD3_TWTR_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tWTRmin", UINT8, 8)
    ]

class SPD3_TWTR_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TWTR_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tRTPmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TRTP_MIN_MTB_STRUCT;
class SPD3_TRTP_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRTPmin", UINT8, 8)
    ]

class SPD3_TRTP_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRTP_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tFAWminUpper :  4;                      ///< Bits 3:0
#     UINT8    Reserved     :  4;                      ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_TFAW_MIN_MTB_UPPER_STRUCT;
class SPD3_TFAW_MIN_MTB_UPPER_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWminUpper",    UINT8, 4),
    ("Reserved",        UINT8, 4)
    ]

class SPD3_TFAW_MIN_MTB_UPPER_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TFAW_MIN_MTB_UPPER_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    tFAWmin :  8;                           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_TFAW_MIN_MTB_STRUCT;
class SPD3_TFAW_MIN_MTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tFAWmin", UINT8, 8)
    ]

class SPD3_TFAW_MIN_MTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TFAW_MIN_MTB_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Rzq6     :  1;                          ///< Bits 0:0
#     UINT8    Rzq7     :  1;                          ///< Bits 1:1
#     UINT8    Reserved :  5;                          ///< Bits 6:2
#     UINT8    DllOff   :  1;                          ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT;
class SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rzq6",        UINT8, 1),
    ("Rzq7",        UINT8, 1),
    ("Reserved",    UINT8, 5),
    ("DllOff",      UINT8, 1)
    ]

class SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ExtendedTemperatureRange       :  1;    ///< Bits 0:0
#     UINT8    ExtendedTemperatureRefreshRate :  1;    ///< Bits 1:1
#     UINT8    AutoSelfRefresh                :  1;    ///< Bits 2:2
#     UINT8    OnDieThermalSensor             :  1;    ///< Bits 3:3
#     UINT8    Reserved                       :  3;    ///< Bits 6:4
#     UINT8    PartialArraySelfRefresh        :  1;    ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_SDRAM_THERMAL_REFRESH_STRUCT;
class SPD3_SDRAM_THERMAL_REFRESH_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ExtendedTemperatureRange",        UINT8, 1),
    ("ExtendedTemperatureRefreshRate",  UINT8, 1),
    ("AutoSelfRefresh",                 UINT8, 1),
    ("OnDieThermalSensor",              UINT8, 1),
    ("Reserved",                        UINT8, 3),
    ("PartialArraySelfRefresh",         UINT8, 1)
    ]

class SPD3_SDRAM_THERMAL_REFRESH_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_THERMAL_REFRESH_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ThermalSensorAccuracy :  7;             ///< Bits 6:0
#     UINT8    ThermalSensorPresence :  1;             ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_MODULE_THERMAL_SENSOR_STRUCT;
class SPD3_MODULE_THERMAL_SENSOR_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ThermalSensorAccuracy",   UINT8, 7),
    ("ThermalSensorPresence",   UINT8, 1)
    ]

class SPD3_MODULE_THERMAL_SENSOR_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MODULE_THERMAL_SENSOR_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    SignalLoading   :  2;                   ///< Bits 1:0
#     UINT8    Reserved        :  2;                   ///< Bits 3:2
#     UINT8    DieCount        :  3;                   ///< Bits 6:4
#     UINT8    SdramDeviceType :  1;                   ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_SDRAM_DEVICE_TYPE_STRUCT;
class SPD3_SDRAM_DEVICE_TYPE_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SignalLoading",   UINT8, 2),
    ("Reserved",        UINT8, 2),
    ("DieCount",        UINT8, 3),
    ("SdramDeviceType", UINT8, 1)
    ]

class SPD3_SDRAM_DEVICE_TYPE_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_SDRAM_DEVICE_TYPE_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tCKminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD3_TCK_MIN_FTB_STRUCT;
class SPD3_TCK_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tCKminFine",  INT8, 8)
    ]

class SPD3_TCK_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TCK_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tAAminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD3_TAA_MIN_FTB_STRUCT;
class SPD3_TAA_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tAAminFine",  INT8, 8)
    ]

class SPD3_TAA_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TAA_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRCDminFine :  8;                        ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD3_TRCD_MIN_FTB_STRUCT;
class SPD3_TRCD_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCDminFine", INT8, 8)
    ]

class SPD3_TRCD_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRCD_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRPminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD3_TRP_MIN_FTB_STRUCT;
class SPD3_TRP_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRPminFine",  INT8, 8)
    ]

class SPD3_TRP_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRP_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     INT8    tRCminFine :  8;                         ///< Bits 7:0
#   } Bits;
#   INT8    Data;
# } SPD3_TRC_MIN_FTB_STRUCT;
class SPD3_TRC_MIN_FTB_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tRCminFine",  INT8, 8)
    ]

class SPD3_TRC_MIN_FTB_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_TRC_MIN_FTB_STRUCT_Bits),
    ("Data",    INT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MaximumActivateCount  :  4;             ///< Bits 3:0
#     UINT8    MaximumActivateWindow :  2;             ///< Bits 5:4
#     UINT8    VendorSpecific        :  2;             ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT;
class SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MaximumActivateCount",    UINT8, 4),
    ("MaximumActivateWindow",   UINT8, 2),
    ("VendorSpecific",          UINT8, 2)
    ]

class SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height           :  5;                  ///< Bits 4:0
#     UINT8    RawCardExtension :  3;                  ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD3_UNBUF_MODULE_NOMINAL_HEIGHT;
class SPD3_UNBUF_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",              UINT8, 5),
    ("RawCardExtension",    UINT8, 3)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                    ///< Bits 3:0
#     UINT8    BackThickness  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_UNBUF_MODULE_NOMINAL_THICKNESS;
class SPD3_UNBUF_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_UNBUF_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_MODULE_NOMINAL_THICKNESS_Bits),
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
# } SPD3_UNBUF_REFERENCE_RAW_CARD;
class SPD3_UNBUF_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_UNBUF_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_REFERENCE_RAW_CARD_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MappingRank1 :  1;                      ///< Bits 0:0
#     UINT8    Reserved     :  7;                      ///< Bits 7:1
#   } Bits;
#   UINT8    Data;
# } SPD3_UNBUF_ADDRESS_MAPPING;
class SPD3_UNBUF_ADDRESS_MAPPING_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MappingRank1",    UINT8, 1),
    ("Reserved",        UINT8, 7)
    ]

class SPD3_UNBUF_ADDRESS_MAPPING (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_UNBUF_ADDRESS_MAPPING_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height   :  5;                          ///< Bits 4:0
#     UINT8    Reserved :  3;                          ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_MODULE_NOMINAL_HEIGHT;
class SPD3_RDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                    ///< Bits 3:0
#     UINT8    BackThickness  :  4;                    ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_MODULE_NOMINAL_THICKNESS;
class SPD3_RDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_RDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_NOMINAL_THICKNESS_Bits),
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
# } SPD3_RDIMM_REFERENCE_RAW_CARD;
class SPD3_RDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_RDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REFERENCE_RAW_CARD_Bits),
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
# } SPD3_RDIMM_MODULE_ATTRIBUTES;
class SPD3_RDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD3_RDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    HeatSpreaderThermalCharacteristics :  7; ///< Bits 6:0
#     UINT8    HeatSpreaderSolution               :  1; ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION;
class SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeatSpreaderThermalCharacteristics",  UINT8, 7),
    ("HeatSpreaderSolution",                UINT8, 1)
    ]

class SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION_Bits),
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
# } SPD3_MANUFACTURER_ID_CODE;
class SPD3_MANUFACTURER_ID_CODE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ContinuationCount",   UINT16, 7),
    ("ContinuationParity",  UINT16, 1),
    ("LastNonZeroByte",     UINT16, 8)
    ]

class SPD3_MANUFACTURER_ID_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_MANUFACTURER_ID_CODE_Bits),
    ("Data",    UINT16),
    ("Data8",   UINT8 * 2)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RegisterRevisionNumber;           ///< Bits 7:0
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_REGISTER_REVISION_NUMBER;
class SPD3_RDIMM_REGISTER_REVISION_NUMBER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterRevisionNumber",  UINT8, 8)
    ]

class SPD3_RDIMM_REGISTER_REVISION_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_REVISION_NUMBER_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Bit0     :  1;                         ///< Bits 0:0
#     UINT8    Bit1     :  1;                         ///< Bits 1:1
#     UINT8    Bit2     :  1;                         ///< Bits 2:2
#     UINT8    Reserved :  5;                         ///< Bits 7:3
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_REGISTER_TYPE;
class SPD3_RDIMM_REGISTER_TYPE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bit0",        UINT8, 1),
    ("Bit1",        UINT8, 1),
    ("Bit2",        UINT8, 1),
    ("Reserved",    UINT8, 5)
    ]

class SPD3_RDIMM_REGISTER_TYPE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_TYPE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved               :  4;           ///< Bits 0:3
#     UINT8    CommandAddressAOutputs :  2;           ///< Bits 5:4
#     UINT8    CommandAddressBOutputs :  2;           ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS;
class SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",                UINT8, 4),
    ("CommandAddressAOutputs",  UINT8, 2),
    ("CommandAddressBOutputs",  UINT8, 2)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    ControlSignalsAOutputs :  2;           ///< Bits 0:1
#     UINT8    ControlSignalsBOutputs :  2;           ///< Bits 3:2
#     UINT8    Y1Y3ClockOutputs       :  2;           ///< Bits 5:4
#     UINT8    Y0Y2ClockOutputs       :  2;           ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK;
class SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ControlSignalsAOutputs",  UINT8, 2),
    ("ControlSignalsBOutputs",  UINT8, 2),
    ("Y1Y3ClockOutputs",        UINT8, 2),
    ("Y0Y2ClockOutputs",        UINT8, 2)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Reserved0 :  4;                        ///< Bits 0:3
#     UINT8    Reserved1 :  4;                        ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_RDIMM_REGISTER_CONTROL_RESERVED;
class SPD3_RDIMM_REGISTER_CONTROL_RESERVED_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved0",   UINT8, 4),
    ("Reserved1",   UINT8, 4)
    ]

class SPD3_RDIMM_REGISTER_CONTROL_RESERVED (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_RDIMM_REGISTER_CONTROL_RESERVED_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Height   :  5;                         ///< Bits 4:0
#     UINT8    Reserved :  3;                         ///< Bits 7:5
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT;
class SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Height",      UINT8, 5),
    ("Reserved",    UINT8, 3)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    FrontThickness :  4;                   ///< Bits 3:0
#     UINT8    BackThickness  :  4;                   ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS;
class SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FrontThickness",  UINT8, 4),
    ("BackThickness",   UINT8, 4)
    ]

class SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS_Bits),
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
# } SPD3_LRDIMM_REFERENCE_RAW_CARD;
class SPD3_LRDIMM_REFERENCE_RAW_CARD_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Card",        UINT8, 5),
    ("Revision",    UINT8, 2),
    ("Extension",   UINT8, 1)
    ]

class SPD3_LRDIMM_REFERENCE_RAW_CARD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_REFERENCE_RAW_CARD_Bits),
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
# } SPD3_LRDIMM_MODULE_ATTRIBUTES;
class SPD3_LRDIMM_MODULE_ATTRIBUTES_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RegisterCount",   UINT8, 2),
    ("DramRowCount",    UINT8, 2),
    ("RegisterType",    UINT8, 4)
    ]

class SPD3_LRDIMM_MODULE_ATTRIBUTES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_ATTRIBUTES_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    AddressCommandPrelaunch :  1;          ///< Bits 0:0
#     UINT8    Rank1Rank5Swap          :  1;          ///< Bits 1:1
#     UINT8    Reserved0               :  1;          ///< Bits 2:2
#     UINT8    Reserved1               :  1;          ///< Bits 3:3
#     UINT8    AddressCommandOutputs   :  2;          ///< Bits 5:4
#     UINT8    QxCS_nOutputs           :  2;          ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH;
class SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AddressCommandPrelaunch", UINT8, 1),
    ("Rank1Rank5Swap",          UINT8, 1),
    ("Reserved0",               UINT8, 1),
    ("Reserved1",               UINT8, 1),
    ("AddressCommandOutputs",   UINT8, 2),
    ("QxCS_nOutputs",           UINT8, 2)
    ]

class SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    QxOdtOutputs     :  2;                 ///< Bits 1:0
#     UINT8    QxCkeOutputs     :  2;                 ///< Bits 3:2
#     UINT8    Y1Y3ClockOutputs :  2;                 ///< Bits 5:4
#     UINT8    Y0Y2ClockOutputs :  2;                 ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_TIMING_DRIVE_STRENGTH;
class SPD3_LRDIMM_TIMING_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("QxOdtOutputs",        UINT8, 2),
    ("QxCkeOutputs",        UINT8, 2),
    ("Y1Y3ClockOutputs",    UINT8, 2),
    ("Y0Y2ClockOutputs",    UINT8, 2)
    ]

class SPD3_LRDIMM_TIMING_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_TIMING_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    YExtendedDelay :  2;                   ///< Bits 1:0
#     UINT8    QxCS_n         :  2;                   ///< Bits 3:2
#     UINT8    QxOdt          :  2;                   ///< Bits 5:4
#     UINT8    QxCke          :  2;                   ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_EXTENDED_DELAY;
class SPD3_LRDIMM_EXTENDED_DELAY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("YExtendedDelay",  UINT8, 2),
    ("QxCS_n",          UINT8, 2),
    ("QxOdt",           UINT8, 2),
    ("QxCke",           UINT8, 2)
    ]

class SPD3_LRDIMM_EXTENDED_DELAY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_EXTENDED_DELAY_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    DelayY   :  3;                         ///< Bits 2:0
#     UINT8    Reserved :  1;                         ///< Bits 3:3
#     UINT8    QxCS_n   :  4;                         ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA;
class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DelayY",      UINT8, 3),
    ("Reserved",    UINT8, 1),
    ("QxCS_n",      UINT8, 4)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    QxCS_n :  4;                           ///< Bits 3:0
#     UINT8    QxOdt  :  4;                           ///< Bits 7:4
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE;
class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("QxCS_n",  UINT8, 4),
    ("QxOdt",   UINT8, 4)
    ]

class SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RC8MdqOdtStrength :  3;                ///< Bits 2:0
#     UINT8    RC8Reserved       :  1;                ///< Bits 3:3
#     UINT8    RC9MdqOdtStrength :  3;                ///< Bits 6:4
#     UINT8    RC9Reserved       :  1;                ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH;
class SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RC8MdqOdtStrength",   UINT8, 3),
    ("RC8Reserved",         UINT8, 1),
    ("RC9MdqOdtStrength",   UINT8, 3),
    ("RC9Reserved",         UINT8, 1)
    ]

class SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    RC10DA3ValueR0 :  1;                   ///< Bits 0:0
#     UINT8    RC10DA4ValueR0 :  1;                   ///< Bits 1:1
#     UINT8    RC10DA3ValueR1 :  1;                   ///< Bits 2:2
#     UINT8    RC10DA4ValueR1 :  1;                   ///< Bits 3:3
#     UINT8    RC11DA3ValueR0 :  1;                   ///< Bits 4:4
#     UINT8    RC11DA4ValueR0 :  1;                   ///< Bits 5:5
#     UINT8    RC11DA3ValueR1 :  1;                   ///< Bits 6:6
#     UINT8    RC11DA4ValueR1 :  1;                   ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL;
class SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RC10DA3ValueR0",   UINT8, 1),
    ("RC10DA4ValueR0",   UINT8, 1),
    ("RC10DA3ValueR1",   UINT8, 1),
    ("RC10DA4ValueR1",   UINT8, 1),
    ("RC11DA3ValueR0",   UINT8, 1),
    ("RC11DA4ValueR0",   UINT8, 1),
    ("RC11DA3ValueR1",   UINT8, 1),
    ("RC11DA4ValueR1",   UINT8, 1)
    ]

class SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    Driver_Impedance :  2;                 ///< Bits 1:0
#     UINT8    Rtt_Nom          :  3;                 ///< Bits 4:2
#     UINT8    Reserved         :  1;                 ///< Bits 5:5
#     UINT8    Rtt_WR           :  2;                 ///< Bits 7:6
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_MR_1_2;
class SPD3_LRDIMM_MR_1_2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Driver_Impedance",    UINT8, 2),
    ("Rtt_Nom",             UINT8, 3),
    ("Reserved",            UINT8, 1),
    ("Rtt_WR",              UINT8, 2)
    ]

class SPD3_LRDIMM_MR_1_2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MR_1_2_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef union {
#   struct {
#     UINT8    MinimumDelayTime :  7;                 ///< Bits 0:6
#     UINT8    Reserved         :  1;                 ///< Bits 7:7
#   } Bits;
#   UINT8    Data;
# } SPD3_LRDIMM_MODULE_DELAY_TIME;
class SPD3_LRDIMM_MODULE_DELAY_TIME_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MinimumDelayTime",    UINT8, 7),
    ("Reserved",            UINT8, 1)
    ]

class SPD3_LRDIMM_MODULE_DELAY_TIME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",    SPD3_LRDIMM_MODULE_DELAY_TIME_Bits),
    ("Data",    UINT8)
    ]

# 
# typedef struct {
#   UINT8    Year;                               ///< Year represented in BCD (00h = 2000)
#   UINT8    Week;                               ///< Year represented in BCD (47h = week 47)
# } SPD3_MANUFACTURING_DATE;
class SPD3_MANUFACTURING_DATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Year",    UINT8),
    ("Week",    UINT8)
    ]

# 
# typedef union {
#   UINT32    Data;
#   UINT16    SerialNumber16[2];
#   UINT8     SerialNumber8[4];
# } SPD3_MANUFACTURER_SERIAL_NUMBER;
class SPD3_MANUFACTURER_SERIAL_NUMBER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Data",            UINT32),
    ("SerialNumber16",  UINT16 * 2),
    ("SerialNumber8",   UINT8  * 4)
    ]

# 
# typedef struct {
#   UINT8    Location;                           ///< Module Manufacturing Location
# } SPD3_MANUFACTURING_LOCATION;
class SPD3_MANUFACTURING_LOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Location",    UINT8)
    ]
# 
# typedef struct {
#   SPD3_MANUFACTURER_ID_CODE          IdCode;                     ///< Module Manufacturer ID Code
#   SPD3_MANUFACTURING_LOCATION        Location;                   ///< Module Manufacturing Location
#   SPD3_MANUFACTURING_DATE            Date;                       ///< Module Manufacturing Year, in BCD (range: 2000-2255)
#   SPD3_MANUFACTURER_SERIAL_NUMBER    SerialNumber;               ///< Module Serial Number
# } SPD3_UNIQUE_MODULE_ID;
class SPD3_UNIQUE_MODULE_ID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IdCode",          SPD3_MANUFACTURER_ID_CODE      ),
    ("Location",        SPD3_MANUFACTURING_LOCATION    ),
    ("Date",            SPD3_MANUFACTURING_DATE        ),
    ("SerialNumber",    SPD3_MANUFACTURER_SERIAL_NUMBER)
    ]

# 
# typedef union {
#   UINT16    Crc[1];
#   UINT8     Data8[2];
# } SPD3_CYCLIC_REDUNDANCY_CODE;
class SPD3_CYCLIC_REDUNDANCY_CODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Crc",    UINT16 * 1),
    ("Data8",  UINT8  * 2)
    ]

# 
# typedef struct {
#   SPD3_DEVICE_DESCRIPTION_STRUCT         Description;              ///< 0   Number of Serial PD Bytes Written / SPD Device Size / CRC Coverage 1, 2
#   SPD3_REVISION_STRUCT                   Revision;                 ///< 1   SPD Revision
#   SPD3_DRAM_DEVICE_TYPE_STRUCT           DramDeviceType;           ///< 2   DRAM Device Type
#   SPD3_MODULE_TYPE_STRUCT                ModuleType;               ///< 3   Module Type
#   SPD3_SDRAM_DENSITY_BANKS_STRUCT        SdramDensityAndBanks;     ///< 4   SDRAM Density and Banks
#   SPD3_SDRAM_ADDRESSING_STRUCT           SdramAddressing;          ///< 5   SDRAM Addressing
#   SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT     ModuleNominalVoltage;     ///< 6   Module Nominal Voltage, VDD
#   SPD3_MODULE_ORGANIZATION_STRUCT        ModuleOrganization;       ///< 7   Module Organization
#   SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT    ModuleMemoryBusWidth;     ///< 8   Module Memory Bus Width
#   SPD3_FINE_TIMEBASE_STRUCT              FineTimebase;             ///< 9   Fine Timebase (FTB) Dividend / Divisor
#   SPD3_MEDIUM_TIMEBASE                   MediumTimebase;           ///< 10-11 Medium Timebase (MTB) Dividend
#   SPD3_TCK_MIN_MTB_STRUCT                tCKmin;                   ///< 12  SDRAM Minimum Cycle Time (tCKmin)
#   UINT8                                  Reserved0;                ///< 13  Reserved
#   SPD3_CAS_LATENCIES_SUPPORTED_STRUCT    CasLatencies;             ///< 14-15 CAS Latencies Supported
#   SPD3_TAA_MIN_MTB_STRUCT                tAAmin;                   ///< 16  Minimum CAS Latency Time (tAAmin)
#   SPD3_TWR_MIN_MTB_STRUCT                tWRmin;                   ///< 17  Minimum Write Recovery Time (tWRmin)
#   SPD3_TRCD_MIN_MTB_STRUCT               tRCDmin;                  ///< 18  Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD3_TRRD_MIN_MTB_STRUCT               tRRDmin;                  ///< 19  Minimum Row Active to Row Active Delay Time (tRRDmin)
#   SPD3_TRP_MIN_MTB_STRUCT                tRPmin;                   ///< 20  Minimum Row Precharge Delay Time (tRPmin)
#   SPD3_TRAS_TRC_MIN_MTB_STRUCT           tRASMintRCMinUpper;       ///< 21  Upper Nibbles for tRAS and tRC
#   SPD3_TRAS_MIN_MTB_STRUCT               tRASmin;                  ///< 22  Minimum Active to Precharge Delay Time (tRASmin), Least Significant Byte
#   SPD3_TRC_MIN_MTB_STRUCT                tRCmin;                   ///< 23  Minimum Active to Active/Refresh Delay Time (tRCmin), Least Significant Byte
#   SPD3_TRFC_MIN_MTB_STRUCT               tRFCmin;                  ///< 24-25  Minimum Refresh Recovery Delay Time (tRFCmin)
#   SPD3_TWTR_MIN_MTB_STRUCT               tWTRmin;                  ///< 26  Minimum Internal Write to Read Command Delay Time (tWTRmin)
#   SPD3_TRTP_MIN_MTB_STRUCT               tRTPmin;                  ///< 27  Minimum Internal Read to Precharge Command Delay Time (tRTPmin)
#   SPD3_TFAW_MIN_MTB_UPPER_STRUCT         tFAWMinUpper;             ///< 28  Upper Nibble for tFAW
#   SPD3_TFAW_MIN_MTB_STRUCT               tFAWmin;                  ///< 29  Minimum Four Activate Window Delay Time (tFAWmin)
#   SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT    SdramOptionalFeatures;    ///< 30  SDRAM Optional Features
#   SPD3_SDRAM_THERMAL_REFRESH_STRUCT      ThermalAndRefreshOptions; ///< 31  SDRAM Thermal And Refresh Options
#   SPD3_MODULE_THERMAL_SENSOR_STRUCT      ModuleThermalSensor;      ///< 32  Module Thermal Sensor
#   SPD3_SDRAM_DEVICE_TYPE_STRUCT          SdramDeviceType;          ///< 33  SDRAM Device Type
#   SPD3_TCK_MIN_FTB_STRUCT                tCKminFine;               ///< 34  Fine Offset for SDRAM Minimum Cycle Time (tCKmin)
#   SPD3_TAA_MIN_FTB_STRUCT                tAAminFine;               ///< 35  Fine Offset for Minimum CAS Latency Time (tAAmin)
#   SPD3_TRCD_MIN_FTB_STRUCT               tRCDminFine;              ///< 36  Fine Offset for Minimum RAS# to CAS# Delay Time (tRCDmin)
#   SPD3_TRP_MIN_FTB_STRUCT                tRPminFine;               ///< 37  Minimum Row Precharge Delay Time (tRPmin)
#   SPD3_TRC_MIN_FTB_STRUCT                tRCminFine;               ///< 38  Fine Offset for Minimum Active to Active/Refresh Delay Time (tRCmin)
#   UINT8                                  Reserved1[40 - 39 + 1];   ///< 39 - 40 Reserved
#   SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT       MacValue;                 ///< 41  SDRAM Maximum Active Count (MAC) Value
#   UINT8                                  Reserved2[59 - 42 + 1];   ///< 42 - 59 Reserved
# } SPD3_BASE_SECTION;
class SPD3_BASE_SECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Description",              SPD3_DEVICE_DESCRIPTION_STRUCT     ),
    ("Revision",                 SPD3_REVISION_STRUCT               ),
    ("DramDeviceType",           SPD3_DRAM_DEVICE_TYPE_STRUCT       ),
    ("ModuleType",               SPD3_MODULE_TYPE_STRUCT            ),
    ("SdramDensityAndBanks",     SPD3_SDRAM_DENSITY_BANKS_STRUCT    ),
    ("SdramAddressing",          SPD3_SDRAM_ADDRESSING_STRUCT       ),
    ("ModuleNominalVoltage",     SPD3_MODULE_NOMINAL_VOLTAGE_STRUCT ),
    ("ModuleOrganization",       SPD3_MODULE_ORGANIZATION_STRUCT    ),
    ("ModuleMemoryBusWidth",     SPD3_MODULE_MEMORY_BUS_WIDTH_STRUCT),
    ("FineTimebase",             SPD3_FINE_TIMEBASE_STRUCT          ),
    ("MediumTimebase",           SPD3_MEDIUM_TIMEBASE               ),
    ("tCKmin",                   SPD3_TCK_MIN_MTB_STRUCT            ),
    ("Reserved0",                UINT8                              ),
    ("CasLatencies",             SPD3_CAS_LATENCIES_SUPPORTED_STRUCT),
    ("tAAmin",                   SPD3_TAA_MIN_MTB_STRUCT            ),
    ("tWRmin",                   SPD3_TWR_MIN_MTB_STRUCT            ),
    ("tRCDmin",                  SPD3_TRCD_MIN_MTB_STRUCT           ),
    ("tRRDmin",                  SPD3_TRRD_MIN_MTB_STRUCT           ),
    ("tRPmin",                   SPD3_TRP_MIN_MTB_STRUCT            ),
    ("tRASMintRCMinUpper",       SPD3_TRAS_TRC_MIN_MTB_STRUCT       ),
    ("tRASmin",                  SPD3_TRAS_MIN_MTB_STRUCT           ),
    ("tRCmin",                   SPD3_TRC_MIN_MTB_STRUCT            ),
    ("tRFCmin",                  SPD3_TRFC_MIN_MTB_STRUCT           ),
    ("tWTRmin",                  SPD3_TWTR_MIN_MTB_STRUCT           ),
    ("tRTPmin",                  SPD3_TRTP_MIN_MTB_STRUCT           ),
    ("tFAWMinUpper",             SPD3_TFAW_MIN_MTB_UPPER_STRUCT     ),
    ("tFAWmin",                  SPD3_TFAW_MIN_MTB_STRUCT           ),
    ("SdramOptionalFeatures",    SPD3_SDRAM_OPTIONAL_FEATURES_STRUCT),
    ("ThermalAndRefreshOptions", SPD3_SDRAM_THERMAL_REFRESH_STRUCT  ),
    ("ModuleThermalSensor",      SPD3_MODULE_THERMAL_SENSOR_STRUCT  ),
    ("SdramDeviceType",          SPD3_SDRAM_DEVICE_TYPE_STRUCT      ),
    ("tCKminFine",               SPD3_TCK_MIN_FTB_STRUCT            ),
    ("tAAminFine",               SPD3_TAA_MIN_FTB_STRUCT            ),
    ("tRCDminFine",              SPD3_TRCD_MIN_FTB_STRUCT           ),
    ("tRPminFine",               SPD3_TRP_MIN_FTB_STRUCT            ),
    ("tRCminFine",               SPD3_TRC_MIN_FTB_STRUCT            ),
    ("Reserved1",                UINT8 * (40 - 39 + 1)              ),
    ("MacValue",                 SPD3_MAXIMUM_ACTIVE_COUNT_STRUCT   ),
    ("Reserved2",                UINT8 * (59 - 42 + 1)              )
    ]

# 
# typedef struct {
#   SPD3_UNBUF_MODULE_NOMINAL_HEIGHT       ModuleNominalHeight;    ///< 60  Module Nominal Height
#   SPD3_UNBUF_MODULE_NOMINAL_THICKNESS    ModuleMaximumThickness; ///< 61  Module Maximum Thickness
#   SPD3_UNBUF_REFERENCE_RAW_CARD          ReferenceRawCardUsed;   ///< 62  Reference Raw Card Used
#   SPD3_UNBUF_ADDRESS_MAPPING             AddressMappingEdgeConn; ///< 63  Address Mapping from Edge Connector to DRAM
#   UINT8                                  Reserved[116 - 64 + 1]; ///< 64-116 Reserved
# } SPD3_MODULE_UNBUFFERED;
class SPD3_MODULE_UNBUFFERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",     SPD3_UNBUF_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",  SPD3_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",    SPD3_UNBUF_REFERENCE_RAW_CARD),
    ("AddressMappingEdgeConn",  SPD3_UNBUF_ADDRESS_MAPPING),
    ("Reserved",                UINT8 * (116 - 64 + 1))
    ]

# 
# typedef struct {
#   SPD3_RDIMM_MODULE_NOMINAL_HEIGHT               ModuleNominalHeight;         ///< 60  Module Nominal Height
#   SPD3_RDIMM_MODULE_NOMINAL_THICKNESS            ModuleMaximumThickness;      ///< 61  Module Maximum Thickness
#   SPD3_RDIMM_REFERENCE_RAW_CARD                  ReferenceRawCardUsed;        ///< 62  Reference Raw Card Used
#   SPD3_RDIMM_MODULE_ATTRIBUTES                   DimmModuleAttributes;        ///< 63  DIMM Module Attributes
#   SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION      ThermalHeatSpreaderSolution; ///< 64     RDIMM Thermal Heat Spreader Solution
#   SPD3_MANUFACTURER_ID_CODE                      RegisterManufacturerIdCode;  ///< 65-66  Register Manufacturer ID Code
#   SPD3_RDIMM_REGISTER_REVISION_NUMBER            RegisterRevisionNumber;      ///< 67     Register Revision Number
#   SPD3_RDIMM_REGISTER_TYPE                       RegisterType;                ///< 68  Register Type
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc1Rc0;                      ///< 69  RC1 (MS Nibble) / RC0 (LS Nibble) - Reserved
#   SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS    Rc3Rc2;                      ///< 70  RC3 (MS Nibble) / RC2 (LS Nibble) - Drive Strength, Command/Address
#   SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK      Rc5Rc4;                      ///< 71  RC5 (MS Nibble) / RC4 (LS Nibble) - Drive Strength, Control and Clock
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc7Rc6;                      ///< 72  RC7 (MS Nibble) / RC6 (LS Nibble) - Reserved for Register Vendor
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc9Rc8;                      ///< 73  RC9 (MS Nibble) / RC8 (LS Nibble) - Reserved
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc11Rc10;                    ///< 74  RC11 (MS Nibble) / RC10 (LS Nibble) - Reserved
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc13Rc12;                    ///< 75  RC12 (MS Nibble) / RC12 (LS Nibble) - Reserved
#   SPD3_RDIMM_REGISTER_CONTROL_RESERVED           Rc15Rc14;                    ///< 76  RC15 (MS Nibble) / RC14 (LS Nibble) - Reserved
#   UINT8                                          Reserved[116 - 77 + 1];      ///< 77-116 Reserved
# } SPD3_MODULE_REGISTERED;
class SPD3_MODULE_REGISTERED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",             SPD3_RDIMM_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",          SPD3_RDIMM_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",            SPD3_RDIMM_REFERENCE_RAW_CARD),
    ("DimmModuleAttributes",            SPD3_RDIMM_MODULE_ATTRIBUTES),
    ("ThermalHeatSpreaderSolution",     SPD3_RDIMM_THERMAL_HEAT_SPREADER_SOLUTION),
    ("RegisterManufacturerIdCode",      SPD3_MANUFACTURER_ID_CODE),
    ("RegisterRevisionNumber",          SPD3_RDIMM_REGISTER_REVISION_NUMBER),
    ("RegisterType",                    SPD3_RDIMM_REGISTER_TYPE),
    ("Rc1Rc0",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc3Rc2",                          SPD3_RDIMM_REGISTER_CONTROL_COMMAND_ADDRESS),
    ("Rc5Rc4",                          SPD3_RDIMM_REGISTER_CONTROL_CONTROL_CLOCK),
    ("Rc7Rc6",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc9Rc8",                          SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc11Rc10",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc13Rc12",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Rc15Rc14",                        SPD3_RDIMM_REGISTER_CONTROL_RESERVED),
    ("Reserved",                        UINT8 * (116 - 77 + 1))
    ]

# 
# typedef struct {
#   SPD3_UNBUF_MODULE_NOMINAL_HEIGHT       ModuleNominalHeight;    ///< 60  Module Nominal Height
#   SPD3_UNBUF_MODULE_NOMINAL_THICKNESS    ModuleMaximumThickness; ///< 61  Module Maximum Thickness
#   SPD3_UNBUF_REFERENCE_RAW_CARD          ReferenceRawCardUsed;   ///< 62  Reference Raw Card Used
#   UINT8                                  Reserved[116 - 63 + 1]; ///< 63-116 Reserved
# } SPD3_MODULE_CLOCKED;
class SPD3_MODULE_CLOCKED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",             SPD3_UNBUF_MODULE_NOMINAL_HEIGHT),
    ("ModuleMaximumThickness",          SPD3_UNBUF_MODULE_NOMINAL_THICKNESS),
    ("ReferenceRawCardUsed",            SPD3_UNBUF_REFERENCE_RAW_CARD),
    ("Reserved",                        UINT8 * (116 - 63 + 1))
    ]

# 
# typedef struct {
#   SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT             ModuleNominalHeight;                     ///< 60  Module Nominal Height
#   SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS          ModuleMaximumThickness;                  ///< 61  Module Maximum Thickness
#   SPD3_LRDIMM_REFERENCE_RAW_CARD                ReferenceRawCardUsed;                    ///< 62  Reference Raw Card Used
#   SPD3_LRDIMM_MODULE_ATTRIBUTES                 DimmModuleAttributes;                    ///< 63  Module Attributes
#   UINT8                                         MemoryBufferRevisionNumber;              ///< 64    Memory Buffer Revision Number
#   SPD3_MANUFACTURER_ID_CODE                     ManufacturerIdCode;                      ///< 65-66 Memory Buffer Manufacturer ID Code
#   SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH     TimingControlDriveStrengthCaCs;          ///< 67    F0RC3 / F0RC2 - Timing Control & Drive Strength, CA & CS
#   SPD3_LRDIMM_TIMING_DRIVE_STRENGTH             DriveStrength;                           ///< 68    F0RC5 / F0RC4 - Drive Strength, ODT & CKE and Y
#   SPD3_LRDIMM_EXTENDED_DELAY                    ExtendedDelay;                           ///< 69    F1RC11 / F1RC8 - Extended Delay for Y, CS and ODT & CKE
#   SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA    AdditiveDelayForCsCa;                    ///< 70    F1RC13 / F1RC12 - Additive Delay for CS and CA
#   SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE    AdditiveDelayForOdtCke;                  ///< 71    F1RC15 / F1RC14 - Additive Delay for ODT & CKE
#   SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH    MdqTerminationDriveStrengthFor800_1066;  ///< 72    F1RC15 / F1RC14 - Additive Delay for ODT & CKE
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_0_1QxOdtControlFor800_1066;         ///< 73    F[3,4]RC11 / F[3,4]RC10 - Rank 0 & 1 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_2_3QxOdtControlFor800_1066;         ///< 74    F[5,6]RC11 / F[5,6]RC10 - Rank 2 & 3 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_4_5QxOdtControlFor800_1066;         ///< 75    F[7,8]RC11 / F[7,8]RC10 - Rank 4 & 5 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_6_7QxOdtControlFor800_1066;         ///< 76    F[9,10]RC11 / F[9,10]RC10 - Rank 6 & 7 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_MR_1_2                            MR_1_2RegistersFor800_1066;              ///< 77    MR1,2 Registers for 800 & 1066
#   SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH    MdqTerminationDriveStrengthFor1333_1600; ///< 78    F1RC15 / F1RC14 - Additive Delay for ODT & CKE
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_0_1QxOdtControlFor1333_1600;        ///< 79    F[3,4]RC11 / F[3,4]RC10 - Rank 0 & 1 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_2_3QxOdtControlFor1333_1600;        ///< 80    F[5,6]RC11 / F[5,6]RC10 - Rank 2 & 3 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_4_5QxOdtControlFor1333_1600;        ///< 81    F[7,8]RC11 / F[7,8]RC10 - Rank 4 & 5 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_6_7QxOdtControlFor1333_1600;        ///< 82    F[9,10]RC11 / F[9,10]RC10 - Rank 6 & 7 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_MR_1_2                            MR_1_2RegistersFor1333_1600;             ///< 83    MR1,2 Registers for 800 & 1066
#   SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH    MdqTerminationDriveStrengthFor1866_2133; ///< 84    F1RC15 / F1RC14 - Additive Delay for ODT & CKE
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_0_1QxOdtControlFor1866_2133;        ///< 85    F[3,4]RC11 / F[3,4]RC10 - Rank 0 & 1 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_2_3QxOdtControlFor1866_2133;        ///< 86    F[5,6]RC11 / F[5,6]RC10 - Rank 2 & 3 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_4_5QxOdtControlFor1866_2133;        ///< 87    F[7,8]RC11 / F[7,8]RC10 - Rank 4 & 5 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL     Rank_6_7QxOdtControlFor1866_2133;        ///< 88    F[9,10]RC11 / F[9,10]RC10 - Rank 6 & 7 RD & WR QxODT Control for 800 & 1066
#   SPD3_LRDIMM_MR_1_2                            MR_1_2RegistersFor1866_2133;             ///< 89    MR1,2 Registers for 800 & 1066
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MinimumModuleDelayTimeFor1_5V;           ///< 90    Minimum Module Delay Time for 1.5 V
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MaximumModuleDelayTimeFor1_5V;           ///< 91    Maximum Module Delay Time for 1.5 V
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MinimumModuleDelayTimeFor1_35V;          ///< 92    Minimum Module Delay Time for 1.35 V
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MaximumModuleDelayTimeFor1_35V;          ///< 93    Maximum Module Delay Time for 1.35 V
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MinimumModuleDelayTimeFor1_25V;          ///< 94    Minimum Module Delay Time for 1.25 V
#   SPD3_LRDIMM_MODULE_DELAY_TIME                 MaximumModuleDelayTimeFor1_25V;          ///< 95    Maximum Module Delay Time for 1.25 V
#   UINT8                                         Reserved[101 - 96 + 1];                  ///< 96-101  Reserved
#   UINT8                                         PersonalityByte[116 - 102 + 1];          ///< 102-116 Memory Buffer Personality Bytes
# } SPD3_MODULE_LOADREDUCED;
class SPD3_MODULE_LOADREDUCED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleNominalHeight",                     SPD3_LRDIMM_MODULE_NOMINAL_HEIGHT         ),
    ("ModuleMaximumThickness",                  SPD3_LRDIMM_MODULE_NOMINAL_THICKNESS      ),
    ("ReferenceRawCardUsed",                    SPD3_LRDIMM_REFERENCE_RAW_CARD            ),
    ("DimmModuleAttributes",                    SPD3_LRDIMM_MODULE_ATTRIBUTES             ),
    ("MemoryBufferRevisionNumber",              UINT8                                     ),
    ("ManufacturerIdCode",                      SPD3_MANUFACTURER_ID_CODE                 ),
    ("TimingControlDriveStrengthCaCs",          SPD3_LRDIMM_TIMING_CONTROL_DRIVE_STRENGTH ),
    ("DriveStrength",                           SPD3_LRDIMM_TIMING_DRIVE_STRENGTH         ),
    ("ExtendedDelay",                           SPD3_LRDIMM_EXTENDED_DELAY                ),
    ("AdditiveDelayForCsCa",                    SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXCS_N_QXCA),
    ("AdditiveDelayForOdtCke",                  SPD3_LRDIMM_ADDITIVE_DELAY_FOR_QXODT_QXCKE),
    ("MdqTerminationDriveStrengthFor800_1066",  SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor800_1066",         SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor800_1066",              SPD3_LRDIMM_MR_1_2                        ),
    ("MdqTerminationDriveStrengthFor1333_1600", SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor1333_1600",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor1333_1600",             SPD3_LRDIMM_MR_1_2                        ),
    ("MdqTerminationDriveStrengthFor1866_2133", SPD3_LRDIMM_MDQ_TERMINATION_DRIVE_STRENGTH),
    ("Rank_0_1QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_2_3QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_4_5QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("Rank_6_7QxOdtControlFor1866_2133",        SPD3_LRDIMM_RANK_READ_WRITE_QXODT_CONTROL ),
    ("MR_1_2RegistersFor1866_2133",             SPD3_LRDIMM_MR_1_2                        ),
    ("MinimumModuleDelayTimeFor1_5V",           SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_5V",           SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MinimumModuleDelayTimeFor1_35V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_35V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MinimumModuleDelayTimeFor1_25V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("MaximumModuleDelayTimeFor1_25V",          SPD3_LRDIMM_MODULE_DELAY_TIME             ),
    ("Reserved",                                UINT8 * (101 - 96 + 1)                    ),
    ("PersonalityByte",                         UINT8 * (116 - 102 + 1)                   )
    ]

# 
# typedef union {
#   SPD3_MODULE_UNBUFFERED     Unbuffered;                        ///< 128-255 Unbuffered Memory Module Types
#   SPD3_MODULE_REGISTERED     Registered;                        ///< 128-255 Registered Memory Module Types
#   SPD3_MODULE_CLOCKED        Clocked;                           ///< 128-255 Registered Memory Module Types
#   SPD3_MODULE_LOADREDUCED    LoadReduced;                       ///< 128-255 Load Reduced Memory Module Types
# } SPD3_MODULE_SPECIFIC;
class SPD3_MODULE_SPECIFIC (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Unbuffered",  SPD3_MODULE_UNBUFFERED ),
    ("Registered",  SPD3_MODULE_REGISTERED ),
    ("Clocked",     SPD3_MODULE_CLOCKED    ),
    ("LoadReduced", SPD3_MODULE_LOADREDUCED)
    ]

# 
# typedef struct {
#   UINT8    ModulePartNumber[145 - 128 + 1];                              ///< 128-145 Module Part Number
# } SPD3_MODULE_PART_NUMBER;
class SPD3_MODULE_PART_NUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModulePartNumber",            UINT8 * (145 - 128 + 1))
    ]

# 
# typedef struct {
#   UINT8    ModuleRevisionCode[147 - 146 + 1];                            ///< 146-147 Module Revision Code
# } SPD3_MODULE_REVISION_CODE;
class SPD3_MODULE_REVISION_CODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ModuleRevisionCode",          UINT8 * (147 - 146 + 1))
    ]

# 
# typedef struct {
#   UINT8    ManufacturerSpecificData[175 - 150 + 1];                      ///< 150-175 Manufacturer's Specific Data
# } SPD3_MANUFACTURER_SPECIFIC;
class SPD3_MANUFACTURER_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ManufacturerSpecificData",    UINT8 * (175 - 150 + 1))
    ]

# 
# ///
# /// DDR3 Serial Presence Detect structure
# ///
# typedef struct {
#   SPD3_BASE_SECTION              General;                             ///< 0-59    General Section
#   SPD3_MODULE_SPECIFIC           Module;                              ///< 60-116  Module-Specific Section
#   SPD3_UNIQUE_MODULE_ID          ModuleId;                            ///< 117-125 Unique Module ID
#   SPD3_CYCLIC_REDUNDANCY_CODE    Crc;                                 ///< 126-127 Cyclical Redundancy Code (CRC)
#   SPD3_MODULE_PART_NUMBER        ModulePartNumber;                    ///< 128-145 Module Part Number
#   SPD3_MODULE_REVISION_CODE      ModuleRevisionCode;                  ///< 146-147 Module Revision Code
#   SPD3_MANUFACTURER_ID_CODE      DramIdCode;                          ///< 148-149 Dram Manufacturer ID Code
#   SPD3_MANUFACTURER_SPECIFIC     ManufacturerSpecificData;            ///< 150-175 Manufacturer's Specific Data
#   UINT8                          Reserved[255 - 176 + 1];             ///< 176-255 Open for Customer Use
# } SPD_DDR3;
class SPD_DDR3 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("General",                     SPD3_BASE_SECTION          ),
    ("Module",                      SPD3_MODULE_SPECIFIC       ),
    ("ModuleId",                    SPD3_UNIQUE_MODULE_ID      ),
    ("Crc",                         SPD3_CYCLIC_REDUNDANCY_CODE),
    ("ModulePartNumber",            SPD3_MODULE_PART_NUMBER    ),
    ("ModuleRevisionCode",          SPD3_MODULE_REVISION_CODE  ),
    ("DramIdCode",                  SPD3_MANUFACTURER_ID_CODE  ),
    ("ManufacturerSpecificData",    SPD3_MANUFACTURER_SPECIFIC ),
    ("Reserved",                    UINT8 * (255 - 176 + 1))
    ]

# 
# #pragma pack (pop)
# #endif
# 