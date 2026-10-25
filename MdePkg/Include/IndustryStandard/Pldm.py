# /** @file
# 
#   The definitions of DMTF Platform Level Data Model (PLDM)
#   Base Specification.
# 
#   Copyright (C) 2023 Advanced Micro Devices, Inc. All rights reserved.
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   DMTF Platform Level Data Model (PLDM) Base Specification
#   Version 1.1.0
#   https://www.dmtf.org/sites/default/files/standards/documents/DSP0240_1.1.0.pdf
# 
# **/
# 
# Pldm.py
#
# EfiPy2.MdePkg.IndustryStandard.Pldm
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef PLDM_H_
# #define PLDM_H_
# 
# #pragma pack(1)
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #define PLDM_MESSAGE_HEADER_VERSION  0
PLDM_MESSAGE_HEADER_VERSION  = 0

# 
# ///
# /// General definitions from Platform Level Data Model (PLDM) Base
# /// Specification (DMTF DSP0240)
# ///
# typedef struct  {
#   UINT8    InstanceId    : 5;          ///< Request instance ID.
#   UINT8    Reserved      : 1;          ///< Reserved bit.
#   UINT8    DatagramBit   : 1;          ///< used to indicate whether the Instance ID field is
#                                        ///< being used for tracking and matching requests and
#                                        ///< responses, or just being used for asynchronous
#                                        ///< notifications.
#   UINT8    RequestBit    : 1;          ///< Request bit.
#   UINT8    PldmType      : 6;          ///< PLDM message type.
#   UINT8    HeaderVersion : 2;          ///< Header version.
#   UINT8    PldmTypeCommandCode;        ///< The command code of PLDM message type.
# } PLDM_MESSAGE_HEADER;
class PLDM_MESSAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("InstanceId",          UINT8, 5),
    ("Reserved",            UINT8, 1),
    ("DatagramBit",         UINT8, 1),
    ("RequestBit",          UINT8, 1),
    ("PldmType",            UINT8, 6),
    ("HeaderVersion",       UINT8, 2),
    ("PldmTypeCommandCode", UINT8)
    ]

# 
# typedef PLDM_MESSAGE_HEADER PLDM_REQUEST_HEADER;
PLDM_REQUEST_HEADER = PLDM_MESSAGE_HEADER

# 
# #define PLDM_MESSAGE_HEADER_IS_REQUEST        1
# #define PLDM_MESSAGE_HEADER_IS_DATAGRAM       1
# #define PLDM_MESSAGE_HEADER_INSTANCE_ID_MASK  0x1f
PLDM_MESSAGE_HEADER_IS_REQUEST        = 1
PLDM_MESSAGE_HEADER_IS_DATAGRAM       = 1
PLDM_MESSAGE_HEADER_INSTANCE_ID_MASK  = 0x1f

# 
# typedef struct {
#   PLDM_MESSAGE_HEADER    PldmHeader;
#   UINT8                  PldmCompletionCode;   ///< PLDM completion  of response message.
# } PLDM_RESPONSE_HEADER;
class PLDM_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("PldmHeader",          PLDM_MESSAGE_HEADER),
    ("PldmCompletionCode",  UINT8)
  ]

# 
# #pragma pack()
# 
# #define PLDM_HEADER_VERSION  0x00
PLDM_HEADER_VERSION  = 0x00

# 
# #define PLDM_COMPLETION_CODE_SUCCESS                     0x00
# #define PLDM_COMPLETION_CODE_ERROR                       0x01
# #define PLDM_COMPLETION_CODE_ERROR_INVALID_DATA          0x02
# #define PLDM_COMPLETION_CODE_ERROR_INVALID_LENGTH        0x03
# #define PLDM_COMPLETION_CODE_ERROR_NOT_READY             0x04
# #define PLDM_COMPLETION_CODE_ERROR_UNSUPPORTED_PLDM_CMD  0x05
# #define PLDM_COMPLETION_CODE_ERROR_INVALID_PLDM_TYPE     0x20
# #define PLDM_COMPLETION_CODE_SPECIFIC_START              0x80
# #define PLDM_COMPLETION_CODE_SPECIFIC_END                0xff
PLDM_COMPLETION_CODE_SUCCESS                     = 0x00
PLDM_COMPLETION_CODE_ERROR                       = 0x01
PLDM_COMPLETION_CODE_ERROR_INVALID_DATA          = 0x02
PLDM_COMPLETION_CODE_ERROR_INVALID_LENGTH        = 0x03
PLDM_COMPLETION_CODE_ERROR_NOT_READY             = 0x04
PLDM_COMPLETION_CODE_ERROR_UNSUPPORTED_PLDM_CMD  = 0x05
PLDM_COMPLETION_CODE_ERROR_INVALID_PLDM_TYPE     = 0x20
PLDM_COMPLETION_CODE_SPECIFIC_START              = 0x80
PLDM_COMPLETION_CODE_SPECIFIC_END                = 0xff

# 
# ///
# /// Type Code definitions from Platform Level Data Model (PLDM) IDs
# /// and Codes Specification (DMTF DSP0245)
# /// https://www.dmtf.org/sites/default/files/standards/documents/DSP0245_1.3.0.pdf
# ///
# #define PLDM_TYPE_MESSAGE_CONTROL_AND_DISCOVERY    0x00
# #define PLDM_TYPE_SMBIOS                           0x01
# #define PLDM_TYPE_PLATFORM_MONITORING_AND_CONTROL  0x02
# #define PLDM_TYPE_BIOS_CONTROL_AND_CONFIGURATION   0x03
PLDM_TYPE_MESSAGE_CONTROL_AND_DISCOVERY    = 0x00
PLDM_TYPE_SMBIOS                           = 0x01
PLDM_TYPE_PLATFORM_MONITORING_AND_CONTROL  = 0x02
PLDM_TYPE_BIOS_CONTROL_AND_CONFIGURATION   = 0x03

# 
# #define PLDM_TRANSFER_FLAG_START          0x01
# #define PLDM_TRANSFER_FLAG_MIDDLE         0x02
# #define PLDM_TRANSFER_FLAG_END            0x04
# #define PLDM_TRANSFER_FLAG_START_AND_END  0x05
PLDM_TRANSFER_FLAG_START          = 0x01
PLDM_TRANSFER_FLAG_MIDDLE         = 0x02
PLDM_TRANSFER_FLAG_END            = 0x04
PLDM_TRANSFER_FLAG_START_AND_END  = 0x05

# 
# #define PLDM_TRANSFER_OPERATION_FLAG_GET_NEXT_PART   0x00
# #define PLDM_TRANSFER_OPERATION_FLAG_GET_FIRST_PART  0x01
PLDM_TRANSFER_OPERATION_FLAG_GET_NEXT_PART   = 0x00
PLDM_TRANSFER_OPERATION_FLAG_GET_FIRST_PART  = 0x01

# #endif // PLDM_H_
# 