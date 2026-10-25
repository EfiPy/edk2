# /** @file
#   EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL as defined in UEFI 2.0.
#   This protocol provides service to convert text to device paths and device nodes.
# 
#   Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# DevicePathFromText.py
#
# EfiPy2.MdePkg.Protocol.DevicePathFromText
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __DEVICE_PATH_FROM_TEXT_PROTOCOL_H__
# #define __DEVICE_PATH_FROM_TEXT_PROTOCOL_H__
from EfiPy2 import *

# 
# ///
# /// Device Path From Text protocol
# ///
# #define EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL_GUID \
#   { \
#     0x5c99a21, 0xc70f, 0x4ad2, {0x8a, 0x5f, 0x35, 0xdf, 0x33, 0x43, 0xf5, 0x1e  } \
#   }
gEfiDevicePathFromTextProtocolGuid      = \
  EFI_GUID (0x5c99a21, 0xc70f, 0x4ad2, (0x8a, 0x5f, 0x35, 0xdf, 0x33, 0x43, 0xf5, 0x1e  ))

# 
# /**
#   Convert text to the binary representation of a device node.
# 
#   @param  TextDeviceNode TextDeviceNode points to the text representation of a device
#                          node. Conversion starts with the first character and continues
#                          until the first non-device node character.
# 
#   @retval a_pointer      Pointer to the EFI device node.
#   @retval NULL           if TextDeviceNode is NULL or there was insufficient memory.
# 
# **/
# typedef
# EFI_DEVICE_PATH_PROTOCOL *
# (EFIAPI *EFI_DEVICE_PATH_FROM_TEXT_NODE)(
#   IN CONST CHAR16                 *TextDeviceNode
#   );
EFI_DEVICE_PATH_FROM_TEXT_NODE = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

# 
# /**
#   Convert text to the binary representation of a device node.
# 
#   @param  TextDeviceNode TextDevicePath points to the text representation of a device
#                          path. Conversion starts with the first character and continues
#                          until the first non-device path character.
# 
#   @retval a_pointer      Pointer to the allocated device path.
#   @retval NULL           if TextDeviceNode is NULL or there was insufficient memory.
# 
# **/
# typedef
# EFI_DEVICE_PATH_PROTOCOL *
# (EFIAPI *EFI_DEVICE_PATH_FROM_TEXT_PATH)(
#   IN CONST CHAR16                 *TextDevicePath
#   );
EFI_DEVICE_PATH_FROM_TEXT_PATH = CFUNCTYPE (
  POINTER (EFI_DEVICE_PATH_PROTOCOL),
  PCHAR16                             # IN *TextDeviceNode
  )

# 
# ///
# /// This protocol converts text to device paths and device nodes.
# ///
# typedef struct {
#   EFI_DEVICE_PATH_FROM_TEXT_NODE    ConvertTextToDeviceNode;
#   EFI_DEVICE_PATH_FROM_TEXT_PATH    ConvertTextToDevicePath;
# } EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL;
class EFI_DEVICE_PATH_FROM_TEXT_PROTOCOL (Structure):
  _fields_ = [
    ("ConvertTextToDeviceNode",  EFI_DEVICE_PATH_FROM_TEXT_NODE),
    ("ConvertTextToDevicePath",  EFI_DEVICE_PATH_FROM_TEXT_PATH)
  ]

# 
# extern EFI_GUID  gEfiDevicePathFromTextProtocolGuid;
# 
# #endif
# 