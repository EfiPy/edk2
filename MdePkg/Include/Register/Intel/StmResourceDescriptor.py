# /** @file
#   STM Resource Descriptor
# 
#   Copyright (c) 2015 - 2019, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Specification Reference:
#   SMI Transfer Monitor (STM) User Guide Revision 1.00
# 
# **/
# 
# StmResourceDescriptor.py
#
# EfiPy2.MdePkg.Register.Intel.StmResourceDescriptor
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _INTEL_STM_RESOURCE_DESCRIPTOR_H_
# #define _INTEL_STM_RESOURCE_DESCRIPTOR_H_
from EfiPy2 import *

# 
# #pragma pack (1)
# 
# /**
#   STM Resource Descriptor Header
# **/
# typedef struct {
#   UINT32    RscType;
#   UINT16    Length;
#   UINT16    ReturnStatus   : 1;
#   UINT16    Reserved       : 14;
#   UINT16    IgnoreResource : 1;
# } STM_RSC_DESC_HEADER;
class STM_RSC_DESC_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("RscType",         UINT32),
    ("Length",          UINT16),
    ("ReturnStatus",    UINT16, 1),
    ("Reserved",        UINT16, 14),
    ("IgnoreResource",  UINT16, 1)
  ]

# 
# /**
#   Define values for the RscType field of #STM_RSC_DESC_HEADER
#   @{
# **/
# #define END_OF_RESOURCES      0
# #define MEM_RANGE             1
# #define IO_RANGE              2
# #define MMIO_RANGE            3
# #define MACHINE_SPECIFIC_REG  4
# #define PCI_CFG_RANGE         5
# #define TRAPPED_IO_RANGE      6
# #define ALL_RESOURCES         7
# #define REGISTER_VIOLATION    8
# #define MAX_DESC_TYPE         8
END_OF_RESOURCES      = 0
MEM_RANGE             = 1
IO_RANGE              = 2
MMIO_RANGE            = 3
MACHINE_SPECIFIC_REG  = 4
PCI_CFG_RANGE         = 5
TRAPPED_IO_RANGE      = 6
ALL_RESOURCES         = 7
REGISTER_VIOLATION    = 8
MAX_DESC_TYPE         = 8

# /// @}
# 
# /**
#   STM Resource End Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT64                 ResourceListContinuation;
# } STM_RSC_END;
class STM_RSC_END (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                         STM_RSC_DESC_HEADER),
    ("ResourceListContinuation",    UINT64)
  ]

# 
# /**
#   STM Resource Memory Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT64                 Base;
#   UINT64                 Length;
#   UINT32                 RWXAttributes : 3;
#   UINT32                 Reserved      : 29;
#   UINT32                 Reserved_2;
# } STM_RSC_MEM_DESC;
class STM_RSC_MEM_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("Base",            UINT64),
    ("Length",          UINT64),
    ("RWXAttributes",   UINT32, 3),
    ("Reserved",        UINT32, 29),
    ("Reserved_2",      UINT32)
  ]

# 
# /**
#   Define values for the RWXAttributes field of #STM_RSC_MEM_DESC
#   @{
# **/
# #define STM_RSC_MEM_R  0x1
# #define STM_RSC_MEM_W  0x2
# #define STM_RSC_MEM_X  0x4
STM_RSC_MEM_R  = 0x1
STM_RSC_MEM_W  = 0x2
STM_RSC_MEM_X  = 0x4

# /// @}
# 
# /**
#   STM Resource I/O Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT16                 Base;
#   UINT16                 Length;
#   UINT32                 Reserved;
# } STM_RSC_IO_DESC;
class STM_RSC_IO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER),
    ("Base",        UINT16),
    ("Length",      UINT16),
    ("Reserved",    UINT32)
  ]

# 
# /**
#   STM Resource MMIO Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT64                 Base;
#   UINT64                 Length;
#   UINT32                 RWXAttributes : 3;
#   UINT32                 Reserved      : 29;
#   UINT32                 Reserved_2;
# } STM_RSC_MMIO_DESC;
class STM_RSC_MMIO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("Base",            UINT64),
    ("Length",          UINT64),
    ("RWXAttributes",   UINT32, 3),
    ("Reserved",        UINT32, 29),
    ("Reserved_2",      UINT32)
  ]

# 
# /**
#   Define values for the RWXAttributes field of #STM_RSC_MMIO_DESC
#   @{
# **/
# #define STM_RSC_MMIO_R  0x1
# #define STM_RSC_MMIO_W  0x2
# #define STM_RSC_MMIO_X  0x4
STM_RSC_MMIO_R  = 0x1
STM_RSC_MMIO_W  = 0x2
STM_RSC_MMIO_X  = 0x4

# /// @}
# 
# /**
#   STM Resource MSR Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT32                 MsrIndex;
#   UINT32                 KernelModeProcessing : 1;
#   UINT32                 Reserved             : 31;
#   UINT64                 ReadMask;
#   UINT64                 WriteMask;
# } STM_RSC_MSR_DESC;
class STM_RSC_MSR_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                     STM_RSC_DESC_HEADER),
    ("MsrIndex",                UINT32),
    ("KernelModeProcessing",    UINT32, 1),
    ("Reserved",                UINT32, 31),
    ("ReadMask",                UINT64),
    ("WriteMask",               UINT64)
  ]

# 
# /**
#   STM PCI Device Path node used for the PciDevicePath field of
#   #STM_RSC_PCI_CFG_DESC
# **/
# typedef struct {
#   ///
#   /// Must be 1, indicating Hardware Device Path
#   ///
#   UINT8     Type;
#   ///
#   /// Must be 1, indicating PCI
#   ///
#   UINT8     Subtype;
#   ///
#   /// sizeof(STM_PCI_DEVICE_PATH_NODE) which is 6
#   ///
#   UINT16    Length;
#   UINT8     PciFunction;
#   UINT8     PciDevice;
# } STM_PCI_DEVICE_PATH_NODE;
class STM_PCI_DEVICE_PATH_NODE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Type",        UINT8),
    ("Subtype",     UINT8),
    ("Length",      UINT16),
    ("PciFunction", UINT8),
    ("PciDevice",   UINT8)
  ]

# 
# /**
#   STM Resource PCI Configuration Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER         Hdr;
#   UINT16                      RWAttributes : 2;
#   UINT16                      Reserved     : 14;
#   UINT16                      Base;
#   UINT16                      Length;
#   UINT8                       OriginatingBusNumber;
#   UINT8                       LastNodeIndex;
#   STM_PCI_DEVICE_PATH_NODE    PciDevicePath[1];
#   // STM_PCI_DEVICE_PATH_NODE  PciDevicePath[LastNodeIndex + 1];
# } STM_RSC_PCI_CFG_DESC;
class STM_RSC_PCI_CFG_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",                     STM_RSC_DESC_HEADER),
    ("RWAttributes",            UINT16, 2),
    ("Reserved",                UINT16, 14),
    ("Base",                    UINT16),
    ("Length",                  UINT16),
    ("OriginatingBusNumber",    UINT8),
    ("LastNodeIndex",           UINT8),
    ("PciDevicePath",           STM_PCI_DEVICE_PATH_NODE * 1)
    # ("PciDevicePath",           STM_PCI_DEVICE_PATH_NODE * (LastNodeIndex + 1))
  ]

# 
# /**
#   Define values for the RWAttributes field of #STM_RSC_PCI_CFG_DESC
#   @{
# **/
# #define STM_RSC_PCI_CFG_R  0x1
# #define STM_RSC_PCI_CFG_W  0x2
STM_RSC_PCI_CFG_R  = 0x1
STM_RSC_PCI_CFG_W  = 0x2

# /// @}
# 
# /**
#   STM Resource Trapped I/O Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT16                 Base;
#   UINT16                 Length;
#   UINT16                 In        : 1;
#   UINT16                 Out       : 1;
#   UINT16                 Api       : 1;
#   UINT16                 Reserved1 : 13;
#   UINT16                 Reserved2;
# } STM_RSC_TRAPPED_IO_DESC;
class STM_RSC_TRAPPED_IO_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER),
    ("Base",        UINT16),
    ("Length",      UINT16),
    ("In",          UINT16, 1),
    ("Out",         UINT16, 1),
    ("Api",         UINT16, 1),
    ("Reserved1",   UINT16, 13),
    ("Reserved2",   UINT16)
  ]

# 
# /**
#   STM Resource All Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
# } STM_RSC_ALL_RESOURCES_DESC;
class STM_RSC_ALL_RESOURCES_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",         STM_RSC_DESC_HEADER)
  ]

# 
# /**
#   STM Register Violation Descriptor
# **/
# typedef struct {
#   STM_RSC_DESC_HEADER    Hdr;
#   UINT32                 RegisterType;
#   UINT32                 Reserved;
#   UINT64                 ReadMask;
#   UINT64                 WriteMask;
# } STM_REGISTER_VIOLATION_DESC;
class STM_REGISTER_VIOLATION_DESC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hdr",             STM_RSC_DESC_HEADER),
    ("RegisterType",    UINT32),
    ("Reserved",        UINT32),
    ("ReadMask",        UINT64),
    ("WriteMask",       UINT64)
  ]

# 
# /**
#   Enum values for the RWAttributes field of #STM_REGISTER_VIOLATION_DESC
# **/
# typedef enum {
#   StmRegisterCr0,
#   StmRegisterCr2,
#   StmRegisterCr3,
#   StmRegisterCr4,
#   StmRegisterCr8,
#   StmRegisterMax,
# } STM_REGISTER_VIOLATION_TYPE;
StmRegisterCr0 = 0
StmRegisterCr2 = 1
StmRegisterCr3 = 2
StmRegisterCr4 = 3
StmRegisterCr8 = 4
StmRegisterMax = 5
STM_REGISTER_VIOLATION_TYPE = ENUM

# 
# /**
#   Union of all STM resource types
# **/
# typedef union {
#   STM_RSC_DESC_HEADER            Header;
#   STM_RSC_END                    End;
#   STM_RSC_MEM_DESC               Mem;
#   STM_RSC_IO_DESC                Io;
#   STM_RSC_MMIO_DESC              Mmio;
#   STM_RSC_MSR_DESC               Msr;
#   STM_RSC_PCI_CFG_DESC           PciCfg;
#   STM_RSC_TRAPPED_IO_DESC        TrappedIo;
#   STM_RSC_ALL_RESOURCES_DESC     All;
#   STM_REGISTER_VIOLATION_DESC    RegisterViolation;
# } STM_RSC;
class STM_RSC (Union):
  _pack_   = 1
  _fields_ = [
    ("Header",              STM_RSC_DESC_HEADER),
    ("End",                 STM_RSC_END),
    ("Mem",                 STM_RSC_MEM_DESC),
    ("Io",                  STM_RSC_IO_DESC),
    ("Mmio",                STM_RSC_MMIO_DESC),
    ("Msr",                 STM_RSC_MSR_DESC),
    ("PciCfg",              STM_RSC_PCI_CFG_DESC),
    ("TrappedIo",           STM_RSC_TRAPPED_IO_DESC),
    ("All",                 STM_RSC_ALL_RESOURCES_DESC),
    ("RegisterViolation",   STM_REGISTER_VIOLATION_DESC)
  ]

# 
# #pragma pack ()
# 
# #endif
# 