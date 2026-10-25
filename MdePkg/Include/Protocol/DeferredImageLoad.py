# /** @file
#   UEFI 2.2 Deferred Image Load Protocol definition.
# 
#   This protocol returns information about images whose load was denied because of security
#   considerations. This information can be used by the Boot Manager or another agent to reevaluate the
#   images when the current security profile has been changed, such as when the current user profile
#   changes. There can be more than one instance of this protocol installed.
# 
#   Copyright (c) 2009 - 2018, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# DeferredImageLoad.py
#
# EfiPy2.MdePkg.Protocol.DeferredImageLoad
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __DEFERRED_IMAGE_LOAD_H__
# #define __DEFERRED_IMAGE_LOAD_H__
from EfiPy2 import *

# 
# ///
# /// Global ID for the Deferred Image Load Protocol
# ///
# #define EFI_DEFERRED_IMAGE_LOAD_PROTOCOL_GUID \
#   { \
#     0x15853d7c, 0x3ddf, 0x43e0, { 0xa1, 0xcb, 0xeb, 0xf8, 0x5b, 0x8f, 0x87, 0x2c } \
#   };
gEfiDeferredImageLoadProtocolGuid   = \
  EFI_GUID (0x15853d7c, 0x3ddf, 0x43e0, ( 0xa1, 0xcb, 0xeb, 0xf8, 0x5b, 0x8f, 0x87, 0x2c ))

# 
# typedef struct _EFI_DEFERRED_IMAGE_LOAD_PROTOCOL EFI_DEFERRED_IMAGE_LOAD_PROTOCOL;
class EFI_DEFERRED_IMAGE_LOAD_PROTOCOL (Structure):
  pass

# 
# /**
#   Returns information about a deferred image.
# 
#   This function returns information about a single deferred image. The deferred images are numbered
#   consecutively, starting with 0.  If there is no image which corresponds to ImageIndex, then
#   EFI_NOT_FOUND is returned. All deferred images may be returned by iteratively calling this
#   function until EFI_NOT_FOUND is returned.
#   Image may be NULL and ImageSize set to 0 if the decision to defer execution was made because
#   of the location of the executable image rather than its actual contents.  record handle until
#   there are no more, at which point UserInfo will point to NULL.
# 
#   @param[in]  This               Points to this instance of the EFI_DEFERRED_IMAGE_LOAD_PROTOCOL.
#   @param[in]  ImageIndex         Zero-based index of the deferred index.
#   @param[out] ImageDevicePath    On return, points to a pointer to the device path of the image.
#                                  The device path should not be freed by the caller.
#   @param[out] Image              On return, points to the first byte of the image or NULL if the
#                                  image is not available. The image should not be freed by the caller
#                                  unless LoadImage() has been called successfully.
#   @param[out] ImageSize          On return, the size of the image, or 0 if the image is not available.
#   @param[out] BootOption         On return, points to TRUE if the image was intended as a boot option
#                                  or FALSE if it was not intended as a boot option.
# 
#   @retval EFI_SUCCESS            Image information returned successfully.
#   @retval EFI_NOT_FOUND          ImageIndex does not refer to a valid image.
#   @retval EFI_INVALID_PARAMETER  ImageDevicePath is NULL or Image is NULL or ImageSize is NULL or
#                                  BootOption is NULL.
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_DEFERRED_IMAGE_INFO)(
#   IN  EFI_DEFERRED_IMAGE_LOAD_PROTOCOL  *This,
#   IN  UINTN                             ImageIndex,
#   OUT EFI_DEVICE_PATH_PROTOCOL          **ImageDevicePath,
#   OUT VOID                              **Image,
#   OUT UINTN                             *ImageSize,
#   OUT BOOLEAN                           *BootOption
#   );
EFI_DEFERRED_IMAGE_INFO = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_DEFERRED_IMAGE_LOAD_PROTOCOL),    # IN      *This
  UINTN,                                        # IN      ImageIndex
  POINTER (POINTER (EFI_DEVICE_PATH_PROTOCOL)), #    OUT  **ImageDevicePath,
  POINTER(PVOID),                               #    OUT  **Image,
  POINTER(UINTN),                               #    OUT  *ImageSize
  POINTER(BOOLEAN)                              #    OUT  *BootOption
  )

# 
# ///
# /// This protocol returns information about a deferred image.
# ///
# struct _EFI_DEFERRED_IMAGE_LOAD_PROTOCOL {
#   EFI_DEFERRED_IMAGE_INFO    GetImageInfo;
# };
EFI_DEFERRED_IMAGE_LOAD_PROTOCOL._fields_ = [
    ("GetImageInfo",  EFI_DEFERRED_IMAGE_INFO)
  ]

# 
# extern EFI_GUID  gEfiDeferredImageLoadProtocolGuid;
# 
# #endif
# 