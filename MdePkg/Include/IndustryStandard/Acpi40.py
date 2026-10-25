# /** @file
#   ACPI 4.0 definitions from the ACPI Specification Revision 4.0a April 5, 2010
# 
#   Copyright (c) 2010 - 2022, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
#
# Acpi40.py
#
# EfiPy2.MdePkg.IndustryStandard.Acpi40
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _ACPI_4_0_H_
# #define _ACPI_4_0_H_
# 
# #include <IndustryStandard/Acpi30.h>
# 
from EfiPy2.MdePkg.IndustryStandard.Acpi30 import *

# //
# // Ensure proper structure formats
# //
# #pragma pack(1)
# 
# ///
# /// ACPI 4.0 Generic Address Space definition
# ///
# typedef struct {
#   UINT8     AddressSpaceId;
#   UINT8     RegisterBitWidth;
#   UINT8     RegisterBitOffset;
#   UINT8     AccessSize;
#   UINT64    Address;
# } EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE;
# 
EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE = EFI_ACPI_3_0_GENERIC_ADDRESS_STRUCTURE

# //
# // Generic Address Space Address IDs
# //
# #define EFI_ACPI_4_0_SYSTEM_MEMORY              0
EFI_ACPI_4_0_SYSTEM_MEMORY              = 0
# #define EFI_ACPI_4_0_SYSTEM_IO                  1
EFI_ACPI_4_0_SYSTEM_IO                  = 1
# #define EFI_ACPI_4_0_PCI_CONFIGURATION_SPACE    2
EFI_ACPI_4_0_PCI_CONFIGURATION_SPACE    = 2
# #define EFI_ACPI_4_0_EMBEDDED_CONTROLLER        3
EFI_ACPI_4_0_EMBEDDED_CONTROLLER        = 3
# #define EFI_ACPI_4_0_SMBUS                      4
EFI_ACPI_4_0_SMBUS                      = 4
# #define EFI_ACPI_4_0_FUNCTIONAL_FIXED_HARDWARE  0x7F
EFI_ACPI_4_0_FUNCTIONAL_FIXED_HARDWARE  = 0x7F
# 

# //
# // Generic Address Space Access Sizes
# //
# #define EFI_ACPI_4_0_UNDEFINED  0
EFI_ACPI_4_0_UNDEFINED  = 0
# #define EFI_ACPI_4_0_BYTE       1
EFI_ACPI_4_0_BYTE       = 1
# #define EFI_ACPI_4_0_WORD       2
EFI_ACPI_4_0_WORD       = 2
# #define EFI_ACPI_4_0_DWORD      3
EFI_ACPI_4_0_DWORD      = 3
# #define EFI_ACPI_4_0_QWORD      4
EFI_ACPI_4_0_QWORD      = 4
# 

# //
# // ACPI 4.0 table structures
# //
# 
# ///
# /// Root System Description Pointer Structure
# ///
# typedef struct {
#   UINT64    Signature;
#   UINT8     Checksum;
#   UINT8     OemId[6];
#   UINT8     Revision;
#   UINT32    RsdtAddress;
#   UINT32    Length;
#   UINT64    XsdtAddress;
#   UINT8     ExtendedChecksum;
#   UINT8     Reserved[3];
# } EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER;
# 
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER

# ///
# /// RSD_PTR Revision (as defined in ACPI 4.0b spec.)
# ///
# #define EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION  0x02 ///< ACPISpec (Revision 4.0a) says current value is 2
# 
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_REVISION = 0x02

# ///
# /// Common table header, this prefaces all ACPI tables, including FACS, but
# /// excluding the RSD PTR structure
# ///
# typedef struct {
#   UINT32    Signature;
#   UINT32    Length;
# } EFI_ACPI_4_0_COMMON_HEADER;
# 
EFI_ACPI_4_0_COMMON_HEADER = EFI_ACPI_3_0_COMMON_HEADER

# //
# // Root System Description Table
# // No definition needed as it is a common description table header, the same with
# // EFI_ACPI_DESCRIPTION_HEADER, followed by a variable number of UINT32 table pointers.
# //
# 
# ///
# /// RSDT Revision (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

# //
# // Extended System Description Table
# // No definition needed as it is a common description table header, the same with
# // EFI_ACPI_DESCRIPTION_HEADER, followed by a variable number of UINT64 table pointers.
# //
# 
# ///
# /// XSDT Revision (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_REVISION = 0x01

# ///
# /// Fixed ACPI Description Table Structure (FADT)
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   UINT32                                    FirmwareCtrl;
#   UINT32                                    Dsdt;
#   UINT8                                     Reserved0;
#   UINT8                                     PreferredPmProfile;
#   UINT16                                    SciInt;
#   UINT32                                    SmiCmd;
#   UINT8                                     AcpiEnable;
#   UINT8                                     AcpiDisable;
#   UINT8                                     S4BiosReq;
#   UINT8                                     PstateCnt;
#   UINT32                                    Pm1aEvtBlk;
#   UINT32                                    Pm1bEvtBlk;
#   UINT32                                    Pm1aCntBlk;
#   UINT32                                    Pm1bCntBlk;
#   UINT32                                    Pm2CntBlk;
#   UINT32                                    PmTmrBlk;
#   UINT32                                    Gpe0Blk;
#   UINT32                                    Gpe1Blk;
#   UINT8                                     Pm1EvtLen;
#   UINT8                                     Pm1CntLen;
#   UINT8                                     Pm2CntLen;
#   UINT8                                     PmTmrLen;
#   UINT8                                     Gpe0BlkLen;
#   UINT8                                     Gpe1BlkLen;
#   UINT8                                     Gpe1Base;
#   UINT8                                     CstCnt;
#   UINT16                                    PLvl2Lat;
#   UINT16                                    PLvl3Lat;
#   UINT16                                    FlushSize;
#   UINT16                                    FlushStride;
#   UINT8                                     DutyOffset;
#   UINT8                                     DutyWidth;
#   UINT8                                     DayAlrm;
#   UINT8                                     MonAlrm;
#   UINT8                                     Century;
#   UINT16                                    IaPcBootArch;
#   UINT8                                     Reserved1;
#   UINT32                                    Flags;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    ResetReg;
#   UINT8                                     ResetValue;
#   UINT8                                     Reserved2[3];
#   UINT64                                    XFirmwareCtrl;
#   UINT64                                    XDsdt;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPm1aEvtBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPm1bEvtBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPm1aCntBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPm1bCntBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPm2CntBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XPmTmrBlk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XGpe0Blk;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    XGpe1Blk;
# } EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE;
# 
EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE = EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE

# ///
# /// FADT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  0x04
# 
EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_REVISION  = 0x04

# //
# // Fixed ACPI Description Table Preferred Power Management Profile
# //
# #define EFI_ACPI_4_0_PM_PROFILE_UNSPECIFIED         0
EFI_ACPI_4_0_PM_PROFILE_UNSPECIFIED         = 0
# #define EFI_ACPI_4_0_PM_PROFILE_DESKTOP             1
EFI_ACPI_4_0_PM_PROFILE_DESKTOP             = 1
# #define EFI_ACPI_4_0_PM_PROFILE_MOBILE              2
EFI_ACPI_4_0_PM_PROFILE_MOBILE              = 2
# #define EFI_ACPI_4_0_PM_PROFILE_WORKSTATION         3
EFI_ACPI_4_0_PM_PROFILE_WORKSTATION         = 3
# #define EFI_ACPI_4_0_PM_PROFILE_ENTERPRISE_SERVER   4
EFI_ACPI_4_0_PM_PROFILE_ENTERPRISE_SERVER   = 4
# #define EFI_ACPI_4_0_PM_PROFILE_SOHO_SERVER         5
EFI_ACPI_4_0_PM_PROFILE_SOHO_SERVER         = 5
# #define EFI_ACPI_4_0_PM_PROFILE_APPLIANCE_PC        6
EFI_ACPI_4_0_PM_PROFILE_APPLIANCE_PC        = 6
# #define EFI_ACPI_4_0_PM_PROFILE_PERFORMANCE_SERVER  7
EFI_ACPI_4_0_PM_PROFILE_PERFORMANCE_SERVER  = 7
# 

# //
# // Fixed ACPI Description Table Boot Architecture Flags
# // All other bits are reserved and must be set to 0.
# //
# #define EFI_ACPI_4_0_LEGACY_DEVICES      BIT0
EFI_ACPI_4_0_LEGACY_DEVICES              = BIT0
# #define EFI_ACPI_4_0_8042                BIT1
EFI_ACPI_4_0_8042                        = BIT1
# #define EFI_ACPI_4_0_VGA_NOT_PRESENT     BIT2
EFI_ACPI_4_0_VGA_NOT_PRESENT             = BIT2
# #define EFI_ACPI_4_0_MSI_NOT_SUPPORTED   BIT3
EFI_ACPI_4_0_MSI_NOT_SUPPORTED           = BIT3
# #define EFI_ACPI_4_0_PCIE_ASPM_CONTROLS  BIT4
EFI_ACPI_4_0_PCIE_ASPM_CONTROLS          = BIT4
# 

# //
# // Fixed ACPI Description Table Fixed Feature Flags
# // All other bits are reserved and must be set to 0.
# //
# #define EFI_ACPI_4_0_WBINVD                                BIT0
EFI_ACPI_4_0_WBINVD                                 = BIT0
# #define EFI_ACPI_4_0_WBINVD_FLUSH                          BIT1
EFI_ACPI_4_0_WBINVD_FLUSH                           = BIT1
# #define EFI_ACPI_4_0_PROC_C1                               BIT2
EFI_ACPI_4_0_PROC_C1                                = BIT2
# #define EFI_ACPI_4_0_P_LVL2_UP                             BIT3
EFI_ACPI_4_0_P_LVL2_UP                              = BIT3
# #define EFI_ACPI_4_0_PWR_BUTTON                            BIT4
EFI_ACPI_4_0_PWR_BUTTON                             = BIT4
# #define EFI_ACPI_4_0_SLP_BUTTON                            BIT5
EFI_ACPI_4_0_SLP_BUTTON                             = BIT5
# #define EFI_ACPI_4_0_FIX_RTC                               BIT6
EFI_ACPI_4_0_FIX_RTC                                = BIT6
# #define EFI_ACPI_4_0_RTC_S4                                BIT7
EFI_ACPI_4_0_RTC_S4                                 = BIT7
# #define EFI_ACPI_4_0_TMR_VAL_EXT                           BIT8
EFI_ACPI_4_0_TMR_VAL_EXT                            = BIT8
# #define EFI_ACPI_4_0_DCK_CAP                               BIT9
EFI_ACPI_4_0_DCK_CAP                                = BIT9
# #define EFI_ACPI_4_0_RESET_REG_SUP                         BIT10
EFI_ACPI_4_0_RESET_REG_SUP                          = BIT10
# #define EFI_ACPI_4_0_SEALED_CASE                           BIT11
EFI_ACPI_4_0_SEALED_CASE                            = BIT11
# #define EFI_ACPI_4_0_HEADLESS                              BIT12
EFI_ACPI_4_0_HEADLESS                               = BIT12
# #define EFI_ACPI_4_0_CPU_SW_SLP                            BIT13
EFI_ACPI_4_0_CPU_SW_SLP                             = BIT13
# #define EFI_ACPI_4_0_PCI_EXP_WAK                           BIT14
EFI_ACPI_4_0_PCI_EXP_WAK                            = BIT14
# #define EFI_ACPI_4_0_USE_PLATFORM_CLOCK                    BIT15
EFI_ACPI_4_0_USE_PLATFORM_CLOCK                     = BIT15
# #define EFI_ACPI_4_0_S4_RTC_STS_VALID                      BIT16
EFI_ACPI_4_0_S4_RTC_STS_VALID                       = BIT16
# #define EFI_ACPI_4_0_REMOTE_POWER_ON_CAPABLE               BIT17
EFI_ACPI_4_0_REMOTE_POWER_ON_CAPABLE                = BIT17
# #define EFI_ACPI_4_0_FORCE_APIC_CLUSTER_MODEL              BIT18
EFI_ACPI_4_0_FORCE_APIC_CLUSTER_MODEL               = BIT18
# #define EFI_ACPI_4_0_FORCE_APIC_PHYSICAL_DESTINATION_MODE  BIT19
EFI_ACPI_4_0_FORCE_APIC_PHYSICAL_DESTINATION_MODE   = BIT19
# 

# ///
# /// Firmware ACPI Control Structure
# ///
# typedef struct {
#   UINT32    Signature;
#   UINT32    Length;
#   UINT32    HardwareSignature;
#   UINT32    FirmwareWakingVector;
#   UINT32    GlobalLock;
#   UINT32    Flags;
#   UINT64    XFirmwareWakingVector;
#   UINT8     Version;
#   UINT8     Reserved0[3];
#   UINT32    OspmFlags;
#   UINT8     Reserved1[24];
# } EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE;
# 
class EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",             UINT32),
    ("Length",                UINT32),
    ("HardwareSignature",     UINT32),
    ("FirmwareWakingVector",  UINT32),
    ("GlobalLock",            UINT32),
    ("Flags",                 UINT32),
    ("XFirmwareWakingVector", UINT64),
    ("Version",               UINT8),
    ("Reserved0",             UINT8 * 3),
    ("OspmFlags",             UINT32),
    ("Reserved1",             UINT8 * 24),
  ]

# ///
# /// FACS Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  0x02
# 
EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_VERSION  = 0x02

# ///
# /// Firmware Control Structure Feature Flags
# /// All other bits are reserved and must be set to 0.
# ///
# #define EFI_ACPI_4_0_S4BIOS_F                BIT0
# #define EFI_ACPI_4_0_64BIT_WAKE_SUPPORTED_F  BIT1
# 
EFI_ACPI_4_0_S4BIOS_F                     = BIT0
EFI_ACPI_4_0_64BIT_WAKE_SUPPORTED_F       = BIT1

# ///
# /// OSPM Enabled Firmware Control Structure Flags
# /// All other bits are reserved and must be set to 0.
# ///
# #define EFI_ACPI_4_0_OSPM_64BIT_WAKE__F  BIT0
# 
EFI_ACPI_4_0_OSPM_64BIT_WAKE__F           = BIT0

# //
# // Differentiated System Description Table,
# // Secondary System Description Table
# // and Persistent System Description Table,
# // no definition needed as they are common description table header, the same with
# // EFI_ACPI_DESCRIPTION_HEADER, followed by a definition block.
# //
# #define EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION  0x02
# #define EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION       0x02
# 
EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_REVISION   = 0x02
EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_REVISION        = 0x02

# ///
# /// Multiple APIC Description Table header definition.  The rest of the table
# /// must be defined in a platform specific manner.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         LocalApicAddress;
#   UINT32                         Flags;
# } EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER;
# 
EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER = EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_HEADER

# ///
# /// MADT Revision (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION  0x03
# 
EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_REVISION = 0x03

# ///
# /// Multiple APIC Flags
# /// All other bits are reserved and must be set to 0.
# ///
# #define EFI_ACPI_4_0_PCAT_COMPAT  BIT0
# 
EFI_ACPI_4_0_PCAT_COMPAT         = BIT0

# //
# // Multiple APIC Description Table APIC structure types
# // All other values between 0x0B an 0xFF are reserved and
# // will be ignored by OSPM.
# //
# #define EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC           0x00
EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC           = 0x00
# #define EFI_ACPI_4_0_IO_APIC                        0x01
EFI_ACPI_4_0_IO_APIC                        = 0x01
# #define EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE      0x02
EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE      = 0x02
# #define EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE  0x03
EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE  = 0x03
# #define EFI_ACPI_4_0_LOCAL_APIC_NMI                 0x04
EFI_ACPI_4_0_LOCAL_APIC_NMI                 = 0x04
# #define EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE    0x05
EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE    = 0x05
# #define EFI_ACPI_4_0_IO_SAPIC                       0x06
EFI_ACPI_4_0_IO_SAPIC                       = 0x06
# #define EFI_ACPI_4_0_LOCAL_SAPIC                    0x07
EFI_ACPI_4_0_LOCAL_SAPIC                    = 0x07
# #define EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES     0x08
EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES     = 0x08
# #define EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC         0x09
EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC         = 0x09
# #define EFI_ACPI_4_0_LOCAL_X2APIC_NMI               0x0A
EFI_ACPI_4_0_LOCAL_X2APIC_NMI               = 0x0A
# 

# //
# // APIC Structure Definitions
# //
# 
# ///
# /// Processor Local APIC Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     AcpiProcessorId;
#   UINT8     ApicId;
#   UINT32    Flags;
# } EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_STRUCTURE;
# 
EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_STRUCTURE = EFI_ACPI_3_0_PROCESSOR_LOCAL_APIC_STRUCTURE

# ///
# /// Local APIC Flags.  All other bits are reserved and must be 0.
# ///
# #define EFI_ACPI_4_0_LOCAL_APIC_ENABLED  BIT0
# 
EFI_ACPI_4_0_LOCAL_APIC_ENABLED        = BIT0

# ///
# /// IO APIC Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     IoApicId;
#   UINT8     Reserved;
#   UINT32    IoApicAddress;
#   UINT32    GlobalSystemInterruptBase;
# } EFI_ACPI_4_0_IO_APIC_STRUCTURE;
# 
EFI_ACPI_4_0_IO_APIC_STRUCTURE = EFI_ACPI_3_0_IO_APIC_STRUCTURE

# ///
# /// Interrupt Source Override Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     Bus;
#   UINT8     Source;
#   UINT32    GlobalSystemInterrupt;
#   UINT16    Flags;
# } EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE;
# 
EFI_ACPI_4_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE = EFI_ACPI_3_0_INTERRUPT_SOURCE_OVERRIDE_STRUCTURE

# ///
# /// Platform Interrupt Sources Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT16    Flags;
#   UINT8     InterruptType;
#   UINT8     ProcessorId;
#   UINT8     ProcessorEid;
#   UINT8     IoSapicVector;
#   UINT32    GlobalSystemInterrupt;
#   UINT32    PlatformInterruptSourceFlags;
#   UINT8     CpeiProcessorOverride;
#   UINT8     Reserved[31];
# } EFI_ACPI_4_0_PLATFORM_INTERRUPT_APIC_STRUCTURE;
# 
EFI_ACPI_4_0_PLATFORM_INTERRUPT_APIC_STRUCTURE = EFI_ACPI_3_0_PLATFORM_INTERRUPT_APIC_STRUCTURE

# //
# // MPS INTI flags.
# // All other bits are reserved and must be set to 0.
# //
# #define EFI_ACPI_4_0_POLARITY      (3 << 0)
# #define EFI_ACPI_4_0_TRIGGER_MODE  (3 << 2)
# 
EFI_ACPI_4_0_POLARITY      = (3 << 0)
EFI_ACPI_4_0_TRIGGER_MODE  = (3 << 2)

# ///
# /// Non-Maskable Interrupt Source Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT16    Flags;
#   UINT32    GlobalSystemInterrupt;
# } EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE;
# 
EFI_ACPI_4_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE = EFI_ACPI_3_0_NON_MASKABLE_INTERRUPT_SOURCE_STRUCTURE

# ///
# /// Local APIC NMI Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     AcpiProcessorId;
#   UINT16    Flags;
#   UINT8     LocalApicLint;
# } EFI_ACPI_4_0_LOCAL_APIC_NMI_STRUCTURE;
# 
EFI_ACPI_4_0_LOCAL_APIC_NMI_STRUCTURE = EFI_ACPI_3_0_LOCAL_APIC_NMI_STRUCTURE

# ///
# /// Local APIC Address Override Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT16    Reserved;
#   UINT64    LocalApicAddress;
# } EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE;
# 
EFI_ACPI_4_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE = EFI_ACPI_3_0_LOCAL_APIC_ADDRESS_OVERRIDE_STRUCTURE

# ///
# /// IO SAPIC Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     IoApicId;
#   UINT8     Reserved;
#   UINT32    GlobalSystemInterruptBase;
#   UINT64    IoSapicAddress;
# } EFI_ACPI_4_0_IO_SAPIC_STRUCTURE;
# 
EFI_ACPI_4_0_IO_SAPIC_STRUCTURE = EFI_ACPI_3_0_IO_SAPIC_STRUCTURE

# ///
# /// Local SAPIC Structure
# /// This struct followed by a null-terminated ASCII string - ACPI Processor UID String
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     AcpiProcessorId;
#   UINT8     LocalSapicId;
#   UINT8     LocalSapicEid;
#   UINT8     Reserved[3];
#   UINT32    Flags;
#   UINT32    ACPIProcessorUIDValue;
# } EFI_ACPI_4_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE;
# 
EFI_ACPI_4_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE = EFI_ACPI_3_0_PROCESSOR_LOCAL_SAPIC_STRUCTURE

# ///
# /// Platform Interrupt Sources Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT16    Flags;
#   UINT8     InterruptType;
#   UINT8     ProcessorId;
#   UINT8     ProcessorEid;
#   UINT8     IoSapicVector;
#   UINT32    GlobalSystemInterrupt;
#   UINT32    PlatformInterruptSourceFlags;
# } EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE;
# 
EFI_ACPI_4_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE = EFI_ACPI_3_0_PLATFORM_INTERRUPT_SOURCES_STRUCTURE

# ///
# /// Platform Interrupt Source Flags.
# /// All other bits are reserved and must be set to 0.
# ///
# #define EFI_ACPI_4_0_CPEI_PROCESSOR_OVERRIDE  BIT0
# 
EFI_ACPI_4_0_CPEI_PROCESSOR_OVERRIDE          = BIT0

# ///
# /// Processor Local x2APIC Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     Reserved[2];
#   UINT32    X2ApicId;
#   UINT32    Flags;
#   UINT32    AcpiProcessorUid;
# } EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_STRUCTURE;
# 
class EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("Reserved",          UINT8 * 2),
    ("X2ApicId",          UINT32),
    ("Flags",             UINT32),
    ("AcpiProcessorUid",  UINT32)
  ]

# ///
# /// Local x2APIC NMI Structure
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT16    Flags;
#   UINT32    AcpiProcessorUid;
#   UINT8     LocalX2ApicLint;
#   UINT8     Reserved[3];
# } EFI_ACPI_4_0_LOCAL_X2APIC_NMI_STRUCTURE;
# 
class EFI_ACPI_4_0_LOCAL_X2APIC_NMI_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",              UINT8),
    ("Length",            UINT8),
    ("Flags",             UINT16),
    ("AcpiProcessorUid",  UINT32),
    ("LocalX2ApicLint",   UINT8),
    ("Reserved",          UINT8 * 3)
  ]

# ///
# /// Smart Battery Description Table (SBST)
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         WarningEnergyLevel;
#   UINT32                         LowEnergyLevel;
#   UINT32                         CriticalEnergyLevel;
# } EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE;
# 
EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE = EFI_ACPI_3_0_SMART_BATTERY_DESCRIPTION_TABLE

# ///
# /// SBST Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_SMART_BATTERY_DESCRIPTION_TABLE_REVISION = 0x01

# ///
# /// Embedded Controller Boot Resources Table (ECDT)
# /// The table is followed by a null terminated ASCII string that contains
# /// a fully qualified reference to the name space object.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER               Header;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    EcControl;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    EcData;
#   UINT32                                    Uid;
#   UINT8                                     GpeBit;
# } EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE;
# 
EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE

# ///
# /// ECDT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION  = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_REVISION

# ///
# /// System Resource Affinity Table (SRAT.  The rest of the table
# /// must be defined in a platform specific manner.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         Reserved1; ///< Must be set to 1
#   UINT64                         Reserved2;
# } EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER;
# 
EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER = EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_HEADER

# ///
# /// SRAT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  0x03
# 
EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_REVISION  = 0x03

# //
# // SRAT structure types.
# // All other values between 0x03 an 0xFF are reserved and
# // will be ignored by OSPM.
# //
# #define EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  0x00
# #define EFI_ACPI_4_0_MEMORY_AFFINITY                      0x01
# #define EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY      0x02
# 
EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY  = 0x00
EFI_ACPI_4_0_MEMORY_AFFINITY                      = 0x01
EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY      = 0x02

# ///
# /// Processor Local APIC/SAPIC Affinity Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     ProximityDomain7To0;
#   UINT8     ApicId;
#   UINT32    Flags;
#   UINT8     LocalSapicEid;
#   UINT8     ProximityDomain31To8[3];
#   UINT32    ClockDomain;
# } EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE;
# 
class EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                  UINT8),
    ("Length",                UINT8),
    ("ProximityDomain7To0",   UINT8),
    ("ApicId",                UINT8),
    ("Flags",                 UINT32),
    ("LocalSapicEid",         UINT8),
    ("ProximityDomain31To8",  UINT8 * 3),
    ("ClockDomain",           UINT32)
  ]

# ///
# /// Local APIC/SAPIC Flags.  All other bits are reserved and must be 0.
# ///
# #define EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED  (1 << 0)
# 
EFI_ACPI_4_0_PROCESSOR_LOCAL_APIC_SAPIC_ENABLED = (1 << 0)

# ///
# /// Memory Affinity Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT32    ProximityDomain;
#   UINT16    Reserved1;
#   UINT32    AddressBaseLow;
#   UINT32    AddressBaseHigh;
#   UINT32    LengthLow;
#   UINT32    LengthHigh;
#   UINT32    Reserved2;
#   UINT32    Flags;
#   UINT64    Reserved3;
# } EFI_ACPI_4_0_MEMORY_AFFINITY_STRUCTURE;
# 
EFI_ACPI_4_0_MEMORY_AFFINITY_STRUCTURE = EFI_ACPI_3_0_MEMORY_AFFINITY_STRUCTURE

# //
# // Memory Flags.  All other bits are reserved and must be 0.
# //
# #define EFI_ACPI_4_0_MEMORY_ENABLED        (1 << 0)
# #define EFI_ACPI_4_0_MEMORY_HOT_PLUGGABLE  (1 << 1)
# #define EFI_ACPI_4_0_MEMORY_NONVOLATILE    (1 << 2)
# 
EFI_ACPI_4_0_MEMORY_ENABLED       = (1 << 0)
EFI_ACPI_4_0_MEMORY_HOT_PLUGGABLE = (1 << 1)
EFI_ACPI_4_0_MEMORY_NONVOLATILE   = (1 << 2)

# ///
# /// Processor Local x2APIC Affinity Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     Reserved1[2];
#   UINT32    ProximityDomain;
#   UINT32    X2ApicId;
#   UINT32    Flags;
#   UINT32    ClockDomain;
#   UINT8     Reserved2[4];
# } EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE;
# 
class EFI_ACPI_4_0_PROCESSOR_LOCAL_X2APIC_AFFINITY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("Reserved1",       UINT8 * 2),
    ("ProximityDomain", UINT32),
    ("X2ApicId",        UINT32),
    ("Flags",           UINT32),
    ("ClockDomain",     UINT32),
    ("Reserved2",       UINT8 * 4)
  ]

# ///
# /// System Locality Distance Information Table (SLIT).
# /// The rest of the table is a matrix.
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT64                         NumberOfSystemLocalities;
# } EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER;
# 
EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER = EFI_ACPI_3_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_HEADER

# ///
# /// SLIT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_SYSTEM_LOCALITY_DISTANCE_INFORMATION_TABLE_REVISION  = 0x01

# ///
# /// Corrected Platform Error Polling Table (CPEP)
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT8                          Reserved[8];
# } EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER;
# 
class EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",    EFI_ACPI_DESCRIPTION_HEADER),
    ("Reserved",  UINT8 * 8)
  ]

# ///
# /// CPEP Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_REVISION = 0x01

# //
# // CPEP processor structure types.
# //
# #define EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC  0x00
# 
EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC  = 0x00

# ///
# /// Corrected Platform Error Polling Processor Structure Definition
# ///
# typedef struct {
#   UINT8     Type;
#   UINT8     Length;
#   UINT8     ProcessorId;
#   UINT8     ProcessorEid;
#   UINT32    PollingInterval;
# } EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE;
# 
class EFI_ACPI_4_0_CPEP_PROCESSOR_APIC_SAPIC_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",            UINT8),
    ("Length",          UINT8),
    ("ProcessorId",     UINT8),
    ("ProcessorEid",    UINT8),
    ("PollingInterval", UINT32)
  ]

# ///
# /// Maximum System Characteristics Table (MSCT)
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         OffsetProxDomInfo;
#   UINT32                         MaximumNumberOfProximityDomains;
#   UINT32                         MaximumNumberOfClockDomains;
#   UINT64                         MaximumPhysicalAddress;
# } EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER;
# 
class EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                          EFI_ACPI_DESCRIPTION_HEADER),
    ("OffsetProxDomInfo",               UINT32),
    ("MaximumNumberOfProximityDomains", UINT32),
    ("MaximumNumberOfClockDomains",     UINT32),
    ("MaximumPhysicalAddress",          UINT64)
  ]

# ///
# /// MSCT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_REVISION = 0x01

# ///
# /// Maximum Proximity Domain Information Structure Definition
# ///
# typedef struct {
#   UINT8     Revision;
#   UINT8     Length;
#   UINT32    ProximityDomainRangeLow;
#   UINT32    ProximityDomainRangeHigh;
#   UINT32    MaximumProcessorCapacity;
#   UINT64    MaximumMemoryCapacity;
# } EFI_ACPI_4_0_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE;
# 
class EFI_ACPI_4_0_MAXIMUM_PROXIMITY_DOMAIN_INFORMATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Revision",                  UINT8),
    ("Length",                    UINT8),
    ("ProximityDomainRangeLow",   UINT32),
    ("ProximityDomainRangeHigh",  UINT32),
    ("MaximumProcessorCapacity",  UINT32),
    ("MaximumMemoryCapacity",     UINT64)
  ]

# ///
# /// Boot Error Record Table (BERT)
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         BootErrorRegionLength;
#   UINT64                         BootErrorRegion;
# } EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_HEADER;
# 
class EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("BootErrorRegionLength",   UINT32),
    ("BootErrorRegion",         UINT64)
  ]

# ///
# /// BERT Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_REVISION = 0x01

# ///
# /// Boot Error Region Block Status Definition
# ///
# typedef struct {
#   UINT32    UncorrectableErrorValid     : 1;
#   UINT32    CorrectableErrorValid       : 1;
#   UINT32    MultipleUncorrectableErrors : 1;
#   UINT32    MultipleCorrectableErrors   : 1;
#   UINT32    ErrorDataEntryCount         : 10;
#   UINT32    Reserved                    : 18;
# } EFI_ACPI_4_0_ERROR_BLOCK_STATUS;
# 
class EFI_ACPI_4_0_ERROR_BLOCK_STATUS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("UncorrectableErrorValid",     UINT32, 1),
    ("CorrectableErrorValid",       UINT32, 1),
    ("MultipleUncorrectableErrors", UINT32, 1),
    ("MultipleCorrectableErrors",   UINT32, 1),
    ("ErrorDataEntryCount",         UINT32, 10),
    ("Reserved",                    UINT32, 18)
  ]

# ///
# /// Boot Error Region Definition
# ///
# typedef struct {
#   EFI_ACPI_4_0_ERROR_BLOCK_STATUS    BlockStatus;
#   UINT32                             RawDataOffset;
#   UINT32                             RawDataLength;
#   UINT32                             DataLength;
#   UINT32                             ErrorSeverity;
# } EFI_ACPI_4_0_BOOT_ERROR_REGION_STRUCTURE;
# 
class EFI_ACPI_4_0_BOOT_ERROR_REGION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlockStatus",   EFI_ACPI_4_0_ERROR_BLOCK_STATUS),
    ("RawDataOffset", UINT32),
    ("RawDataLength", UINT32),
    ("DataLength",    UINT32),
    ("ErrorSeverity", UINT32)
  ]

# //
# // Boot Error Severity types
# //
# #define EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTABLE  0x00
# #define EFI_ACPI_4_0_ERROR_SEVERITY_RECOVERABLE  0x00
# #define EFI_ACPI_4_0_ERROR_SEVERITY_FATAL        0x01
# #define EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTED    0x02
# #define EFI_ACPI_4_0_ERROR_SEVERITY_NONE         0x03
# 
EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTABLE  = 0x00
EFI_ACPI_4_0_ERROR_SEVERITY_FATAL        = 0x01
EFI_ACPI_4_0_ERROR_SEVERITY_CORRECTED    = 0x02
EFI_ACPI_4_0_ERROR_SEVERITY_NONE         = 0x03

# ///
# /// Generic Error Data Entry Definition
# ///
# typedef struct {
#   UINT8     SectionType[16];
#   UINT32    ErrorSeverity;
#   UINT16    Revision;
#   UINT8     ValidationBits;
#   UINT8     Flags;
#   UINT32    ErrorDataLength;
#   UINT8     FruId[16];
#   UINT8     FruText[20];
# } EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_STRUCTURE;
# 
class EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SectionType",     UINT8 * 16),
    ("ErrorSeverity",   UINT32),
    ("Revision",        UINT16),
    ("ValidationBits",  UINT8),
    ("Flags",           UINT8),
    ("ErrorDataLength", UINT32),
    ("FruId",           UINT8 * 16),
    ("FruText",         UINT8 * 20)
  ]

# ///
# /// Generic Error Data Entry Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_REVISION  0x0201
# 
EFI_ACPI_4_0_GENERIC_ERROR_DATA_ENTRY_REVISION  = 0x0201

# ///
# /// HEST - Hardware Error Source Table
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         ErrorSourceCount;
# } EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_HEADER;
# 
class EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",            EFI_ACPI_DESCRIPTION_HEADER),
    ("ErrorSourceCount",  UINT32)
  ]

# ///
# /// HEST Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_REVISION = 0x01

# //
# // Error Source structure types.
# //
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION  0x00
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK  0x01
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR                0x02
# #define EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER                  0x06
# #define EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER                     0x07
# #define EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER                     0x08
# #define EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR                     0x09
# 
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION  = 0x00
EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK  = 0x01
EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR                = 0x02
EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER                  = 0x06
EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER                     = 0x07
EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER                     = 0x08
EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR                     = 0x09

# //
# // Error Source structure flags.
# //
# #define EFI_ACPI_4_0_ERROR_SOURCE_FLAG_FIRMWARE_FIRST  (1 << 0)
# #define EFI_ACPI_4_0_ERROR_SOURCE_FLAG_GLOBAL          (1 << 1)
# 
EFI_ACPI_4_0_ERROR_SOURCE_FLAG_FIRMWARE_FIRST       = (1 << 0)
EFI_ACPI_4_0_ERROR_SOURCE_FLAG_GLOBAL               = (1 << 1)

# ///
# /// IA-32 Architecture Machine Check Exception Structure Definition
# ///
# typedef struct {
#   UINT16    Type;
#   UINT16    SourceId;
#   UINT8     Reserved0[2];
#   UINT8     Flags;
#   UINT8     Enabled;
#   UINT32    NumberOfRecordsToPreAllocate;
#   UINT32    MaxSectionsPerRecord;
#   UINT64    GlobalCapabilityInitData;
#   UINT64    GlobalControlInitData;
#   UINT8     NumberOfHardwareBanks;
#   UINT8     Reserved1[7];
# } EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE;
# 
class EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_EXCEPTION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("GlobalCapabilityInitData",      UINT64),
    ("GlobalCapabilityInitData",      UINT64),
    ("NumberOfHardwareBanks",         UINT8),
    ("Reserved1",                     UINT8 * 7)
  ]

# ///
# /// IA-32 Architecture Machine Check Bank Structure Definition
# ///
# typedef struct {
#   UINT8     BankNumber;
#   UINT8     ClearStatusOnInitialization;
#   UINT8     StatusDataFormat;
#   UINT8     Reserved0;
#   UINT32    ControlRegisterMsrAddress;
#   UINT64    ControlInitData;
#   UINT32    StatusRegisterMsrAddress;
#   UINT32    AddressRegisterMsrAddress;
#   UINT32    MiscRegisterMsrAddress;
# } EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE;
# 
class EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_BANK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BankNumber",                    UINT8),
    ("ClearStatusOnInitialization",   UINT8),
    ("StatusDataFormat",              UINT8),
    ("Reserved0",                     UINT8),
    ("ControlRegisterMsrAddress",     UINT32),
    ("ControlInitData",               UINT64),
    ("StatusRegisterMsrAddress",      UINT32),
    ("AddressRegisterMsrAddress",     UINT32),
    ("MiscRegisterMsrAddress",        UINT32)
  ]

# ///
# /// IA-32 Architecture Machine Check Bank Structure MCA data format
# ///
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32     0x00
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64  0x01
# #define EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64    0x02
# 
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_IA32      = 0x00
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_INTEL64   = 0x01
EFI_ACPI_4_0_IA32_ARCHITECTURE_MACHINE_CHECK_ERROR_DATA_FORMAT_AMD64     = 0x02

# //
# // Hardware Error Notification types. All other values are reserved
# //
# #define EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_POLLED              0x00
# #define EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT  0x01
# #define EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT     0x02
# #define EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_SCI                 0x03
# #define EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_NMI                 0x04
# 
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_POLLED                = 0x00
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_EXTERNAL_INTERRUPT    = 0x01
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_LOCAL_INTERRUPT       = 0x02
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_SCI                   = 0x03
EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_NMI                   = 0x04

# ///
# /// Hardware Error Notification Configuration Write Enable Structure Definition
# ///
# typedef struct {
#   UINT16    Type                           : 1;
#   UINT16    PollInterval                   : 1;
#   UINT16    SwitchToPollingThresholdValue  : 1;
#   UINT16    SwitchToPollingThresholdWindow : 1;
#   UINT16    ErrorThresholdValue            : 1;
#   UINT16    ErrorThresholdWindow           : 1;
#   UINT16    Reserved                       : 10;
# } EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE;
# 
class EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                            UINT16, 1),
    ("PollInterval",                    UINT16, 1),
    ("SwitchToPollingThresholdValue",   UINT16, 1),
    ("SwitchToPollingThresholdWindow",  UINT16, 1),
    ("ErrorThresholdValue",             UINT16, 1),
    ("ErrorThresholdWindow",            UINT16, 1),
    ("Reserved",                        UINT16, 10)
  ]

# ///
# /// Hardware Error Notification Structure Definition
# ///
# typedef struct {
#   UINT8                                                                            Type;
#   UINT8                                                                            Length;
#   EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE    ConfigurationWriteEnable;
#   UINT32                                                                           PollInterval;
#   UINT32                                                                           Vector;
#   UINT32                                                                           SwitchToPollingThresholdValue;
#   UINT32                                                                           SwitchToPollingThresholdWindow;
#   UINT32                                                                           ErrorThresholdValue;
#   UINT32                                                                           ErrorThresholdWindow;
# } EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE;
# 
class EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT8),
    ("Length",                        UINT8),
    ("ConfigurationWriteEnable",      EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_CONFIGURATION_WRITE_ENABLE_STRUCTURE),
    ("PollInterval",                  UINT32),
    ("Vector",                        UINT32),
    ("SwitchToPollingThresholdValue", UINT32),
    ("SwitchToPollingThresholdWindow",UINT32),
    ("ErrorThresholdValue",           UINT32),
    ("ErrorThresholdWindow",          UINT32)
  ]

# ///
# /// IA-32 Architecture Corrected Machine Check Structure Definition
# ///
# typedef struct {
#   UINT16                                                Type;
#   UINT16                                                SourceId;
#   UINT8                                                 Reserved0[2];
#   UINT8                                                 Flags;
#   UINT8                                                 Enabled;
#   UINT32                                                NumberOfRecordsToPreAllocate;
#   UINT32                                                MaxSectionsPerRecord;
#   EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE    NotificationStructure;
#   UINT8                                                 NumberOfHardwareBanks;
#   UINT8                                                 Reserved1[3];
# } EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE;
# 
class EFI_ACPI_4_0_IA32_ARCHITECTURE_CORRECTED_MACHINE_CHECK_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("NotificationStructure",         EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("NumberOfHardwareBanks",         UINT8),
    ("Reserved1",                     UINT8 * 3)
  ]

# ///
# /// IA-32 Architecture NMI Error Structure Definition
# ///
# typedef struct {
#   UINT16    Type;
#   UINT16    SourceId;
#   UINT8     Reserved0[2];
#   UINT32    NumberOfRecordsToPreAllocate;
#   UINT32    MaxSectionsPerRecord;
#   UINT32    MaxRawDataLength;
# } EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE;
# 
class EFI_ACPI_4_0_IA32_ARCHITECTURE_NMI_ERROR_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("Reserved0",                     UINT8 * 2),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32)
  ]

# ///
# /// PCI Express Root Port AER Structure Definition
# ///
# typedef struct {
#   UINT16    Type;
#   UINT16    SourceId;
#   UINT8     Reserved0[2];
#   UINT8     Flags;
#   UINT8     Enabled;
#   UINT32    NumberOfRecordsToPreAllocate;
#   UINT32    MaxSectionsPerRecord;
#   UINT32    Bus;
#   UINT16    Device;
#   UINT16    Function;
#   UINT16    DeviceControl;
#   UINT8     Reserved1[2];
#   UINT32    UncorrectableErrorMask;
#   UINT32    UncorrectableErrorSeverity;
#   UINT32    CorrectableErrorMask;
#   UINT32    AdvancedErrorCapabilitiesAndControl;
#   UINT32    RootErrorCommand;
# } EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE;
# 
class EFI_ACPI_4_0_PCI_EXPRESS_ROOT_PORT_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("SourceId",                            UINT16),
    ("Reserved0",                           UINT8 * 2),
    ("Flags",                               UINT8),
    ("Enabled",                             UINT8),
    ("NumberOfRecordsToPreAllocate",        UINT32),
    ("MaxSectionsPerRecord",                UINT32),
    ("Bus",                                 UINT32),
    ("Device",                              UINT16),
    ("Function",                            UINT16),
    ("DeviceControl",                       UINT16),
    ("Reserved1",                           UINT8 * 2),
    ("UncorrectableErrorMask",              UINT32),
    ("UncorrectableErrorSeverity",          UINT32),
    ("CorrectableErrorMask",                UINT32),
    ("AdvancedErrorCapabilitiesAndControl", UINT32),
    ("RootErrorCommand",                    UINT32)
  ]

# ///
# /// PCI Express Device AER Structure Definition
# ///
# typedef struct {
#   UINT16    Type;
#   UINT16    SourceId;
#   UINT8     Reserved0[2];
#   UINT8     Flags;
#   UINT8     Enabled;
#   UINT32    NumberOfRecordsToPreAllocate;
#   UINT32    MaxSectionsPerRecord;
#   UINT32    Bus;
#   UINT16    Device;
#   UINT16    Function;
#   UINT16    DeviceControl;
#   UINT8     Reserved1[2];
#   UINT32    UncorrectableErrorMask;
#   UINT32    UncorrectableErrorSeverity;
#   UINT32    CorrectableErrorMask;
#   UINT32    AdvancedErrorCapabilitiesAndControl;
# } EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER_STRUCTURE;
# 
class EFI_ACPI_4_0_PCI_EXPRESS_DEVICE_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                UINT16),
    ("SourceId",                            UINT16),
    ("Reserved0",                           UINT8 * 2),
    ("Flags",                               UINT8),
    ("Enabled",                             UINT8),
    ("NumberOfRecordsToPreAllocate",        UINT32),
    ("MaxSectionsPerRecord",                UINT32),
    ("Bus",                                 UINT32),
    ("Device",                              UINT16),
    ("Function",                            UINT16),
    ("DeviceControl",                       UINT16),
    ("Reserved1",                           UINT8 * 2),
    ("UncorrectableErrorMask",              UINT32),
    ("UncorrectableErrorSeverity",          UINT32),
    ("CorrectableErrorMask",                UINT32),
    ("AdvancedErrorCapabilitiesAndControl", UINT32)
  ]

# ///
# /// PCI Express Bridge AER Structure Definition
# ///
# typedef struct {
#   UINT16    Type;
#   UINT16    SourceId;
#   UINT8     Reserved0[2];
#   UINT8     Flags;
#   UINT8     Enabled;
#   UINT32    NumberOfRecordsToPreAllocate;
#   UINT32    MaxSectionsPerRecord;
#   UINT32    Bus;
#   UINT16    Device;
#   UINT16    Function;
#   UINT16    DeviceControl;
#   UINT8     Reserved1[2];
#   UINT32    UncorrectableErrorMask;
#   UINT32    UncorrectableErrorSeverity;
#   UINT32    CorrectableErrorMask;
#   UINT32    AdvancedErrorCapabilitiesAndControl;
#   UINT32    SecondaryUncorrectableErrorMask;
#   UINT32    SecondaryUncorrectableErrorSeverity;
#   UINT32    SecondaryAdvancedErrorCapabilitiesAndControl;
# } EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER_STRUCTURE;
# 
class EFI_ACPI_4_0_PCI_EXPRESS_BRIDGE_AER_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                                          UINT16),
    ("SourceId",                                      UINT16),
    ("Reserved0",                                     UINT8 * 2),
    ("Flags",                                         UINT8),
    ("Enabled",                                       UINT8),
    ("NumberOfRecordsToPreAllocate",                  UINT32),
    ("MaxSectionsPerRecord",                          UINT32),
    ("Bus",                                           UINT32),
    ("Device",                                        UINT16),
    ("Function",                                      UINT16),
    ("DeviceControl",                                 UINT16),
    ("Reserved1",                                     UINT8 * 2),
    ("UncorrectableErrorMask",                        UINT32),
    ("UncorrectableErrorSeverity",                    UINT32),
    ("CorrectableErrorMask",                          UINT32),
    ("AdvancedErrorCapabilitiesAndControl",           UINT32),
    ("SecondaryUncorrectableErrorMask",               UINT32),
    ("SecondaryUncorrectableErrorSeverity",           UINT32),
    ("SecondaryAdvancedErrorCapabilitiesAndControl",  UINT32)
  ]

# ///
# /// Generic Hardware Error Source Structure Definition
# ///
# typedef struct {
#   UINT16                                                Type;
#   UINT16                                                SourceId;
#   UINT16                                                RelatedSourceId;
#   UINT8                                                 Flags;
#   UINT8                                                 Enabled;
#   UINT32                                                NumberOfRecordsToPreAllocate;
#   UINT32                                                MaxSectionsPerRecord;
#   UINT32                                                MaxRawDataLength;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE                ErrorStatusAddress;
#   EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE    NotificationStructure;
#   UINT32                                                ErrorStatusBlockLength;
# } EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE;
# 
class EFI_ACPI_4_0_GENERIC_HARDWARE_ERROR_SOURCE_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",                          UINT16),
    ("SourceId",                      UINT16),
    ("RelatedSourceId",               UINT16),
    ("Flags",                         UINT8),
    ("Enabled",                       UINT8),
    ("NumberOfRecordsToPreAllocate",  UINT32),
    ("MaxSectionsPerRecord",          UINT32),
    ("MaxRawDataLength",              UINT32),
    ("ErrorStatusAddress",            EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("NotificationStructure",         EFI_ACPI_4_0_HARDWARE_ERROR_NOTIFICATION_STRUCTURE),
    ("ErrorStatusBlockLength",        UINT32)
  ]

# ///
# /// Generic Error Status Definition
# ///
# typedef struct {
#   EFI_ACPI_4_0_ERROR_BLOCK_STATUS    BlockStatus;
#   UINT32                             RawDataOffset;
#   UINT32                             RawDataLength;
#   UINT32                             DataLength;
#   UINT32                             ErrorSeverity;
# } EFI_ACPI_4_0_GENERIC_ERROR_STATUS_STRUCTURE;
# 
class EFI_ACPI_4_0_GENERIC_ERROR_STATUS_STRUCTURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BlockStatus",     EFI_ACPI_4_0_ERROR_BLOCK_STATUS),
    ("RawDataOffset",   UINT32),
    ("RawDataLength",   UINT32),
    ("DataLength",      UINT32),
    ("ErrorSeverity",   UINT32)
  ]

# ///
# /// ERST - Error Record Serialization Table
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         SerializationHeaderSize;
#   UINT8                          Reserved0[4];
#   UINT32                         InstructionEntryCount;
# } EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_HEADER;
# 
class EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",                  EFI_ACPI_DESCRIPTION_HEADER),
    ("SerializationHeaderSize", UINT32),
    ("Reserved0",               UINT8 * 4),
    ("InstructionEntryCount",   UINT32)
  ]

# ///
# /// ERST Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_REVISION = 0x01

# ///
# /// ERST Serialization Actions
# ///
# #define EFI_ACPI_4_0_ERST_BEGIN_WRITE_OPERATION                   0x00
# #define EFI_ACPI_4_0_ERST_BEGIN_READ_OPERATION                    0x01
# #define EFI_ACPI_4_0_ERST_BEGIN_CLEAR_OPERATION                   0x02
# #define EFI_ACPI_4_0_ERST_END_OPERATION                           0x03
# #define EFI_ACPI_4_0_ERST_SET_RECORD_OFFSET                       0x04
# #define EFI_ACPI_4_0_ERST_EXECUTE_OPERATION                       0x05
# #define EFI_ACPI_4_0_ERST_CHECK_BUSY_STATUS                       0x06
# #define EFI_ACPI_4_0_ERST_GET_COMMAND_STATUS                      0x07
# #define EFI_ACPI_4_0_ERST_GET_RECORD_IDENTIFIER                   0x08
# #define EFI_ACPI_4_0_ERST_SET_RECORD_IDENTIFIER                   0x09
# #define EFI_ACPI_4_0_ERST_GET_RECORD_COUNT                        0x0A
# #define EFI_ACPI_4_0_ERST_BEGIN_DUMMY_WRITE_OPERATION             0x0B
# #define EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE             0x0D
# #define EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH      0x0E
# #define EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES  0x0F
# 
EFI_ACPI_4_0_ERST_BEGIN_WRITE_OPERATION                    = 0x00
EFI_ACPI_4_0_ERST_BEGIN_READ_OPERATION                     = 0x01
EFI_ACPI_4_0_ERST_BEGIN_CLEAR_OPERATION                    = 0x02
EFI_ACPI_4_0_ERST_END_OPERATION                            = 0x03
EFI_ACPI_4_0_ERST_SET_RECORD_OFFSET                        = 0x04
EFI_ACPI_4_0_ERST_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_4_0_ERST_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_4_0_ERST_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_4_0_ERST_GET_RECORD_IDENTIFIER                    = 0x08
EFI_ACPI_4_0_ERST_SET_RECORD_IDENTIFIER                    = 0x09
EFI_ACPI_4_0_ERST_GET_RECORD_COUNT                         = 0x0A
EFI_ACPI_4_0_ERST_BEGIN_DUMMY_WRITE_OPERATION              = 0x0B
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE              = 0x0D
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_LENGTH       = 0x0E
EFI_ACPI_4_0_ERST_GET_ERROR_LOG_ADDRESS_RANGE_ATTRIBUTES   = 0x0F

# ///
# /// ERST Action Command Status
# ///
# #define EFI_ACPI_4_0_EINJ_STATUS_SUCCESS                 0x00
# #define EFI_ACPI_4_0_EINJ_STATUS_NOT_ENOUGH_SPACE        0x01
# #define EFI_ACPI_4_0_EINJ_STATUS_HARDWARE_NOT_AVAILABLE  0x02
# #define EFI_ACPI_4_0_EINJ_STATUS_FAILED                  0x03
# #define EFI_ACPI_4_0_EINJ_STATUS_RECORD_STORE_EMPTY      0x04
# #define EFI_ACPI_4_0_EINJ_STATUS_RECORD_NOT_FOUND        0x05
# 
EFI_ACPI_4_0_EINJ_STATUS_SUCCESS                           = 0x00
EFI_ACPI_4_0_EINJ_STATUS_NOT_ENOUGH_SPACE                  = 0x01
EFI_ACPI_4_0_EINJ_STATUS_HARDWARE_NOT_AVAILABLE            = 0x02
EFI_ACPI_4_0_EINJ_STATUS_FAILED                            = 0x03
EFI_ACPI_4_0_EINJ_STATUS_RECORD_STORE_EMPTY                = 0x04
EFI_ACPI_4_0_EINJ_STATUS_RECORD_NOT_FOUND                  = 0x05

# ///
# /// ERST Serialization Instructions
# ///
# #define EFI_ACPI_4_0_ERST_READ_REGISTER                  0x00
# #define EFI_ACPI_4_0_ERST_READ_REGISTER_VALUE            0x01
# #define EFI_ACPI_4_0_ERST_WRITE_REGISTER                 0x02
# #define EFI_ACPI_4_0_ERST_WRITE_REGISTER_VALUE           0x03
# #define EFI_ACPI_4_0_ERST_NOOP                           0x04
# #define EFI_ACPI_4_0_ERST_LOAD_VAR1                      0x05
# #define EFI_ACPI_4_0_ERST_LOAD_VAR2                      0x06
# #define EFI_ACPI_4_0_ERST_STORE_VAR1                     0x07
# #define EFI_ACPI_4_0_ERST_ADD                            0x08
# #define EFI_ACPI_4_0_ERST_SUBTRACT                       0x09
# #define EFI_ACPI_4_0_ERST_ADD_VALUE                      0x0A
# #define EFI_ACPI_4_0_ERST_SUBTRACT_VALUE                 0x0B
# #define EFI_ACPI_4_0_ERST_STALL                          0x0C
# #define EFI_ACPI_4_0_ERST_STALL_WHILE_TRUE               0x0D
# #define EFI_ACPI_4_0_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE  0x0E
# #define EFI_ACPI_4_0_ERST_GOTO                           0x0F
# #define EFI_ACPI_4_0_ERST_SET_SRC_ADDRESS_BASE           0x10
# #define EFI_ACPI_4_0_ERST_SET_DST_ADDRESS_BASE           0x11
# #define EFI_ACPI_4_0_ERST_MOVE_DATA                      0x12
# 
EFI_ACPI_4_0_ERST_READ_REGISTER                            = 0x00
EFI_ACPI_4_0_ERST_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_4_0_ERST_WRITE_REGISTER                           = 0x02
EFI_ACPI_4_0_ERST_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_4_0_ERST_NOOP                                     = 0x04
EFI_ACPI_4_0_ERST_LOAD_VAR1                                = 0x05
EFI_ACPI_4_0_ERST_LOAD_VAR2                                = 0x06
EFI_ACPI_4_0_ERST_STORE_VAR1                               = 0x07
EFI_ACPI_4_0_ERST_ADD                                      = 0x08
EFI_ACPI_4_0_ERST_SUBTRACT                                 = 0x09
EFI_ACPI_4_0_ERST_ADD_VALUE                                = 0x0A
EFI_ACPI_4_0_ERST_SUBTRACT_VALUE                           = 0x0B
EFI_ACPI_4_0_ERST_STALL                                    = 0x0C
EFI_ACPI_4_0_ERST_STALL_WHILE_TRUE                         = 0x0D
EFI_ACPI_4_0_ERST_SKIP_NEXT_INSTRUCTION_IF_TRUE            = 0x0E
EFI_ACPI_4_0_ERST_GOTO                                     = 0x0F
EFI_ACPI_4_0_ERST_SET_SRC_ADDRESS_BASE                     = 0x10
EFI_ACPI_4_0_ERST_SET_DST_ADDRESS_BASE                     = 0x11
EFI_ACPI_4_0_ERST_MOVE_DATA                                = 0x12

# ///
# /// ERST Instruction Flags
# ///
# #define EFI_ACPI_4_0_ERST_PRESERVE_REGISTER  0x01
# 
EFI_ACPI_4_0_ERST_PRESERVE_REGISTER                        = 0x01

# ///
# /// ERST Serialization Instruction Entry
# ///
# typedef struct {
#   UINT8                                     SerializationAction;
#   UINT8                                     Instruction;
#   UINT8                                     Flags;
#   UINT8                                     Reserved0;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    RegisterRegion;
#   UINT64                                    Value;
#   UINT64                                    Mask;
# } EFI_ACPI_4_0_ERST_SERIALIZATION_INSTRUCTION_ENTRY;
# 
class EFI_ACPI_4_0_ERST_SERIALIZATION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("SerializationAction", UINT8),
    ("Instruction",         UINT8),
    ("Flags",               UINT8),
    ("Reserved0",           UINT8),
    ("RegisterRegion",      EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",               UINT64),
    ("Mask",                UINT64)
  ]

# ///
# /// EINJ - Error Injection Table
# ///
# typedef struct {
#   EFI_ACPI_DESCRIPTION_HEADER    Header;
#   UINT32                         InjectionHeaderSize;
#   UINT8                          InjectionFlags;
#   UINT8                          Reserved0[3];
#   UINT32                         InjectionEntryCount;
# } EFI_ACPI_4_0_ERROR_INJECTION_TABLE_HEADER;
# 
class EFI_ACPI_4_0_ERROR_INJECTION_TABLE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Header",              EFI_ACPI_DESCRIPTION_HEADER),
    ("InjectionHeaderSize", UINT32),
    ("InjectionFlags",      UINT8),
    ("Reserved0",           UINT8 * 3),
    ("InjectionEntryCount", UINT32)
  ]

# ///
# /// EINJ Version (as defined in ACPI 4.0 spec.)
# ///
# #define EFI_ACPI_4_0_ERROR_INJECTION_TABLE_REVISION  0x01
# 
EFI_ACPI_4_0_ERROR_INJECTION_TABLE_REVISION = 0x01

# ///
# /// EINJ Error Injection Actions
# ///
# #define EFI_ACPI_4_0_EINJ_BEGIN_INJECTION_OPERATION       0x00
# #define EFI_ACPI_4_0_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE  0x01
# #define EFI_ACPI_4_0_EINJ_SET_ERROR_TYPE                  0x02
# #define EFI_ACPI_4_0_EINJ_GET_ERROR_TYPE                  0x03
# #define EFI_ACPI_4_0_EINJ_END_OPERATION                   0x04
# #define EFI_ACPI_4_0_EINJ_EXECUTE_OPERATION               0x05
# #define EFI_ACPI_4_0_EINJ_CHECK_BUSY_STATUS               0x06
# #define EFI_ACPI_4_0_EINJ_GET_COMMAND_STATUS              0x07
# #define EFI_ACPI_4_0_EINJ_TRIGGER_ERROR                   0xFF
# 
EFI_ACPI_4_0_EINJ_BEGIN_INJECTION_OPERATION                = 0x00
EFI_ACPI_4_0_EINJ_GET_TRIGGER_ERROR_ACTION_TABLE           = 0x01
EFI_ACPI_4_0_EINJ_SET_ERROR_TYPE                           = 0x02
EFI_ACPI_4_0_EINJ_GET_ERROR_TYPE                           = 0x03
EFI_ACPI_4_0_EINJ_END_OPERATION                            = 0x04
EFI_ACPI_4_0_EINJ_EXECUTE_OPERATION                        = 0x05
EFI_ACPI_4_0_EINJ_CHECK_BUSY_STATUS                        = 0x06
EFI_ACPI_4_0_EINJ_GET_COMMAND_STATUS                       = 0x07
EFI_ACPI_4_0_EINJ_TRIGGER_ERROR                            = 0xFF

# ///
# /// EINJ Action Command Status
# ///
# #define EFI_ACPI_4_0_EINJ_STATUS_SUCCESS          0x00
# #define EFI_ACPI_4_0_EINJ_STATUS_UNKNOWN_FAILURE  0x01
# #define EFI_ACPI_4_0_EINJ_STATUS_INVALID_ACCESS   0x02
# 
EFI_ACPI_4_0_EINJ_STATUS_SUCCESS                           = 0x00
EFI_ACPI_4_0_EINJ_STATUS_UNKNOWN_FAILURE                   = 0x01
EFI_ACPI_4_0_EINJ_STATUS_INVALID_ACCESS                    = 0x02

# ///
# /// EINJ Error Type Definition
# ///
# #define EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_CORRECTABLE               (1 << 0)
# #define EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL    (1 << 1)
# #define EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL       (1 << 2)
# #define EFI_ACPI_4_0_EINJ_ERROR_MEMORY_CORRECTABLE                  (1 << 3)
# #define EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL       (1 << 4)
# #define EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL          (1 << 5)
# #define EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE             (1 << 6)
# #define EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL  (1 << 7)
# #define EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL     (1 << 8)
# #define EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_CORRECTABLE                (1 << 9)
# #define EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL     (1 << 10)
# #define EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL        (1 << 11)
# 
EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_CORRECTABLE                 = (1 << 0)
EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_NONFATAL      = (1 << 1)
EFI_ACPI_4_0_EINJ_ERROR_PROCESSOR_UNCORRECTABLE_FATAL         = (1 << 2)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_CORRECTABLE                    = (1 << 3)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_NONFATAL         = (1 << 4)
EFI_ACPI_4_0_EINJ_ERROR_MEMORY_UNCORRECTABLE_FATAL            = (1 << 5)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_CORRECTABLE               = (1 << 6)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_NONFATAL    = (1 << 7)
EFI_ACPI_4_0_EINJ_ERROR_PCI_EXPRESS_UNCORRECTABLE_FATAL       = (1 << 8)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_CORRECTABLE                  = (1 << 9)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_NONFATAL       = (1 << 10)
EFI_ACPI_4_0_EINJ_ERROR_PLATFORM_UNCORRECTABLE_FATAL          = (1 << 11)

# ///
# /// EINJ Injection Instructions
# ///
# #define EFI_ACPI_4_0_EINJ_READ_REGISTER         0x00
# #define EFI_ACPI_4_0_EINJ_READ_REGISTER_VALUE   0x01
# #define EFI_ACPI_4_0_EINJ_WRITE_REGISTER        0x02
# #define EFI_ACPI_4_0_EINJ_WRITE_REGISTER_VALUE  0x03
# #define EFI_ACPI_4_0_EINJ_NOOP                  0x04
# 
EFI_ACPI_4_0_EINJ_READ_REGISTER                            = 0x00
EFI_ACPI_4_0_EINJ_READ_REGISTER_VALUE                      = 0x01
EFI_ACPI_4_0_EINJ_WRITE_REGISTER                           = 0x02
EFI_ACPI_4_0_EINJ_WRITE_REGISTER_VALUE                     = 0x03
EFI_ACPI_4_0_EINJ_NOOP                                     = 0x04

# ///
# /// EINJ Instruction Flags
# ///
# #define EFI_ACPI_4_0_EINJ_PRESERVE_REGISTER  0x01
# 
EFI_ACPI_4_0_EINJ_PRESERVE_REGISTER                        = 0x01

# ///
# /// EINJ Injection Instruction Entry
# ///
# typedef struct {
#   UINT8                                     InjectionAction;
#   UINT8                                     Instruction;
#   UINT8                                     Flags;
#   UINT8                                     Reserved0;
#   EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE    RegisterRegion;
#   UINT64                                    Value;
#   UINT64                                    Mask;
# } EFI_ACPI_4_0_EINJ_INJECTION_INSTRUCTION_ENTRY;
# 
class EFI_ACPI_4_0_EINJ_INJECTION_INSTRUCTION_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InjectionAction", UINT8),
    ("Instruction",     UINT8),
    ("Flags",           UINT8),
    ("Reserved0",       UINT8),
    ("RegisterRegion",  EFI_ACPI_4_0_GENERIC_ADDRESS_STRUCTURE),
    ("Value",           UINT64),
    ("Mask",            UINT64)
  ]

# ///
# /// EINJ Trigger Action Table
# ///
# typedef struct {
#   UINT32    HeaderSize;
#   UINT32    Revision;
#   UINT32    TableSize;
#   UINT32    EntryCount;
# } EFI_ACPI_4_0_EINJ_TRIGGER_ACTION_TABLE;
# 
class EFI_ACPI_4_0_EINJ_TRIGGER_ACTION_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("HeaderSize",  UINT32),
    ("Revision",    UINT32),
    ("TableSize",   UINT32),
    ("EntryCount",  UINT32)
  ]

# //
# // Known table signatures
# //
# 
# ///
# /// "RSD PTR " Root System Description Pointer
# ///
# #define EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  SIGNATURE_64('R', 'S', 'D', ' ', 'P', 'T', 'R', ' ')
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE  = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_POINTER_SIGNATURE
# 
# ///
# /// "APIC" Multiple APIC Description Table
# ///
# #define EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('A', 'P', 'I', 'C')
EFI_ACPI_4_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_MULTIPLE_APIC_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "BERT" Boot Error Record Table
# ///
# #define EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_SIGNATURE  SIGNATURE_32('B', 'E', 'R', 'T')
EFI_ACPI_4_0_BOOT_ERROR_RECORD_TABLE_SIGNATURE  = SIGNATURE_32('B', 'E', 'R', 'T')
# 
# ///
# /// "CPEP" Corrected Platform Error Polling Table
# ///
# #define EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  SIGNATURE_32('C', 'P', 'E', 'P')
EFI_ACPI_4_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE  = EFI_ACPI_3_0_CORRECTED_PLATFORM_ERROR_POLLING_TABLE_SIGNATURE
# 
# ///
# /// "DSDT" Differentiated System Description Table
# ///
# #define EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('D', 'S', 'D', 'T')
EFI_ACPI_4_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_DIFFERENTIATED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "ECDT" Embedded Controller Boot Resources Table
# ///
# #define EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  SIGNATURE_32('E', 'C', 'D', 'T')
EFI_ACPI_4_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE  = EFI_ACPI_3_0_EMBEDDED_CONTROLLER_BOOT_RESOURCES_TABLE_SIGNATURE
# 
# ///
# /// "EINJ" Error Injection Table
# ///
# #define EFI_ACPI_4_0_ERROR_INJECTION_TABLE_SIGNATURE  SIGNATURE_32('E', 'I', 'N', 'J')
EFI_ACPI_4_0_ERROR_INJECTION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'I', 'N', 'J')
# 
# ///
# /// "ERST" Error Record Serialization Table
# ///
# #define EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE  SIGNATURE_32('E', 'R', 'S', 'T')
EFI_ACPI_4_0_ERROR_RECORD_SERIALIZATION_TABLE_SIGNATURE  = SIGNATURE_32('E', 'R', 'S', 'T')
# 
# ///
# /// "FACP" Fixed ACPI Description Table
# ///
# #define EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('F', 'A', 'C', 'P')
EFI_ACPI_4_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_FIXED_ACPI_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "FACS" Firmware ACPI Control Structure
# ///
# #define EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  SIGNATURE_32('F', 'A', 'C', 'S')
EFI_ACPI_4_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE  = EFI_ACPI_3_0_FIRMWARE_ACPI_CONTROL_STRUCTURE_SIGNATURE
# 
# ///
# /// "HEST" Hardware Error Source Table
# ///
# #define EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE  SIGNATURE_32('H', 'E', 'S', 'T')
EFI_ACPI_4_0_HARDWARE_ERROR_SOURCE_TABLE_SIGNATURE  = SIGNATURE_32('H', 'E', 'S', 'T')
# 
# ///
# /// "MSCT" Maximum System Characteristics Table
# ///
# #define EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE  SIGNATURE_32('M', 'S', 'C', 'T')
EFI_ACPI_4_0_MAXIMUM_SYSTEM_CHARACTERISTICS_TABLE_SIGNATURE  = SIGNATURE_32('M', 'S', 'C', 'T')
# 
# ///
# /// "PSDT" Persistent System Description Table
# ///
# #define EFI_ACPI_4_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('P', 'S', 'D', 'T')
EFI_ACPI_4_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_PERSISTENT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "RSDT" Root System Description Table
# ///
# #define EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('R', 'S', 'D', 'T')
EFI_ACPI_4_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_ROOT_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "SBST" Smart Battery Specification Table
# ///
# #define EFI_ACPI_4_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  SIGNATURE_32('S', 'B', 'S', 'T')
EFI_ACPI_4_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SMART_BATTERY_SPECIFICATION_TABLE_SIGNATURE
# 
# ///
# /// "SLIT" System Locality Information Table
# ///
# #define EFI_ACPI_4_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  SIGNATURE_32('S', 'L', 'I', 'T')
EFI_ACPI_4_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SYSTEM_LOCALITY_INFORMATION_TABLE_SIGNATURE
# 
# ///
# /// "SRAT" System Resource Affinity Table
# ///
# #define EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  SIGNATURE_32('S', 'R', 'A', 'T')
EFI_ACPI_4_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE  = EFI_ACPI_3_0_SYSTEM_RESOURCE_AFFINITY_TABLE_SIGNATURE
# 
# ///
# /// "SSDT" Secondary System Description Table
# ///
# #define EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('S', 'S', 'D', 'T')
EFI_ACPI_4_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SECONDARY_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "XSDT" Extended System Description Table
# ///
# #define EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('X', 'S', 'D', 'T')
EFI_ACPI_4_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_EXTENDED_SYSTEM_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "BOOT" MS Simple Boot Spec
# ///
# #define EFI_ACPI_4_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  SIGNATURE_32('B', 'O', 'O', 'T')
EFI_ACPI_4_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE  = EFI_ACPI_3_0_SIMPLE_BOOT_FLAG_TABLE_SIGNATURE
# 
# ///
# /// "DBGP" MS Debug Port Spec
# ///
# #define EFI_ACPI_4_0_DEBUG_PORT_TABLE_SIGNATURE  SIGNATURE_32('D', 'B', 'G', 'P')
EFI_ACPI_4_0_DEBUG_PORT_TABLE_SIGNATURE  = EFI_ACPI_3_0_DEBUG_PORT_TABLE_SIGNATURE
# 
# ///
# /// "DMAR" DMA Remapping Table
# ///
# #define EFI_ACPI_4_0_DMA_REMAPPING_TABLE_SIGNATURE  SIGNATURE_32('D', 'M', 'A', 'R')
EFI_ACPI_4_0_DMA_REMAPPING_TABLE_SIGNATURE  = SIGNATURE_32('D', 'M', 'A', 'R')
# 
# ///
# /// "ETDT" Event Timer Description Table
# ///
# #define EFI_ACPI_4_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('E', 'T', 'D', 'T')
EFI_ACPI_4_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_EVENT_TIMER_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "HPET" IA-PC High Precision Event Timer Table
# ///
# #define EFI_ACPI_4_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  SIGNATURE_32('H', 'P', 'E', 'T')
EFI_ACPI_4_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE  = EFI_ACPI_3_0_HIGH_PRECISION_EVENT_TIMER_TABLE_SIGNATURE
# 
# ///
# /// "iBFT" iSCSI Boot Firmware Table
# ///
# #define EFI_ACPI_4_0_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  SIGNATURE_32('i', 'B', 'F', 'T')
EFI_ACPI_4_0_ISCSI_BOOT_FIRMWARE_TABLE_SIGNATURE  = SIGNATURE_32('i', 'B', 'F', 'T')
# 
# ///
# /// "IVRS" I/O Virtualization Reporting Structure
# ///
# #define EFI_ACPI_4_0_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE  SIGNATURE_32('I', 'V', 'R', 'S')
EFI_ACPI_4_0_IO_VIRTUALIZATION_REPORTING_STRUCTURE_SIGNATURE  = SIGNATURE_32('I', 'V', 'R', 'S')
# 
# ///
# /// "MCFG" PCI Express Memory Mapped Configuration Space Base Address Description Table
# ///
# #define EFI_ACPI_4_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  SIGNATURE_32('M', 'C', 'F', 'G')
EFI_ACPI_4_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_PCI_EXPRESS_MEMORY_MAPPED_CONFIGURATION_SPACE_BASE_ADDRESS_DESCRIPTION_TABLE_SIGNATURE
# 
# ///
# /// "MCHI" Management Controller Host Interface Table
# ///
# #define EFI_ACPI_4_0_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE  SIGNATURE_32('M', 'C', 'H', 'I')
EFI_ACPI_4_0_MANAGEMENT_CONTROLLER_HOST_INTERFACE_TABLE_SIGNATURE  = SIGNATURE_32('M', 'C', 'H', 'I')
# 
# ///
# /// "SPCR" Serial Port Console Redirection Table
# ///
# #define EFI_ACPI_4_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  SIGNATURE_32('S', 'P', 'C', 'R')
EFI_ACPI_4_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_SERIAL_PORT_CONSOLE_REDIRECTION_TABLE_SIGNATURE
# 
# ///
# /// "SPMI" Server Platform Management Interface Table
# ///
# #define EFI_ACPI_4_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  SIGNATURE_32('S', 'P', 'M', 'I')
EFI_ACPI_4_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE  = EFI_ACPI_3_0_SERVER_PLATFORM_MANAGEMENT_INTERFACE_TABLE_SIGNATURE
# 
# ///
# /// "TCPA" Trusted Computing Platform Alliance Capabilities Table
# ///
# #define EFI_ACPI_4_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  SIGNATURE_32('T', 'C', 'P', 'A')
EFI_ACPI_4_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE  = EFI_ACPI_3_0_TRUSTED_COMPUTING_PLATFORM_ALLIANCE_CAPABILITIES_TABLE_SIGNATURE
# 
# ///
# /// "UEFI" UEFI ACPI Data Table
# ///
# #define EFI_ACPI_4_0_UEFI_ACPI_DATA_TABLE_SIGNATURE  SIGNATURE_32('U', 'E', 'F', 'I')
EFI_ACPI_4_0_UEFI_ACPI_DATA_TABLE_SIGNATURE  = SIGNATURE_32('U', 'E', 'F', 'I')
# 
# ///
# /// "WAET" Windows ACPI Enlightenment Table
# ///
# #define EFI_ACPI_4_0_WINDOWS_ACPI_ENLIGHTENMENT_TABLE_SIGNATURE  SIGNATURE_32('W', 'A', 'E', 'T')
EFI_ACPI_4_0_WINDOWS_ACPI_ENLIGHTENMENT_TABLE_SIGNATURE  = SIGNATURE_32('W', 'A', 'E', 'T')
# 
# ///
# /// "WDAT" Watchdog Action Table
# ///
# #define EFI_ACPI_4_0_WATCHDOG_ACTION_TABLE_SIGNATURE  SIGNATURE_32('W', 'D', 'A', 'T')
EFI_ACPI_4_0_WATCHDOG_ACTION_TABLE_SIGNATURE  = EFI_ACPI_3_0_WATCHDOG_ACTION_TABLE_SIGNATURE
# 
# ///
# /// "WDRT" Watchdog Resource Table
# ///
# #define EFI_ACPI_4_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE  SIGNATURE_32('W', 'D', 'R', 'T')
EFI_ACPI_4_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE  = EFI_ACPI_3_0_WATCHDOG_RESOURCE_TABLE_SIGNATURE
# 
# #pragma pack()
# 
# #endif
# 