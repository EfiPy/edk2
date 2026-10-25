# /** @file
#   UGA IO protocol from the EFI 1.10 specification.
# 
#   Abstraction of a very simple graphics device.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# UgaIo.py
#
# EfiPy2.MdePkg.Protocol.UgaIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __UGA_IO_H__
# #define __UGA_IO_H__
from EfiPy2 import *

# 
# #define EFI_UGA_IO_PROTOCOL_GUID \
#   { 0x61a4d49e, 0x6f68, 0x4f1b, { 0xb9, 0x22, 0xa8, 0x6e, 0xed, 0xb, 0x7, 0xa2 } }
gEfiUgaIoProtocolGuid   = \
  EFI_GUID (0x61a4d49e, 0x6f68, 0x4f1b, ( 0xb9, 0x22, 0xa8, 0x6e, 0xed, 0xb, 0x7, 0xa2 ))

# 
# typedef struct _EFI_UGA_IO_PROTOCOL EFI_UGA_IO_PROTOCOL;
class EFI_UGA_IO_PROTOCOL (Structure):
  pass

# 
# typedef UINT32 UGA_STATUS;
UGA_STATUS      = UINT32

# 
# typedef enum {
#   UgaDtParentBus = 1,
#   UgaDtGraphicsController,
#   UgaDtOutputController,
#   UgaDtOutputPort,
#   UgaDtOther
# } UGA_DEVICE_TYPE, *PUGA_DEVICE_TYPE;
UgaDtParentBus            = 1
UgaDtGraphicsController   = 2
UgaDtOutputController     = 3
UgaDtOutputPort           = 4
UgaDtOther                = 5
UGA_DEVICE_TYPE           = ENUM

# 
# typedef UINT32 UGA_DEVICE_ID, *PUGA_DEVICE_ID;
UGA_DEVICE_ID   = UINT32
PUGA_DEVICE_ID  = POINTER(UGA_DEVICE_ID)

# 
# typedef struct {
#   UGA_DEVICE_TYPE    deviceType;
#   UGA_DEVICE_ID      deviceId;
#   UINT32             ui32DeviceContextSize;
#   UINT32             ui32SharedContextSize;
# } UGA_DEVICE_DATA, *PUGA_DEVICE_DATA;
class UGA_DEVICE_DATA (Structure):
  _fields_ = [
    ("deviceType",            UGA_DEVICE_TYPE),
    ("deviceId",              UGA_DEVICE_ID),
    ("ui32DeviceContextSize", UINT32),
    ("ui32SharedContextSize", UINT32)
  ]
PUGA_DEVICE_DATA  = POINTER(UGA_DEVICE_DATA)

# 
# typedef struct _UGA_DEVICE {
#   VOID                  *pvDeviceContext;
#   VOID                  *pvSharedContext;
#   VOID                  *pvRunTimeContext;
#   struct _UGA_DEVICE    *pParentDevice;
#   VOID                  *pvBusIoServices;
#   VOID                  *pvStdIoServices;
#   UGA_DEVICE_DATA       deviceData;
# } UGA_DEVICE, *PUGA_DEVICE;
class UGA_DEVICE (Structure):
  pass

PUGA_DEVICE  = POINTER(UGA_DEVICE)

UGA_DEVICE._fields_ = [
    ("pvDeviceContext",   PVOID),
    ("pvSharedContext",   PVOID),
    ("pvRunTimeContext",  PVOID),
    ("pParentDevice",     POINTER(UGA_DEVICE)),
    ("pvBusIoServices",   PVOID),
    ("pvStdIoServices",   PVOID),
    ("deviceData",        UGA_DEVICE_DATA)
  ]

# 
# typedef enum {
#   UgaIoGetVersion = 1,
#   UgaIoGetChildDevice,
#   UgaIoStartDevice,
#   UgaIoStopDevice,
#   UgaIoFlushDevice,
#   UgaIoResetDevice,
#   UgaIoGetDeviceState,
#   UgaIoSetDeviceState,
#   UgaIoSetPowerState,
#   UgaIoGetMemoryConfiguration,
#   UgaIoSetVideoMode,
#   UgaIoCopyRectangle,
#   UgaIoGetEdidSegment,
#   UgaIoDeviceChannelOpen,
#   UgaIoDeviceChannelClose,
#   UgaIoDeviceChannelRead,
#   UgaIoDeviceChannelWrite,
#   UgaIoGetPersistentDataSize,
#   UgaIoGetPersistentData,
#   UgaIoSetPersistentData,
#   UgaIoGetDevicePropertySize,
#   UgaIoGetDeviceProperty,
#   UgaIoBtPrivateInterface
# } UGA_IO_REQUEST_CODE, *PUGA_IO_REQUEST_CODE;
UgaIoGetVersion             = 1
UgaIoGetChildDevice         = 2
UgaIoStartDevice            = 3
UgaIoStopDevice             = 4
UgaIoFlushDevice            = 5
UgaIoResetDevice            = 6
UgaIoGetDeviceState         = 7
UgaIoSetDeviceState         = 8
UgaIoSetPowerState          = 9
UgaIoGetMemoryConfiguration = 10
UgaIoSetVideoMode           = 11
UgaIoCopyRectangle          = 12
UgaIoGetEdidSegment         = 13
UgaIoDeviceChannelOpen      = 14
UgaIoDeviceChannelClose     = 15
UgaIoDeviceChannelRead      = 16
UgaIoDeviceChannelWrite     = 17
UgaIoGetPersistentDataSize  = 18
UgaIoGetPersistentData      = 19
UgaIoSetPersistentData      = 20
UgaIoGetDevicePropertySize  = 21
UgaIoGetDeviceProperty      = 22
UgaIoBtPrivateInterface     = 23
UGA_IO_REQUEST_CODE         = ENUM
PUGA_IO_REQUEST_CODE = POINTER (UGA_IO_REQUEST_CODE)

# 
# typedef struct {
#   IN UGA_IO_REQUEST_CODE    ioRequestCode;
#   IN VOID                   *pvInBuffer;
#   IN UINT64                 ui64InBufferSize;
#   OUT VOID                  *pvOutBuffer;
#   IN UINT64                 ui64OutBufferSize;
#   OUT UINT64                ui64BytesReturned;
# } UGA_IO_REQUEST, *PUGA_IO_REQUEST;
class UGA_IO_REQUEST (Structure):
  _fields_ = [
    ("ioRequestCode",     UGA_IO_REQUEST_CODE), #   IN
    ("pvInBuffer",        PVOID),               #   IN
    ("ui64InBufferSize",  UINT64),              #   IN
    ("pvOutBuffer",       PVOID),               #   OUT
    ("ui64OutBufferSize", UINT64),              #   IN
    ("ui64BytesReturned", UINT64)               #   OUT
  ]
PUGA_IO_REQUEST = POINTER (UGA_IO_REQUEST)

# 
# /**
#   Dynamically allocate storage for a child UGA_DEVICE.
# 
#   @param[in]     This            The EFI_UGA_IO_PROTOCOL instance.
#   @param[in]     ParentDevice    ParentDevice specifies a pointer to the parent device of Device.
#   @param[in]     DeviceData      A pointer to UGA_DEVICE_DATA returned from a call to DispatchService()
#                                  with a UGA_DEVICE of Parent and an IoRequest of type UgaIoGetChildDevice.
#   @param[in]     RunTimeContext  Context to associate with Device.
#   @param[out]    Device          The Device returns a dynamically allocated child UGA_DEVICE object
#                                  for ParentDevice. The caller is responsible for deleting Device.
# 
# 
#   @retval  EFI_SUCCESS           Device was returned.
#   @retval  EFI_INVALID_PARAMETER One of the arguments was not valid.
#   @retval  EFI_DEVICE_ERROR      The device had an error and could not complete the request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_UGA_IO_PROTOCOL_CREATE_DEVICE)(
#   IN  EFI_UGA_IO_PROTOCOL  *This,
#   IN  UGA_DEVICE           *ParentDevice,
#   IN  UGA_DEVICE_DATA      *DeviceData,
#   IN  VOID                 *RunTimeContext,
#   OUT UGA_DEVICE           **Device
#   );
EFI_UGA_IO_PROTOCOL_CREATE_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_IO_PROTOCOL), # IN  *This
  POINTER(UGA_DEVICE),          # IN  *ParentDevice,
  POINTER(UGA_DEVICE_DATA),     # IN  *DeviceData,
  PVOID,                        # IN  *RunTimeContext,
  POINTER(POINTER(UGA_DEVICE))  # OUT **Device
  )
  
# 
# /**
#   Delete a dynamically allocated child UGA_DEVICE object that was allocated via CreateDevice().
# 
#   @param[in]     This            The EFI_UGA_IO_PROTOCOL instance. Type EFI_UGA_IO_PROTOCOL is
#                                  defined in Section 10.7.
#   @param[in]     Device          The Device points to a UGA_DEVICE object that was dynamically
#                                  allocated via a CreateDevice() call.
# 
# 
#   @retval  EFI_SUCCESS           Device was returned.
#   @retval  EFI_INVALID_PARAMETER The Device was not allocated via CreateDevice().
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_UGA_IO_PROTOCOL_DELETE_DEVICE)(
#   IN EFI_UGA_IO_PROTOCOL  *This,
#   IN UGA_DEVICE           *Device
#   );
EFI_UGA_IO_PROTOCOL_DELETE_DEVICE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UGA_IO_PROTOCOL), # IN  *This
  POINTER(UGA_DEVICE)           # OUT *Device
  )
  
# 
# /**
#   This is the main UGA service dispatch routine for all UGA_IO_REQUEST s.
# 
#   @param pDevice pDevice specifies a pointer to a device object associated with a
#                  device enumerated by a pIoRequest->ioRequestCode of type
#                  UgaIoGetChildDevice. The root device for the EFI_UGA_IO_PROTOCOL
#                  is represented by pDevice being set to NULL.
# 
#   @param pIoRequest
#                  pIoRequest points to a caller allocated buffer that contains data
#                  defined by pIoRequest->ioRequestCode. See Related Definitions for
#                  a definition of UGA_IO_REQUEST_CODE s and their associated data
#                  structures.
# 
#   @return UGA_STATUS
# 
# **/
# typedef UGA_STATUS
# (EFIAPI *PUGA_FW_SERVICE_DISPATCH)(
#   IN PUGA_DEVICE pDevice,
#   IN OUT PUGA_IO_REQUEST pIoRequest
#   );
PUGA_FW_SERVICE_DISPATCH = CFUNCTYPE (
  UGA_STATUS,
  PUGA_DEVICE,          # IN      pDevice
  PUGA_IO_REQUEST       # IN  OUT pIoRequest
  )

# 
# ///
# /// Provides a basic abstraction to send I/O requests to the graphics device and any of its children.
# ///
# struct _EFI_UGA_IO_PROTOCOL {
#   EFI_UGA_IO_PROTOCOL_CREATE_DEVICE    CreateDevice;
#   EFI_UGA_IO_PROTOCOL_DELETE_DEVICE    DeleteDevice;
#   PUGA_FW_SERVICE_DISPATCH             DispatchService;
# };
EFI_UGA_IO_PROTOCOL._fields_ = [
    ("CreateDevice",    EFI_UGA_IO_PROTOCOL_CREATE_DEVICE),
    ("DeleteDevice",    EFI_UGA_IO_PROTOCOL_DELETE_DEVICE),
    ("DispatchService", PUGA_FW_SERVICE_DISPATCH)
  ]

# 
# extern EFI_GUID  gEfiUgaIoProtocolGuid;
# 
# //
# // Data structure that is stored in the EFI Configuration Table with the
# // EFI_UGA_IO_PROTOCOL_GUID.  The option ROMs listed in this table may have
# // EBC UGA drivers.
# //
# typedef struct {
#   UINT32    Version;
#   UINT32    HeaderSize;
#   UINT32    SizeOfEntries;
#   UINT32    NumberOfEntries;
# } EFI_DRIVER_OS_HANDOFF_HEADER;
class EFI_DRIVER_OS_HANDOFF_HEADER (Structure):
  _fields_ = [
    ("Version",         UINT32),
    ("HeaderSize",      UINT32),
    ("SizeOfEntries",   UINT32),
    ("NumberOfEntries", UINT32)
  ]

# 
# typedef enum {
#   EfiUgaDriverFromPciRom,
#   EfiUgaDriverFromSystem,
#   EfiDriverHandoffMax
# } EFI_DRIVER_HANOFF_ENUM;
EfiUgaDriverFromPciRom  = 0
EfiUgaDriverFromSystem  = 1
EfiDriverHandoffMax     = 2
EFI_DRIVER_HANOFF_ENUM  = ENUM

# 
# typedef struct {
#   EFI_DRIVER_HANOFF_ENUM      Type;
#   EFI_DEVICE_PATH_PROTOCOL    *DevicePath;
#   VOID                        *PciRomImage;
#   UINT64                      PciRomSize;
# } EFI_DRIVER_OS_HANDOFF;
class EFI_DRIVER_OS_HANDOFF (Structure):
  _fields_ = [
    ("Type",        EFI_DRIVER_HANOFF_ENUM),
    ("DevicePath",  POINTER(EFI_DEVICE_PATH_PROTOCOL)),
    ("PciRomImage", PVOID),
    ("PciRomSize",  UINT64)
  ]

# 
# #endif
# 