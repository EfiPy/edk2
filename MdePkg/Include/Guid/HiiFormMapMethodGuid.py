# /** @file
#   Guid used to identify HII FormMap configuration method.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   GUID defined in UEFI 2.2 spec.
# **/
# 
# HiiFormMapMethodGuid.py
#
# EfiPy2.MdePkg.Guid.HiiFormMapMethodGuid
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __EFI_HII_FORMMAP_GUID_H__
# #define __EFI_HII_FORMMAP_GUID_H__
from EfiPy2 import *

# 
# #define EFI_HII_STANDARD_FORM_GUID \
#   { 0x3bd2f4ec, 0xe524, 0x46e4, { 0xa9, 0xd8, 0x51, 0x1, 0x17, 0x42, 0x55, 0x62 } }
# 
# extern EFI_GUID  gEfiHiiStandardFormGuid;
gEfiHiiStandardFormGuid = \
  EFI_GUID (0x3bd2f4ec, 0xe524, 0x46e4, ( 0xa9, 0xd8, 0x51, 0x1, 0x17, 0x42, 0x55, 0x62 ))
# 
# #endif
# 