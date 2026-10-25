# /** @file
#   This file declares the SMBus definitions defined in SmBus Specification V2.0
#   and defined in PI1.0 specification volume 5.
# 
#   Copyright (c) 2007 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# SmBus.py
#
# EfiPy2.MdePkg.IndustryStandard.SmBus
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _SMBUS_H_
# #define _SMBUS_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# ///
# /// UDID of SMBUS device.
# ///
# typedef struct {
#   UINT32    VendorSpecificId;
#   UINT16    SubsystemDeviceId;
#   UINT16    SubsystemVendorId;
#   UINT16    Interface;
#   UINT16    DeviceId;
#   UINT16    VendorId;
#   UINT8     VendorRevision;
#   UINT8     DeviceCapabilities;
# } EFI_SMBUS_UDID;
class EFI_SMBUS_UDID (Structure):
  _fields_ = [
    ("VendorSpecificId",    UINT32),
    ("SubsystemDeviceId",   UINT16),
    ("SubsystemVendorId",   UINT16),
    ("Interface",           UINT16),
    ("DeviceId",            UINT16),
    ("VendorId",            UINT16),
    ("VendorRevision",      UINT8),
    ("DeviceCapabilities",  UINT8),
  ]

# 
# ///
# /// Smbus Device Address
# ///
# typedef struct {
#   ///
#   /// The SMBUS hardware address to which the SMBUS device is preassigned or allocated.
#   ///
#   UINTN    SmbusDeviceAddress : 7;
# } EFI_SMBUS_DEVICE_ADDRESS;
class EFI_SMBUS_DEVICE_ADDRESS (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",    UINTN, 7)
  ]

# 
# typedef struct {
#   ///
#   /// The SMBUS hardware address to which the SMBUS device is preassigned or
#   /// allocated. Type EFI_SMBUS_DEVICE_ADDRESS is defined in EFI_PEI_SMBUS2_PPI.Execute().
#   ///
#   EFI_SMBUS_DEVICE_ADDRESS    SmbusDeviceAddress;
#   ///
#   /// The SMBUS Unique Device Identifier (UDID) as defined in EFI_SMBUS_UDID.
#   /// Type EFI_SMBUS_UDID is defined in EFI_PEI_SMBUS2_PPI.ArpDevice().
#   ///
#   EFI_SMBUS_UDID              SmbusDeviceUdid;
# } EFI_SMBUS_DEVICE_MAP;
class EFI_SMBUS_DEVICE_MAP (Structure):
  _fields_ = [
    ("SmbusDeviceAddress",  EFI_SMBUS_DEVICE_ADDRESS),
    ("SmbusDeviceUdid",     EFI_SMBUS_UDID)
  ]

# 
# ///
# /// Smbus Operations
# ///
# typedef enum _EFI_SMBUS_OPERATION {
#   EfiSmbusQuickRead,
#   EfiSmbusQuickWrite,
#   EfiSmbusReceiveByte,
#   EfiSmbusSendByte,
#   EfiSmbusReadByte,
#   EfiSmbusWriteByte,
#   EfiSmbusReadWord,
#   EfiSmbusWriteWord,
#   EfiSmbusReadBlock,
#   EfiSmbusWriteBlock,
#   EfiSmbusProcessCall,
#   EfiSmbusBWBRProcessCall
# } EFI_SMBUS_OPERATION;
EfiSmbusQuickRead       =  0
EfiSmbusQuickWrite      =  1
EfiSmbusReceiveByte     =  2
EfiSmbusSendByte        =  3
EfiSmbusReadByte        =  4
EfiSmbusWriteByte       =  5
EfiSmbusReadWord        =  6
EfiSmbusWriteWord       =  7
EfiSmbusReadBlock       =  8
EfiSmbusWriteBlock      =  9
EfiSmbusProcessCall     = 10
EfiSmbusBWBRProcessCall = 11
EFI_SMBUS_OPERATION = ENUM

EFI_SMBUS_DEVICE_COMMAND = UINTN

# 
# ///
# /// EFI_SMBUS_DEVICE_COMMAND
# ///
# typedef UINTN EFI_SMBUS_DEVICE_COMMAND;
EFI_SMBUS_DEVICE_COMMAND = UINTN

# 
# #endif
# 