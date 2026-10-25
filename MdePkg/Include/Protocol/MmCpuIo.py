# /** @file
#   MM CPU I/O 2 protocol as defined in the PI 1.5 specification.
# 
#   This protocol provides CPU I/O and memory access within MM.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# MmCpuIo.py
#
# EfiPy2.MdePkg.Protocol.MmCpuIo
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _MM_CPU_IO_H_
# #define _MM_CPU_IO_H_
from EfiPy2  import *

# 
# #define EFI_MM_CPU_IO_PROTOCOL_GUID \
#   { \
#     0x3242A9D8, 0xCE70, 0x4AA0, { 0x95, 0x5D, 0x5E, 0x7B, 0x14, 0x0D, 0xE4, 0xD2 } \
#   }
gEfiMmCpuIoProtocolGuid      = EFI_GUID( 0x3242A9D8, 0xCE70, 0x4AA0, ( 0x95, 0x5D, 0x5E, 0x7B, 0x14, 0x0D, 0xE4, 0xD2 ))

# 
# typedef struct _EFI_MM_CPU_IO_PROTOCOL EFI_MM_CPU_IO_PROTOCOL;
class EFI_MM_CPU_IO_PROTOCOL (Structure):
  pass

# 
# ///
# /// Width of the MM CPU I/O operations
# ///
# typedef enum {
#   MM_IO_UINT8  = 0,
#   MM_IO_UINT16 = 1,
#   MM_IO_UINT32 = 2,
#   MM_IO_UINT64 = 3
# } EFI_MM_IO_WIDTH;
MM_IO_UINT8  = 0
MM_IO_UINT16 = 1
MM_IO_UINT32 = 2
MM_IO_UINT64 = 3
EFI_MM_IO_WIDTH = ENUM

# 
# /**
#   Provides the basic memory and I/O interfaces used toabstract accesses to devices.
# 
#   The I/O operations are carried out exactly as requested.  The caller is
#   responsible for any alignment and I/O width issues that the bus, device,
#   platform, or type of I/O might require.
# 
#   @param[in]      This     The EFI_MM_CPU_IO_PROTOCOL instance.
#   @param[in]      Width    Signifies the width of the I/O operations.
#   @param[in]      Address  The base address of the I/O operations.  The caller is
#                            responsible for aligning the Address if required.
#   @param[in]      Count    The number of I/O operations to perform.
#   @param[in,out]  Buffer   For read operations, the destination buffer to store
#                            the results.  For write operations, the source buffer
#                            from which to write data.
# 
#   @retval EFI_SUCCESS            The data was read from or written to the device.
#   @retval EFI_UNSUPPORTED        The Address is not valid for this system.
#   @retval EFI_INVALID_PARAMETER  Width or Count, or both, were invalid.
#   @retval EFI_OUT_OF_RESOURCES   The request could not be completed due to a lack
#                                  of resources.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_MM_CPU_IO)(
#   IN     CONST EFI_MM_CPU_IO_PROTOCOL    *This,
#   IN     EFI_MM_IO_WIDTH                 Width,
#   IN     UINT64                          Address,
#   IN     UINTN                           Count,
#   IN OUT VOID                            *Buffer
#   );
EFI_MM_CPU_IO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_MM_CPU_IO_PROTOCOL),  # IN     CONST *This,
  EFI_MM_IO_WIDTH,                  # IN           Width,
  UINT64,                           # IN           Address,
  UINTN,                            # IN           Count,
  PVOID                             # IN OUT       *Buffer
  )

# 
# typedef struct {
#   ///
#   /// This service provides the various modalities of memory and I/O read.
#   ///
#   EFI_MM_CPU_IO    Read;
#   ///
#   /// This service provides the various modalities of memory and I/O write.
#   ///
#   EFI_MM_CPU_IO    Write;
# } EFI_MM_IO_ACCESS;
class EFI_MM_IO_ACCESS (Structure):
  _fields_ = [
    ("Read",    EFI_MM_CPU_IO),
    ("Write",   EFI_MM_CPU_IO)
  ]

# 
# ///
# /// MM CPU I/O Protocol provides CPU I/O and memory access within MM.
# ///
# struct _EFI_MM_CPU_IO_PROTOCOL {
#   ///
#   /// Allows reads and writes to memory-mapped I/O space.
#   ///
#   EFI_MM_IO_ACCESS    Mem;
#   ///
#   /// Allows reads and writes to I/O space.
#   ///
#   EFI_MM_IO_ACCESS    Io;
# };
EFI_MM_CPU_IO_PROTOCOL._fields_ = [
    ("Mem", EFI_MM_IO_ACCESS),
    ("Io",  EFI_MM_IO_ACCESS)
  ]

# 
# extern EFI_GUID  gEfiMmCpuIoProtocolGuid;
# 
# #endif
# 