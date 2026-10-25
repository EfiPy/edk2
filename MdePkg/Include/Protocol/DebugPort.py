# /** @file
# 
#   The file defines the EFI Debugport protocol.
#   This protocol is used by debug agent to communicate with the
#   remote debug host.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# DebugPort.py
#
# EfiPy2.MdePkg.Protocol.DebugPort
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __DEBUG_PORT_H__
# #define __DEBUG_PORT_H__
from EfiPy2  import *

from EfiPy2.MdePkg.Protocol.DevicePathEfiPy  import EFI_DEVICE_PATH_PROTOCOL

# 
# ///
# /// DebugPortIo protocol {EBA4E8D2-3858-41EC-A281-2647BA9660D0}
# ///
# #define EFI_DEBUGPORT_PROTOCOL_GUID \
#   { \
#     0xEBA4E8D2, 0x3858, 0x41EC, {0xA2, 0x81, 0x26, 0x47, 0xBA, 0x96, 0x60, 0xD0 } \
#   }
gEfiDebugPortProtocolGuid               = \
  EFI_GUID (0xEBA4E8D2, 0x3858, 0x41EC, (0xA2, 0x81, 0x26, 0x47, 0xBA, 0x96, 0x60, 0xD0 ))

EFI_DEBUGPORT_PROTOCOL_GUID = gEfiDebugPortProtocolGuid

# 
# extern EFI_GUID  gEfiDebugPortProtocolGuid;
# 
# typedef struct _EFI_DEBUGPORT_PROTOCOL EFI_DEBUGPORT_PROTOCOL;
class EFI_DEBUGPORT_PROTOCOL (Structure):
  pass

# 
# //
# // DebugPort member functions
# //
# 
# /**
#   Resets the debugport.
# 
#   @param  This                  A pointer to the EFI_DEBUGPORT_PROTOCOL instance.
# 
#   @retval EFI_SUCCESS           The debugport device was reset and is in usable state.
#   @retval EFI_DEVICE_ERROR      The debugport device could not be reset and is unusable.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DEBUGPORT_RESET)(
#   IN EFI_DEBUGPORT_PROTOCOL               *This
#   );
EFI_DEBUGPORT_RESET = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL) # IN *This
  )

# 
# /**
#   Writes data to the debugport.
# 
#   @param  This                  A pointer to the EFI_DEBUGPORT_PROTOCOL instance.
#   @param  Timeout               The number of microseconds to wait before timing out a write operation.
#   @param  BufferSize            On input, the requested number of bytes of data to write. On output, the
#                                 number of bytes of data actually written.
#   @param  Buffer                A pointer to a buffer containing the data to write.
# 
#   @retval EFI_SUCCESS           The data was written.
#   @retval EFI_DEVICE_ERROR      The device reported an error.
#   @retval EFI_TIMEOUT           The data write was stopped due to a timeout.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DEBUGPORT_WRITE)(
#   IN EFI_DEBUGPORT_PROTOCOL               *This,
#   IN UINT32                               Timeout,
#   IN OUT UINTN                            *BufferSize,
#   IN VOID                                 *Buffer
#   );
EFI_DEBUGPORT_WRITE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             # IN     *Buffer
  )

# 
# /**
#   Reads data from the debugport.
# 
#   @param  This                  A pointer to the EFI_DEBUGPORT_PROTOCOL instance.
#   @param  Timeout               The number of microseconds to wait before timing out a read operation.
#   @param  BufferSize            On input, the requested number of bytes of data to read. On output, the
#                                 number of bytes of data actually number of bytes
#                                 of data read and returned in Buffer.
#   @param  Buffer                A pointer to a buffer into which the data read will be saved.
# 
#   @retval EFI_SUCCESS           The data was read.
#   @retval EFI_DEVICE_ERROR      The device reported an error.
#   @retval EFI_TIMEOUT           The operation was stopped due to a timeout or overrun.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DEBUGPORT_READ)(
#   IN EFI_DEBUGPORT_PROTOCOL               *This,
#   IN UINT32                               Timeout,
#   IN OUT UINTN                            *BufferSize,
#   OUT VOID                                *Buffer
#   );
EFI_DEBUGPORT_READ = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL),  # IN     *This
  UINT32,                           # IN     Timeout,
  POINTER (UINTN),                  # IN OUT *BufferSize,
  PVOID                             #    OUT *Buffer
  )

# 
# /**
#   Checks to see if any data is available to be read from the debugport device.
# 
#   @param  This                  A pointer to the EFI_DEBUGPORT_PROTOCOL instance.
# 
#   @retval EFI_SUCCESS           At least one byte of data is available to be read.
#   @retval EFI_DEVICE_ERROR      The debugport device is not functioning correctly.
#   @retval EFI_NOT_READY         No data is available to be read.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DEBUGPORT_POLL)(
#   IN EFI_DEBUGPORT_PROTOCOL               *This
#   );
EFI_DEBUGPORT_POLL = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEBUGPORT_PROTOCOL)   # IN     *This
  )

# 
# ///
# /// This protocol provides the communication link between the debug agent and the remote host.
# ///
# struct _EFI_DEBUGPORT_PROTOCOL {
#   EFI_DEBUGPORT_RESET    Reset;
#   EFI_DEBUGPORT_WRITE    Write;
#   EFI_DEBUGPORT_READ     Read;
#   EFI_DEBUGPORT_POLL     Poll;
# };
EFI_DEBUGPORT_PROTOCOL._fields_ = [
    ("Reset",   EFI_DEBUGPORT_RESET),
    ("Write",   EFI_DEBUGPORT_WRITE),
    ("Read",    EFI_DEBUGPORT_READ),
    ("Poll",    EFI_DEBUGPORT_POLL)
  ]

# 
# //
# // DEBUGPORT variable definitions...
# //
# #define EFI_DEBUGPORT_VARIABLE_NAME  L"DEBUGPORT"
# #define EFI_DEBUGPORT_VARIABLE_GUID  EFI_DEBUGPORT_PROTOCOL_GUID
EFI_DEBUGPORT_VARIABLE_NAME = "DEBUGPORT"
EFI_DEBUGPORT_VARIABLE_GUID = EFI_DEBUGPORT_PROTOCOL_GUID

# 
# extern EFI_GUID  gEfiDebugPortVariableGuid;
gEfiDebugPortVariableGuid = gEfiDebugPortProtocolGuid

# 
# //
# // DebugPort device path definitions...
# //
# #define DEVICE_PATH_MESSAGING_DEBUGPORT  EFI_DEBUGPORT_PROTOCOL_GUID
DEVICE_PATH_MESSAGING_DEBUGPORT  = EFI_DEBUGPORT_PROTOCOL_GUID
# 
# extern EFI_GUID  gEfiDebugPortDevicePathGuid;
gEfiDebugPortDevicePathGuid = gEfiDebugPortProtocolGuid
# 
# typedef struct {
#   EFI_DEVICE_PATH_PROTOCOL    Header;
#   EFI_GUID                    Guid;
# } DEBUGPORT_DEVICE_PATH;
class DEBUGPORT_DEVICE_PATH (Structure):
  _fields_ = [
    ("Header",  EFI_DEVICE_PATH_PROTOCOL),
    ("Guid",    EFI_GUID)
  ]

# 
# #endif
# 