# /** @file
#   The USB Function Protocol provides an I/O abstraction for a USB Controller
#   operating in Function mode (also commonly referred to as Device, Peripheral,
#   or Target mode) and the mechanisms by which the USB Function can communicate
#   with the USB Host. It is used by other UEFI drivers or applications to
#   perform data transactions and basic USB controller management over a USB
#   Function port.
# 
#   This simple protocol only supports USB 2.0 bulk transfers on systems with a
#   single configuration and a single interface. It does not support isochronous
#   or interrupt transfers, alternate interfaces, or USB 3.0 functionality.
#   Future revisions of this protocol may support these or additional features.
# 
#   Copyright (c) 2015 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol was introduced in UEFI Specification 2.5.
# 
# **/
# UsbFunctionIo.py
#
# EfiPy2.MdePkg.Protocol.UsbFunctionIo
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __USB_FUNCTION_IO_H__
# #define __USB_FUNCTION_IO_H__
from EfiPy2 import *

# 
# #include <Protocol/UsbIo.h>
from EfiPy2.MdePkg.Protocol.UsbIo import    EFI_USB_INTERFACE_DESCRIPTOR,   \
                                            EFI_USB_ENDPOINT_DESCRIPTOR,    \
                                            EFI_USB_CONFIG_DESCRIPTOR,      \
                                            EFI_USB_DEVICE_DESCRIPTOR,      \
                                            EFI_USB_DEVICE_REQUEST

# 
# #define EFI_USBFN_IO_PROTOCOL_GUID \
#     { \
#       0x32d2963a, 0xfe5d, 0x4f30, {0xb6, 0x33, 0x6e, 0x5d, 0xc5, 0x58, 0x3, 0xcc} \
#     }
gEfiUsbFunctionIoProtocolGuid = \
  EFI_GUID (0x32d2963a, 0xfe5d, 0x4f30, (0xb6, 0x33, 0x6e, 0x5d, 0xc5, 0x58, 0x3, 0xcc))

# 
# typedef struct _EFI_USBFN_IO_PROTOCOL EFI_USBFN_IO_PROTOCOL;
class EFI_USBFN_IO_PROTOCOL (Structure):
  pass

# 
# #define EFI_USBFN_IO_PROTOCOL_REVISION  0x00010001
# 
# typedef enum _EFI_USBFN_PORT_TYPE {
#   EfiUsbUnknownPort = 0,
#   EfiUsbStandardDownstreamPort,
#   EfiUsbChargingDownstreamPort,
#   EfiUsbDedicatedChargingPort,
#   EfiUsbInvalidDedicatedChargingPort
# } EFI_USBFN_PORT_TYPE;
EfiUsbUnknownPort                   = 0
EfiUsbStandardDownstreamPort        = 1
EfiUsbChargingDownstreamPort        = 2
EfiUsbDedicatedChargingPort         = 3
EfiUsbInvalidDedicatedChargingPort  = 4
EFI_USBFN_PORT_TYPE                 = ENUM

# 
# typedef struct {
#   EFI_USB_INTERFACE_DESCRIPTOR    *InterfaceDescriptor;
#   EFI_USB_ENDPOINT_DESCRIPTOR     **EndpointDescriptorTable;
# } EFI_USB_INTERFACE_INFO;
class EFI_USB_INTERFACE_INFO (Structure):
  _fields_ = [
    ("InterfaceDescriptor",     POINTER(EFI_USB_INTERFACE_DESCRIPTOR)),
    ("EndpointDescriptorTable", POINTER(POINTER(EFI_USB_ENDPOINT_DESCRIPTOR)))
  ]

# 
# typedef struct {
#   EFI_USB_CONFIG_DESCRIPTOR    *ConfigDescriptor;
#   EFI_USB_INTERFACE_INFO       **InterfaceInfoTable;
# } EFI_USB_CONFIG_INFO;
class EFI_USB_CONFIG_INFO (Structure):
  _fields_ = [
    ("ConfigDescriptor",    POINTER(EFI_USB_CONFIG_DESCRIPTOR)),
    ("InterfaceInfoTable",  POINTER(POINTER(EFI_USB_INTERFACE_INFO)))
  ]

# 
# typedef struct {
#   EFI_USB_DEVICE_DESCRIPTOR    *DeviceDescriptor;
#   EFI_USB_CONFIG_INFO          **ConfigInfoTable;
# } EFI_USB_DEVICE_INFO;
class EFI_USB_DEVICE_INFO (Structure):
  _fields_ = [
    ("DeviceDescriptor",  POINTER(EFI_USB_DEVICE_DESCRIPTOR)),
    ("ConfigInfoTable",   POINTER(POINTER(EFI_USB_CONFIG_INFO)))
  ]

# 
# typedef enum _EFI_USB_ENDPOINT_TYPE {
#   UsbEndpointControl = 0x00,
#   // UsbEndpointIsochronous = 0x01,
#   UsbEndpointBulk = 0x02,
#   // UsbEndpointInterrupt = 0x03
# } EFI_USB_ENDPOINT_TYPE;
UsbEndpointControl      = 0x00
# UsbEndpointIsochronous  = 0x01
UsbEndpointBulk         = 0x02
# UsbEndpointInterrupt    = 0x03
EFI_USB_ENDPOINT_TYPE   = ENUM

# 
# typedef enum _EFI_USBFN_DEVICE_INFO_ID {
#   EfiUsbDeviceInfoUnknown = 0,
#   EfiUsbDeviceInfoSerialNumber,
#   EfiUsbDeviceInfoManufacturerName,
#   EfiUsbDeviceInfoProductName
# } EFI_USBFN_DEVICE_INFO_ID;
EfiUsbDeviceInfoUnknown           = 0
EfiUsbDeviceInfoSerialNumber      = 1
EfiUsbDeviceInfoManufacturerName  = 2
EfiUsbDeviceInfoProductName       = 3
EFI_USBFN_DEVICE_INFO_ID          = ENUM

# 
# typedef enum _EFI_USBFN_ENDPOINT_DIRECTION {
#   EfiUsbEndpointDirectionHostOut = 0,
#   EfiUsbEndpointDirectionHostIn,
#   EfiUsbEndpointDirectionDeviceTx = EfiUsbEndpointDirectionHostIn,
#   EfiUsbEndpointDirectionDeviceRx = EfiUsbEndpointDirectionHostOut
# } EFI_USBFN_ENDPOINT_DIRECTION;
EfiUsbEndpointDirectionHostOut  = 0
EfiUsbEndpointDirectionHostIn   = 1
EfiUsbEndpointDirectionDeviceTx = EfiUsbEndpointDirectionHostIn,
EfiUsbEndpointDirectionDeviceRx = EfiUsbEndpointDirectionHostOut
EFI_USBFN_ENDPOINT_DIRECTION    = ENUM

# 
# typedef enum _EFI_USBFN_MESSAGE {
#   //
#   // Nothing
#   //
#   EfiUsbMsgNone = 0,
#   //
#   // SETUP packet is received, returned Buffer contains
#   // EFI_USB_DEVICE_REQUEST struct
#   //
#   EfiUsbMsgSetupPacket,
#   //
#   // Indicates that some of the requested data has been received from the
#   // host. It is the responsibility of the class driver to determine if it
#   // needs to wait for any remaining data. Returned Buffer contains
#   // EFI_USBFN_TRANSFER_RESULT struct containing endpoint number, transfer
#   // status and count of bytes received.
#   //
#   EfiUsbMsgEndpointStatusChangedRx,
#   //
#   // Indicates that some of the requested data has been transmitted to the
#   // host. It is the responsibility of the class driver to determine if any
#   // remaining data needs to be resent. Returned Buffer contains
#   // EFI_USBFN_TRANSFER_RESULT struct containing endpoint number, transfer
#   // status and count of bytes sent.
#   //
#   EfiUsbMsgEndpointStatusChangedTx,
#   //
#   // DETACH bus event signaled
#   //
#   EfiUsbMsgBusEventDetach,
#   //
#   // ATTACH bus event signaled
#   //
#   EfiUsbMsgBusEventAttach,
#   //
#   // RESET bus event signaled
#   //
#   EfiUsbMsgBusEventReset,
#   //
#   // SUSPEND bus event signaled
#   //
#   EfiUsbMsgBusEventSuspend,
#   //
#   // RESUME bus event signaled
#   //
#   EfiUsbMsgBusEventResume,
#   //
#   // Bus speed updated, returned buffer indicated bus speed using
#   // following enumeration named EFI_USB_BUS_SPEED
#   //
#   EfiUsbMsgBusEventSpeed
# } EFI_USBFN_MESSAGE;
EfiUsbMsgNone                     = 0
EfiUsbMsgSetupPacket              = 1
EfiUsbMsgEndpointStatusChangedRx  = 2
EfiUsbMsgEndpointStatusChangedTx  = 3
EfiUsbMsgBusEventDetach           = 4
EfiUsbMsgBusEventAttach           = 5
EfiUsbMsgBusEventReset            = 6
EfiUsbMsgBusEventSuspend          = 7
EfiUsbMsgBusEventResume           = 8
EfiUsbMsgBusEventSpeed            = 9
EFI_USBFN_MESSAGE                 = ENUM

# 
# typedef enum _EFI_USBFN_TRANSFER_STATUS {
#   UsbTransferStatusUnknown = 0,
#   UsbTransferStatusComplete,
#   UsbTransferStatusAborted,
#   UsbTransferStatusActive,
#   UsbTransferStatusNone
# } EFI_USBFN_TRANSFER_STATUS;
UsbTransferStatusUnknown    = 0
UsbTransferStatusComplete   = 1
UsbTransferStatusAborted    = 2
UsbTransferStatusActive     = 3
UsbTransferStatusNone       = 4
EFI_USBFN_TRANSFER_STATUS   = ENUM

# 
# typedef struct _EFI_USBFN_TRANSFER_RESULT {
#   UINTN                           BytesTransferred;
#   EFI_USBFN_TRANSFER_STATUS       TransferStatus;
#   UINT8                           EndpointIndex;
#   EFI_USBFN_ENDPOINT_DIRECTION    Direction;
#   VOID                            *Buffer;
# } EFI_USBFN_TRANSFER_RESULT;
class EFI_USBFN_TRANSFER_RESULT (Structure):
  _fields_ = [
    ("BytesTransferred",  UINTN),
    ("TransferStatus",    EFI_USBFN_TRANSFER_STATUS),
    ("EndpointIndex",     UINT8),
    ("Direction",         EFI_USBFN_ENDPOINT_DIRECTION),
    ("Buffer",            PVOID)
  ]

# 
# typedef enum _EFI_USB_BUS_SPEED {
#   UsbBusSpeedUnknown = 0,
#   UsbBusSpeedLow,
#   UsbBusSpeedFull,
#   UsbBusSpeedHigh,
#   UsbBusSpeedSuper,
#   UsbBusSpeedMaximum = UsbBusSpeedSuper
# } EFI_USB_BUS_SPEED;
UsbBusSpeedUnknown  = 0
UsbBusSpeedLow      = 1
UsbBusSpeedFull     = 2
UsbBusSpeedHigh     = 3
UsbBusSpeedSuper    = 4
UsbBusSpeedMaximum  = UsbBusSpeedSuper
EFI_USB_BUS_SPEED   = ENUM

# 
# typedef union _EFI_USBFN_MESSAGE_PAYLOAD {
#   EFI_USB_DEVICE_REQUEST       udr;
#   EFI_USBFN_TRANSFER_RESULT    utr;
#   EFI_USB_BUS_SPEED            ubs;
# } EFI_USBFN_MESSAGE_PAYLOAD;
class EFI_USBFN_MESSAGE_PAYLOAD (Union):
  _fields_ = [
    ("udr", EFI_USB_DEVICE_REQUEST),
    ("utr", EFI_USBFN_TRANSFER_RESULT),
    ("ubs", EFI_USB_BUS_SPEED)
  ]

# 
# typedef enum _EFI_USBFN_POLICY_TYPE {
#   EfiUsbPolicyUndefined = 0,
#   EfiUsbPolicyMaxTransactionSize,
#   EfiUsbPolicyZeroLengthTerminationSupport,
#   EfiUsbPolicyZeroLengthTermination
# } EFI_USBFN_POLICY_TYPE;
EfiUsbPolicyUndefined                     = 0
EfiUsbPolicyMaxTransactionSize            = 1
EfiUsbPolicyZeroLengthTerminationSupport  = 2
EfiUsbPolicyZeroLengthTermination         = 3
EFI_USBFN_POLICY_TYPE                     = ENUM

# 
# /**
#   Returns information about what USB port type was attached.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[out] PortType          Returns the USB port type.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to
#                                 process this request or there is no USB port
#                                 attached to the device.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_DETECT_PORT)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   OUT EFI_USBFN_PORT_TYPE           *PortType
#   );
EFI_USBFN_IO_DETECT_PORT = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  POINTER(EFI_USBFN_PORT_TYPE)    # OUT *PortType
  )

# 
# /**
#   Configures endpoints based on supplied device and configuration descriptors.
# 
#   Assuming that the hardware has already been initialized, this function configures
#   the endpoints using the device information supplied by DeviceInfo, activates the
#   port, and starts receiving USB events.
# 
#   This function must ignore the bMaxPacketSize0field of the Standard Device Descriptor
#   and the wMaxPacketSize field of the Standard Endpoint Descriptor that are made
#   available through DeviceInfo.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[out] DeviceInfo        A pointer to EFI_USBFN_DEVICE_INFO instance.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
#   @retval EFI_OUT_OF_RESOURCES  The request could not be completed due to lack of
#                                 resources.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   OUT EFI_USB_DEVICE_INFO           *DeviceInfo
#   );
EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  POINTER(EFI_USB_DEVICE_INFO)    # OUT *DeviceInfo
  )

# 
# /**
#   Returns the maximum packet size of the specified endpoint type for the supplied
#   bus speed.
# 
#   If the BusSpeed is UsbBusSpeedUnknown, the maximum speed the underlying controller
#   supports is assumed.
# 
#   This protocol currently does not support isochronous or interrupt transfers. Future
#   revisions of this protocol may eventually support it.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOLinstance.
#   @param[in]  EndpointType      Endpoint type as defined as EFI_USB_ENDPOINT_TYPE.
#   @param[in]  BusSpeed          Bus speed as defined as EFI_USB_BUS_SPEED.
#   @param[out] MaxPacketSize     The maximum packet size, in bytes, of the specified
#                                 endpoint type.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     EFI_USB_ENDPOINT_TYPE         EndpointType,
#   IN     EFI_USB_BUS_SPEED             BusSpeed,
#   OUT UINT16                        *MaxPacketSize
#   );
EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  EFI_USB_ENDPOINT_TYPE,          # IN  EndpointType
  EFI_USB_BUS_SPEED,              # IN  BusSpeed
  POINTER(UINT16)                 # OUT *MaxPacketSize
  )

# 
# /**
#   Returns device specific information based on the supplied identifier as a Unicode string.
# 
#   If the supplied Buffer isn't large enough, or is NULL, the method fails with
#   EFI_BUFFER_TOO_SMALL and the required size is returned through BufferSize. All returned
#   strings are in Unicode format.
# 
#   An Id of EfiUsbDeviceInfoUnknown is treated as an invalid parameter.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOLinstance.
#   @param[in]  Id                The requested information id.
# 
# 
#   @param[in]  BufferSize        On input, the size of the Buffer in bytes. On output, the
#                                 amount of data returned in Buffer in bytes.
#   @param[out] Buffer            A pointer to a buffer to returnthe requested information
#                                 as a Unicode string.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER One or more of the following conditions is TRUE:
#                                 BufferSize is NULL.
#                                 *BufferSize is not 0 and Buffer is NULL.
#                                 Id in invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_BUFFER_TOO_SMALL  The buffer is too small to hold the buffer.
#                                 *BufferSize has been updated with the size needed to hold the request string.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_DEVICE_INFO)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     EFI_USBFN_DEVICE_INFO_ID      Id,
#   IN OUT UINTN                         *BufferSize,
#   OUT VOID                          *Buffer OPTIONAL
#   );
EFI_USBFN_IO_GET_DEVICE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  EFI_USBFN_DEVICE_INFO_ID,       # IN      Id
  POINTER(UINTN),                 # IN OUT  *BufferSize,
  PVOID                           # OUT     *Buffer OPTIONAL
  )

# 
# /**
#   Returns the vendor-id and product-id of the device.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[out] Vid               Returned vendor-id of the device.
#   @param[out] Pid               Returned product-id of the device.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_NOT_FOUND         Unable to return the vendor-id or the product-id.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   OUT UINT16                        *Vid,
#   OUT UINT16                        *Pid
#   );
EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  POINTER(UINT16),                #    OUT  *Vid,
  POINTER(UINT16)                 #    OUT  *Pid
  )

# 
# /**
#   Aborts the transfer on the specified endpoint.
# 
#   This function should fail with EFI_INVALID_PARAMETER if the specified direction
#   is incorrect for the endpoint.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]  EndpointIndex     Indicates the endpoint on which the ongoing transfer
#                                 needs to be canceled.
#   @param[in]  Direction         Direction of the endpoint.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_ABORT_TRANSFER)(
#   IN  EFI_USBFN_IO_PROTOCOL            *This,
#   IN  UINT8                            EndpointIndex,
#   IN  EFI_USBFN_ENDPOINT_DIRECTION     Direction
#   );
EFI_USBFN_IO_ABORT_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN  *This
  UINT8,                          # IN  EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION    # IN  Direction
  )

# 
# /**
#   Returns the stall state on the specified endpoint.
# 
#   This function should fail with EFI_INVALID_PARAMETER if the specified direction
#   is incorrect for the endpoint.
# 
#   @param[in]      This          A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]      EndpointIndex Indicates the endpoint.
#   @param[in]      Direction     Direction of the endpoint.
#   @param[in, out] State         Boolean, true value indicates that the endpoint
#                                 is in a stalled state, false otherwise.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     UINT8                         EndpointIndex,
#   IN     EFI_USBFN_ENDPOINT_DIRECTION  Direction,
#   IN OUT BOOLEAN                       *State
#   );
EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction
  POINTER(BOOLEAN)                # IN OUT  *State
  )

# 
# /**
#   Sets or clears the stall state on the specified endpoint.
# 
#   This function should fail with EFI_INVALID_PARAMETER if the specified direction
#   is incorrect for the endpoint.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]  EndpointIndex     Indicates the endpoint.
#   @param[in]  Direction         Direction of the endpoint.
#   @param[in]  State             Requested stall state on the specified endpoint.
#                                 True value causes the endpoint to stall; false
#                                 value clears an existing stall.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     UINT8                         EndpointIndex,
#   IN     EFI_USBFN_ENDPOINT_DIRECTION  Direction,
#   IN OUT BOOLEAN                       *State
#   );
EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  POINTER(BOOLEAN)                # IN OUT  *State
  )

# 
# /**
#   This function is called repeatedly to get information on USB bus states,
#   receive-completion and transmit-completion events on the endpoints, and
#   notification on setup packet on endpoint 0.
# 
#   A class driver must call EFI_USBFN_IO_PROTOCOL.EventHandler()repeatedly
#   to receive updates on the transfer status and number of bytes transferred
#   on various endpoints.
# 
#   @param[in]      This          A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[out]     Message       Indicates the event that initiated this notification.
#   @param[in, out] PayloadSize   On input, the size of the memory pointed by
#                                 Payload. On output, the amount ofdata returned
#                                 in Payload.
#   @param[out]     Payload       A pointer to EFI_USBFN_MESSAGE_PAYLOAD instance
#                                 to return additional payload for current message.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
#   @retval EFI_BUFFER_TOO_SMALL  The Supplied buffer is not large enough to hold
#                                 the message payload.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_EVENTHANDLER)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   OUT EFI_USBFN_MESSAGE             *Message,
#   IN OUT UINTN                         *PayloadSize,
#   OUT EFI_USBFN_MESSAGE_PAYLOAD     *Payload
#   );
EFI_USBFN_IO_EVENTHANDLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL),     # IN      *This
  POINTER(EFI_USBFN_MESSAGE),         #    OUT *Message,
  POINTER(UINTN),                     # IN OUT *PayloadSize,
  POINTER(EFI_USBFN_MESSAGE_PAYLOAD)  #    OUT *Payload
  )

# 
# /**
#   This function handles transferring data to or from the host on the specified
#   endpoint, depending on the direction specified.
# 
#   A class driver must call EFI_USBFN_IO_PROTOCOL.EventHandler() repeatedly to
#   receive updates on the transfer status and the number of bytes transferred on
#   various endpoints. Upon an update of the transfer status, the Buffer field of
#   the EFI_USBFN_TRANSFER_RESULT structure (as described in the function description
#   for EFI_USBFN_IO_PROTOCOL.EventHandler()) must be initialized with the Buffer
#   pointer that was supplied to this method.
# 
#   The overview of the call sequence is illustrated in the Figure 54.
# 
#   This function should fail with EFI_INVALID_PARAMETER if the specified direction
#   is incorrect for the endpoint.
# 
#   @param[in]      This          A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]      EndpointIndex Indicates the endpoint on which TX or RX transfer
#                                 needs to take place.
#   @param[in]      Direction     Direction of the endpoint.
#   @param[in, out] BufferSize    If Direction is EfiUsbEndpointDirectionDeviceRx:
#                                   On input, the size of the Bufferin bytes.
#                                   On output, the amount of data returned in Buffer
#                                   in bytes.
#                                 If Direction is EfiUsbEndpointDirectionDeviceTx:
#                                   On input, the size of the Bufferin bytes.
#                                   On output, the amount of data transmitted in bytes.
#   @param[in, out] Buffer        If Direction is EfiUsbEndpointDirectionDeviceRx:
#                                   The Buffer to return the received data.
#                                 If Directionis EfiUsbEndpointDirectionDeviceTx:
#                                   The Buffer that contains the data to be transmitted.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_TRANSFER)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     UINT8                         EndpointIndex,
#   IN     EFI_USBFN_ENDPOINT_DIRECTION  Direction,
#   IN OUT UINTN                         *BufferSize,
#   IN OUT VOID                          *Buffer
#   );
EFI_USBFN_IO_TRANSFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  POINTER(UINTN),                 # IN OUT *BufferSize,
  PVOID                           # IN OUT *Buffer
  )

# 
# /**
#   Returns the maximum supported transfer size.
# 
#   Returns the maximum number of bytes that the underlying controller can accommodate
#   in a single transfer.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[out] MaxTransferSize   The maximum supported transfer size, in bytes.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_NOT_READY         The physical device is busy or not ready to process
#                                 this request.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_MAXTRANSFER_SIZE)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   OUT UINTN                         *MaxTransferSize
#   );
EFI_USBFN_IO_GET_MAXTRANSFER_SIZE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  POINTER(UINTN)                  #    OUT  *MaxTransferSize
  )

# 
# /**
#   Allocates a transfer buffer of the specified sizethat satisfies the controller
#   requirements.
# 
#   The AllocateTransferBuffer() function allocates a memory region of Size bytes and
#   returns the address of the allocated memory that satisfies the underlying controller
#   requirements in the location referenced by Buffer.
# 
#   The allocated transfer buffer must be freed using a matching call to
#   EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer()function.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]  Size              The number of bytes to allocate for the transfer buffer.
#   @param[out] Buffer            A pointer to a pointer to the allocated buffer if the
#                                 call succeeds; undefined otherwise.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_OUT_OF_RESOURCES  The requested transfer buffer could not be allocated.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     UINTN                         Size,
#   OUT VOID                          **Buffer
#   );
EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINTN,                          # IN      Size,
  POINTER(PVOID)                  #    OUT  **Buffer
  )

# 
# /**
#   Deallocates the memory allocated for the transfer buffer by the
#   EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer() function.
# 
#   The EFI_USBFN_IO_PROTOCOL.FreeTransferBuffer() function deallocates the
#   memory specified by Buffer. The Buffer that is freed must have been allocated
#   by EFI_USBFN_IO_PROTOCOL.AllocateTransferBuffer().
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]  Buffer            A pointer to the transfer buffer to deallocate.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_FREE_TRANSFER_BUFFER)(
#   IN  EFI_USBFN_IO_PROTOCOL         *This,
#   IN  VOID                          *Buffer
#   );
EFI_USBFN_IO_FREE_TRANSFER_BUFFER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  PVOID                           # IN      *Buffer
  )

# 
# /**
#   This function supplies power to the USB controller if needed and initializes
#   the hardware and the internal data structures. The port must not be activated
#   by this function.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_START_CONTROLLER)(
#   IN  EFI_USBFN_IO_PROTOCOL         *This
#   );
EFI_USBFN_IO_START_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL)  # IN      *This
  )

# 
# /**
#   This function stops the USB hardware device.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_STOP_CONTROLLER)(
#   IN  EFI_USBFN_IO_PROTOCOL         *This
#   );
EFI_USBFN_IO_STOP_CONTROLLER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL)  # IN      *This
  )

# 
# /**
#   This function sets the configuration policy for the specified non-control
#   endpoint.
# 
#   This function can only be called before EFI_USBFN_IO_PROTOCOL.StartController()
#   or after EFI_USBFN_IO_PROTOCOL.StopController() has been called.
# 
#   @param[in]  This              A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]  EndpointIndex     Indicates the non-control endpoint for which the
#                                 policy needs to be set.
#   @param[in]  Direction         Direction of the endpoint.
#   @param[in]  PolicyType        Policy type the user is trying to set for the
#                                 specified non-control endpoint.
#   @param[in]  BufferSize        The size of the Bufferin bytes.
#   @param[in]  Buffer            The new value for the policy parameter that
#                                 PolicyType specifies.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The physical device reported an error.
#   @retval EFI_UNSUPPORTED       Changing this policy value is not supported.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_SET_ENDPOINT_POLICY)(
#   IN  EFI_USBFN_IO_PROTOCOL         *This,
#   IN  UINT8                         EndpointIndex,
#   IN  EFI_USBFN_ENDPOINT_DIRECTION  Direction,
#   IN  EFI_USBFN_POLICY_TYPE         PolicyType,
#   IN  UINTN                         BufferSize,
#   IN  VOID                          *Buffer
#   );
EFI_USBFN_IO_SET_ENDPOINT_POLICY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN *This
  UINT8,                          # IN EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN Direction,
  EFI_USBFN_POLICY_TYPE,          # IN PolicyType,
  UINTN,                          # IN BufferSize,
  PVOID                           # IN Buffer
  )

# 
# /**
#   This function sets the configuration policy for the specified non-control
#   endpoint.
# 
#   This function can only be called before EFI_USBFN_IO_PROTOCOL.StartController()
#   or after EFI_USBFN_IO_PROTOCOL.StopController() has been called.
# 
#   @param[in]      This          A pointer to the EFI_USBFN_IO_PROTOCOL instance.
#   @param[in]      EndpointIndex Indicates the non-control endpoint for which the
#                                 policy needs to be set.
#   @param[in]      Direction     Direction of the endpoint.
#   @param[in]      PolicyType    Policy type the user is trying to retrieve for
#                                 the specified non-control endpoint.
#   @param[in, out] BufferSize    On input, the size of Bufferin bytes. On output,
#                                 the amount of data returned in Bufferin bytes.
#   @param[in, out] Buffer        A pointer to a buffer to return requested endpoint
#                                 policy value.
# 
#   @retval EFI_SUCCESS           The function returned successfully.
#   @retval EFI_INVALID_PARAMETER A parameter is invalid.
#   @retval EFI_DEVICE_ERROR      The specified policy value is not supported.
#   @retval EFI_BUFFER_TOO_SMALL  Supplied buffer is not large enough to hold requested
#                                 policy value.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_USBFN_IO_GET_ENDPOINT_POLICY)(
#   IN     EFI_USBFN_IO_PROTOCOL         *This,
#   IN     UINT8                         EndpointIndex,
#   IN     EFI_USBFN_ENDPOINT_DIRECTION  Direction,
#   IN     EFI_USBFN_POLICY_TYPE         PolicyType,
#   IN OUT UINTN                         *BufferSize,
#   IN OUT VOID                          *Buffer
#   );
EFI_USBFN_IO_GET_ENDPOINT_POLICY = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_USBFN_IO_PROTOCOL), # IN      *This
  UINT8,                          # IN      EndpointIndex,
  EFI_USBFN_ENDPOINT_DIRECTION,   # IN      Direction,
  EFI_USBFN_POLICY_TYPE,          # IN      PolicyType,
  POINTER(UINTN),                 # IN OUT  *BufferSize,
  PVOID                           # IN OUT  *Buffer
  )

# 
# ///
# /// The EFI_USBFN_IO_PROTOCOL provides basic data transactions and basic USB
# /// controller management for a USB Function port.
# ///
# struct _EFI_USBFN_IO_PROTOCOL {
#   UINT32                                      Revision;
#   EFI_USBFN_IO_DETECT_PORT                    DetectPort;
#   EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS     ConfigureEnableEndpoints;
#   EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE    GetEndpointMaxPacketSize;
#   EFI_USBFN_IO_GET_DEVICE_INFO                GetDeviceInfo;
#   EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID       GetVendorIdProductId;
#   EFI_USBFN_IO_ABORT_TRANSFER                 AbortTransfer;
#   EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE       GetEndpointStallState;
#   EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE       SetEndpointStallState;
#   EFI_USBFN_IO_EVENTHANDLER                   EventHandler;
#   EFI_USBFN_IO_TRANSFER                       Transfer;
#   EFI_USBFN_IO_GET_MAXTRANSFER_SIZE           GetMaxTransferSize;
#   EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER       AllocateTransferBuffer;
#   EFI_USBFN_IO_FREE_TRANSFER_BUFFER           FreeTransferBuffer;
#   EFI_USBFN_IO_START_CONTROLLER               StartController;
#   EFI_USBFN_IO_STOP_CONTROLLER                StopController;
#   EFI_USBFN_IO_SET_ENDPOINT_POLICY            SetEndpointPolicy;
#   EFI_USBFN_IO_GET_ENDPOINT_POLICY            GetEndpointPolicy;
# };
EFI_USBFN_IO_PROTOCOL._fields_ = [
    ("Revision",                  UINT32),
    ("DetectPort",                EFI_USBFN_IO_DETECT_PORT),
    ("ConfigureEnableEndpoints",  EFI_USBFN_IO_CONFIGURE_ENABLE_ENDPOINTS),
    ("GetEndpointMaxPacketSize",  EFI_USBFN_IO_GET_ENDPOINT_MAXPACKET_SIZE),
    ("GetDeviceInfo",             EFI_USBFN_IO_GET_DEVICE_INFO),
    ("GetVendorIdProductId",      EFI_USBFN_IO_GET_VENDOR_ID_PRODUCT_ID),
    ("AbortTransfer",             EFI_USBFN_IO_ABORT_TRANSFER),
    ("GetEndpointStallState",     EFI_USBFN_IO_GET_ENDPOINT_STALL_STATE),
    ("SetEndpointStallState",     EFI_USBFN_IO_SET_ENDPOINT_STALL_STATE),
    ("EventHandler",              EFI_USBFN_IO_EVENTHANDLER),
    ("Transfer",                  EFI_USBFN_IO_TRANSFER),
    ("GetMaxTransferSize",        EFI_USBFN_IO_GET_MAXTRANSFER_SIZE),
    ("AllocateTransferBuffer",    EFI_USBFN_IO_ALLOCATE_TRANSFER_BUFFER),
    ("FreeTransferBuffer",        EFI_USBFN_IO_FREE_TRANSFER_BUFFER),
    ("StartController",           EFI_USBFN_IO_START_CONTROLLER),
    ("StopController",            EFI_USBFN_IO_STOP_CONTROLLER),
    ("SetEndpointPolicy",         EFI_USBFN_IO_SET_ENDPOINT_POLICY),
    ("GetEndpointPolicy",         EFI_USBFN_IO_GET_ENDPOINT_POLICY)
  ]

# 
# extern EFI_GUID  gEfiUsbFunctionIoProtocolGuid;
# 
# #endif
# 