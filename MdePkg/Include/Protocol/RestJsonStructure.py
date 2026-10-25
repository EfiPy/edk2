# /** @file
#   This file defines the EFI REST JSON Structure Protocol interface.
# 
#   (C) Copyright 2020 Hewlett Packard Enterprise Development LP<BR>
# 
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   This Protocol is introduced in UEFI Specification 2.8
# 
# **/
# RestJsonStructure.py
#
# EfiPy2.MdePkg.Protocol.RestJsonStructure
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef EFI_REST_JSON_STRUCTURE_PROTOCOL_H_
# #define EFI_REST_JSON_STRUCTURE_PROTOCOL_H_
from EfiPy2 import *

# 
# ///
# /// GUID definitions
# ///
# #define EFI_REST_JSON_STRUCTURE_PROTOCOL_GUID \
#   { \
#     0xa9a048f6, 0x48a0, 0x4714, {0xb7, 0xda, 0xa9, 0xad,0x87, 0xd4, 0xda, 0xc9 } \
#   }
EFI_REST_JSON_STRUCTURE_PROTOCOL_GUID           = \
  EFI_GUID (0xa9a048f6, 0x48a0, 0x4714, (0xb7, 0xda, 0xa9, 0xad,0x87, 0xd4, 0xda, 0xc9 ))

# 
# typedef struct _EFI_REST_JSON_STRUCTURE_PROTOCOL  EFI_REST_JSON_STRUCTURE_PROTOCOL;
class EFI_REST_JSON_STRUCTURE_PROTOCOL (Structure):
  pass

# typedef CHAR8                                     *EFI_REST_JSON_RESOURCE_TYPE_DATATYPE;
EFI_REST_JSON_RESOURCE_TYPE_DATATYPE = POINTER(CHAR8)

# 
# ///
# /// Structure defintions of resource name space.
# ///
# /// The fields declared in this structure define the
# /// name and revision of payload delievered throught
# /// REST API.
# ///
# typedef struct _EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE {
#   CHAR8    *ResourceTypeName; ///< Resource type name
#   CHAR8    *MajorVersion;     ///< Resource major version
#   CHAR8    *MinorVersion;     ///< Resource minor version
#   CHAR8    *ErrataVersion;    ///< Resource errata version
# } EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE;
class EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE (Structure):
  _fields_ = [
    ("ResourceTypeName",    POINTER(CHAR8)),
    ("MajorVersion",        POINTER(CHAR8)),
    ("MinorVersion",        POINTER(CHAR8)),
    ("ErrataVersion",       POINTER(CHAR8))
  ]

# 
# ///
# /// REST resource type identifier
# ///
# /// REST resource type consists of name space and data type.
# ///
# typedef struct _EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER {
#   EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE    NameSpace; ///< Namespace of this resource type.
#   EFI_REST_JSON_RESOURCE_TYPE_DATATYPE     DataType;  ///< Name of data type declared in this
#                                                       ///< resource type.
# } EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER;
class EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER (Structure):
  _fields_ = [
    ("NameSpace",   EFI_REST_JSON_RESOURCE_TYPE_NAMESPACE),
    ("DataType",    EFI_REST_JSON_RESOURCE_TYPE_DATATYPE)
  ]

# 
# ///
# /// List of JSON to C structure conversions which this convertor supports.
# ///
# typedef struct _EFI_REST_JSON_STRUCTURE_SUPPORTED {
#   LIST_ENTRY                                NextSupportedRsrcInterp; ///< Linklist to next supported conversion.
#   EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER    RestResourceInterp;      ///< JSON resource type this convertor supports.
# } EFI_REST_JSON_STRUCTURE_SUPPORTED;
class EFI_REST_JSON_STRUCTURE_SUPPORTED (Structure):
  _fields_ = [
    ("NextSupportedRsrcInterp", LIST_ENTRY),
    ("RestResourceInterp",      EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER)
  ]

# 
# ///
# /// The header file of JSON C structure
# ///
# typedef struct _EFI_REST_JSON_STRUCTURE_HEADER {
#   EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER    JsonRsrcIdentifier; ///< Resource identifier which use to
#                                                                 ///< choice the proper interpreter.
#   ///< Follow by a pointer points to JSON structure, the content in the
#   ///< JSON structure is implementation-specific according to converter producer.
#   VOID                                      *JsonStructurePointer;
# } EFI_REST_JSON_STRUCTURE_HEADER;
class EFI_REST_JSON_STRUCTURE_HEADER (Structure):
  _fields_ = [
    ("JsonRsrcIdentifier",      EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER),
    ("JsonStructurePointer",    PVOID)
  ]

# 
# /**
#   JSON-IN C Structure-OUT function. Convert the given REST JSON resource into structure.
# 
#   @param[in]    This                This is the EFI_REST_JSON_STRUCTURE_PROTOCOL instance.
#   @param[in]    JsonRsrcIdentifier  This indicates the resource type and version is given in
#                                     ResourceJsonText.
#   @param[in]    ResourceJsonText    REST JSON resource in text format.
#   @param[out]   JsonStructure       Pointer to receive the pointer to EFI_REST_JSON_STRUCTURE_HEADER
# 
#   @retval EFI_SUCCESS
#   @retval Others
# --*/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REST_JSON_STRUCTURE_TO_STRUCTURE)(
#   IN  EFI_REST_JSON_STRUCTURE_PROTOCOL        *This,
#   IN  EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER *JsonRsrcIdentifier OPTIONAL,
#   IN  CHAR8                                   *ResourceJsonText,
#   OUT  EFI_REST_JSON_STRUCTURE_HEADER         **JsonStructure
#   );
EFI_REST_JSON_STRUCTURE_TO_STRUCTURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_RESOURCE_TYPE_IDENTIFIER),  #   IN  *JsonRsrcIdentifier OPTIONAL,
  POINTER(CHAR8),                                   #   IN  *ResourceJsonText,
  POINTER(POINTER(EFI_REST_JSON_STRUCTURE_HEADER))  #   OUT **JsonStructure
  )

# 
# /**
#   Convert the given REST JSON structure into JSON text.
# 
#   @param[in]    This                 This is the EFI_REST_JSON_STRUCTURE_PROTOCOL instance.
#   @param[in]    JsonStructureHeader  The point to EFI_REST_JSON_STRUCTURE_HEADER  structure.
#   @param[out]   ResourceJsonText     Pointer to receive REST JSON resource in text format.
# 
#   @retval EFI_SUCCESS
#   @retval Others
# 
# --*/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REST_JSON_STRUCTURE_TO_JSON)(
#   IN EFI_REST_JSON_STRUCTURE_PROTOCOL     *This,
#   IN EFI_REST_JSON_STRUCTURE_HEADER       *JsonStructureHeader,
#   OUT CHAR8                               **ResourceJsonText
#   );
EFI_REST_JSON_STRUCTURE_TO_JSON = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_STRUCTURE_HEADER),          #   IN  *JsonStructureHeader,
  POINTER(POINTER(CHAR8))                           #   OUT **ResourceJsonText
  )

# 
# /**
#   This function destroys the REST JSON structure.
# 
#   @param[in]    This                 This is the EFI_REST_JSON_STRUCTURE_PROTOCOL instance.
#   @param[in]    JsonStructureHeader  JSON structure to destroy.
# 
#   @retval EFI_SUCCESS
#   @retval Others
# 
# --*/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE)(
#   IN EFI_REST_JSON_STRUCTURE_PROTOCOL   *This,
#   IN EFI_REST_JSON_STRUCTURE_HEADER     *JsonStructureHeader
#   );
EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),        #   IN  *This
  POINTER(EFI_REST_JSON_STRUCTURE_HEADER)           #   IN  *JsonStructureHeader
  )

# 
# /**
#   This function provides REST JSON resource to structure converter registration.
# 
#   @param[in]    This                     This is the EFI_REST_JSON_STRUCTURE_PROTOCOL instance.
#   @param[in]    JsonStructureSupported   The type and version of REST JSON resource which this converter
#                                          supports.
#   @param[in]    ToStructure              The function to convert REST JSON resource to structure.
#   @param[in]    ToJson                   The function to convert REST JSON structure to JSON in text format.
#   @param[in]    DestroyStructure         Destroy REST JSON structure returned in ToStructure() function.
# 
#   @retval EFI_SUCCESS             Register successfully.
#   @retval Others                  Fail to register.
# 
# --*/
# typedef
# EFI_STATUS
# (EFIAPI *EFI_REST_JSON_STRUCTURE_REGISTER)(
#   IN EFI_REST_JSON_STRUCTURE_PROTOCOL       *This,
#   IN EFI_REST_JSON_STRUCTURE_SUPPORTED      *JsonStructureSupported,
#   IN EFI_REST_JSON_STRUCTURE_TO_STRUCTURE   ToStructure,
#   IN EFI_REST_JSON_STRUCTURE_TO_JSON        ToJson,
#   IN EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE DestroyStructure
#   );
EFI_REST_JSON_STRUCTURE_REGISTER = CFUNCTYPE (
  EFI_STATUS,
  POINTER(EFI_REST_JSON_STRUCTURE_PROTOCOL),    #   IN *This
  POINTER(EFI_REST_JSON_STRUCTURE_SUPPORTED),   #   IN *JsonStructureSupported,
  EFI_REST_JSON_STRUCTURE_TO_STRUCTURE,         #   IN ToStructure,
  EFI_REST_JSON_STRUCTURE_TO_JSON,              #   IN ToJson,
  EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE     #   IN DestroyStructure
  )

# 
# ///
# /// EFI REST JSON to C structure protocol definition.
# ///
# struct _EFI_REST_JSON_STRUCTURE_PROTOCOL {
#   EFI_REST_JSON_STRUCTURE_REGISTER             Register;         ///< Register JSON to C structure convertor
#   EFI_REST_JSON_STRUCTURE_TO_STRUCTURE         ToStructure;      ///< The function to convert JSON to C structure
#   EFI_REST_JSON_STRUCTURE_TO_JSON              ToJson;           ///< The function to convert C structure to JSON
#   EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE    DestoryStructure; ///< Destory C structure.
# };
EFI_REST_JSON_STRUCTURE_PROTOCOL._fields_ = [
    ("Register",            EFI_REST_JSON_STRUCTURE_REGISTER),
    ("ToStructure",         EFI_REST_JSON_STRUCTURE_TO_STRUCTURE),
    ("ToJson",              EFI_REST_JSON_STRUCTURE_TO_JSON),
    ("DestoryStructure",    EFI_REST_JSON_STRUCTURE_DESTORY_STRUCTURE)
  ]

# 
# #endif
# 