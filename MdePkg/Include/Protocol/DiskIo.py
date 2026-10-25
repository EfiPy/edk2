# /** @file
#   Disk IO protocol as defined in the UEFI 2.0 specification.
# 
#   The Disk IO protocol is used to convert block oriented devices into byte
#   oriented devices. The Disk IO protocol is intended to layer on top of the
#   Block IO protocol.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# DiskIo.py
#
# EfiPy2.MdePkg.Protocol.DiskIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __DISK_IO_H__
# #define __DISK_IO_H__
from EfiPy2 import *

# 
# #define EFI_DISK_IO_PROTOCOL_GUID \
#   { \
#     0xce345171, 0xba0b, 0x11d2, {0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b } \
#   }
gEfiDiskIoProtocolGuid      = \
  EFI_GUID (0xce345171, 0xba0b, 0x11d2, (0x8e, 0x4f, 0x0, 0xa0, 0xc9, 0x69, 0x72, 0x3b ))

# 
# ///
# /// Protocol GUID name defined in EFI1.1.
# ///
# #define DISK_IO_PROTOCOL  EFI_DISK_IO_PROTOCOL_GUID
DISK_IO_PROTOCOL  = gEfiDiskIoProtocolGuid

# 
# typedef struct _EFI_DISK_IO_PROTOCOL EFI_DISK_IO_PROTOCOL;
class EFI_DISK_IO_PROTOCOL (Structure):
  pass

# 
# ///
# /// Protocol defined in EFI1.1.
# ///
# typedef EFI_DISK_IO_PROTOCOL EFI_DISK_IO;
# 
# /**
#   Read BufferSize bytes from Offset into Buffer.
# 
#   @param  This                  Protocol instance pointer.
#   @param  MediaId               Id of the media, changes every time the media is replaced.
#   @param  Offset                The starting byte offset to read from
#   @param  BufferSize            Size of Buffer
#   @param  Buffer                Buffer containing read data
# 
#   @retval EFI_SUCCESS           The data was read correctly from the device.
#   @retval EFI_DEVICE_ERROR      The device reported an error while performing the read.
#   @retval EFI_NO_MEDIA          There is no media in the device.
#   @retval EFI_MEDIA_CHNAGED     The MediaId does not matched the current device.
#   @retval EFI_INVALID_PARAMETER The read request contains device addresses that are not
#                                 valid for the device.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DISK_READ)(
#   IN EFI_DISK_IO_PROTOCOL         *This,
#   IN UINT32                       MediaId,
#   IN UINT64                       Offset,
#   IN UINTN                        BufferSize,
#   OUT VOID                        *Buffer
#   );
EFI_DISK_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # OUT *Buffer
  )

# 
# /**
#   Writes a specified number of bytes to a device.
# 
#   @param  This       Indicates a pointer to the calling context.
#   @param  MediaId    ID of the medium to be written.
#   @param  Offset     The starting byte offset on the logical block I/O device to write.
#   @param  BufferSize The size in bytes of Buffer. The number of bytes to write to the device.
#   @param  Buffer     A pointer to the buffer containing the data to be written.
# 
#   @retval EFI_SUCCESS           The data was written correctly to the device.
#   @retval EFI_WRITE_PROTECTED   The device can not be written to.
#   @retval EFI_DEVICE_ERROR      The device reported an error while performing the write.
#   @retval EFI_NO_MEDIA          There is no media in the device.
#   @retval EFI_MEDIA_CHNAGED     The MediaId does not matched the current device.
#   @retval EFI_INVALID_PARAMETER The write request contains device addresses that are not
#                                  valid for the device.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DISK_WRITE)(
#   IN EFI_DISK_IO_PROTOCOL         *This,
#   IN UINT32                       MediaId,
#   IN UINT64                       Offset,
#   IN UINTN                        BufferSize,
#   IN VOID                         *Buffer
#   );
EFI_DISK_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DISK_IO_PROTOCOL),    # IN  *This
  UINT32,                           # IN  MediaId,
  UINT64,                           # IN  Offset,
  UINTN,                            # IN  BufferSize,
  PVOID                             # IN  *Buffer
  )

# 
# #define EFI_DISK_IO_PROTOCOL_REVISION  0x00010000
EFI_DISK_IO_PROTOCOL_REVISION = 0x00010000

# 
# ///
# /// Revision defined in EFI1.1
# ///
# #define EFI_DISK_IO_INTERFACE_REVISION  EFI_DISK_IO_PROTOCOL_REVISION
EFI_DISK_IO_INTERFACE_REVISION  = EFI_DISK_IO_PROTOCOL_REVISION

# 
# ///
# /// This protocol is used to abstract Block I/O interfaces.
# ///
# struct _EFI_DISK_IO_PROTOCOL {
#   ///
#   /// The revision to which the disk I/O interface adheres. All future
#   /// revisions must be backwards compatible. If a future version is not
#   /// backwards compatible, it is not the same GUID.
#   ///
#   UINT64            Revision;
#   EFI_DISK_READ     ReadDisk;
#   EFI_DISK_WRITE    WriteDisk;
# };
EFI_DISK_IO_PROTOCOL._fields_ = [
    ("Revision",  UINT64),
    ("ReadDisk",  EFI_DISK_READ),
    ("WriteDisk", EFI_DISK_WRITE)
  ]

# 
# extern EFI_GUID  gEfiDiskIoProtocolGuid;
# 
# #endif
# 