# /** @file
#   Present the boot mode values in PI.
# 
#   Copyright (c) 2006 - 2012, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   PI Version 1.2.1A
# 
# **/
# PiBootMode.py
#
# EfiPy2.MdePkg.Pi.PiBootMode
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __PI_BOOT_MODE_H__
# #define __PI_BOOT_MODE_H__
from EfiPy2 import *

# 
# ///
# /// EFI boot mode
# ///
# typedef UINT32 EFI_BOOT_MODE;
EFI_BOOT_MODE = UINT32

# 
# //
# // 0x21 - 0xf..f are reserved.
# //
# #define BOOT_WITH_FULL_CONFIGURATION                   0x00
# #define BOOT_WITH_MINIMAL_CONFIGURATION                0x01
# #define BOOT_ASSUMING_NO_CONFIGURATION_CHANGES         0x02
# #define BOOT_WITH_FULL_CONFIGURATION_PLUS_DIAGNOSTICS  0x03
# #define BOOT_WITH_DEFAULT_SETTINGS                     0x04
# #define BOOT_ON_S4_RESUME                              0x05
# #define BOOT_ON_S5_RESUME                              0x06
# #define BOOT_WITH_MFG_MODE_SETTINGS                    0x07
# #define BOOT_ON_S2_RESUME                              0x10
# #define BOOT_ON_S3_RESUME                              0x11
# #define BOOT_ON_FLASH_UPDATE                           0x12
# #define BOOT_IN_RECOVERY_MODE                          0x20
BOOT_WITH_FULL_CONFIGURATION                   = 0x00
BOOT_WITH_MINIMAL_CONFIGURATION                = 0x01
BOOT_ASSUMING_NO_CONFIGURATION_CHANGES         = 0x02
BOOT_WITH_FULL_CONFIGURATION_PLUS_DIAGNOSTICS  = 0x03
BOOT_WITH_DEFAULT_SETTINGS                     = 0x04
BOOT_ON_S4_RESUME                              = 0x05
BOOT_ON_S5_RESUME                              = 0x06
BOOT_WITH_MFG_MODE_SETTINGS                    = 0x07
BOOT_ON_S2_RESUME                              = 0x10
BOOT_ON_S3_RESUME                              = 0x11
BOOT_ON_FLASH_UPDATE                           = 0x12
BOOT_IN_RECOVERY_MODE                          = 0x20

# 
# #endif
# 