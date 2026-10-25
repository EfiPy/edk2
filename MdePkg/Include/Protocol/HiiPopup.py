# /** @file
#   This protocol provides services to display a popup window.
#   The protocol is typically produced by the forms browser and consumed by a driver callback handler.
# 
#   Copyright (c) 2017-2021, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol was introduced in UEFI Specification 2.7.
# 
# **/
# HiiPopup.py
#
# EfiPy2.MdePkg.Protocol.HiiPopup
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __HII_POPUP_H__
# #define __HII_POPUP_H__
from EfiPy2 import *
from EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation import \
    EFI_HII_HANDLE, \
    EFI_STRING_ID

# 
# #define EFI_HII_POPUP_PROTOCOL_GUID \
#   {0x4311edc0, 0x6054, 0x46d4, {0x9e, 0x40, 0x89, 0x3e, 0xa9, 0x52, 0xfc, 0xcc}}
gEfiHiiPopupProtocolGuid = \
  EFI_GUID (0x4311edc0, 0x6054, 0x46d4, (0x9e, 0x40, 0x89, 0x3e, 0xa9, 0x52, 0xfc, 0xcc ))

# 
# #define EFI_HII_POPUP_PROTOCOL_REVISION  1
EFI_HII_POPUP_PROTOCOL_REVISION  = 1

# 
# typedef struct _EFI_HII_POPUP_PROTOCOL EFI_HII_POPUP_PROTOCOL;
class EFI_HII_POPUP_PROTOCOL (Structure):
  pass

# 
# typedef enum {
#   EfiHiiPopupStyleInfo,
#   EfiHiiPopupStyleWarning,
#   EfiHiiPopupStyleError
# } EFI_HII_POPUP_STYLE;
EfiHiiPopupStyleInfo    = 1
EfiHiiPopupStyleWarning = 2
EfiHiiPopupStyleError   = 3
EFI_HII_POPUP_STYLE     = ENUM

# 
# typedef enum {
#   EfiHiiPopupTypeOk,
#   EfiHiiPopupTypeOkCancel,
#   EfiHiiPopupTypeYesNo,
#   EfiHiiPopupTypeYesNoCancel
# } EFI_HII_POPUP_TYPE;
EfiHiiPopupTypeOk           = 1
EfiHiiPopupTypeOkCancel     = 2
EfiHiiPopupTypeYesNo        = 3
EfiHiiPopupTypeYesNoCancel  = 4
EFI_HII_POPUP_TYPE          = ENUM

# 
# typedef enum {
#   EfiHiiPopupSelectionOk,
#   EfiHiiPopupSelectionCancel,
#   EfiHiiPopupSelectionYes,
#   EfiHiiPopupSelectionNo
# } EFI_HII_POPUP_SELECTION;
EfiHiiPopupSelectionOk      = 1
EfiHiiPopupSelectionCancel  = 2
EfiHiiPopupSelectionYes     = 3
EfiHiiPopupSelectionNo      = 4
EFI_HII_POPUP_SELECTION     = ENUM

# 
# /**
#   Displays a popup window.
# 
#   @param  This           A pointer to the EFI_HII_POPUP_PROTOCOL instance.
#   @param  PopupStyle     Popup style to use.
#   @param  PopupType      Type of the popup to display.
#   @param  HiiHandle      HII handle of the string pack containing Message
#   @param  Message        A message to display in the popup box.
#   @param  UserSelection  User selection.
# 
#   @retval EFI_SUCCESS            The popup box was successfully displayed.
#   @retval EFI_INVALID_PARAMETER  HiiHandle and Message do not define a valid HII string.
#   @retval EFI_INVALID_PARAMETER  PopupType is not one of the values defined by this specification.
#   @retval EFI_OUT_OF_RESOURCES   There are not enough resources available to display the popup box.
# 
# **/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_HII_CREATE_POPUP)(
#   IN  EFI_HII_POPUP_PROTOCOL  *This,
#   IN  EFI_HII_POPUP_STYLE     PopupStyle,
#   IN  EFI_HII_POPUP_TYPE      PopupType,
#   IN  EFI_HII_HANDLE          HiiHandle,
#   IN  EFI_STRING_ID           Message,
#   OUT EFI_HII_POPUP_SELECTION *UserSelection OPTIONAL
#   );
EFI_HII_CREATE_POPUP = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_HII_POPUP_PROTOCOL),  #   IN  *This,
  EFI_HII_POPUP_STYLE,              #   IN  PopupStyle,
  EFI_HII_POPUP_TYPE,               #   IN  PopupType,
  EFI_HII_HANDLE,                   #   IN  HiiHandle,
  EFI_STRING_ID,                    #   IN  Message,
  POINTER(EFI_HII_POPUP_SELECTION)  #   OUT *UserSelection OPTIONAL
  )

# 
# struct _EFI_HII_POPUP_PROTOCOL {
#   UINT64                  Revision;
#   EFI_HII_CREATE_POPUP    CreatePopup;
# };
EFI_HII_POPUP_PROTOCOL._fields_ = [
    ("Revision",        UINT64)
  ]

# 
# extern EFI_GUID  gEfiHiiPopupProtocolGuid;
# 
# #endif
# 