# /** @file
#   Hob guid for Information about the graphics mode.
# 
#   Copyright (c) 2015 - 2016, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This HOB is introduced in in PI Version 1.4.
# 
# **/
# 
# GraphicsInfoHob.py
#
# EfiPy2.MdePkg.Guid.GraphicsInfoHob
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _GRAPHICS_INFO_HOB_GUID_H_
# #define _GRAPHICS_INFO_HOB_GUID_H_
from EfiPy2 import *

# 
# #include <Protocol/GraphicsOutput.h>
from EfiPy2.MdePkg.Protocol  import GraphicsOutput

# 
# #define EFI_PEI_GRAPHICS_INFO_HOB_GUID \
#   { \
#     0x39f62cce, 0x6825, 0x4669, { 0xbb, 0x56, 0x54, 0x1a, 0xba, 0x75, 0x3a, 0x07 } \
#   }
gEfiGraphicsInfoHobGuid = \
  EFI_GUID (0x39f62cce, 0x6825, 0x4669, ( 0xbb, 0x56, 0x54, 0x1a, 0xba, 0x75, 0x3a, 0x07 ))

# 
# #define EFI_PEI_GRAPHICS_DEVICE_INFO_HOB_GUID \
#   { \
#     0xe5cb2ac9, 0xd35d, 0x4430, { 0x93, 0x6e, 0x1d, 0xe3, 0x32, 0x47, 0x8d, 0xe7 } \
#   }
gEfiGraphicsDeviceInfoHobGuid = \
  EFI_GUID (0xe5cb2ac9, 0xd35d, 0x4430, ( 0x93, 0x6e, 0x1d, 0xe3, 0x32, 0x47, 0x8d, 0xe7 ))

# 
# typedef struct {
#   EFI_PHYSICAL_ADDRESS                    FrameBufferBase;
#   UINT32                                  FrameBufferSize;
#   EFI_GRAPHICS_OUTPUT_MODE_INFORMATION    GraphicsMode;
# } EFI_PEI_GRAPHICS_INFO_HOB;
class EFI_PEI_GRAPHICS_INFO_HOB (Structure):
  _fields_ = [
    ("FrameBufferBase", EFI_PHYSICAL_ADDRESS),
    ("FrameBufferSize", UINT32),
    ("GraphicsMode",    GraphicsOutput.EFI_GRAPHICS_OUTPUT_MODE_INFORMATION)
  ]

# 
# typedef struct {
#   UINT16    VendorId;                                       ///< Ignore if the value is 0xFFFF.
#   UINT16    DeviceId;                                       ///< Ignore if the value is 0xFFFF.
#   UINT16    SubsystemVendorId;                              ///< Ignore if the value is 0xFFFF.
#   UINT16    SubsystemId;                                    ///< Ignore if the value is 0xFFFF.
#   UINT8     RevisionId;                                     ///< Ignore if the value is 0xFF.
#   UINT8     BarIndex;                                       ///< Ignore if the value is 0xFF.
# } EFI_PEI_GRAPHICS_DEVICE_INFO_HOB;
class EFI_PEI_GRAPHICS_DEVICE_INFO_HOB (Structure):
  _fields_ = [
    ("VendorId",            UINT16),
    ("DeviceId",            UINT16),
    ("SubsystemVendorId",   UINT16),
    ("SubsystemId",         UINT16),
    ("RevisionId",          UINT8),
    ("BarIndex",            UINT8)
  ]

# 
# extern EFI_GUID  gEfiGraphicsInfoHobGuid;
# extern EFI_GUID  gEfiGraphicsDeviceInfoHobGuid;
# 
# #endif
# 