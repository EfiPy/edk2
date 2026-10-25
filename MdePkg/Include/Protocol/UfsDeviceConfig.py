# /** @file
#   This file defines the EFI UFS Device Config Protocol.
# 
#   Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol is introduced in UEFI Specification 2.7
# 
# **/
# UfsDeviceConfig.py
#
# EfiPy2.MdePkg.Protocol.UfsDeviceConfig
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __UFS_DEVICE_CONFIG_PROTOCOL_H__
# #define __UFS_DEVICE_CONFIG_PROTOCOL_H__
from EfiPy2 import *

# 
# //
# // EFI UFS Device Config Protocol GUID value
# //
# #define EFI_UFS_DEVICE_CONFIG_GUID \
#   { 0xb81bfab0, 0xeb3, 0x4cf9, { 0x84, 0x65, 0x7f, 0xa9, 0x86, 0x36, 0x16, 0x64 }};
gEfiUfsDeviceConfigProtocolGuid  = \
  EFI_GUID (0xb81bfab0, 0xeb3, 0x4cf9, ( 0x84, 0x65, 0x7f, 0xa9, 0x86, 0x36, 0x16, 0x64 ))

# 
# //
# // Forward reference for pure ANSI compatability
# //
# typedef struct _EFI_UFS_DEVICE_CONFIG_PROTOCOL EFI_UFS_DEVICE_CONFIG_PROTOCOL;
class EFI_UFS_DEVICE_CONFIG_PROTOCOL (Structure):
  pass

# 
# /**
#   Read or write specified device descriptor of a UFS device.
# 
#   The service is used to read/write UFS device descriptors. The consumer of this API is responsible
#   for allocating the data buffer pointed by Descriptor.
# 
#   @param[in]      This          The pointer to the EFI_UFS_DEVICE_CONFIG_PROTOCOL instance.
#   @param[in]      Read          The boolean variable to show r/w direction.
#   @param[in]      DescId        The ID of device descriptor.
#   @param[in]      Index         The Index of device descriptor.
#   @param[in]      Selector      The Selector of device descriptor.
#   @param[in, out] Descriptor    The buffer of device descriptor to be read or written.
#   @param[in, out] DescSize      The size of device descriptor buffer. On input, the size, in bytes,
#                                 of the data buffer specified by Descriptor. On output, the number
#                                 of bytes that were actually transferred.
# 
#   @retval EFI_SUCCESS           The device descriptor is read/written successfully.
#   @retval EFI_INVALID_PARAMETER This is NULL or Descriptor is NULL or DescSize is NULL.
#                                 DescId, Index and Selector are invalid combination to point to a
#                                 type of UFS device descriptor.
#   @retval EFI_DEVICE_ERROR      The device descriptor is not read/written successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR)(
#   IN EFI_UFS_DEVICE_CONFIG_PROTOCOL    *This,
#   IN BOOLEAN                           Read,
#   IN UINT8                             DescId,
#   IN UINT8                             Index,
#   IN UINT8                             Selector,
#   IN OUT UINT8                         *Descriptor,
#   IN OUT UINT32                        *DescSize
#   );
EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     DescId,
  UINT8,                                    #   IN     Index,
  UINT8,                                    #   IN     Selector,
  POINTER(UINT8),                           #   IN OUT *Descriptor,
  POINTER(UINT32)                           #   IN OUT *DescSize
  )

# 
# /**
#   Read or write specified flag of a UFS device.
# 
#   The service is used to read/write UFS flag descriptors. The consumer of this API is responsible
#   for allocating the buffer pointed by Flag. The buffer size is 1 byte as UFS flag descriptor is
#   just a single Boolean value that represents a TRUE or FALSE, '0' or '1', ON or OFF type of value.
# 
#   @param[in]      This          The pointer to the EFI_UFS_DEVICE_CONFIG_PROTOCOL instance.
#   @param[in]      Read          The boolean variable to show r/w direction.
#   @param[in]      FlagId        The ID of flag to be read or written.
#   @param[in, out] Flag          The buffer to set or clear flag.
# 
#   @retval EFI_SUCCESS           The flag descriptor is set/clear successfully.
#   @retval EFI_INVALID_PARAMETER This is NULL or Flag is NULL.
#                                 FlagId is an invalid UFS flag ID.
#   @retval EFI_DEVICE_ERROR      The flag is not set/clear successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_UFS_DEVICE_CONFIG_RW_FLAG)(
#   IN EFI_UFS_DEVICE_CONFIG_PROTOCOL    *This,
#   IN BOOLEAN                           Read,
#   IN UINT8                             FlagId,
#   IN OUT UINT8                         *Flag
#   );
EFI_UFS_DEVICE_CONFIG_RW_FLAG = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     FlagId,
  POINTER(UINT8),                           #   IN OUT *Flag
  )

# 
# /**
#   Read or write specified attribute of a UFS device.
# 
#   The service is used to read/write UFS attributes. The consumer of this API is responsible for
#   allocating the data buffer pointed by Attribute.
# 
#   @param[in]      This          The pointer to the EFI_UFS_DEVICE_CONFIG_PROTOCOL instance.
#   @param[in]      Read          The boolean variable to show r/w direction.
#   @param[in]      AttrId        The ID of Attribute.
#   @param[in]      Index         The Index of Attribute.
#   @param[in]      Selector      The Selector of Attribute.
#   @param[in, out] Attribute     The buffer of Attribute to be read or written.
#   @param[in, out] AttrSize      The size of Attribute buffer. On input, the size, in bytes, of the
#                                 data buffer specified by Attribute. On output, the number of bytes
#                                 that were actually transferred.
# 
#   @retval EFI_SUCCESS           The attribute is read/written successfully.
#   @retval EFI_INVALID_PARAMETER This is NULL or Attribute is NULL or AttrSize is NULL.
#                                 AttrId, Index and Selector are invalid combination to point to a
#                                 type of UFS attribute.
#   @retval EFI_DEVICE_ERROR      The attribute is not read/written successfully.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE)(
#   IN EFI_UFS_DEVICE_CONFIG_PROTOCOL    *This,
#   IN BOOLEAN                           Read,
#   IN UINT8                             AttrId,
#   IN UINT8                             Index,
#   IN UINT8                             Selector,
#   IN OUT UINT8                         *Attribute,
#   IN OUT UINT32                        *AttrSize
#   );
EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_UFS_DEVICE_CONFIG_PROTOCOL),  #   IN     *This,
  BOOLEAN,                                  #   IN     Read,
  UINT8,                                    #   IN     AttrId,
  UINT8,                                    #   IN     Index,
  UINT8,                                    #   IN     Selector,
  POINTER(UINT8),                           #   IN OUT *Attribute,
  POINTER(UINT32),                          #   IN OUT *AttrSize
  )

# 
# ///
# /// UFS Device Config Protocol structure.
# ///
# struct _EFI_UFS_DEVICE_CONFIG_PROTOCOL {
#   EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR    RwUfsDescriptor;
#   EFI_UFS_DEVICE_CONFIG_RW_FLAG          RwUfsFlag;
#   EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE     RwUfsAttribute;
# };
EFI_UFS_DEVICE_CONFIG_PROTOCOL._fields_ = [
    ("RwUfsDescriptor", EFI_UFS_DEVICE_CONFIG_RW_DESCRIPTOR),
    ("RwUfsFlag",       EFI_UFS_DEVICE_CONFIG_RW_FLAG),
    ("RwUfsAttribute",  EFI_UFS_DEVICE_CONFIG_RW_ATTRIBUTE)
  ]

# 
# ///
# /// UFS Device Config Protocol GUID variable.
# ///
# extern EFI_GUID  gEfiUfsDeviceConfigProtocolGuid;
# 
# #endif
# 