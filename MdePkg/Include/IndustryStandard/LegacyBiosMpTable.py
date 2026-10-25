# /** @file
#   Defives data structures per MultiProcessor Specification Ver 1.4.
# 
#   The MultiProcessor Specification defines an enhancement to the standard
#   to which PC manufacturers design DOS-compatible systems.
# 
# Copyright (c) 2007 - 2018, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# LegacyBiosMpTable.py
#
# EfiPy2.MdePkg.IndustryStandard.LegacyBiosMpTable
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _LEGACY_BIOS_MPTABLE_H_
# #define _LEGACY_BIOS_MPTABLE_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #define EFI_LEGACY_MP_TABLE_REV_1_4  0x04
EFI_LEGACY_MP_TABLE_REV_1_4 = 0x04

# 
# //
# // Define MP table structures. All are packed.
# //
# #pragma pack(1)
# 
# #define EFI_LEGACY_MP_TABLE_FLOATING_POINTER_SIGNATURE  SIGNATURE_32 ('_', 'M', 'P', '_')
EFI_LEGACY_MP_TABLE_FLOATING_POINTER_SIGNATURE  = SIGNATURE_32 ('_', 'M', 'P', '_')
# typedef struct {
#   UINT32    Reserved1  : 6;
#   UINT32    MutipleClk : 1;
#   UINT32    Imcr       : 1;
#   UINT32    Reserved2  : 24;
# } FEATUREBYTE2_5;
class FEATUREBYTE2_5 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved1",   UINT32, 6),
    ("MutipleClk",  UINT32, 1),
    ("Imcr",        UINT32, 1),
    ("Reserved2",   UINT32, 24)
  ]

# 
# typedef struct {
#   UINT32            Signature;
#   UINT32            PhysicalAddress;
#   UINT8             Length;
#   UINT8             SpecRev;
#   UINT8             Checksum;
#   UINT8             FeatureByte1;
#   FEATUREBYTE2_5    FeatureByte2_5;
# } EFI_LEGACY_MP_TABLE_FLOATING_POINTER;
class EFI_LEGACY_MP_TABLE_FLOATING_POINTER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("PhysicalAddress", UINT32),
    ("Length",          UINT8),
    ("SpecRev",         UINT8),
    ("Checksum",        UINT8),
    ("FeatureByte1",    UINT8),
    ("FeatureByte2_5",  FEATUREBYTE2_5)
  ]

# 
# #define EFI_LEGACY_MP_TABLE_HEADER_SIGNATURE  SIGNATURE_32 ('P', 'C', 'M', 'P')
EFI_LEGACY_MP_TABLE_HEADER_SIGNATURE  = SIGNATURE_32 ('P', 'C', 'M', 'P')

# typedef struct {
#   UINT32    Signature;
#   UINT16    BaseTableLength;
#   UINT8     SpecRev;
#   UINT8     Checksum;
#   CHAR8     OemId[8];
#   CHAR8     OemProductId[12];
#   UINT32    OemTablePointer;
#   UINT16    OemTableSize;
#   UINT16    EntryCount;
#   UINT32    LocalApicAddress;
#   UINT16    ExtendedTableLength;
#   UINT8     ExtendedChecksum;
#   UINT8     Reserved;
# } EFI_LEGACY_MP_TABLE_HEADER;
class EFI_LEGACY_MP_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT32),
    ("BaseTableLength",     UINT16),
    ("SpecRev",             UINT8),
    ("Checksum",            UINT8),
    ("OemId",               CHAR8 * 8),
    ("OemProductId",        CHAR8 * 12),
    ("OemTablePointer",     UINT32),
    ("OemTableSize",        UINT16),
    ("EntryCount",          UINT16),
    ("LocalApicAddress",    UINT32),
    ("ExtendedTableLength", UINT16),
    ("ExtendedChecksum",    UINT8),
    ("Reserved",            UINT8)
  ]

# 
# typedef struct {
#   UINT8    EntryType;
# } EFI_LEGACY_MP_TABLE_ENTRY_TYPE;
class EFI_LEGACY_MP_TABLE_ENTRY_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8)
  ]

# 
# //
# // Entry Type 0: Processor.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_TYPE_PROCESSOR  0x00
EFI_LEGACY_MP_TABLE_ENTRY_TYPE_PROCESSOR  = 0x00
# typedef struct {
#   UINT8    Enabled  : 1;
#   UINT8    Bsp      : 1;
#   UINT8    Reserved : 6;
# } EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS;
class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Enabled",   UINT8, 1),
    ("Bsp",       UINT8, 1),
    ("Reserved",  UINT8, 6)
  ]

# 
# typedef struct {
#   UINT32    Stepping : 4;
#   UINT32    Model    : 4;
#   UINT32    Family   : 4;
#   UINT32    Reserved : 20;
# } EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE;
class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Stepping",  UINT32, 4),
    ("Model",     UINT32, 4),
    ("Family",    UINT32, 4),
    ("Reserved",  UINT32, 20)
  ]

# 
# typedef struct {
#   UINT32    Fpu       : 1;
#   UINT32    Reserved1 : 6;
#   UINT32    Mce       : 1;
#   UINT32    Cx8       : 1;
#   UINT32    Apic      : 1;
#   UINT32    Reserved2 : 22;
# } EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES;
class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fpu",       UINT32, 1),
    ("Reserved1", UINT32, 6),
    ("Mce",       UINT32, 1),
    ("Cx8",       UINT32, 1),
    ("Apic",      UINT32, 1),
    ("Reserved2", UINT32, 22)
  ]

# 
# typedef struct {
#   UINT8                                            EntryType;
#   UINT8                                            Id;
#   UINT8                                            Ver;
#   EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS        Flags;
#   EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE    Signature;
#   EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES     Features;
#   UINT32                                           Reserved1;
#   UINT32                                           Reserved2;
# } EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR;
class EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Id",        UINT8),
    ("Ver",       UINT8),
    ("Flags",     EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FLAGS),
    ("Signature", EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_SIGNATURE),
    ("Features",  EFI_LEGACY_MP_TABLE_ENTRY_PROCESSOR_FEATURES),
    ("Reserved1", UINT32),
    ("Reserved2", UINT32)
  ]

# 
# //
# // Entry Type 1: Bus.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_TYPE_BUS  0x01
EFI_LEGACY_MP_TABLE_ENTRY_TYPE_BUS  = 0x01

# typedef struct {
#   UINT8    EntryType;
#   UINT8    Id;
#   CHAR8    TypeString[6];
# } EFI_LEGACY_MP_TABLE_ENTRY_BUS;
class EFI_LEGACY_MP_TABLE_ENTRY_BUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",   UINT8),
    ("Id",          UINT8),
    ("TypeString",  UINT8 * 6)
  ]

# 
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUS    "CBUS  " // Corollary CBus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUSII  "CBUSII" // Corollary CBUS II
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_EISA    "EISA  " // Extended ISA
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_FUTURE  "FUTURE" // IEEE FutureBus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_INTERN  "INTERN" // Internal bus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_ISA     "ISA   " // Industry Standard Architecture
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBI     "MBI   " // Multibus I
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBII    "MBII  " // Multibus II
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MCA     "MCA   " // Micro Channel Architecture
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPI     "MPI   " // MPI
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPSA    "MPSA  " // MPSA
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_NUBUS   "NUBUS " // Apple Macintosh NuBus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCI     "PCI   " // Peripheral Component Interconnect
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCMCIA  "PCMCIA" // PC Memory Card International Assoc.
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_TC      "TC    " // DEC TurboChannel
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VL      "VL    " // VESA Local Bus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VME     "VME   " // VMEbus
# #define EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_XPRESS  "XPRESS" // Express System Bus
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUS   = b"CBUS  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_CBUSII = b"CBUSII"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_EISA   = b"EISA  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_FUTURE = b"FUTURE"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_INTERN = b"INTERN"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_ISA    = b"ISA   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBI    = b"MBI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MBII   = b"MBII  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MCA    = b"MCA   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPI    = b"MPI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_MPSA   = b"MPSA  "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_NUBUS  = b"NUBUS "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCI    = b"PCI   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_PCMCIA = b"PCMCIA"
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_TC     = b"TC    "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VL     = b"VL    "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_VME    = b"VME   "
EFI_LEGACY_MP_TABLE_ENTRY_BUS_STRING_XPRESS = b"XPRESS"

# //
# // Entry Type 2: I/O APIC.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IOAPIC  0x02
EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IOAPIC = 0x02

# typedef struct {
#   UINT8    Enabled  : 1;
#   UINT8    Reserved : 7;
# } EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS;
class EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Enabled",   UINT8, 1),
    ("Reserved",  UINT8, 7)
  ]

# 
# typedef struct {
#   UINT8                                     EntryType;
#   UINT8                                     Id;
#   UINT8                                     Ver;
#   EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS    Flags;
#   UINT32                                    Address;
# } EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC;
class EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Id",        UINT8),
    ("Ver",       UINT8),
    ("Flags",     EFI_LEGACY_MP_TABLE_ENTRY_IOAPIC_FLAGS),
    ("Address",   UINT32)
  ]

# 
# //
# // Entry Type 3: I/O Interrupt Assignment.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IO_INT  0x03
EFI_LEGACY_MP_TABLE_ENTRY_TYPE_IO_INT = 0x03

# typedef struct {
#   UINT16    Polarity : 2;
#   UINT16    Trigger  : 2;
#   UINT16    Reserved : 12;
# } EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS;
class EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Polarity",  UINT16, 2),
    ("Trigger",   UINT16, 2),
    ("Reserved",  UINT16, 12)
  ]

# 
# typedef struct {
#   UINT8    IntNo    : 2;
#   UINT8    Dev      : 5;
#   UINT8    Reserved : 1;
# } EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS;
class EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("IntNo",     UINT16, 2),
    ("Dev",       UINT16, 5),
    ("Reserved",  UINT16, 1)
  ]

# 
# typedef union {
#   EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS    fields;
#   UINT8                                   byte;
# } EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ;
class EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("fields",  EFI_LEGACY_MP_TABLE_ENTRY_INT_FIELDS),
    ("byte",    UINT8)
  ]

# 
# typedef struct {
#   UINT8                                           EntryType;
#   UINT8                                           IntType;
#   EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS             Flags;
#   UINT8                                           SourceBusId;
#   EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ    SourceBusIrq;
#   UINT8                                           DestApicId;
#   UINT8                                           DestApicIntIn;
# } EFI_LEGACY_MP_TABLE_ENTRY_IO_INT;
class EFI_LEGACY_MP_TABLE_ENTRY_IO_INT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("IntType",       UINT8),
    ("Flags",         EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS),
    ("SourceBusId",   UINT8),
    ("SourceBusIrq",  UINT8),
    ("DestApicId",    EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ),
    ("DestApicIntIn", UINT8)
  ]

# 
# typedef enum {
#   EfiLegacyMpTableEntryIoIntTypeInt    = 0,
#   EfiLegacyMpTableEntryIoIntTypeNmi    = 1,
#   EfiLegacyMpTableEntryIoIntTypeSmi    = 2,
#   EfiLegacyMpTableEntryIoIntTypeExtInt = 3,
# } EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_TYPE;
EfiLegacyMpTableEntryIoIntTypeInt   = 0
EfiLegacyMpTableEntryIoIntTypeNmi   = 1
EfiLegacyMpTableEntryIoIntTypeSmi   = 2
EfiLegacyMpTableEntryIoIntTypeExtInt= 3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_TYPE = ENUM

# 
# typedef enum {
#   EfiLegacyMpTableEntryIoIntFlagsPolaritySpec       = 0x0,
#   EfiLegacyMpTableEntryIoIntFlagsPolarityActiveHigh = 0x1,
#   EfiLegacyMpTableEntryIoIntFlagsPolarityReserved   = 0x2,
#   EfiLegacyMpTableEntryIoIntFlagsPolarityActiveLow  = 0x3,
# } EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_POLARITY;
EfiLegacyMpTableEntryIoIntFlagsPolaritySpec       = 0x0
EfiLegacyMpTableEntryIoIntFlagsPolarityActiveHigh = 0x1
EfiLegacyMpTableEntryIoIntFlagsPolarityReserved   = 0x2
EfiLegacyMpTableEntryIoIntFlagsPolarityActiveLow  = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_POLARITY = ENUM

# 
# typedef enum {
#   EfiLegacyMpTableEntryIoIntFlagsTriggerSpec     = 0x0,
#   EfiLegacyMpTableEntryIoIntFlagsTriggerEdge     = 0x1,
#   EfiLegacyMpTableEntryIoIntFlagsTriggerReserved = 0x2,
#   EfiLegacyMpTableEntryIoIntFlagsTriggerLevel    = 0x3,
# } EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_TRIGGER;
EfiLegacyMpTableEntryIoIntFlagsTriggerSpec        = 0x0
EfiLegacyMpTableEntryIoIntFlagsTriggerEdge        = 0x1
EfiLegacyMpTableEntryIoIntFlagsTriggerReserved    = 0x2
EfiLegacyMpTableEntryIoIntFlagsTriggerLevel       = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_IO_INT_FLAGS_TRIGGER = ENUM

# 
# //
# // Entry Type 4: Local Interrupt Assignment.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_TYPE_LOCAL_INT  0x04
EFI_LEGACY_MP_TABLE_ENTRY_TYPE_LOCAL_INT  = 0x04

# typedef struct {
#   UINT8                                           EntryType;
#   UINT8                                           IntType;
#   EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS             Flags;
#   UINT8                                           SourceBusId;
#   EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ    SourceBusIrq;
#   UINT8                                           DestApicId;
#   UINT8                                           DestApicIntIn;
# } EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT;
class EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("IntType",       UINT8),
    ("Flags",         EFI_LEGACY_MP_TABLE_ENTRY_INT_FLAGS),
    ("SourceBusId",   UINT8),
    ("SourceBusIrq",  EFI_LEGACY_MP_TABLE_ENTRY_INT_SOURCE_BUS_IRQ ),
    ("DestApicId",    UINT8),
    ("DestApicIntIn", UINT8)
  ]

# 
# typedef enum {
#   EfiLegacyMpTableEntryLocalIntTypeInt    = 0,
#   EfiLegacyMpTableEntryLocalIntTypeNmi    = 1,
#   EfiLegacyMpTableEntryLocalIntTypeSmi    = 2,
#   EfiLegacyMpTableEntryLocalIntTypeExtInt = 3,
# } EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_TYPE;
EfiLegacyMpTableEntryLocalIntTypeInt              = 0
EfiLegacyMpTableEntryLocalIntTypeNmi              = 1
EfiLegacyMpTableEntryLocalIntTypeSmi              = 2
EfiLegacyMpTableEntryLocalIntTypeExtInt           = 3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_TYPE = ENUM

# 
# typedef enum {
#   EfiLegacyMpTableEntryLocalIntFlagsPolaritySpec       = 0x0,
#   EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveHigh = 0x1,
#   EfiLegacyMpTableEntryLocalIntFlagsPolarityReserved   = 0x2,
#   EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveLow  = 0x3,
# } EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_POLARITY;
EfiLegacyMpTableEntryLocalIntFlagsPolaritySpec      = 0x0
EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveHigh= 0x1
EfiLegacyMpTableEntryLocalIntFlagsPolarityReserved  = 0x2
EfiLegacyMpTableEntryLocalIntFlagsPolarityActiveLow = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_POLARITY = ENUM

# 
# typedef enum {
#   EfiLegacyMpTableEntryLocalIntFlagsTriggerSpec     = 0x0,
#   EfiLegacyMpTableEntryLocalIntFlagsTriggerEdge     = 0x1,
#   EfiLegacyMpTableEntryLocalIntFlagsTriggerReserved = 0x2,
#   EfiLegacyMpTableEntryLocalIntFlagsTriggerLevel    = 0x3,
# } EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_TRIGGER;
EfiLegacyMpTableEntryLocalIntFlagsTriggerSpec       = 0x0
EfiLegacyMpTableEntryLocalIntFlagsTriggerEdge       = 0x1
EfiLegacyMpTableEntryLocalIntFlagsTriggerReserved   = 0x2
EfiLegacyMpTableEntryLocalIntFlagsTriggerLevel      = 0x3
EFI_LEGACY_MP_TABLE_ENTRY_LOCAL_INT_FLAGS_TRIGGER = ENUM

# 
# //
# // Entry Type 128: System Address Space Mapping.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_SYS_ADDR_SPACE_MAPPING  0x80
EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_SYS_ADDR_SPACE_MAPPING = 0x80

# typedef struct {
#   UINT8     EntryType;
#   UINT8     Length;
#   UINT8     BusId;
#   UINT8     AddressType;
#   UINT64    AddressBase;
#   UINT64    AddressLength;
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING;
class EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",     UINT8),
    ("Length",        UINT8),
    ("BusId",         UINT8),
    ("AddressType",   UINT8),
    ("AddressBase",   UINT64),
    ("AddressLength", UINT64)
  ]

# 
# typedef enum {
#   EfiLegacyMpTableEntryExtSysAddrSpaceMappingIo       = 0,
#   EfiLegacyMpTableEntryExtSysAddrSpaceMappingMemory   = 1,
#   EfiLegacyMpTableEntryExtSysAddrSpaceMappingPrefetch = 2,
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING_TYPE;
EfiLegacyMpTableEntryExtSysAddrSpaceMappingIo       = 0
EfiLegacyMpTableEntryExtSysAddrSpaceMappingMemory   = 1
EfiLegacyMpTableEntryExtSysAddrSpaceMappingPrefetch = 2
EFI_LEGACY_MP_TABLE_ENTRY_EXT_SYS_ADDR_SPACE_MAPPING_TYPE = ENUM

# 
# //
# // Entry Type 129: Bus Hierarchy.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_BUS_HIERARCHY  0x81
EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_BUS_HIERARCHY  = 0x81

# typedef struct {
#   UINT8    SubtractiveDecode : 1;
#   UINT8    Reserved          : 7;
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO;
class EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SubtractiveDecode", UINT8, 1),
    ("Reserved",          UINT8, 7)
  ]

# 
# typedef struct {
#   UINT8                                                  EntryType;
#   UINT8                                                  Length;
#   UINT8                                                  BusId;
#   EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO    BusInfo;
#   UINT8                                                  ParentBus;
#   UINT8                                                  Reserved1;
#   UINT8                                                  Reserved2;
#   UINT8                                                  Reserved3;
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY;
class EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType", UINT8),
    ("Length",    UINT8),
    ("BusId",     UINT8),
    ("BusInfo",   EFI_LEGACY_MP_TABLE_ENTRY_EXT_BUS_HIERARCHY_BUSINFO),
    ("ParentBus", UINT8),
    ("Reserved1", UINT8),
    ("Reserved2", UINT8),
    ("Reserved3", UINT8)
  ]

# 
# //
# // Entry Type 130: Compatibility Bus Address Space Modifier.
# //
# #define EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_COMPAT_BUS_ADDR_SPACE_MODIFIER  0x82
EFI_LEGACY_MP_TABLE_ENTRY_EXT_TYPE_COMPAT_BUS_ADDR_SPACE_MODIFIER = 0x82

# typedef struct {
#   UINT8    RangeMode : 1;
#   UINT8    Reserved  : 7;
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE;
class EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("RangeMode", UINT8, 1),
    ("Reserved",  UINT8, 7)
  ]

# 
# typedef struct {
#   UINT8                                                                     EntryType;
#   UINT8                                                                     Length;
#   UINT8                                                                     BusId;
#   EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE    AddrMode;
#   UINT32                                                                    PredefinedRangeList;
# } EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER;
class EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("EntryType",           UINT8),
    ("Length",              UINT8),
    ("BusId",               UINT8),
    ("AddrMode",            EFI_LEGACY_MP_TABLE_ENTRY_EXT_COMPAT_BUS_ADDR_SPACE_MODIFIER_ADDR_MODE),
    ("PredefinedRangeList", UINT32)
  ]

# 
# #pragma pack()
# 
# #endif
# 