# /** @file
#   IPMI 2.0 definitions from the IPMI Specification Version 2.0, Revision 1.1.
# 
#   Copyright (c) 1999 - 2015, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# **/
# 
# IpmiNetFnFirmware.py
#
# EfiPy2.MdePkg.IndustryStandard.IpmiNetFnFirmware
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2016 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _IPMI_NET_FN_FIRMWARE_H_
# #define _IPMI_NET_FN_FIRMWARE_H_
from EfiPy2 import *

# 
# //
# // Net function definition for Firmware command
# //
# #define IPMI_NETFN_FIRMWARE  0x08
IPMI_NETFN_FIRMWARE  = 0x08

# 
# //
# // All Firmware commands and their structure definitions to follow here
# //
# 
# // ----------------------------------------------------------------------------------------
# //    Definitions for Get BMC Execution Context
# // ----------------------------------------------------------------------------------------
# #define IPMI_GET_BMC_EXECUTION_CONTEXT  0x23
IPMI_GET_BMC_EXECUTION_CONTEXT  = 0x23

# 
# //
# //  Constants and Structure definitions for "Get Device ID" command to follow here
# //
# typedef struct {
#   UINT8    CurrentExecutionContext;
#   UINT8    PartitionPointer;
# } IPMI_MSG_GET_BMC_EXEC_RSP;
class IPMI_MSG_GET_BMC_EXEC_RSP (Structure):
  _fields_ = [
    ("CurrentExecutionContext", UINT8),
    ("PartitionPointer",        UINT8)
  ]

# 
# //
# // Current Execution Context responses
# //
# #define IPMI_BMC_IN_FORCED_UPDATE_MODE  0x11
IPMI_BMC_IN_FORCED_UPDATE_MODE  = 0x11

# 
# #endif
# 