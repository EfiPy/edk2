# /** @file
#   PCI Enumeration Complete Protocol as defined in the PI 1.1 specification.
#   This protocol indicates that pci enumeration complete
# 
#   Copyright (c) 2009, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol is defined in UEFI Platform Initialization Specification 1.2
#   Volume 5: Standards
# 
# **/
# PciEnumerationComplete.py
#
# EfiPy2.MdePkg.Protocol.PciEnumerationComplete
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef _PCI_ENUMERATION_COMPLETE_H_
# #define _PCI_ENUMERATION_COMPLETE_H_
from EfiPy2 import EFI_GUID

# 
# #define EFI_PCI_ENUMERATION_COMPLETE_GUID \
#   {  \
#    0x30cfe3e7, 0x3de1, 0x4586, { 0xbe, 0x20, 0xde, 0xab, 0xa1, 0xb3, 0xb7, 0x93  } \
#   }
gEfiPciEnumerationCompleteProtocolGuid  = \
  EFI_GUID (0x30cfe3e7, 0x3de1, 0x4586, ( 0xbe, 0x20, 0xde, 0xab, 0xa1, 0xb3, 0xb7, 0x93  ))

# 
# extern EFI_GUID  gEfiPciEnumerationCompleteProtocolGuid;
# 
# #endif
# 