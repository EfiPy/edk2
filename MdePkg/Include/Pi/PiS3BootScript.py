# /** @file
#   This file contains the boot script defintions that are shared between the
#   Boot Script Executor PPI and the Boot Script Save Protocol.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# PiS3BootScript.py
#
# EfiPy2.MdePkg.Pi.PiS3BootScript
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _PI_S3_BOOT_SCRIPT_H_
# #define _PI_S3_BOOT_SCRIPT_H_
from EfiPy2 import *

# 
# // *******************************************
# // EFI Boot Script Opcode definitions
# // *******************************************
# #define EFI_BOOT_SCRIPT_IO_WRITE_OPCODE                0x00
# #define EFI_BOOT_SCRIPT_IO_READ_WRITE_OPCODE           0x01
# #define EFI_BOOT_SCRIPT_MEM_WRITE_OPCODE               0x02
# #define EFI_BOOT_SCRIPT_MEM_READ_WRITE_OPCODE          0x03
# #define EFI_BOOT_SCRIPT_PCI_CONFIG_WRITE_OPCODE        0x04
# #define EFI_BOOT_SCRIPT_PCI_CONFIG_READ_WRITE_OPCODE   0x05
# #define EFI_BOOT_SCRIPT_SMBUS_EXECUTE_OPCODE           0x06
# #define EFI_BOOT_SCRIPT_STALL_OPCODE                   0x07
# #define EFI_BOOT_SCRIPT_DISPATCH_OPCODE                0x08
# #define EFI_BOOT_SCRIPT_DISPATCH_2_OPCODE              0x09
# #define EFI_BOOT_SCRIPT_INFORMATION_OPCODE             0x0A
# #define EFI_BOOT_SCRIPT_PCI_CONFIG2_WRITE_OPCODE       0x0B
# #define EFI_BOOT_SCRIPT_PCI_CONFIG2_READ_WRITE_OPCODE  0x0C
# #define EFI_BOOT_SCRIPT_IO_POLL_OPCODE                 0x0D
# #define EFI_BOOT_SCRIPT_MEM_POLL_OPCODE                0x0E
# #define EFI_BOOT_SCRIPT_PCI_CONFIG_POLL_OPCODE         0x0F
# #define EFI_BOOT_SCRIPT_PCI_CONFIG2_POLL_OPCODE        0x10
EFI_BOOT_SCRIPT_IO_WRITE_OPCODE                = 0x00
EFI_BOOT_SCRIPT_IO_READ_WRITE_OPCODE           = 0x01
EFI_BOOT_SCRIPT_MEM_WRITE_OPCODE               = 0x02
EFI_BOOT_SCRIPT_MEM_READ_WRITE_OPCODE          = 0x03
EFI_BOOT_SCRIPT_PCI_CONFIG_WRITE_OPCODE        = 0x04
EFI_BOOT_SCRIPT_PCI_CONFIG_READ_WRITE_OPCODE   = 0x05
EFI_BOOT_SCRIPT_SMBUS_EXECUTE_OPCODE           = 0x06
EFI_BOOT_SCRIPT_STALL_OPCODE                   = 0x07
EFI_BOOT_SCRIPT_DISPATCH_OPCODE                = 0x08
EFI_BOOT_SCRIPT_DISPATCH_2_OPCODE              = 0x09
EFI_BOOT_SCRIPT_INFORMATION_OPCODE             = 0x0A
EFI_BOOT_SCRIPT_PCI_CONFIG2_WRITE_OPCODE       = 0x0B
EFI_BOOT_SCRIPT_PCI_CONFIG2_READ_WRITE_OPCODE  = 0x0C
EFI_BOOT_SCRIPT_IO_POLL_OPCODE                 = 0x0D
EFI_BOOT_SCRIPT_MEM_POLL_OPCODE                = 0x0E
EFI_BOOT_SCRIPT_PCI_CONFIG_POLL_OPCODE         = 0x0F
EFI_BOOT_SCRIPT_PCI_CONFIG2_POLL_OPCODE        = 0x10

# 
# // *******************************************
# // EFI_BOOT_SCRIPT_WIDTH
# // *******************************************
# typedef enum {
#   EfiBootScriptWidthUint8,
#   EfiBootScriptWidthUint16,
#   EfiBootScriptWidthUint32,
#   EfiBootScriptWidthUint64,
#   EfiBootScriptWidthFifoUint8,
#   EfiBootScriptWidthFifoUint16,
#   EfiBootScriptWidthFifoUint32,
#   EfiBootScriptWidthFifoUint64,
#   EfiBootScriptWidthFillUint8,
#   EfiBootScriptWidthFillUint16,
#   EfiBootScriptWidthFillUint32,
#   EfiBootScriptWidthFillUint64,
#   EfiBootScriptWidthMaximum
# } EFI_BOOT_SCRIPT_WIDTH;
EfiBootScriptWidthUint8       = 0
EfiBootScriptWidthUint16      = 1
EfiBootScriptWidthUint32      = 2
EfiBootScriptWidthUint64      = 3
EfiBootScriptWidthFifoUint8   = 4
EfiBootScriptWidthFifoUint16  = 5
EfiBootScriptWidthFifoUint32  = 6
EfiBootScriptWidthFifoUint64  = 7
EfiBootScriptWidthFillUint8   = 8
EfiBootScriptWidthFillUint16  = 9
EfiBootScriptWidthFillUint32  = 10
EfiBootScriptWidthFillUint64  = 11
EfiBootScriptWidthMaximum     = 12
EFI_BOOT_SCRIPT_WIDTH         = ENUM

# 
# #endif
# 