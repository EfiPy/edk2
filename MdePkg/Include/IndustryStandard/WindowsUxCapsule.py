# /** @file
#   Defines Windows UX Capsule GUID and layout defined at Microsoft
#   Windows UEFI Firmware Update Platform specification
# 
#   Copyright (c) 2015 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# WindowsUxCapsule.py
#
# EfiPy2.MdePkg.IndustryStandard.WindowsUxCapsule
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _WINDOWS_UX_CAPSULE_GUID_H_
# #define _WINDOWS_UX_CAPSULE_GUID_H_
from EfiPy2.MdePkg.IndustryStandard  import *
from EfiPy2.MdePkg.Uefi.UefiSpec     import EFI_CAPSULE_HEADER

# 
# #pragma pack(1)
# 
# typedef struct {
#   UINT8     Version;
#   UINT8     Checksum;
#   UINT8     ImageType;
#   UINT8     Reserved;
#   UINT32    Mode;
#   UINT32    OffsetX;
#   UINT32    OffsetY;
#   // UINT8  Image[];
# } DISPLAY_DISPLAY_PAYLOAD;
class DISPLAY_DISPLAY_PAYLOAD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Version",   UINT8),
    ("Checksum",  UINT8),
    ("ImageType", UINT8),
    ("Reserved",  UINT8),
    ("Mode",      UINT32),
    ("OffsetX",   UINT32),
    ("OffsetY",   UINT32)
    # ("Image",     UINT8 * N)
  ]

# 
# typedef struct {
#   EFI_CAPSULE_HEADER         CapsuleHeader;
#   DISPLAY_DISPLAY_PAYLOAD    ImagePayload;
# } EFI_DISPLAY_CAPSULE;
class EFI_DISPLAY_CAPSULE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CapsuleHeader", EFI_CAPSULE_HEADER),
    ("ImagePayload",  DISPLAY_DISPLAY_PAYLOAD)
  ]

# 
# #pragma pack()
# 
# #define WINDOWS_UX_CAPSULE_GUID \
#   { \
#     0x3b8c8162, 0x188c, 0x46a4, { 0xae, 0xc9, 0xbe, 0x43, 0xf1, 0xd6, 0x56, 0x97}  \
#   }
gWindowsUxCapsuleGuid = EFI_GUID (0x3b8c8162, 0x188c, 0x46a4, ( 0xae, 0xc9, 0xbe, 0x43, 0xf1, 0xd6, 0x56, 0x97))
# 
# extern EFI_GUID  gWindowsUxCapsuleGuid;
# 
# #endif
# 