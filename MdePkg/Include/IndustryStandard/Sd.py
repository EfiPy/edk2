# /** @file
#   Header file for SD memory card support.
# 
#   This header file contains some definitions defined in SD Physical Layer Simplified
#   Specification Version 4.10 spec.
# 
#   Copyright (c) 2015, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
# Sd.py
#
# EfiPy2.MdePkg.IndustryStandard.Sd
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __SD_H__
# #define __SD_H__
from EfiPy2.MdePkg.IndustryStandard import *

# 
# //
# // SD command index
# //
# #define  SD_GO_IDLE_STATE         0
# #define  SD_ALL_SEND_CID          2
# #define  SD_SET_RELATIVE_ADDR     3
# #define  SD_SET_DSR               4
# #define  SDIO_SEND_OP_COND        5
# #define  SD_SWITCH_FUNC           6
# #define  SD_SELECT_DESELECT_CARD  7
# #define  SD_SEND_IF_COND          8
# #define  SD_SEND_CSD              9
# #define  SD_SEND_CID              10
# #define  SD_VOLTAGE_SWITCH        11
# #define  SD_STOP_TRANSMISSION     12
# #define  SD_SEND_STATUS           13
# #define  SD_GO_INACTIVE_STATE     15
# #define  SD_SET_BLOCKLEN          16
# #define  SD_READ_SINGLE_BLOCK     17
# #define  SD_READ_MULTIPLE_BLOCK   18
# #define  SD_SEND_TUNING_BLOCK     19
# #define  SD_SPEED_CLASS_CONTROL   20
# #define  SD_SET_BLOCK_COUNT       23
# #define  SD_WRITE_SINGLE_BLOCK    24
# #define  SD_WRITE_MULTIPLE_BLOCK  25
# #define  SD_PROGRAM_CSD           27
# #define  SD_SET_WRITE_PROT        28
# #define  SD_CLR_WRITE_PROT        29
# #define  SD_SEND_WRITE_PROT       30
# #define  SD_ERASE_WR_BLK_START    32
# #define  SD_ERASE_WR_BLK_END      33
# #define  SD_ERASE                 38
# #define  SD_LOCK_UNLOCK           42
# #define  SD_READ_EXTR_SINGLE      48
# #define  SD_WRITE_EXTR_SINGLE     49
# #define  SDIO_RW_DIRECT           52
# #define  SDIO_RW_EXTENDED         53
# #define  SD_APP_CMD               55
# #define  SD_GEN_CMD               56
# #define  SD_READ_EXTR_MULTI       58
# #define  SD_WRITE_EXTR_MULTI      59
SD_GO_IDLE_STATE         = 0
SD_ALL_SEND_CID          = 2
SD_SET_RELATIVE_ADDR     = 3
SD_SET_DSR               = 4
SDIO_SEND_OP_COND        = 5
SD_SWITCH_FUNC           = 6
SD_SELECT_DESELECT_CARD  = 7
SD_SEND_IF_COND          = 8
SD_SEND_CSD              = 9
SD_SEND_CID              = 10
SD_VOLTAGE_SWITCH        = 11
SD_STOP_TRANSMISSION     = 12
SD_SEND_STATUS           = 13
SD_GO_INACTIVE_STATE     = 15
SD_SET_BLOCKLEN          = 16
SD_READ_SINGLE_BLOCK     = 17
SD_READ_MULTIPLE_BLOCK   = 18
SD_SEND_TUNING_BLOCK     = 19
SD_SPEED_CLASS_CONTROL   = 20
SD_SET_BLOCK_COUNT       = 23
SD_WRITE_SINGLE_BLOCK    = 24
SD_WRITE_MULTIPLE_BLOCK  = 25
SD_PROGRAM_CSD           = 27
SD_SET_WRITE_PROT        = 28
SD_CLR_WRITE_PROT        = 29
SD_SEND_WRITE_PROT       = 30
SD_ERASE_WR_BLK_START    = 32
SD_ERASE_WR_BLK_END      = 33
SD_ERASE                 = 38
SD_LOCK_UNLOCK           = 42
SD_READ_EXTR_SINGLE      = 48
SD_WRITE_EXTR_SINGLE     = 49
SDIO_RW_DIRECT           = 52
SDIO_RW_EXTENDED         = 53
SD_APP_CMD               = 55
SD_GEN_CMD               = 56
SD_READ_EXTR_MULTI       = 58
SD_WRITE_EXTR_MULTI      = 59

# 
# #define  SD_SET_BUS_WIDTH           6           // ACMD6
# #define  SD_STATUS                  13          // ACMD13
# #define  SD_SEND_NUM_WR_BLOCKS      22          // ACMD22
# #define  SD_SET_WR_BLK_ERASE_COUNT  23          // ACMD23
# #define  SD_SEND_OP_COND            41          // ACMD41
# #define  SD_SET_CLR_CARD_DETECT     42          // ACMD42
# #define  SD_SEND_SCR                51          // ACMD51
SD_SET_BUS_WIDTH           = 6           # ACMD6
SD_STATUS                  = 13          # ACMD13
SD_SEND_NUM_WR_BLOCKS      = 22          # ACMD22
SD_SET_WR_BLK_ERASE_COUNT  = 23          # ACMD23
SD_SEND_OP_COND            = 41          # ACMD41
SD_SET_CLR_CARD_DETECT     = 42          # ACMD42
SD_SEND_SCR                = 51          # ACMD51

# 
# #pragma pack(1)
# typedef struct {
#   UINT8     NotUsed           : 1;              // Not used [0:0]
#   UINT8     Crc               : 7;              // CRC [7:1]
#   UINT16    ManufacturingDate : 12;             // Manufacturing date [19:8]
#   UINT16    Reserved          : 4;              // Reserved [23:20]
#   UINT8     ProductSerialNumber[4];             // Product serial number [55:24]
#   UINT8     ProductRevision;                    // Product revision [63:56]
#   UINT8     ProductName[5];                     // Product name [103:64]
#   UINT8     OemId[2];                           // OEM/Application ID [119:104]
#   UINT8     ManufacturerId;                     // Manufacturer ID [127:120]
# } SD_CID;
class SD_CID (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT8,  1),
    ("Crc",                 UINT8,  7),
    ("ManufacturingDate",   UINT16, 12),
    ("Reserved",            UINT16, 4),
    ("ProductSerialNumber", UINT8 * 4),
    ("ProductRevision",     UINT8),
    ("ProductName",         UINT8 * 5),
    ("OemId",               UINT8 * 2),
    ("ManufacturerId",      UINT8)
    ]

# 
# typedef struct {
#   UINT32    NotUsed          : 1;               // Not used [0:0]
#   UINT32    Crc              : 7;               // CRC [7:1]
#   UINT32    Reserved         : 2;               // Reserved [9:8]
#   UINT32    FileFormat       : 2;               // File format [11:10]
#   UINT32    TmpWriteProtect  : 1;               // Temporary write protection [12:12]
#   UINT32    PermWriteProtect : 1;               // Permanent write protection [13:13]
#   UINT32    Copy             : 1;               // Copy flag (OTP) [14:14]
#   UINT32    FileFormatGrp    : 1;               // File format group [15:15]
#   UINT32    Reserved1        : 5;               // Reserved [20:16]
#   UINT32    WriteBlPartial   : 1;               // Partial blocks for write allowed [21:21]
#   UINT32    WriteBlLen       : 4;               // Max. write data block length [25:22]
#   UINT32    R2WFactor        : 3;               // Write speed factor [28:26]
#   UINT32    Reserved2        : 2;               // Manufacturer default ECC [30:29]
#   UINT32    WpGrpEnable      : 1;               // Write protect group enable [31:31]
# 
#   UINT32    WpGrpSize        : 7;               // Write protect group size [38:32]
#   UINT32    SectorSize       : 7;               // Erase sector size [45:39]
#   UINT32    EraseBlkEn       : 1;               // Erase single block enable [46:46]
#   UINT32    CSizeMul         : 3;               // device size multiplier [49:47]
#   UINT32    VddWCurrMax      : 3;               // max. write current @VDD max [52:50]
#   UINT32    VddWCurrMin      : 3;               // max. write current @VDD min [55:53]
#   UINT32    VddRCurrMax      : 3;               // max. read current @VDD max [58:56]
#   UINT32    VddRCurrMin      : 3;               // max. read current @VDD min [61:59]
#   UINT32    CSizeLow         : 2;               // Device size low 2 bits [63:62]
# 
#   UINT32    CSizeHigh        : 10;              // Device size high 10 bits [73:64]
#   UINT32    Reserved4        : 2;               // Reserved [75:74]
#   UINT32    DsrImp           : 1;               // DSR implemented [76:76]
#   UINT32    ReadBlkMisalign  : 1;               // Read block misalignment [77:77]
#   UINT32    WriteBlkMisalign : 1;               // Write block misalignment [78:78]
#   UINT32    ReadBlPartial    : 1;               // Partial blocks for read allowed [79:79]
#   UINT32    ReadBlLen        : 4;               // Max. read data block length [83:80]
#   UINT32    Ccc              : 12;              // Card command classes [95:84]
# 
#   UINT32    TranSpeed        : 8;               // Max. data transfer rate [103:96]
#   UINT32    Nsac             : 8;               // Data read access-time in CLK cycles (NSAC*100) [111:104]
#   UINT32    Taac             : 8;               // Data read access-time [119:112]
#   UINT32    Reserved5        : 6;               // Reserved [125:120]
#   UINT32    CsdStructure     : 2;               // CSD structure [127:126]
# } SD_CSD;
class SD_CSD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",         UINT32, 1),
    ("Crc",             UINT32, 7),
    ("Reserved",        UINT32, 2),
    ("FileFormat",      UINT32, 2),
    ("TmpWriteProtect", UINT32, 1),
    ("PermWriteProtect",UINT32, 1),
    ("Copy",            UINT32, 1),
    ("FileFormatGrp",   UINT32, 1),
    ("Reserved1",       UINT32, 5),
    ("WriteBlPartial",  UINT32, 1),
    ("WriteBlLen",      UINT32, 4),
    ("R2WFactor",       UINT32, 3),
    ("Reserved2",       UINT32, 2),
    ("WpGrpEnable",     UINT32, 1),

    ("WpGrpSize",       UINT32, 7),
    ("SectorSize",      UINT32, 7),
    ("EraseBlkEn",      UINT32, 1),
    ("CSizeMul",        UINT32, 3),
    ("VddWCurrMax",     UINT32, 3),
    ("VddWCurrMin",     UINT32, 3),
    ("VddRCurrMax",     UINT32, 3),
    ("VddRCurrMin",     UINT32, 3),
    ("CSizeLow",        UINT32, 2),

    ("CSizeHigh",       UINT32, 10),
    ("Reserved4",       UINT32, 2),
    ("DsrImp",          UINT32, 1),
    ("ReadBlkMisalign", UINT32, 1),
    ("WriteBlkMisalign",UINT32, 1),
    ("ReadBlPartial",   UINT32, 1),
    ("ReadBlLen",       UINT32, 4),
    ("Ccc",             UINT32, 12),

    ("TranSpeed",       UINT32, 8),
    ("Nsac",            UINT32, 8),
    ("Taac",            UINT32, 8),
    ("Reserved5",       UINT32, 6),
    ("CsdStructure",    UINT32, 2)
    ]

# 
# typedef struct {
#   UINT32    NotUsed          : 1;               // Not used [0:0]
#   UINT32    Crc              : 7;               // CRC [7:1]
#   UINT32    Reserved         : 2;               // Reserved [9:8]
#   UINT32    FileFormat       : 2;               // File format [11:10]
#   UINT32    TmpWriteProtect  : 1;               // Temporary write protection [12:12]
#   UINT32    PermWriteProtect : 1;               // Permanent write protection [13:13]
#   UINT32    Copy             : 1;               // Copy flag (OTP) [14:14]
#   UINT32    FileFormatGrp    : 1;               // File format group [15:15]
#   UINT32    Reserved1        : 5;               // Reserved [20:16]
#   UINT32    WriteBlPartial   : 1;               // Partial blocks for write allowed [21:21]
#   UINT32    WriteBlLen       : 4;               // Max. write data block length [25:22]
#   UINT32    R2WFactor        : 3;               // Write speed factor [28:26]
#   UINT32    Reserved2        : 2;               // Manufacturer default ECC [30:29]
#   UINT32    WpGrpEnable      : 1;               // Write protect group enable [31:31]
# 
#   UINT32    WpGrpSize        : 7;               // Write protect group size [38:32]
#   UINT32    SectorSize       : 7;               // Erase sector size [45:39]
#   UINT32    EraseBlkEn       : 1;               // Erase single block enable [46:46]
#   UINT32    Reserved3        : 1;               // Reserved [47:47]
#   UINT32    CSizeLow         : 16;              // Device size low 16 bits [63:48]
# 
#   UINT32    CSizeHigh        : 6;               // Device size high 6 bits [69:64]
#   UINT32    Reserved4        : 6;               // Reserved [75:70]
#   UINT32    DsrImp           : 1;               // DSR implemented [76:76]
#   UINT32    ReadBlkMisalign  : 1;               // Read block misalignment [77:77]
#   UINT32    WriteBlkMisalign : 1;               // Write block misalignment [78:78]
#   UINT32    ReadBlPartial    : 1;               // Partial blocks for read allowed [79:79]
#   UINT32    ReadBlLen        : 4;               // Max. read data block length [83:80]
#   UINT32    Ccc              : 12;              // Card command classes [95:84]
# 
#   UINT32    TranSpeed        : 8;               // Max. data transfer rate [103:96]
#   UINT32    Nsac             : 8;               // Data read access-time in CLK cycles (NSAC*100) [111:104]
#   UINT32    Taac             : 8;               // Data read access-time [119:112]
#   UINT32    Reserved5        : 6;               // Reserved [125:120]
#   UINT32    CsdStructure     : 2;               // CSD structure [127:126]
# } SD_CSD2;
class SD_CSD2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NotUsed",             UINT32, 1),
    ("Crc",                 UINT32, 7),
    ("Reserved",            UINT32, 2),
    ("FileFormat",          UINT32, 2),
    ("TmpWriteProtect",     UINT32, 1),
    ("PermWriteProtect",    UINT32, 1),
    ("Copy",                UINT32, 1),
    ("FileFormatGrp",       UINT32, 1),
    ("Reserved1",           UINT32, 5),
    ("WriteBlPartial",      UINT32, 1),
    ("WriteBlLen",          UINT32, 4),
    ("R2WFactor",           UINT32, 3),
    ("Reserved2",           UINT32, 2),
    ("WpGrpEnable",         UINT32, 1),

    ("WpGrpSize",           UINT32, 7),
    ("SectorSize",          UINT32, 7),
    ("EraseBlkEn",          UINT32, 1),
    ("Reserved3",           UINT32, 1),
    ("CSizeLow",            UINT32, 16),

    ("CSizeHigh",           UINT32, 6),
    ("Reserved4",           UINT32, 6),
    ("DsrImp",              UINT32, 1),
    ("ReadBlkMisalign",     UINT32, 1),
    ("WriteBlkMisalign",    UINT32, 1),
    ("ReadBlPartial",       UINT32, 1),
    ("ReadBlLen",           UINT32, 4),
    ("Ccc",                 UINT32, 12),

    ("TranSpeed",           UINT32, 8),
    ("Nsac",                UINT32, 8),
    ("Taac",                UINT32, 8),
    ("Reserved5",           UINT32, 6),
    ("CsdStructure",        UINT32, 2)
    ]

# 
# typedef struct {
#   UINT32    Reserved;                           // Reserved [31:0]
# 
#   UINT32    CmdSupport         : 4;             // Command Support bits [35:32]
#   UINT32    Reserved1          : 6;             // Reserved [41:36]
#   UINT32    SdSpec4            : 1;             // Spec. Version 4.00 or higher [42:42]
#   UINT32    ExSecurity         : 4;             // Extended Security Support [46:43]
#   UINT32    SdSpec3            : 1;             // Spec. Version 3.00 or higher [47:47]
#   UINT32    SdBusWidths        : 4;             // DAT Bus widths supported [51:48]
#   UINT32    SdSecurity         : 3;             // CPRM security support [54:52]
#   UINT32    DataStatAfterErase : 1;             // Data status after erases [55]
#   UINT32    SdSpec             : 4;             // SD Memory Card Spec. Version [59:56]
#   UINT32    ScrStructure       : 4;             // SCR Structure [63:60]
# } SD_SCR;
class SD_SCR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Reserved",            UINT32),

    ("CmdSupport",          UINT32, 4),
    ("Reserved1",           UINT32, 6),
    ("SdSpec4",             UINT32, 1),
    ("ExSecurity",          UINT32, 4),
    ("SdSpec3",             UINT32, 1),
    ("SdBusWidths",         UINT32, 4),
    ("SdSecurity",          UINT32, 3),
    ("DataStatAfterErase",  UINT32, 1),
    ("SdSpec",              UINT32, 4),
    ("ScrStructure",        UINT32, 4)
    ]

# 
# #pragma pack()
# 
# #endif
# 