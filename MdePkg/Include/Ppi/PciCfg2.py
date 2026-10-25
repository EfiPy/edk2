# /** @file
#   This file declares PciCfg2 PPI.
# 
#   This ppi Provides platform or chipset-specific access to
#   the PCI configuration space for a specific PCI segment.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This PPI is introduced in PI Version 1.0.
# 
# **/
# PciCfg2.py
#
# EfiPy2.MdePkg.Ppi.PciCfg2
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __PEI_PCI_CFG2_H__
# #define __PEI_PCI_CFG2_H__
from EfiPy2 import *

# 
# #include <Library/BaseLib.h>
# 
# #define EFI_PEI_PCI_CFG2_PPI_GUID \
#   { 0x57a449a, 0x1fdc, 0x4c06, { 0xbf, 0xc9, 0xf5, 0x3f, 0x6a, 0x99, 0xbb, 0x92 } }
gEfiPciCfg2PpiGuid            = \
  EFI_GUID (0x57a449a, 0x1fdc, 0x4c06, ( 0xbf, 0xc9, 0xf5, 0x3f, 0x6a, 0x99, 0xbb, 0x92 ))

# 
# typedef struct _EFI_PEI_PCI_CFG2_PPI EFI_PEI_PCI_CFG2_PPI;
class EFI_PEI_PCI_CFG2_PPI (Structure):
  pass

from EfiPy2.MdePkg.Pi.PiPeiCis import EFI_PEI_SERVICES

# 
# #define EFI_PEI_PCI_CFG_ADDRESS(bus, dev, func, reg) \
#   (UINT64) ( \
#   (((UINTN) bus) << 24) | \
#   (((UINTN) dev) << 16) | \
#   (((UINTN) func) << 8) | \
#   (((UINTN) (reg)) < 256 ? ((UINTN) (reg)) : (UINT64) (LShiftU64 ((UINT64) (reg), 32))))
def EFI_PEI_PCI_CFG_ADDRESS(bus, dev, func, reg):
  if reg < 256:
   return (bus  << 24) | \
          (dev  << 16) | \
          (func << 8 ) | \
           reg

  return (bus  << 24) | \
         (dev  << 16) | \
         (func << 8 ) | \
          reg  << 32

# 
# ///
# /// EFI_PEI_PCI_CFG_PPI_WIDTH
# ///
# typedef enum {
#   ///
#   ///  8-bit access
#   ///
#   EfiPeiPciCfgWidthUint8 = 0,
#   ///
#   /// 16-bit access
#   ///
#   EfiPeiPciCfgWidthUint16 = 1,
#   ///
#   /// 32-bit access
#   ///
#   EfiPeiPciCfgWidthUint32 = 2,
#   ///
#   /// 64-bit access
#   ///
#   EfiPeiPciCfgWidthUint64 = 3,
#   EfiPeiPciCfgWidthMaximum
# } EFI_PEI_PCI_CFG_PPI_WIDTH;
EfiPeiPciCfgWidthUint8    = 0
EfiPeiPciCfgWidthUint16   = 1
EfiPeiPciCfgWidthUint32   = 2
EfiPeiPciCfgWidthUint64   = 3
EfiPeiPciCfgWidthMaximum  = 4
EFI_PEI_PCI_CFG_PPI_WIDTH = ENUM

# 
# ///
# /// EFI_PEI_PCI_CFG_PPI_PCI_ADDRESS
# ///
# typedef struct {
#   ///
#   /// 8-bit register offset within the PCI configuration space for a given device's function
#   /// space.
#   ///
#   UINT8     Register;
#   ///
#   /// Only the 3 least-significant bits are used to encode one of 8 possible functions within a
#   /// given device.
#   ///
#   UINT8     Function;
#   ///
#   /// Only the 5 least-significant bits are used to encode one of 32 possible devices.
#   ///
#   UINT8     Device;
#   ///
#   /// 8-bit value to encode between 0 and 255 buses.
#   ///
#   UINT8     Bus;
#   ///
#   /// Register number in PCI configuration space. If this field is zero, then Register is used
#   /// for the register number. If this field is non-zero, then Register is ignored and this field
#   /// is used for the register number.
#   ///
#   UINT32    ExtendedRegister;
# } EFI_PEI_PCI_CFG_PPI_PCI_ADDRESS;
class EFI_PEI_PCI_CFG_PPI_PCI_ADDRESS (Structure):
  _fields_ = [
    ("Register",            UINT8),
    ("Function",            UINT8),
    ("Device",              UINT8),
    ("Bus",                 UINT8),
    ("ExtendedRegister",    UINT32)
  ]

# 
# /**
#   Reads from or write to a given location in the PCI configuration space.
# 
#   @param  PeiServices     An indirect pointer to the PEI Services Table published by the PEI Foundation.
# 
#   @param  This            Pointer to local data for the interface.
# 
#   @param  Width           The width of the access. Enumerated in bytes.
#                           See EFI_PEI_PCI_CFG_PPI_WIDTH above.
# 
#   @param  Address         The physical address of the access. The format of
#                           the address is described by EFI_PEI_PCI_CFG_PPI_PCI_ADDRESS.
# 
#   @param  Buffer          A pointer to the buffer of data..
# 
# 
#   @retval EFI_SUCCESS           The function completed successfully.
# 
#   @retval EFI_DEVICE_ERROR      There was a problem with the transaction.
# 
#   @retval EFI_DEVICE_NOT_READY  The device is not capable of supporting the operation at this
#                                 time.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_PEI_PCI_CFG2_PPI_IO)(
#   IN CONST  EFI_PEI_SERVICES          **PeiServices,
#   IN CONST  EFI_PEI_PCI_CFG2_PPI      *This,
#   IN        EFI_PEI_PCI_CFG_PPI_WIDTH Width,
#   IN        UINT64                    Address,
#   IN OUT    VOID                      *Buffer
#   );
EFI_PEI_PCI_CFG2_PPI_IO = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_PCI_CFG2_PPI),        # IN     CONST *This,
  EFI_PEI_PCI_CFG_PPI_WIDTH,            # IN           Width
  UINT64,                               # IN           Address
  PVOID                                 # IN OUT       *Buffer
  )

# 
# /**
#   Performs a read-modify-write operation on the contents
#   from a given location in the PCI configuration space.
# 
#   @param  PeiServices     An indirect pointer to the PEI Services Table
#                           published by the PEI Foundation.
# 
#   @param  This            Pointer to local data for the interface.
# 
#   @param  Width           The width of the access. Enumerated in bytes. Type
#                           EFI_PEI_PCI_CFG_PPI_WIDTH is defined in Read().
# 
#   @param  Address         The physical address of the access.
# 
#   @param  SetBits         Points to value to bitwise-OR with the read configuration value.
# 
#                           The size of the value is determined by Width.
# 
#   @param  ClearBits       Points to the value to negate and bitwise-AND with the read configuration value.
#                           The size of the value is determined by Width.
# 
# 
#   @retval EFI_SUCCESS           The function completed successfully.
# 
#   @retval EFI_DEVICE_ERROR      There was a problem with the transaction.
# 
#   @retval EFI_DEVICE_NOT_READY  The device is not capable of supporting
#                                 the operation at this time.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_PEI_PCI_CFG2_PPI_RW)(
#   IN CONST  EFI_PEI_SERVICES          **PeiServices,
#   IN CONST  EFI_PEI_PCI_CFG2_PPI      *This,
#   IN        EFI_PEI_PCI_CFG_PPI_WIDTH Width,
#   IN        UINT64                    Address,
#   IN        VOID                      *SetBits,
#   IN        VOID                      *ClearBits
#   );
EFI_PEI_PCI_CFG2_PPI_RW = CFUNCTYPE (
  UINT8,
  POINTER(POINTER(EFI_PEI_SERVICES)),   # IN     CONST **PeiServices,
  POINTER(EFI_PEI_PCI_CFG2_PPI),        # IN     CONST *This,
  EFI_PEI_PCI_CFG_PPI_WIDTH,            # IN           Width
  UINT64,                               # IN           Address
  PVOID,                                # IN           *SetBits
  PVOID                                 # IN           *ClearBits
  )

# 
# ///
# /// The EFI_PEI_PCI_CFG_PPI interfaces are used to abstract accesses to PCI
# /// controllers behind a PCI root bridge controller.
# ///
# struct _EFI_PEI_PCI_CFG2_PPI {
#   EFI_PEI_PCI_CFG2_PPI_IO    Read;
#   EFI_PEI_PCI_CFG2_PPI_IO    Write;
#   EFI_PEI_PCI_CFG2_PPI_RW    Modify;
#   ///
#   /// The PCI bus segment which the specified functions will access.
#   ///
#   UINT16                     Segment;
# };
EFI_PEI_PCI_CFG2_PPI._fields_ = [
    ("Read",    EFI_PEI_PCI_CFG2_PPI_IO),
    ("Write",   EFI_PEI_PCI_CFG2_PPI_IO),
    ("Modify",  EFI_PEI_PCI_CFG2_PPI_RW),
    ("Segment", UINT16)
  ]

# 
# extern EFI_GUID  gEfiPciCfg2PpiGuid;
# 
# #endif
# 