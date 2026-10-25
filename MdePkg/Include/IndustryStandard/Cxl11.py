# /** @file
#   CXL 1.1 Register definitions
# 
#   This file contains the register definitions based on the Compute Express Link
#   (CXL) Specification Revision 1.1.
# 
# Copyright (c) 2020, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Cxl11.py
#
# EfiPy2.MdePkg.IndustryStandard.Cxl11
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _CXL11_H_
# #define _CXL11_H_
# 
# #include <IndustryStandard/Pci.h>
from EfiPy2 import *
from EfiPy2.MdePkg.IndustryStandard import EFIPY_INDUSTRY_STRUCTURE, EFIPY_INDUSTRY_UNION
from EfiPy2.MdePkg.IndustryStandard.Pci import PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER,        \
                                               PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1, \
                                               PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2

# //
# // DVSEC Vendor ID
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.1.1 - Table 58
# // (subject to change as per CXL assigned Vendor ID)
# //
# #define INTEL_CXL_DVSEC_VENDOR_ID  0x8086
INTEL_CXL_DVSEC_VENDOR_ID  = 0x8086

# 
# //
# // CXL Flex Bus Device default device and function number
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.1.1
# //
# #define CXL_DEV_DEV   0
# #define CXL_DEV_FUNC  0
# 
CXL_DEV_DEV   = 0
CXL_DEV_FUNC  = 0

# //
# // Ensure proper structure formats
# //
# #pragma pack(1)
# 
# /**
#   Macro used to verify the size of a data type at compile time and trigger a
#   STATIC_ASSERT() with an error message if the size of the data type does not
#   match the expected size.
# 
#   @param  TypeName      Type name of data type to verify.
#   @param  ExpectedSize  The expected size, in bytes, of the data type specified
#                         by TypeName.
# **/
# #define CXL_11_SIZE_ASSERT(TypeName, ExpectedSize)        \
#   STATIC_ASSERT (                                         \
#     sizeof (TypeName) == ExpectedSize,                    \
#     "Size of " #TypeName                                  \
#     " does not meet CXL 1.1 Specification requirements."  \
#     )
# 
# /**
#   Macro used to verify the offset of a field in a data type at compile time and
#   trigger a STATIC_ASSERT() with an error message if the offset of the field in
#   the data type does not match the expected offset.
# 
#   @param  TypeName        Type name of data type to verify.
#   @param  FieldName       Field name in the data type specified by TypeName to
#                           verify.
#   @param  ExpectedOffset  The expected offset, in bytes, of the field specified
#                           by TypeName and FieldName.
# **/
# #define CXL_11_OFFSET_ASSERT(TypeName, FieldName, ExpectedOffset)  \
#   STATIC_ASSERT (                                                  \
#     OFFSET_OF (TypeName, FieldName) == ExpectedOffset,             \
#     "Offset of " #TypeName "." #FieldName                          \
#     " does not meet CXL 1.1 Specification requirements."           \
#     )
# 
# ///
# /// The PCIe DVSEC for Flex Bus Device
# ///@{
# typedef union {
#   struct {
#     UINT16    CacheCapable  : 1;                                     // bit 0
#     UINT16    IoCapable     : 1;                                     // bit 1
#     UINT16    MemCapable    : 1;                                     // bit 2
#     UINT16    MemHwInitMode : 1;                                     // bit 3
#     UINT16    HdmCount      : 2;                                     // bit 4..5
#     UINT16    Reserved1     : 8;                                     // bit 6..13
#     UINT16    ViralCapable  : 1;                                     // bit 14
#     UINT16    Reserved2     : 1;                                     // bit 15
#   } Bits;
#   UINT16    Uint16;
# } CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY;
class CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheCapable",    UINT16, 1),
    ("IoCapable",       UINT16, 1),
    ("MemCapable",      UINT16, 1),
    ("MemHwInitMode",   UINT16, 1),
    ("HdmCount",        UINT16, 2),
    ("Reserved1",       UINT16, 8),
    ("ViralCapable",    UINT16, 1),
    ("Reserved2",       UINT16, 1)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    CacheEnable        : 1;                                // bit 0
#     UINT16    IoEnable           : 1;                                // bit 1
#     UINT16    MemEnable          : 1;                                // bit 2
#     UINT16    CacheSfCoverage    : 5;                                // bit 3..7
#     UINT16    CacheSfGranularity : 3;                                // bit 8..10
#     UINT16    CacheCleanEviction : 1;                                // bit 11
#     UINT16    Reserved1          : 2;                                // bit 12..13
#     UINT16    ViralEnable        : 1;                                // bit 14
#     UINT16    Reserved2          : 1;                                // bit 15
#   } Bits;
#   UINT16    Uint16;
# } CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL;
class CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",         UINT16, 1),
    ("IoEnable",            UINT16, 1),
    ("MemEnable",           UINT16, 1),
    ("CacheSfCoverage",     UINT16, 5),
    ("CacheSfGranularity",  UINT16, 3),
    ("CacheCleanEviction",  UINT16, 1),
    ("Reserved1",           UINT16, 2),
    ("ViralEnable",         UINT16, 1),
    ("Reserved2",           UINT16, 1)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    Reserved1   : 14;                                       // bit 0..13
#     UINT16    ViralStatus : 1;                                        // bit 14
#     UINT16    Reserved2   : 1;                                        // bit 15
#   } Bits;
#   UINT16    Uint16;
# } CXL_DVSEC_FLEX_BUS_DEVICE_STATUS;
class CXL_DVSEC_FLEX_BUS_DEVICE_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 14),
    ("ViralStatus", UINT16, 1),
    ("Reserved2",   UINT16, 1)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_STATUS_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    Reserved1 : 1;                                          // bit 0
#     UINT16    Reserved2 : 1;                                          // bit 1
#     UINT16    Reserved3 : 1;                                          // bit 2
#     UINT16    Reserved4 : 13;                                         // bit 3..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2;
class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 1),
    ("Reserved2",   UINT16, 1),
    ("Reserved3",   UINT16, 1),
    ("Reserved4",   UINT16, 13)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    Reserved1 : 1;                                          // bit 0
#     UINT16    Reserved2 : 1;                                          // bit 1
#     UINT16    Reserved3 : 14;                                         // bit 2..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2;
class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT16, 1),
    ("Reserved2",   UINT16, 1),
    ("Reserved3",   UINT16, 14)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    ConfigLock : 1;                                         // bit 0
#     UINT16    Reserved1  : 15;                                        // bit 1..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_DVSEC_FLEX_BUS_DEVICE_LOCK;
class CXL_DVSEC_FLEX_BUS_DEVICE_LOCK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ConfigLock",  UINT16, 1),
    ("Reserved1",   UINT16, 15)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_LOCK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_LOCK_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemorySizeHigh : 32;                                    // bit 0..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh",  UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemoryInfoValid   : 1;                                  // bit 0
#     UINT32    MemoryActive      : 1;                                  // bit 1
#     UINT32    MediaType         : 3;                                  // bit 2..4
#     UINT32    MemoryClass       : 3;                                  // bit 5..7
#     UINT32    DesiredInterleave : 3;                                  // bit 8..10
#     UINT32    Reserved          : 17;                                 // bit 11..27
#     UINT32    MemorySizeLow     : 4;                                  // bit 28..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryInfoValid",     UINT32, 1),
    ("MemoryActive",        UINT32, 1),
    ("MediaType",           UINT32, 3),
    ("MemoryClass",         UINT32, 3),
    ("DesiredInterleave",   UINT32, 3),
    ("Reserved",            UINT32, 17),
    ("MemorySizeLow",       UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemoryBaseHigh : 32;                                    // bit 0..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",      UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    Reserved      : 28;                                     // bit 0..27
#     UINT32    MemoryBaseLow : 4;                                      // bit 28..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemoryBaseLow",   UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemorySizeHigh : 32;                                    // bit 0..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemorySizeHigh",  UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemoryInfoValid   : 1;                                  // bit 0
#     UINT32    MemoryActive      : 1;                                  // bit 1
#     UINT32    MediaType         : 3;                                  // bit 2..4
#     UINT32    MemoryClass       : 3;                                  // bit 5..7
#     UINT32    DesiredInterleave : 3;                                  // bit 8..10
#     UINT32    Reserved          : 17;                                 // bit 11..27
#     UINT32    MemorySizeLow     : 4;                                  // bit 28..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryInfoValid",     UINT32, 1),
    ("MemoryActive",        UINT32, 1),
    ("MediaType",           UINT32, 3),
    ("MemoryClass",         UINT32, 3),
    ("DesiredInterleave",   UINT32, 3),
    ("Reserved",            UINT32, 17),
    ("MemorySizeLow",       UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MemoryBaseHigh : 32;                                    // bit 0..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MemoryBaseHigh",      UINT32, 32)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    Reserved      : 28;                                     // bit 0..27
#     UINT32    MemoryBaseLow : 4;                                      // bit 28..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW;
class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",        UINT32, 28),
    ("MemoryBaseLow",   UINT32, 4)
  ]

class CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW_Bits),
    ("Uint32",          UINT32)
  ]

# 
# //
# // Flex Bus Device DVSEC ID
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.1.1, Table 58
# //
# #define FLEX_BUS_DEVICE_DVSEC_ID  0
# 
FLEX_BUS_DEVICE_DVSEC_ID  = 0

# //
# // PCIe DVSEC for Flex Bus Device
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.1.1, Figure 95
# //
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER           Header;                                      // offset 0
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1    DesignatedVendorSpecificHeader1;             // offset 4
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2    DesignatedVendorSpecificHeader2;             // offset 8
#   CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY               DeviceCapability;                            // offset 10
#   CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL                  DeviceControl;                               // offset 12
#   CXL_DVSEC_FLEX_BUS_DEVICE_STATUS                   DeviceStatus;                                // offset 14
#   CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2             DeviceControl2;                              // offset 16
#   CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2              DeviceStatus2;                               // offset 18
#   CXL_DVSEC_FLEX_BUS_DEVICE_LOCK                     DeviceLock;                                  // offset 20
#   UINT16                                             Reserved;                                    // offset 22
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH         DeviceRange1SizeHigh;                        // offset 24
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW          DeviceRange1SizeLow;                         // offset 28
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH         DeviceRange1BaseHigh;                        // offset 32
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW          DeviceRange1BaseLow;                         // offset 36
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH         DeviceRange2SizeHigh;                        // offset 40
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW          DeviceRange2SizeLow;                         // offset 44
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH         DeviceRange2BaseHigh;                        // offset 48
#   CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW          DeviceRange2BaseLow;                         // offset 52
# } CXL_1_1_DVSEC_FLEX_BUS_DEVICE;
class CXL_1_1_DVSEC_FLEX_BUS_DEVICE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER       ),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("DeviceCapability",                CXL_DVSEC_FLEX_BUS_DEVICE_CAPABILITY           ),
    ("DeviceControl",                   CXL_DVSEC_FLEX_BUS_DEVICE_CONTROL              ),
    ("DeviceStatus",                    CXL_DVSEC_FLEX_BUS_DEVICE_STATUS               ),
    ("DeviceControl2",                  CXL_1_1_DVSEC_FLEX_BUS_DEVICE_CONTROL2         ),
    ("DeviceStatus2",                   CXL_1_1_DVSEC_FLEX_BUS_DEVICE_STATUS2          ),
    ("DeviceLock",                      CXL_DVSEC_FLEX_BUS_DEVICE_LOCK                 ),
    ("Reserved",                        UINT16                                         ),
    ("DeviceRange1SizeHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_HIGH     ),
    ("DeviceRange1SizeLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_SIZE_LOW      ),
    ("DeviceRange1BaseHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_HIGH     ),
    ("DeviceRange1BaseLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE1_BASE_LOW      ),
    ("DeviceRange2SizeHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_HIGH     ),
    ("DeviceRange2SizeLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_SIZE_LOW      ),
    ("DeviceRange2BaseHigh",            CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_HIGH     ),
    ("DeviceRange2BaseLow",             CXL_DVSEC_FLEX_BUS_DEVICE_RANGE2_BASE_LOW      )
  ]
# 
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, Header, 0x00);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DesignatedVendorSpecificHeader1, 0x04);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DesignatedVendorSpecificHeader2, 0x08);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceCapability, 0x0A);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceControl, 0x0C);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceStatus, 0x0E);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceControl2, 0x10);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceStatus2, 0x12);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceLock, 0x14);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange1SizeHigh, 0x18);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange1SizeLow, 0x1C);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange1BaseHigh, 0x20);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange1BaseLow, 0x24);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange2SizeHigh, 0x28);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange2SizeLow, 0x2C);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange2BaseHigh, 0x30);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, DeviceRange2BaseLow, 0x34);
# CXL_11_SIZE_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_DEVICE, 0x38);
# ///@}
# 
# ///
# /// PCIe DVSEC for FLex Bus Port
# ///@{
# typedef union {
#   struct {
#     UINT16    CacheCapable : 1;                                       // bit 0
#     UINT16    IoCapable    : 1;                                       // bit 1
#     UINT16    MemCapable   : 1;                                       // bit 2
#     UINT16    Reserved     : 13;                                      // bit 3..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY;
class CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheCapable",    UINT16, 1),
    ("IoCapable",       UINT16, 1),
    ("MemCapable",      UINT16, 1),
    ("Reserved",        UINT16, 13)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    CacheEnable         : 1;                               // bit 0
#     UINT16    IoEnable            : 1;                               // bit 1
#     UINT16    MemEnable           : 1;                               // bit 2
#     UINT16    CxlSyncBypassEnable : 1;                               // bit 3
#     UINT16    DriftBufferEnable   : 1;                               // bit 4
#     UINT16    Reserved            : 3;                               // bit 5..7
#     UINT16    Retimer1Present     : 1;                               // bit 8
#     UINT16    Retimer2Present     : 1;                               // bit 9
#     UINT16    Reserved2           : 6;                               // bit 10..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL;
class CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",         UINT16, 1),
    ("IoEnable",            UINT16, 1),
    ("MemEnable",           UINT16, 1),
    ("CxlSyncBypassEnable", UINT16, 1),
    ("DriftBufferEnable",   UINT16, 1),
    ("Reserved",            UINT16, 3),
    ("Retimer1Present",     UINT16, 1),
    ("Retimer2Present",     UINT16, 1),
    ("Reserved2",           UINT16, 6)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL_Bits),
    ("Uint16",          UINT16)
  ]

# 
# typedef union {
#   struct {
#     UINT16    CacheEnable                            : 1;            // bit 0
#     UINT16    IoEnable                               : 1;            // bit 1
#     UINT16    MemEnable                              : 1;            // bit 2
#     UINT16    CxlSyncBypassEnable                    : 1;            // bit 3
#     UINT16    DriftBufferEnable                      : 1;            // bit 4
#     UINT16    Reserved                               : 3;            // bit 5..7
#     UINT16    CxlCorrectableProtocolIdFramingError   : 1;            // bit 8
#     UINT16    CxlUncorrectableProtocolIdFramingError : 1;            // bit 9
#     UINT16    CxlUnexpectedProtocolIdDropped         : 1;            // bit 10
#     UINT16    Reserved2                              : 5;            // bit 11..15
#   } Bits;
#   UINT16    Uint16;
# } CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS;
class CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheEnable",                             UINT16, 1),
    ("IoEnable",                                UINT16, 1),
    ("MemEnable",                               UINT16, 1),
    ("CxlSyncBypassEnable",                     UINT16, 1),
    ("DriftBufferEnable",                       UINT16, 1),
    ("Reserved",                                UINT16, 3),
    ("CxlCorrectableProtocolIdFramingError",    UINT16, 1),
    ("CxlUncorrectableProtocolIdFramingError",  UINT16, 1),
    ("CxlUnexpectedProtocolIdDropped",          UINT16, 1),
    ("Reserved2",                               UINT16, 5)
  ]

class CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS_Bits),
    ("Uint16",          UINT16)
  ]

# 
# //
# // Flex Bus Port DVSEC ID
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.2.1.3, Table 62
# //
# #define FLEX_BUS_PORT_DVSEC_ID  7
# 
FLEX_BUS_PORT_DVSEC_ID  = 7

# //
# // PCIe DVSEC for Flex Bus Port
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.2.1.3, Figure 99
# //
# typedef struct {
#   PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER           Header;                                      // offset 0
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1    DesignatedVendorSpecificHeader1;             // offset 4
#   PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2    DesignatedVendorSpecificHeader2;             // offset 8
#   CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY             PortCapability;                              // offset 10
#   CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL                PortControl;                                 // offset 12
#   CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS                 PortStatus;                                  // offset 14
# } CXL_1_1_DVSEC_FLEX_BUS_PORT;
class CXL_1_1_DVSEC_FLEX_BUS_PORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          PCI_EXPRESS_EXTENDED_CAPABILITIES_HEADER       ),
    ("DesignatedVendorSpecificHeader1", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_1),
    ("DesignatedVendorSpecificHeader2", PCI_EXPRESS_DESIGNATED_VENDOR_SPECIFIC_HEADER_2),
    ("PortCapability",                  CXL_1_1_DVSEC_FLEX_BUS_PORT_CAPABILITY         ),
    ("PortControl",                     CXL_1_1_DVSEC_FLEX_BUS_PORT_CONTROL            ),
    ("PortStatus",                      CXL_1_1_DVSEC_FLEX_BUS_PORT_STATUS             )
  ]

# 
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, Header, 0x00);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, DesignatedVendorSpecificHeader1, 0x04);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, DesignatedVendorSpecificHeader2, 0x08);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, PortCapability, 0x0A);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, PortControl, 0x0C);
# CXL_11_OFFSET_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, PortStatus, 0x0E);
# CXL_11_SIZE_ASSERT (CXL_1_1_DVSEC_FLEX_BUS_PORT, 0x10);
# ///@}
# 
# ///
# /// CXL 1.1 Upstream and Downstream Port Subsystem Component registers
# ///
# 
# /// The CXL.Cache and CXL.Memory Architectural register definitions
# /// Based on chapter 7.2.2 of Compute Express Link Specification Revision: 1.1
# ///@{
# 
# #define CXL_CAPABILITY_HEADER_OFFSET  0
CXL_CAPABILITY_HEADER_OFFSET  = 0
# typedef union {
#   struct {
#     UINT32    CxlCapabilityId      : 16;                              // bit 0..15
#     UINT32    CxlCapabilityVersion :  4;                              // bit 16..19
#     UINT32    CxlCacheMemVersion   :  4;                              // bit 20..23
#     UINT32    ArraySize            :  8;                              // bit 24..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_CAPABILITY_HEADER;
class CXL_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",         UINT32, 16),
    ("CxlCapabilityVersion",    UINT32,  4),
    ("CxlCacheMemVersion",      UINT32,  4),
    ("ArraySize",               UINT32,  8)
  ]

class CXL_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

# 
# #define CXL_RAS_CAPABILITY_HEADER_OFFSET  4
CXL_RAS_CAPABILITY_HEADER_OFFSET  = 4
# typedef union {
#   struct {
#     UINT32    CxlCapabilityId         : 16;                           // bit 0..15
#     UINT32    CxlCapabilityVersion    :  4;                           // bit 16..19
#     UINT32    CxlRasCapabilityPointer : 12;                           // bit 20..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_RAS_CAPABILITY_HEADER;
class CXL_RAS_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",         UINT32, 16),
    ("CxlCapabilityVersion",    UINT32,  4),
    ("CxlRasCapabilityPointer", UINT32, 12)
  ]

class CXL_RAS_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_RAS_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

# 
# #define CXL_SECURITY_CAPABILITY_HEADER_OFFSET  8
CXL_SECURITY_CAPABILITY_HEADER_OFFSET  = 8
# typedef union {
#   struct {
#     UINT32    CxlCapabilityId              : 16;                      // bit 0..15
#     UINT32    CxlCapabilityVersion         :  4;                      // bit 16..19
#     UINT32    CxlSecurityCapabilityPointer : 12;                      // bit 20..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_SECURITY_CAPABILITY_HEADER;
class CXL_SECURITY_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",                 UINT32, 16),
    ("CxlCapabilityVersion",            UINT32,  4),
    ("CxlSecurityCapabilityPointer",    UINT32, 12)
  ]

class CXL_SECURITY_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_SECURITY_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

# 
# #define CXL_LINK_CAPABILITY_HEADER_OFFSET  0xC
CXL_LINK_CAPABILITY_HEADER_OFFSET  = 0xC
# typedef union {
#   struct {
#     UINT32    CxlCapabilityId          : 16;                          // bit 0..15
#     UINT32    CxlCapabilityVersion     :  4;                          // bit 16..19
#     UINT32    CxlLinkCapabilityPointer : 12;                          // bit 20..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_LINK_CAPABILITY_HEADER;
class CXL_LINK_CAPABILITY_HEADER_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlCapabilityId",             UINT32, 16),
    ("CxlCapabilityVersion",        UINT32,  4),
    ("CxlLinkCapabilityPointer",    UINT32, 12)
  ]

class CXL_LINK_CAPABILITY_HEADER (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_CAPABILITY_HEADER_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    CacheDataParity       :  1;                             // bit 0..0
#     UINT32    CacheAddressParity    :  1;                             // bit 1..1
#     UINT32    CacheByteEnableParity :  1;                             // bit 2..2
#     UINT32    CacheDataEcc          :  1;                             // bit 3..3
#     UINT32    MemDataParity         :  1;                             // bit 4..4
#     UINT32    MemAddressParity      :  1;                             // bit 5..5
#     UINT32    MemByteEnableParity   :  1;                             // bit 6..6
#     UINT32    MemDataEcc            :  1;                             // bit 7..7
#     UINT32    ReInitThreshold       :  1;                             // bit 8..8
#     UINT32    RsvdEncodingViolation :  1;                             // bit 9..9
#     UINT32    PoisonReceived        :  1;                             // bit 10..10
#     UINT32    ReceiverOverflow      :  1;                             // bit 11..11
#     UINT32    Reserved              : 20;                             // bit 12..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_1_1_UNCORRECTABLE_ERROR_STATUS;
class CXL_1_1_UNCORRECTABLE_ERROR_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParity",         UINT32,  1),
    ("CacheAddressParity",      UINT32,  1),
    ("CacheByteEnableParity",   UINT32,  1),
    ("CacheDataEcc",            UINT32,  1),
    ("MemDataParity",           UINT32,  1),
    ("MemAddressParity",        UINT32,  1),
    ("MemByteEnableParity",     UINT32,  1),
    ("MemDataEcc",              UINT32,  1),
    ("ReInitThreshold",         UINT32,  1),
    ("RsvdEncodingViolation",   UINT32,  1),
    ("PoisonReceived",          UINT32,  1),
    ("ReceiverOverflow",        UINT32,  1),
    ("Reserved",                UINT32, 20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_STATUS_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    CacheDataParityMask       :  1;                         // bit 0..0
#     UINT32    CacheAddressParityMask    :  1;                         // bit 1..1
#     UINT32    CacheByteEnableParityMask :  1;                         // bit 2..2
#     UINT32    CacheDataEccMask          :  1;                         // bit 3..3
#     UINT32    MemDataParityMask         :  1;                         // bit 4..4
#     UINT32    MemAddressParityMask      :  1;                         // bit 5..5
#     UINT32    MemByteEnableParityMask   :  1;                         // bit 6..6
#     UINT32    MemDataEccMask            :  1;                         // bit 7..7
#     UINT32    ReInitThresholdMask       :  1;                         // bit 8..8
#     UINT32    RsvdEncodingViolationMask :  1;                         // bit 9..9
#     UINT32    PoisonReceivedMask        :  1;                         // bit 10..10
#     UINT32    ReceiverOverflowMask      :  1;                         // bit 11..11
#     UINT32    Reserved                  : 20;                         // bit 12..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_1_1_UNCORRECTABLE_ERROR_MASK;
class CXL_1_1_UNCORRECTABLE_ERROR_MASK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParityMask",         UINT32,   1),
    ("CacheAddressParityMask",      UINT32,   1),
    ("CacheByteEnableParityMask",   UINT32,   1),
    ("CacheDataEccMask",            UINT32,   1),
    ("MemDataParityMask",           UINT32,   1),
    ("MemAddressParityMask",        UINT32,   1),
    ("MemByteEnableParityMask",     UINT32,   1),
    ("MemDataEccMask",              UINT32,   1),
    ("ReInitThresholdMask",         UINT32,   1),
    ("RsvdEncodingViolationMask",   UINT32,   1),
    ("PoisonReceivedMask",          UINT32,   1),
    ("ReceiverOverflowMask",        UINT32,   1),
    ("Reserved",                    UINT32,  20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_MASK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_MASK_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    CacheDataParitySeverity       :  1;                     // bit 0..0
#     UINT32    CacheAddressParitySeverity    :  1;                     // bit 1..1
#     UINT32    CacheByteEnableParitySeverity :  1;                     // bit 2..2
#     UINT32    CacheDataEccSeverity          :  1;                     // bit 3..3
#     UINT32    MemDataParitySeverity         :  1;                     // bit 4..4
#     UINT32    MemAddressParitySeverity      :  1;                     // bit 5..5
#     UINT32    MemByteEnableParitySeverity   :  1;                     // bit 6..6
#     UINT32    MemDataEccSeverity            :  1;                     // bit 7..7
#     UINT32    ReInitThresholdSeverity       :  1;                     // bit 8..8
#     UINT32    RsvdEncodingViolationSeverity :  1;                     // bit 9..9
#     UINT32    PoisonReceivedSeverity        :  1;                     // bit 10..10
#     UINT32    ReceiverOverflowSeverity      :  1;                     // bit 11..11
#     UINT32    Reserved                      : 20;                     // bit 12..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY;
class CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataParitySeverity",         UINT32,   1),
    ("CacheAddressParitySeverity",      UINT32,   1),
    ("CacheByteEnableParitySeverity",   UINT32,   1),
    ("CacheDataEccSeverity",            UINT32,   1),
    ("MemDataParitySeverity",           UINT32,   1),
    ("MemAddressParitySeverity",        UINT32,   1),
    ("MemByteEnableParitySeverity",     UINT32,   1),
    ("MemDataEccSeverity",              UINT32,   1),
    ("ReInitThresholdSeverity",         UINT32,   1),
    ("RsvdEncodingViolationSeverity",   UINT32,   1),
    ("PoisonReceivedSeverity",          UINT32,   1),
    ("ReceiverOverflowSeverity",        UINT32,   1),
    ("Reserved",                        UINT32,  20)
  ]

class CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    CacheDataEcc         :  1;                              // bit 0..0
#     UINT32    MemoryDataEcc        :  1;                              // bit 1..1
#     UINT32    CrcThreshold         :  1;                              // bit 2..2
#     UINT32    RetryThreshold       :  1;                              // bit 3..3
#     UINT32    CachePoisonReceived  :  1;                              // bit 4..4
#     UINT32    MemoryPoisonReceived :  1;                              // bit 5..5
#     UINT32    PhysicalLayerError   :  1;                              // bit 6..6
#     UINT32    Reserved             : 25;                              // bit 7..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_CORRECTABLE_ERROR_STATUS;
class CXL_CORRECTABLE_ERROR_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataEcc",        UINT32,  1),
    ("MemoryDataEcc",       UINT32,  1),
    ("CrcThreshold",        UINT32,  1),
    ("RetryThreshold",      UINT32,  1),
    ("CachePoisonReceived", UINT32,  1),
    ("MemoryPoisonReceived",UINT32,  1),
    ("PhysicalLayerError",  UINT32,  1),
    ("Reserved",            UINT32, 25)
  ]

class CXL_CORRECTABLE_ERROR_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CORRECTABLE_ERROR_STATUS_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    CacheDataEccMask         :  1;                          // bit 0..0
#     UINT32    MemoryDataEccMask        :  1;                          // bit 1..1
#     UINT32    CrcThresholdMask         :  1;                          // bit 2..2
#     UINT32    RetryThresholdMask       :  1;                          // bit 3..3
#     UINT32    CachePoisonReceivedMask  :  1;                          // bit 4..4
#     UINT32    MemoryPoisonReceivedMask :  1;                          // bit 5..5
#     UINT32    PhysicalLayerErrorMask   :  1;                          // bit 6..6
#     UINT32    Reserved                 : 25;                          // bit 7..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_CORRECTABLE_ERROR_MASK;
class CXL_CORRECTABLE_ERROR_MASK_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheDataEccMask",        UINT32,  1),
    ("MemoryDataEccMask",       UINT32,  1),
    ("CrcThresholdMask",        UINT32,  1),
    ("RetryThresholdMask",      UINT32,  1),
    ("CachePoisonReceivedMask", UINT32,  1),
    ("MemoryPoisonReceivedMask",UINT32,  1),
    ("PhysicalLayerErrorMask",  UINT32,  1),
    ("Reserved",                UINT32, 25)
  ]

class CXL_CORRECTABLE_ERROR_MASK (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CORRECTABLE_ERROR_MASK_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef union {
#   struct {
#     UINT32    FirstErrorPointer                 :  4;                 // bit 0..3
#     UINT32    Reserved1                         :  5;                 // bit 4..8
#     UINT32    MultipleHeaderRecordingCapability :  1;                 // bit 9..9
#     UINT32    Reserved2                         :  3;                 // bit 10..12
#     UINT32    PoisonEnabled                     :  1;                 // bit 13..13
#     UINT32    Reserved3                         : 18;                 // bit 14..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_ERROR_CAPABILITIES_AND_CONTROL;
class CXL_ERROR_CAPABILITIES_AND_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("FirstErrorPointer",                   UINT32,  4),
    ("Reserved1",                           UINT32,  5),
    ("MultipleHeaderRecordingCapability",   UINT32,  1),
    ("Reserved2",                           UINT32,  3),
    ("PoisonEnabled",                       UINT32,  1),
    ("Reserved3",                           UINT32, 18)
  ]

class CXL_ERROR_CAPABILITIES_AND_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_ERROR_CAPABILITIES_AND_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef struct {
#   CXL_1_1_UNCORRECTABLE_ERROR_STATUS      UncorrectableErrorStatus;
#   CXL_1_1_UNCORRECTABLE_ERROR_MASK        UncorrectableErrorMask;
#   CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY    UncorrectableErrorSeverity;
#   CXL_CORRECTABLE_ERROR_STATUS            CorrectableErrorStatus;
#   CXL_CORRECTABLE_ERROR_MASK              CorrectableErrorMask;
#   CXL_ERROR_CAPABILITIES_AND_CONTROL      ErrorCapabilitiesAndControl;
#   UINT32                                  HeaderLog[16];
# } CXL_1_1_RAS_CAPABILITY_STRUCTURE;
class CXL_1_1_RAS_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UncorrectableErrorStatus",    CXL_1_1_UNCORRECTABLE_ERROR_STATUS  ),
    ("UncorrectableErrorMask",      CXL_1_1_UNCORRECTABLE_ERROR_MASK    ),
    ("UncorrectableErrorSeverity",  CXL_1_1_UNCORRECTABLE_ERROR_SEVERITY),
    ("CorrectableErrorStatus",      CXL_CORRECTABLE_ERROR_STATUS        ),
    ("CorrectableErrorMask",        CXL_CORRECTABLE_ERROR_MASK          ),
    ("ErrorCapabilitiesAndControl", CXL_ERROR_CAPABILITIES_AND_CONTROL  ),
    ("HeaderLog",                   UINT32 * 16                         )
  ]

# 
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, UncorrectableErrorStatus, 0x00);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, UncorrectableErrorMask, 0x04);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, UncorrectableErrorSeverity, 0x08);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, CorrectableErrorStatus, 0x0C);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, CorrectableErrorMask, 0x10);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, ErrorCapabilitiesAndControl, 0x14);
# CXL_11_OFFSET_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, HeaderLog, 0x18);
# CXL_11_SIZE_ASSERT (CXL_1_1_RAS_CAPABILITY_STRUCTURE, 0x58);
# 
# typedef union {
#   struct {
#     UINT32    DeviceTrustLevel :  2;                                  // bit 0..1
#     UINT32    Reserved         : 30;                                  // bit 2..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_1_1_SECURITY_POLICY;
class CXL_1_1_SECURITY_POLICY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DeviceTrustLevel",    UINT32, 2),
    ("Reserved",            UINT32, 30)
  ]

class CXL_1_1_SECURITY_POLICY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_1_1_SECURITY_POLICY_Bits),
    ("Uint32",          UINT32)
  ]

# 
# typedef struct {
#   CXL_1_1_SECURITY_POLICY    SecurityPolicy;
# } CXL_1_1_SECURITY_CAPABILITY_STRUCTURE;
class CXL_1_1_SECURITY_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SecurityPolicy",  CXL_1_1_SECURITY_POLICY)
  ]

# 
# CXL_11_OFFSET_ASSERT (CXL_1_1_SECURITY_CAPABILITY_STRUCTURE, SecurityPolicy, 0x0);
# CXL_11_SIZE_ASSERT (CXL_1_1_SECURITY_CAPABILITY_STRUCTURE, 0x4);
# 
# typedef union {
#   struct {
#     UINT64    CxlLinkVersionSupported :  4;                           // bit 0..3
#     UINT64    CxlLinkVersionReceived  :  4;                           // bit 4..7
#     UINT64    LlrWrapValueSupported   :  8;                           // bit 8..15
#     UINT64    LlrWrapValueReceived    :  8;                           // bit 16..23
#     UINT64    NumRetryReceived        :  5;                           // bit 24..28
#     UINT64    NumPhyReinitReceived    :  5;                           // bit 29..33
#     UINT64    WrPtrReceived           :  8;                           // bit 34..41
#     UINT64    EchoEseqReceived        :  8;                           // bit 42..49
#     UINT64    NumFreeBufReceived      :  8;                           // bit 50..57
#     UINT64    Reserved                :  6;                           // bit 58..63
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_CAPABILITY;
class CXL_LINK_LAYER_CAPABILITY_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CxlLinkVersionSupported", UINT64, 4),
    ("CxlLinkVersionReceived",  UINT64, 4),
    ("LlrWrapValueSupported",   UINT64, 8),
    ("LlrWrapValueReceived",    UINT64, 8),
    ("NumRetryReceived",        UINT64, 5),
    ("NumPhyReinitReceived",    UINT64, 5),
    ("WrPtrReceived",           UINT64, 8),
    ("EchoEseqReceived",        UINT64, 8),
    ("NumFreeBufReceived",      UINT64, 8),
    ("Reserved",                UINT64, 6)
  ]

class CXL_LINK_LAYER_CAPABILITY (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_CAPABILITY_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT16    LlReset               :  1;                             // bit 0..0
#     UINT16    LlInitStall           :  1;                             // bit 1..1
#     UINT16    LlCrdStall            :  1;                             // bit 2..2
#     UINT16    InitState             :  2;                             // bit 3..4
#     UINT16    LlRetryBufferConsumed :  8;                             // bit 5..12
#     UINT16    Reserved              :  3;                             // bit 13..15
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_CONTROL_AND_STATUS;
class CXL_LINK_LAYER_CONTROL_AND_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LlReset",                 UINT64, 1),
    ("LlInitStall",             UINT64, 1),
    ("LlCrdStall",              UINT64, 1),
    ("InitState",               UINT64, 2),
    ("LlRetryBufferConsumed",   UINT64, 8),
    ("Reserved",                UINT64, 3)
  ]

class CXL_LINK_LAYER_CONTROL_AND_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_CONTROL_AND_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT64    CacheReqCredits  : 10;                                  // bit 0..9
#     UINT64    CacheRspCredits  : 10;                                  // bit 10..19
#     UINT64    CacheDataCredits : 10;                                  // bit 20..29
#     UINT64    MemReqRspCredits : 10;                                  // bit 30..39
#     UINT64    MemDataCredits   : 10;                                  // bit 40..49
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_RX_CREDIT_CONTROL;
class CXL_LINK_LAYER_RX_CREDIT_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_RX_CREDIT_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_RX_CREDIT_CONTROL_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT64    CacheReqCredits  : 10;                                  // bit 0..9
#     UINT64    CacheRspCredits  : 10;                                  // bit 10..19
#     UINT64    CacheDataCredits : 10;                                  // bit 20..29
#     UINT64    MemReqRspCredits : 10;                                  // bit 30..39
#     UINT64    MemDataCredits   : 10;                                  // bit 40..49
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS;
class CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT64    CacheReqCredits  : 10;                                  // bit 0..9
#     UINT64    CacheRspCredits  : 10;                                  // bit 10..19
#     UINT64    CacheDataCredits : 10;                                  // bit 20..29
#     UINT64    MemReqRspCredits : 10;                                  // bit 30..39
#     UINT64    MemDataCredits   : 10;                                  // bit 40..49
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_TX_CREDIT_STATUS;
class CXL_LINK_LAYER_TX_CREDIT_STATUS_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CacheReqCredits",  UINT64, 10),
    ("CacheRspCredits",  UINT64, 10),
    ("CacheDataCredits", UINT64, 10),
    ("MemReqRspCredits", UINT64, 10),
    ("MemDataCredits",   UINT64, 10)
  ]

class CXL_LINK_LAYER_TX_CREDIT_STATUS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_TX_CREDIT_STATUS_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT32    AckForceThreshold :  8;                                 // bit 0..7
#     UINT32    AckFLushRetimer   : 10;                                 // bit 8..17
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_ACK_TIMER_CONTROL;
class CXL_LINK_LAYER_ACK_TIMER_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("AckForceThreshold",  UINT64, 8),
    ("AckFLushRetimer",    UINT64, 10)
  ]

class CXL_LINK_LAYER_ACK_TIMER_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_ACK_TIMER_CONTROL_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef union {
#   struct {
#     UINT32    MdhDisable :  1;                                        // bit 0..0
#     UINT32    Reserved   : 31;                                        // bit 1..31
#   } Bits;
#   UINT64    Uint64;
# } CXL_LINK_LAYER_DEFEATURE;
class CXL_LINK_LAYER_DEFEATURE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MdhDisable",  UINT32, 1),
    ("Reserved",    UINT32, 31)
  ]

class CXL_LINK_LAYER_DEFEATURE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_LINK_LAYER_DEFEATURE_Bits),
    ("Uint64",          UINT64)
  ]

# 
# typedef struct {
#   CXL_LINK_LAYER_CAPABILITY                 LinkLayerCapability;
#   CXL_LINK_LAYER_CONTROL_AND_STATUS         LinkLayerControlStatus;
#   CXL_LINK_LAYER_RX_CREDIT_CONTROL          LinkLayerRxCreditControl;
#   CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS    LinkLayerRxCreditReturnStatus;
#   CXL_LINK_LAYER_TX_CREDIT_STATUS           LinkLayerTxCreditStatus;
#   CXL_LINK_LAYER_ACK_TIMER_CONTROL          LinkLayerAckTimerControl;
#   CXL_LINK_LAYER_DEFEATURE                  LinkLayerDefeature;
# } CXL_1_1_LINK_CAPABILITY_STRUCTURE;
class CXL_1_1_LINK_CAPABILITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LinkLayerCapability",             CXL_LINK_LAYER_CAPABILITY             ),
    ("LinkLayerControlStatus",          CXL_LINK_LAYER_CONTROL_AND_STATUS     ),
    ("LinkLayerRxCreditControl",        CXL_LINK_LAYER_RX_CREDIT_CONTROL      ),
    ("LinkLayerRxCreditReturnStatus",   CXL_LINK_LAYER_RX_CREDIT_RETURN_STATUS),
    ("LinkLayerTxCreditStatus",         CXL_LINK_LAYER_TX_CREDIT_STATUS       ),
    ("LinkLayerAckTimerControl",        CXL_LINK_LAYER_ACK_TIMER_CONTROL      ),
    ("LinkLayerDefeature",              CXL_LINK_LAYER_DEFEATURE              )
  ]

# 
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerCapability, 0x00);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerControlStatus, 0x08);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerRxCreditControl, 0x10);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerRxCreditReturnStatus, 0x18);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerTxCreditStatus, 0x20);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerAckTimerControl, 0x28);
# CXL_11_OFFSET_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, LinkLayerDefeature, 0x30);
# CXL_11_SIZE_ASSERT (CXL_1_1_LINK_CAPABILITY_STRUCTURE, 0x38);
# 
# #define CXL_IO_ARBITRATION_CONTROL_OFFSET  0x180
# typedef union {
#   struct {
#     UINT32    Reserved1                           :  4;               // bit 0..3
#     UINT32    WeightedRoundRobinArbitrationWeight :  4;               // bit 4..7
#     UINT32    Reserved2                           : 24;               // bit 8..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_IO_ARBITRATION_CONTROL;
class CXL_IO_ARBITRATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",                           UINT32,  4),
    ("WeightedRoundRobinArbitrationWeight", UINT32,  4),
    ("Reserved2",                           UINT32, 24)
  ]

class CXL_IO_ARBITRATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_IO_ARBITRATION_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

# 
# CXL_11_SIZE_ASSERT (CXL_IO_ARBITRATION_CONTROL, 0x4);
# 
# #define CXL_CACHE_MEMORY_ARBITRATION_CONTROL_OFFSET  0x1C0
# typedef union {
#   struct {
#     UINT32    Reserved1                           :  4;               // bit 0..3
#     UINT32    WeightedRoundRobinArbitrationWeight :  4;               // bit 4..7
#     UINT32    Reserved2                           : 24;               // bit 8..31
#   } Bits;
#   UINT32    Uint32;
# } CXL_CACHE_MEMORY_ARBITRATION_CONTROL;
class CXL_CACHE_MEMORY_ARBITRATION_CONTROL_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",                           UINT32,  4),
    ("WeightedRoundRobinArbitrationWeight", UINT32,  4),
    ("Reserved2",                           UINT32, 24)
  ]

class CXL_CACHE_MEMORY_ARBITRATION_CONTROL (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_CACHE_MEMORY_ARBITRATION_CONTROL_Bits),
    ("Uint32",          UINT32)
  ]

# 
# CXL_11_SIZE_ASSERT (CXL_CACHE_MEMORY_ARBITRATION_CONTROL, 0x4);
# 
# ///@}
# 
# /// The CXL.RCRB base register definition
# /// Based on chapter 7.3 of Compute Express Link Specification Revision: 1.1
# ///@{
# typedef union {
#   struct {
#     UINT64    RcrbEnable      :  1;                                   // bit 0..0
#     UINT64    Reserved        : 12;                                   // bit 1..12
#     UINT64    RcrbBaseAddress : 51;                                   // bit 13..63
#   } Bits;
#   UINT64    Uint64;
# } CXL_RCRB_BASE;
class CXL_RCRB_BASE_Bits (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RcrbEnable",      UINT64,  1),
    ("Reserved",        UINT64, 12),
    ("RcrbBaseAddress", UINT64, 51)
  ]

class CXL_RCRB_BASE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Bits",            CXL_RCRB_BASE_Bits),
    ("Uint64",          UINT64)
  ]

# 
# CXL_11_SIZE_ASSERT (CXL_RCRB_BASE, 0x8);
# 
# ///@}
# 
# #pragma pack()
# 
# //
# // CXL Downstream / Upstream Port RCRB space register offsets
# // Compute Express Link Specification Revision: 1.1 - Chapter 7.2.1.1 - Figure 97
# //
# #define CXL_PORT_RCRB_MEMBAR0_LOW_OFFSET               0x010
# #define CXL_PORT_RCRB_MEMBAR0_HIGH_OFFSET              0x014
# #define CXL_PORT_RCRB_EXTENDED_CAPABILITY_BASE_OFFSET  0x100
# 
CXL_PORT_RCRB_MEMBAR0_LOW_OFFSET               = 0x010
CXL_PORT_RCRB_MEMBAR0_HIGH_OFFSET              = 0x014
CXL_PORT_RCRB_EXTENDED_CAPABILITY_BASE_OFFSET  = 0x100

# #endif
# 