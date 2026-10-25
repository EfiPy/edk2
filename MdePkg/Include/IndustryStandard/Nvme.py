# /** @file
#   Definitions based on NVMe spec. version 1.1.
# 
#   (C) Copyright 2016 Hewlett Packard Enterprise Development LP<BR>
#   Copyright (c) 2017 - 2023, Intel Corporation. All rights reserved.<BR>
#   SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Specification Reference:
#   NVMe Specification 1.1
#   NVMe Specification 1.4
#   NVMe Specification 2.0
# 
# **/
# Nvme.py
#
# EfiPy2.MdePkg.IndustryStandard.Nvme
#   part of EfiPy2
#
# Copyright (C) 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __NVM_E_H__
# #define __NVM_E_H__
# 
# #pragma pack(1)
from EfiPy2.MdePkg.IndustryStandard import *

# 
# //
# // controller register offsets
# //
# #define NVME_CAP_OFFSET     0x0000        // Controller Capabilities
# #define NVME_VER_OFFSET     0x0008        // Version
# #define NVME_INTMS_OFFSET   0x000c        // Interrupt Mask Set
# #define NVME_INTMC_OFFSET   0x0010        // Interrupt Mask Clear
# #define NVME_CC_OFFSET      0x0014        // Controller Configuration
# #define NVME_CSTS_OFFSET    0x001c        // Controller Status
# #define NVME_NSSR_OFFSET    0x0020        // NVM Subsystem Reset
# #define NVME_AQA_OFFSET     0x0024        // Admin Queue Attributes
# #define NVME_ASQ_OFFSET     0x0028        // Admin Submission Queue Base Address
# #define NVME_ACQ_OFFSET     0x0030        // Admin Completion Queue Base Address
# #define NVME_BPINFO_OFFSET  0x0040        // Boot Partition Information
# #define NVME_BPRSEL_OFFSET  0x0044        // Boot Partition Read Select
# #define NVME_BPMBL_OFFSET   0x0048        // Boot Partition Memory Buffer Location
# #define NVME_SQ0_OFFSET     0x1000        // Submission Queue 0 (admin) Tail Doorbell
# #define NVME_CQ0_OFFSET     0x1004        // Completion Queue 0 (admin) Head Doorbell
NVME_CAP_OFFSET     = 0x0000        # Controller Capabilities
NVME_VER_OFFSET     = 0x0008        # Version
NVME_INTMS_OFFSET   = 0x000c        # Interrupt Mask Set
NVME_INTMC_OFFSET   = 0x0010        # Interrupt Mask Clear
NVME_CC_OFFSET      = 0x0014        # Controller Configuration
NVME_CSTS_OFFSET    = 0x001c        # Controller Status
NVME_NSSR_OFFSET    = 0x0020        # NVM Subsystem Reset
NVME_AQA_OFFSET     = 0x0024        # Admin Queue Attributes
NVME_ASQ_OFFSET     = 0x0028        # Admin Submission Queue Base Address
NVME_ACQ_OFFSET     = 0x0030        # Admin Completion Queue Base Address
NVME_BPINFO_OFFSET  = 0x0040        # Boot Partition Information
NVME_BPRSEL_OFFSET  = 0x0044        # Boot Partition Read Select
NVME_BPMBL_OFFSET   = 0x0048        # Boot Partition Memory Buffer Location
NVME_SQ0_OFFSET     = 0x1000        # Submission Queue 0 (admin) Tail Doorbell
NVME_CQ0_OFFSET     = 0x1004        # Completion Queue 0 (admin) Head Doorbell

# 
# //
# // These register offsets are defined as 0x1000 + (N * (4 << CAP.DSTRD))
# // Get the doorbell stride bit shift value from the controller capabilities.
# //
# #define NVME_SQTDBL_OFFSET(QID, DSTRD)  0x1000 + ((2 * (QID)) * (4 << (DSTRD)))         // Submission Queue y (NVM) Tail Doorbell
# #define NVME_CQHDBL_OFFSET(QID, DSTRD)  0x1000 + (((2 * (QID)) + 1) * (4 << (DSTRD)))   // Completion Queue y (NVM) Head Doorbell
def NVME_SQTDBL_OFFSET(QID, DSTRD):
  return 0x1000 + ((2 * (QID)) * (4 << (DSTRD)))         # Submission Queue y (NVM) Tail Doorbell

def NVME_CQHDBL_OFFSET(QID, DSTRD):
  return 0x1000 + (((2 * (QID)) + 1) * (4 << (DSTRD)))   # Completion Queue y (NVM) Head Doorbell

# 
# #pragma pack(1)
# 
# //
# // 3.1.1 Offset 00h: CAP - Controller Capabilities
# //
# typedef struct {
#   UINT16    Mqes;       // Maximum Queue Entries Supported
#   UINT8     Cqr    : 1; // Contiguous Queues Required
#   UINT8     Ams    : 2; // Arbitration Mechanism Supported
#   UINT8     Rsvd1  : 5;
#   UINT8     To;     // Timeout
#   UINT16    Dstrd  : 4;
#   UINT16    Nssrs  : 1; // NVM Subsystem Reset Supported NSSRS
#   UINT16    Css    : 8; // Command Sets Supported - Bit 37
#   UINT16    Bps    : 1; // Boot Partition Support - Bit 45 in NVMe1.4
#   UINT16    Rsvd3  : 2;
#   UINT8     Mpsmin : 4;
#   UINT8     Mpsmax : 4;
#   UINT8     Pmrs   : 1;
#   UINT8     Cmbs   : 1;
#   UINT8     Rsvd4  : 6;
# } NVME_CAP;
class NVME_CAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mqes",   UINT16),
    ("Cqr",    UINT8,  1),
    ("Ams",    UINT8,  2),
    ("Rsvd1",  UINT8,  5),
    ("To",     UINT8),
    ("Dstrd",  UINT16, 4),
    ("Nssrs",  UINT16, 1),
    ("Css",    UINT16, 8),
    ("Bps",    UINT16, 1),
    ("Rsvd3",  UINT16, 2),
    ("Mpsmin", UINT8,  4),
    ("Mpsmax", UINT8,  4),
    ("Pmrs",   UINT8,  1),
    ("Cmbs",   UINT8,  1),
    ("Rsvd4",  UINT8,  6)
    ]

# 
# //
# // 3.1.2 Offset 08h: VS - Version
# //
# typedef struct {
#   UINT16    Mnr;    // Minor version number
#   UINT16    Mjr;    // Major version number
# } NVME_VER;
class NVME_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mnr", UINT16),
    ("Mjr", UINT16)
    ]

# 
# //
# // 3.1.5 Offset 14h: CC - Controller Configuration
# //
# typedef struct {
#   UINT16    En     : 1; // Enable
#   UINT16    Rsvd1  : 3;
#   UINT16    Css    : 3; // I/O Command Set Selected
#   UINT16    Mps    : 4; // Memory Page Size
#   UINT16    Ams    : 3; // Arbitration Mechanism Selected
#   UINT16    Shn    : 2; // Shutdown Notification
#   UINT8     Iosqes : 4; // I/O Submission Queue Entry Size
#   UINT8     Iocqes : 4; // I/O Completion Queue Entry Size
#   UINT8     Rsvd2;
# } NVME_CC;
class NVME_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("En",     UINT16, 1),
    ("Rsvd1",  UINT16, 3),
    ("Css",    UINT16, 3),
    ("Mps",    UINT16, 4),
    ("Ams",    UINT16, 3),
    ("Shn",    UINT16, 2),
    ("Iosqes", UINT8,  4),
    ("Iocqes", UINT8,  4),
    ("Rsvd2",  UINT8)
    ]

# #define NVME_CC_SHN_NORMAL_SHUTDOWN  1
# #define NVME_CC_SHN_ABRUPT_SHUTDOWN  2
NVME_CC_SHN_NORMAL_SHUTDOWN  = 1
NVME_CC_SHN_ABRUPT_SHUTDOWN  = 2

# 
# //
# // 3.1.6 Offset 1Ch: CSTS - Controller Status
# //
# typedef struct {
#   UINT32    Rdy   : 1; // Ready
#   UINT32    Cfs   : 1; // Controller Fatal Status
#   UINT32    Shst  : 2; // Shutdown Status
#   UINT32    Nssro : 1; // NVM Subsystem Reset Occurred
#   UINT32    Rsvd1 : 27;
# } NVME_CSTS;
class NVME_CSTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rdy",   UINT32,  1),
    ("Cfs",   UINT32,  1),
    ("Shst",  UINT32,  2),
    ("Nssro", UINT32,  1),
    ("Rsvd1", UINT32,  27)
    ]

# #define NVME_CSTS_SHST_SHUTDOWN_OCCURRING  1
# #define NVME_CSTS_SHST_SHUTDOWN_COMPLETED  2
NVME_CSTS_SHST_SHUTDOWN_OCCURRING  = 1
NVME_CSTS_SHST_SHUTDOWN_COMPLETED  = 2

# //
# // 3.1.8 Offset 24h: AQA - Admin Queue Attributes
# //
# typedef struct {
#   UINT16    Asqs  : 12; // Submission Queue Size
#   UINT16    Rsvd1 : 4;
#   UINT16    Acqs  : 12; // Completion Queue Size
#   UINT16    Rsvd2 : 4;
# } NVME_AQA;
class NVME_AQA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Asqs",  UINT16,  12),
    ("Rsvd1", UINT16,  4),
    ("Acqs",  UINT16,  12),
    ("Rsvd2", UINT16,  4)
    ]

# 
# //
# // 3.1.9 Offset 28h: ASQ - Admin Submission Queue Base Address
# //
# #define NVME_ASQ  UINT64
NVME_ASQ  = UINT64

# //
# // 3.1.10 Offset 30h: ACQ - Admin Completion Queue Base Address
# //
# #define NVME_ACQ  UINT64
NVME_ACQ = UINT64

# 
# //
# // 3.1.13 Offset 40h: BPINFO - Boot Partition Information
# //
# typedef struct {
#   UINT32    Bpsz  : 15; // Boot Partition Size
#   UINT32    Rsvd1 : 9;
#   UINT32    Brs   : 2;  // Boot Read Status
#   UINT32    Rsvd2 : 5;
#   UINT32    Abpid : 1;  // Active Boot Partition ID
# } NVME_BPINFO;
class NVME_BPINFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bpsz",  UINT32,  15),
    ("Rsvd1", UINT32,  9),
    ("Brs",   UINT32,  2),
    ("Rsvd2", UINT32,  5),
    ("Abpid", UINT32,  1)
    ]

# 
# //
# // 3.1.14 Offset 44h: BPRSEL - Boot Partition Read Select
# //
# typedef struct {
#   UINT32    Bprsz : 10; // Boot Partition Read Size
#   UINT32    Bprof : 20; // Boot Partition Read Offset
#   UINT32    Rsvd1 : 1;
#   UINT32    Bpid  : 1;  // Boot Partition Identifier
# } NVME_BPRSEL;
class NVME_BPRSEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bprsz", UINT32,  10),
    ("Bprof", UINT32,  20),
    ("Rsvd1", UINT32,  1),
    ("Bpid",  UINT32,  1)
    ]

# 
# //
# // 3.1.15 Offset 48h: BPMBL - Boot Partition Memory Buffer Location (Optional)
# //
# typedef struct {
#   UINT64    Rsvd1 : 12;
#   UINT64    Bmbba : 52; // Boot Partition Memory Buffer Base Address
# } NVME_BPMBL;
class NVME_BPMBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1", UINT64,  12),
    ("Bmbba", UINT64,  52)
    ]

# 
# //
# // 3.1.25 Offset (1000h + ((2y) * (4 << CAP.DSTRD))): SQyTDBL - Submission Queue y Tail Doorbell
# //
# typedef struct {
#   UINT16    Sqt;
#   UINT16    Rsvd1;
# } NVME_SQTDBL;
class NVME_SQTDBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Sqt",   UINT16),
    ("Rsvd1", UINT16)
    ]

# 
# //
# // 3.1.12 Offset (1000h + ((2y + 1) * (4 << CAP.DSTRD))): CQyHDBL - Completion Queue y Head Doorbell
# //
# typedef struct {
#   UINT16    Cqh;
#   UINT16    Rsvd1;
# } NVME_CQHDBL;
class NVME_CQHDBL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cqh",   UINT16),
    ("Rsvd1", UINT16)
    ]

# 
# //
# // NVM command set structures
# //
# // Read Command
# //
# typedef struct {
#   //
#   // CDW 10, 11
#   //
#   UINT64    Slba;             /* Starting Sector Address */
#   //
#   // CDW 12
#   //
#   UINT16    Nlb;              /* Number of Sectors */
#   UINT16    Rsvd1  : 10;
#   UINT16    Prinfo : 4;       /* Protection Info Check */
#   UINT16    Fua    : 1;       /* Force Unit Access */
#   UINT16    Lr     : 1;       /* Limited Retry */
#   //
#   // CDW 13
#   //
#   UINT32    Af     : 4;       /* Access Frequency */
#   UINT32    Al     : 2;       /* Access Latency */
#   UINT32    Sr     : 1;       /* Sequential Request */
#   UINT32    In     : 1;       /* Incompressible */
#   UINT32    Rsvd2  : 24;
#   //
#   // CDW 14
#   //
#   UINT32    Eilbrt;           /* Expected Initial Logical Block Reference Tag */
#   //
#   // CDW 15
#   //
#   UINT16    Elbat;            /* Expected Logical Block Application Tag */
#   UINT16    Elbatm;           /* Expected Logical Block Application Tag Mask */
# } NVME_READ;
class NVME_READ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64), 
    ("Nlb",     UINT16), 
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Af",      UINT32, 4 ),
    ("Al",      UINT32, 2 ),
    ("Sr",      UINT32, 1 ),
    ("In",      UINT32, 1 ),
    ("Rsvd2",   UINT32, 24),
    ("Eilbrt",  UINT32), 
    ("Elbat ",  UINT16), 
    ("Elbatm",  UINT16)
    ]

# 
# //
# // Write Command
# //
# typedef struct {
#   //
#   // CDW 10, 11
#   //
#   UINT64    Slba;             /* Starting Sector Address */
#   //
#   // CDW 12
#   //
#   UINT16    Nlb;              /* Number of Sectors */
#   UINT16    Rsvd1  : 10;
#   UINT16    Prinfo : 4;       /* Protection Info Check */
#   UINT16    Fua    : 1;       /* Force Unit Access */
#   UINT16    Lr     : 1;       /* Limited Retry */
#   //
#   // CDW 13
#   //
#   UINT32    Af     : 4;       /* Access Frequency */
#   UINT32    Al     : 2;       /* Access Latency */
#   UINT32    Sr     : 1;       /* Sequential Request */
#   UINT32    In     : 1;       /* Incompressible */
#   UINT32    Rsvd2  : 24;
#   //
#   // CDW 14
#   //
#   UINT32    Ilbrt;            /* Initial Logical Block Reference Tag */
#   //
#   // CDW 15
#   //
#   UINT16    Lbat;             /* Logical Block Application Tag */
#   UINT16    Lbatm;            /* Logical Block Application Tag Mask */
# } NVME_WRITE;
class NVME_WRITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Af",      UINT32, 4 ),
    ("Al",      UINT32, 2 ),
    ("Sr",      UINT32, 1 ),
    ("In",      UINT32, 1 ),
    ("Rsvd2",   UINT32, 24),
    ("Ilbrt",   UINT32),
    ("Lbat",    UINT16),
    ("Lbatm",   UINT16)
    ]

# 
# //
# // Flush
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Flush;            /* Flush */
# } NVME_FLUSH;
class NVME_FLUSH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Flush",   UINT32)
    ]

# 
# //
# // Write Uncorrectable command
# //
# typedef struct {
#   //
#   // CDW 10, 11
#   //
#   UINT64    Slba;             /* Starting LBA */
#   //
#   // CDW 12
#   //
#   UINT32    Nlb   : 16;       /* Number of  Logical Blocks */
#   UINT32    Rsvd1 : 16;
# } NVME_WRITE_UNCORRECTABLE;
class NVME_WRITE_UNCORRECTABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT32, 16),
    ("Rsvd1",   UINT32, 16)
    ]

# 
# //
# // Write Zeroes command
# //
# typedef struct {
#   //
#   // CDW 10, 11
#   //
#   UINT64    Slba;             /* Starting LBA */
#   //
#   // CDW 12
#   //
#   UINT16    Nlb;              /* Number of Logical Blocks */
#   UINT16    Rsvd1  : 10;
#   UINT16    Prinfo : 4;       /* Protection Info Check */
#   UINT16    Fua    : 1;       /* Force Unit Access */
#   UINT16    Lr     : 1;       /* Limited Retry */
#   //
#   // CDW 13
#   //
#   UINT32    Rsvd2;
#   //
#   // CDW 14
#   //
#   UINT32    Ilbrt;            /* Initial Logical Block Reference Tag */
#   //
#   // CDW 15
#   //
#   UINT16    Lbat;             /* Logical Block Application Tag */
#   UINT16    Lbatm;            /* Logical Block Application Tag Mask */
# } NVME_WRITE_ZEROES;
class NVME_WRITE_ZEROES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Rsvd2",   UINT32),
    ("Ilbrt",   UINT32),
    ("Lbat",    UINT16),
    ("Lbatm",   UINT16)
    ]

# 
# //
# // Compare command
# //
# typedef struct {
#   //
#   // CDW 10, 11
#   //
#   UINT64    Slba;             /* Starting LBA */
#   //
#   // CDW 12
#   //
#   UINT16    Nlb;              /* Number of Logical Blocks */
#   UINT16    Rsvd1  : 10;
#   UINT16    Prinfo : 4;       /* Protection Info Check */
#   UINT16    Fua    : 1;       /* Force Unit Access */
#   UINT16    Lr     : 1;       /* Limited Retry */
#   //
#   // CDW 13
#   //
#   UINT32    Rsvd2;
#   //
#   // CDW 14
#   //
#   UINT32    Eilbrt;           /* Expected Initial Logical Block Reference Tag */
#   //
#   // CDW 15
#   //
#   UINT16    Elbat;            /* Expected Logical Block Application Tag */
#   UINT16    Elbatm;           /* Expected Logical Block Application Tag Mask */
# } NVME_COMPARE;
class NVME_COMPARE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Slba",    UINT64),
    ("Nlb",     UINT16),
    ("Rsvd1",   UINT16, 10),
    ("Prinfo",  UINT16, 4 ),
    ("Fua",     UINT16, 1 ),
    ("Lr",      UINT16, 1 ),
    ("Rsvd2",   UINT32),
    ("Eilbrt",  UINT32),
    ("Elbat",   UINT16),
    ("Elbatm",  UINT16)
    ]

# 
# typedef union {
#   NVME_READ                   Read;
#   NVME_WRITE                  Write;
#   NVME_FLUSH                  Flush;
#   NVME_WRITE_UNCORRECTABLE    WriteUncorrectable;
#   NVME_WRITE_ZEROES           WriteZeros;
#   NVME_COMPARE                Compare;
# } NVME_CMD;
class NVME_CMD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Read",                NVME_READ               ),
    ("Write",               NVME_WRITE              ),
    ("Flush",               NVME_FLUSH              ),
    ("WriteUncorrectable",  NVME_WRITE_UNCORRECTABLE),
    ("WriteZeros",          NVME_WRITE_ZEROES       ),
    ("Compare",             NVME_COMPARE            )
    ]

# 
# typedef struct {
#   UINT16    Mp;             /* Maximum Power */
#   UINT8     Rsvd1;          /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8     Mps   : 1;      /* Max Power Scale */
#   UINT8     Nops  : 1;      /* Non-Operational State */
#   UINT8     Rsvd2 : 6;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT32    Enlat;          /* Entry Latency */
#   UINT32    Exlat;          /* Exit Latency */
#   UINT8     Rrt   : 5;      /* Relative Read Throughput */
#   UINT8     Rsvd3 : 3;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8     Rrl   : 5;      /* Relative Read Latency */
#   UINT8     Rsvd4 : 3;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8     Rwt   : 5;      /* Relative Write Throughput */
#   UINT8     Rsvd5 : 3;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8     Rwl   : 5;      /* Relative Write Latency */
#   UINT8     Rsvd6 : 3;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8     Rsvd7[16];      /* Reserved as of Nvm Express 1.1 Spec */
# } NVME_PSDESCRIPTOR;
class NVME_PSDESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Mp",      UINT16),
    ("Rsvd1",   UINT8 ),
    ("Mps",     UINT8,  1),
    ("Nops",    UINT8,  1),
    ("Rsvd2",   UINT8,  6),
    ("Enlat",   UINT32),
    ("Exlat",   UINT32),
    ("Rrt",     UINT8, 5),
    ("Rsvd3",   UINT8, 3),
    ("Rrl",     UINT8, 5),
    ("Rsvd4",   UINT8, 3),
    ("Rwt",     UINT8, 5),
    ("Rsvd5",   UINT8, 3),
    ("Rwl",     UINT8, 5),
    ("Rsvd6",   UINT8, 3),
    ("Rsvd7",   UINT8 * 16)
    ]

# 
# //
# //  Identify Controller Data
# //
# typedef struct {
#   //
#   // Controller Capabilities and Features 0-255
#   //
#   UINT16               Vid;    /* PCI Vendor ID */
#   UINT16               Ssvid;  /* PCI sub-system vendor ID */
#   UINT8                Sn[20]; /* Product serial number */
# 
#   UINT8                Mn[40];      /* Product model number */
#   UINT8                Fr[8];       /* Firmware Revision */
#   UINT8                Rab;         /* Recommended Arbitration Burst */
#   UINT8                Ieee_oui[3]; /* Organization Unique Identifier */
#   UINT8                Cmic;        /* Multi-interface Capabilities */
#   UINT8                Mdts;        /* Maximum Data Transfer Size */
#   UINT8                Cntlid[2];   /* Controller ID */
#   UINT8                Rsvd1[176];  /* Reserved as of Nvm Express 1.1 Spec */
#   //
#   // Admin Command Set Attributes
#   //
#   UINT16               Oacs;  /* Optional Admin Command Support */
#   #define NAMESPACE_MANAGEMENT_SUPPORTED   BIT3
#   #define FW_DOWNLOAD_ACTIVATE_SUPPORTED   BIT2
#   #define FORMAT_NVM_SUPPORTED             BIT1
#   #define SECURITY_SEND_RECEIVE_SUPPORTED  BIT0
#   UINT8                Acl;   /* Abort Command Limit */
#   UINT8                Aerl;  /* Async Event Request Limit */
#   UINT8                Frmw;  /* Firmware updates */
#   UINT8                Lpa;   /* Log Page Attributes */
#   UINT8                Elpe;  /* Error Log Page Entries */
#   UINT8                Npss;  /* Number of Power States Support */
#   UINT8                Avscc; /* Admin Vendor Specific Command Configuration */
#   UINT8                Apsta; /* Autonomous Power State Transition Attributes */
#   //
#   // Below fields before Rsvd2 are defined in NVM Express 1.4 Spec
#   //
#   UINT16               Wctemp;      /* Warning Composite Temperature Threshold */
#   UINT16               Cctemp;      /* Critical Composite Temperature Threshold */
#   UINT16               Mtfa;        /* Maximum Time for Firmware Activation */
#   UINT32               Hmpre;       /* Host Memory Buffer Preferred Size */
#   UINT32               Hmmin;       /* Host Memory Buffer Minimum Size */
#   UINT8                Tnvmcap[16]; /* Total NVM Capacity */
#   UINT8                Unvmcap[16]; /* Unallocated NVM Capacity */
#   UINT32               Rpmbs;       /* Replay Protected Memory Block Support */
#   UINT16               Edstt;       /* Extended Device Self-test Time */
#   UINT8                Dsto;        /* Device Self-test Options  */
#   UINT8                Fwug;        /* Firmware Update Granularity */
#   UINT8                Rsvd2[192];  /* Reserved as of Nvm Express 1.4 Spec */
#   //
#   // NVM Command Set Attributes
#   //
#   UINT8                Sqes;       /* Submission Queue Entry Size */
#   UINT8                Cqes;       /* Completion Queue Entry Size */
#   UINT16               Rsvd3;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT32               Nn;         /* Number of Namespaces */
#   UINT16               Oncs;       /* Optional NVM Command Support */
#   UINT16               Fuses;      /* Fused Operation Support */
#   UINT8                Fna;        /* Format NVM Attributes */
#   UINT8                Vwc;        /* Volatile Write Cache */
#   UINT16               Awun;       /* Atomic Write Unit Normal */
#   UINT16               Awupf;      /* Atomic Write Unit Power Fail */
#   UINT8                Nvscc;      /* NVM Vendor Specific Command Configuration */
#   UINT8                Rsvd4;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT16               Acwu;       /* Atomic Compare & Write Unit */
#   UINT16               Rsvd5;      /* Reserved as of Nvm Express 1.1 Spec */
#   UINT32               Sgls;       /* SGL Support  */
#   UINT8                Rsvd6[164]; /* Reserved as of Nvm Express 1.1 Spec */
#   //
#   // I/O Command set Attributes
#   //
#   UINT8                Rsvd7[1344]; /* Reserved as of Nvm Express 1.1 Spec */
#   //
#   // Power State Descriptors
#   //
#   NVME_PSDESCRIPTOR    PsDescriptor[32];
# 
#   UINT8                VendorData[1024]; /* Vendor specific data */
# } NVME_ADMIN_CONTROLLER_DATA;
NAMESPACE_MANAGEMENT_SUPPORTED   = BIT3
FW_DOWNLOAD_ACTIVATE_SUPPORTED   = BIT2
FORMAT_NVM_SUPPORTED             = BIT1
SECURITY_SEND_RECEIVE_SUPPORTED  = BIT0

class NVME_ADMIN_CONTROLLER_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Vid",                 UINT16           ),
    ("Ssvid",               UINT16           ),
    ("Sn",                  UINT8  * 20      ),
    ("Mn",                  UINT8  * 40      ),
    ("Fr",                  UINT8            ),
    ("Rab",                 UINT8  * 3       ),
    ("Ieee_oui",            UINT8            ),
    ("Cmic",                UINT8            ),
    ("Mdts",                UINT8            ),
    ("Cntlid",              UINT8  * 2       ),
    ("Rsvd1",               UINT8  * 176     ),
    ("Oacs",                UINT16           ),
    ("Acl",                 UINT8            ),
    ("Aerl",                UINT8            ),
    ("Frmw",                UINT8            ),
    ("Lpa",                 UINT8            ),
    ("Elpe",                UINT8            ),
    ("Npss",                UINT8            ),
    ("Avscc",               UINT8            ),
    ("Apsta",               UINT8            ),
    ("Wctemp",              UINT16           ),
    ("Cctemp",              UINT16           ),
    ("Mtfa",                UINT16           ),
    ("Hmpre",               UINT32           ),
    ("Hmmin",               UINT32           ),
    ("Tnvmcap",             UINT8   * 16     ),
    ("Unvmcap",             UINT8   * 16     ),
    ("Rpmbs",               UINT32           ),
    ("Edstt",               UINT16           ),
    ("Dsto",                UINT8            ),
    ("Fwug",                UINT8            ),
    ("Rsvd2",               UINT8   * 192    ),
    ("Sqes",                UINT8            ),
    ("Cqes",                UINT8            ),
    ("Rsvd3",               UINT16           ),
    ("Nn",                  UINT32           ),
    ("Oncs ",               UINT16           ),
    ("Fuses",               UINT16           ),
    ("Fna",                 UINT8            ),
    ("Vwc",                 UINT8            ),
    ("Awun",                UINT16           ),
    ("Awupf",               UINT16           ),
    ("Nvscc",               UINT8            ),
    ("Rsvd4",               UINT8            ),
    ("Acwu",                UINT16           ),
    ("Rsvd5",               UINT16           ),
    ("Sgls",                UINT32           ),
    ("Rsvd6",               UINT8   * 164    ),
    ("Rsvd7",               UINT8   * 1344   ),
    ("PsDescriptor",        NVME_PSDESCRIPTOR * 32),
    ("VendorData",          UINT8   * 1024   )
  ]

# 
# typedef struct {
#   UINT16    Ms;             /* Metadata Size */
#   UINT8     Lbads;          /* LBA Data Size */
#   UINT8     Rp    : 2;      /* Relative Performance */
#   #define LBAF_RP_BEST      00b
#   #define LBAF_RP_BETTER    01b
#   #define LBAF_RP_GOOD      10b
#   #define LBAF_RP_DEGRADED  11b
#   UINT8     Rsvd1 : 6;      /* Reserved as of Nvm Express 1.1 Spec */
# } NVME_LBAFORMAT;
LBAF_RP_BEST      = 0b00
LBAF_RP_BETTER    = 0b01
LBAF_RP_GOOD      = 0b10
LBAF_RP_DEGRADED  = 0b11

class NVME_LBAFORMAT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Ms",      UINT16),
    ("Lbads",   UINT8 ),
    ("Rp",      UINT8,  2),
    ("Rsvd1",   UINT8,  6),
    ]

# 
# //
# // Identify Namespace Data
# //
# typedef struct {
#   //
#   // NVM Command Set Specific
#   //
#   UINT64            Nsze;      /* Namespace Size (total number of blocks in formatted namespace) */
#   UINT64            Ncap;      /* Namespace Capacity (max number of logical blocks) */
#   UINT64            Nuse;      /* Namespace Utilization */
#   UINT8             Nsfeat;    /* Namespace Features */
#   UINT8             Nlbaf;     /* Number of LBA Formats */
#   UINT8             Flbas;     /* Formatted LBA size */
#   UINT8             Mc;        /* Metadata Capabilities */
#   UINT8             Dpc;       /* End-to-end Data Protection capabilities */
#   UINT8             Dps;       /* End-to-end Data Protection Type Settings */
#   UINT8             Nmic;      /* Namespace Multi-path I/O and Namespace Sharing Capabilities */
#   UINT8             Rescap;    /* Reservation Capabilities */
#   UINT8             Rsvd1[88]; /* Reserved as of Nvm Express 1.1 Spec */
#   UINT64            Eui64;     /* IEEE Extended Unique Identifier */
#   //
#   // LBA Format
#   //
#   NVME_LBAFORMAT    LbaFormat[16];
# 
#   UINT8             Rsvd2[192];       /* Reserved as of Nvm Express 1.1 Spec */
#   UINT8             VendorData[3712]; /* Vendor specific data */
# } NVME_ADMIN_NAMESPACE_DATA;
class NVME_ADMIN_NAMESPACE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Nsze",            UINT64        ),
    ("Ncap",            UINT64        ),
    ("Nuse",            UINT64        ),
    ("Nsfeat",          UINT8         ),
    ("Nlbaf",           UINT8         ),
    ("Flbas",           UINT8         ),
    ("Mc",              UINT8         ),
    ("Dpc",             UINT8         ),
    ("Dps",             UINT8         ),
    ("Nmic",            UINT8         ),
    ("Rescap",          UINT8         ),
    ("Rsvd1",           UINT8  * 88   ),
    ("Eui64",           UINT64        ),
    ("LbaFormat",       NVME_LBAFORMAT * 16),
    ("Rsvd2",           UINT8  * 192  ),
    ("VendorData",      UINT8  *3712  )
    ]

# 
# //
# // RPMB Device Configuration Block Data Structure as of Nvm Express 1.4 Spec
# //
# typedef struct {
#   UINT8    Bppe;       /* Boot Partition Protection Enable */
#   UINT8    Bpl;        /* Boot Partition Lock */
#   UINT8    Nwpac;      /* Namespace Write Protection Authentication Control */
#   UINT8    Rsvd1[509]; /* Reserved as of Nvm Express 1.4 Spec */
# } NVME_RPMB_CONFIGURATION_DATA;
class NVME_RPMB_CONFIGURATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Bppe",    UINT8),
    ("Bpl",     UINT8),
    ("Nwpac",   UINT8),
    ("Rsvd1",   UINT8  * 509)
    ]

# 
# #define RPMB_FRAME_STUFF_BYTES  223
# 
# //
# // RPMB Data Frame as of Nvm Express 1.4 Spec
# //
# typedef struct {
#   UINT8     Sbakamc[RPMB_FRAME_STUFF_BYTES]; /* [222-N:00] Stuff Bytes */
#                                              /* [222:222-(N-1)] Authentication Key or Message Authentication Code (MAC) */
#   UINT8     Rpmbt;                           /* RPMB Target */
#   UINT64    Nonce[2];
#   UINT32    Wcounter;                        /* Write Counter */
#   UINT32    Address;                         /* Starting address of data to be programmed to or read from the RPMB. */
#   UINT32    Scount;                          /* Sector Count */
#   UINT16    Result;
#   UINT16    Rpmessage;                       /* Request/Response Message */
#   // UINT8    *Data;                         /* Data to be written or read by signed access where M = 512 * Sector Count. */
# } NVME_RPMB_DATA_FRAME;
class NVME_RPMB_DATA_FRAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rpmbt",       UINT8 ),
    ("Nonce",       UINT64 * 2),
    ("Wcounter",    UINT32),
    ("Address",     UINT32),
    ("Scount",      UINT32),
    ("Result",      UINT16),
    ("Rpmessage",   UINT16)
    # ("Data",      UINT8 * N)
    ]

# 
# //
# // RPMB Device Configuration Block Data Structure.
# // (ref. NVMe Base spec. v2.0 Figure 460).
# //
# typedef struct {
#   UINT8    BPPEnable;     /* Boot Partition Protection Enabled */
#   UINT8    BPLock;        /* Boot Partition Lock */
#   UINT8    NameSpaceWrP;  /* Namespace Write Protection */
#   UINT8    Rsvd1[509];    /* Reserved as of Nvm Express 2.0 Spec */
# } NVME_RPMB_DCB;
class NVME_RPMB_DCB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("BPPEnable",    UINT8),
    ("BPLock",       UINT8),
    ("NameSpaceWrP", UINT8),
    ("Rsvd1",        UINT8 * 509)
    ]

# 
# //
# // RPMB Request and Response Message Types.
# // (ref. NVMe Base spec. v2.0 Figure 461).
# //
# #define NVME_RPMB_AUTHKEY_PROGRAM           0x0001
# #define NVME_RPMB_COUNTER_READ              0x0002
# #define NVME_RPMB_AUTHDATA_WRITE            0x0003
# #define NVME_RPMB_AUTHDATA_READ             0x0004
# #define NVME_RPMB_RESULT_READ               0x0005
# #define NVME_RPMB_DCB_WRITE                 0x0006
# #define NVME_RPMB_DCB_READ                  0x0007
# #define NVME_RPMB_AUTHKEY_PROGRAM_RESPONSE  0x0100
# #define NVME_RPMB_COUNTER_READ_RESPONSE     0x0200
# #define NVME_RPMB_AUTHDATA_WRITE_RESPONSE   0x0300
# #define NVME_RPMB_AUTHDATA_READ_RESPONSE    0x0400
# #define NVME_RPMB_DCB_WRITE_RESPONSE        0x0600
# #define NVME_RPMB_DCB_READ_RESPONSE         0x0700
NVME_RPMB_AUTHKEY_PROGRAM           = 0x0001
NVME_RPMB_COUNTER_READ              = 0x0002
NVME_RPMB_AUTHDATA_WRITE            = 0x0003
NVME_RPMB_AUTHDATA_READ             = 0x0004
NVME_RPMB_RESULT_READ               = 0x0005
NVME_RPMB_DCB_WRITE                 = 0x0006
NVME_RPMB_DCB_READ                  = 0x0007
NVME_RPMB_AUTHKEY_PROGRAM_RESPONSE  = 0x0100
NVME_RPMB_COUNTER_READ_RESPONSE     = 0x0200
NVME_RPMB_AUTHDATA_WRITE_RESPONSE   = 0x0300
NVME_RPMB_AUTHDATA_READ_RESPONSE    = 0x0400
NVME_RPMB_DCB_WRITE_RESPONSE        = 0x0600
NVME_RPMB_DCB_READ_RESPONSE         = 0x0700

# 
# //
# // RPMB Operation Result.
# // (ref. NVMe Base spec. v2.0 Figure 462).
# //
# #define NVME_RPMB_RESULT_SUCCESS                 0x00
# #define NVME_RPMB_RESULT_GENERAL_FAILURE         0x01
# #define NVME_RPMB_RESULT_AHTHENTICATION_FAILURE  0x02
# #define NVME_RPMB_RESULT_COUNTER_FAILURE         0x03
# #define NVME_RPMB_RESULT_ADDRESS_FAILURE         0x04
# #define NVME_RPMB_RESULT_WRITE_FAILURE           0x05
# #define NVME_RPMB_RESULT_READ_FAILURE            0x06
# #define NVME_RPMB_RESULT_AUTHKEY_NOT_PROGRAMMED  0x07
# #define NVME_RPMB_RESULT_INVALID_DCB             0x08
NVME_RPMB_RESULT_SUCCESS                 = 0x00
NVME_RPMB_RESULT_GENERAL_FAILURE         = 0x01
NVME_RPMB_RESULT_AHTHENTICATION_FAILURE  = 0x02
NVME_RPMB_RESULT_COUNTER_FAILURE         = 0x03
NVME_RPMB_RESULT_ADDRESS_FAILURE         = 0x04
NVME_RPMB_RESULT_WRITE_FAILURE           = 0x05
NVME_RPMB_RESULT_READ_FAILURE            = 0x06
NVME_RPMB_RESULT_AUTHKEY_NOT_PROGRAMMED  = 0x07
NVME_RPMB_RESULT_INVALID_DCB             = 0x08

# 
# //
# // Get Log Page - Boot Partition Log Header.
# // (ref. NVMe Base spec. v2.0 Figure 262).
# //
# typedef struct {
#   UINT8     LogIdentifier;   /* Log Identifier, shall be set to 15h */
#   UINT8     Rsvd1[3];
#   UINT32    Bpsz  : 15;      /* Boot Partition Size */
#   UINT32    Rsvd2 : 16;
#   UINT32    Abpid : 1;       /* Active Boot Partition ID */
#   UINT8     Rsvd3[8];
# } NVME_BOOT_PARTITION_HEADER;
class NVME_BOOT_PARTITION_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("LogIdentifier",   UINT8),
    ("Rsvd1",           UINT8 * 3),
    ("Bpsz",            UINT32, 15),
    ("Rsvd2",           UINT32, 16),
    ("Abpid",           UINT32, 1),
    ("Rsvd3",           UINT8 * 8)
    ]

# 
# //
# // NvmExpress Admin Identify Cmd
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Cns   : 2;
#   UINT32    Rsvd1 : 30;
# } NVME_ADMIN_IDENTIFY;
class NVME_ADMIN_IDENTIFY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cns",     UINT32, 2),
    ("Rsvd1",   UINT32, 30),
    ]

# 
# //
# // NvmExpress Admin Create I/O Completion Queue
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Qid   : 16;       /* Queue Identifier */
#   UINT32    Qsize : 16;       /* Queue Size */
# 
#   //
#   // CDW 11
#   //
#   UINT32    Pc    : 1;        /* Physically Contiguous */
#   UINT32    Ien   : 1;        /* Interrupts Enabled */
#   UINT32    Rsvd1 : 14;       /* reserved as of Nvm Express 1.1 Spec */
#   UINT32    Iv    : 16;       /* Interrupt Vector for MSI-X or MSI*/
# } NVME_ADMIN_CRIOCQ;
class NVME_ADMIN_CRIOCQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT32, 16),
    ("Qsize", UINT32, 16),
    ("Pc",    UINT32, 1 ),
    ("Ien",   UINT32, 1 ),
    ("Rsvd1", UINT32, 14),
    ("Iv",    UINT32, 16)
    ]

# 
# //
# // NvmExpress Admin Create I/O Submission Queue
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Qid   : 16;       /* Queue Identifier */
#   UINT32    Qsize : 16;       /* Queue Size */
# 
#   //
#   // CDW 11
#   //
#   UINT32    Pc    : 1;        /* Physically Contiguous */
#   UINT32    Qprio : 2;        /* Queue Priority */
#   UINT32    Rsvd1 : 13;       /* Reserved as of Nvm Express 1.1 Spec */
#   UINT32    Cqid  : 16;       /* Completion Queue ID */
# } NVME_ADMIN_CRIOSQ;
class NVME_ADMIN_CRIOSQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT32, 16),
    ("Qsize", UINT32, 16),
    ("Pc",    UINT32, 1 ),
    ("Qprio", UINT32, 2),
    ("Rsvd1", UINT32, 13),
    ("Cqid",  UINT32, 16),
    ]

# 
# //
# // NvmExpress Admin Delete I/O Completion Queue
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT16    Qid;
#   UINT16    Rsvd1;
# } NVME_ADMIN_DEIOCQ;
class NVME_ADMIN_DEIOCQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT16),
    ("Rsvd1", UINT16)
    ]

# 
# //
# // NvmExpress Admin Delete I/O Submission Queue
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT16    Qid;
#   UINT16    Rsvd1;
# } NVME_ADMIN_DEIOSQ;
class NVME_ADMIN_DEIOSQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Qid",   UINT16),
    ("Rsvd1", UINT16)
    ]

# 
# //
# // NvmExpress Admin Abort Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Sqid : 16;        /* Submission Queue identifier */
#   UINT32    Cid  : 16;        /* Command Identifier */
# } NVME_ADMIN_ABORT;
class NVME_ADMIN_ABORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Sqid",    UINT32, 16),
    ("Cid",     UINT32, 16)
    ]

# 
# //
# // NvmExpress Admin Firmware Activate Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Fs    : 3;        /* Submission Queue identifier */
#   UINT32    Aa    : 2;        /* Command Identifier */
#   UINT32    Rsvd1 : 27;
# } NVME_ADMIN_FIRMWARE_ACTIVATE;
class NVME_ADMIN_FIRMWARE_ACTIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fs",      UINT32, 3),
    ("Aa",      UINT32, 2),
    ("Rsvd1",   UINT32, 27)
    ]

# 
# //
# // NvmExpress Admin Firmware Image Download Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Numd;             /* Number of Dwords */
#   //
#   // CDW 11
#   //
#   UINT32    Ofst;             /* Offset */
# } NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD;
class NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Numd",    UINT32),
    ("Ofst",    UINT32)
    ]

# 
# //
# // NvmExpress Admin Get Features Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Fid   : 8;         /* Feature Identifier */
#   UINT32    Sel   : 3;         /* Select */
#   UINT32    Rsvd1 : 21;
# } NVME_ADMIN_GET_FEATURES;
class NVME_ADMIN_GET_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fid",     UINT32, 8),
    ("Sel",     UINT32, 3),
    ("Rsvd1",   UINT32, 21),
    ]

# 
# //
# // NvmExpress Admin Get Log Page Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Lid   : 8;        /* Log Page Identifier */
#   #define LID_ERROR_INFO    0x1
#   #define LID_SMART_INFO    0x2
#   #define LID_FW_SLOT_INFO  0x3
#   #define LID_BP_INFO       0x15
#   UINT32    Rsvd1 : 8;
#   UINT32    Numd  : 12;       /* Number of Dwords */
#   UINT32    Rsvd2 : 4;        /* Reserved as of Nvm Express 1.1 Spec */
# } NVME_ADMIN_GET_LOG_PAGE;
LID_ERROR_INFO    = 0x1
LID_SMART_INFO    = 0x2
LID_FW_SLOT_INFO  = 0x3
LID_BP_INFO       = 0x15

class NVME_ADMIN_GET_LOG_PAGE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Lid",     UINT32, 8),
    ("Rsvd1",   UINT32, 8),
    ("Numd",    UINT32, 12),
    ("Rsvd2",   UINT32, 4),
    ]

# 
# //
# // NvmExpress Admin Set Features Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Fid   : 8;        /* Feature Identifier */
#   UINT32    Rsvd1 : 23;
#   UINT32    Sv    : 1;        /* Save */
# } NVME_ADMIN_SET_FEATURES;
class NVME_ADMIN_SET_FEATURES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Fid",     UINT32, 8),
    ("Rsvd1",   UINT32, 23),
    ("Sv",      UINT32, 1),
    ]

# 
# //
# // NvmExpress Admin Format NVM Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Lbaf  : 4;        /* LBA Format */
#   UINT32    Ms    : 1;        /* Metadata Settings */
#   UINT32    Pi    : 3;        /* Protection Information */
#   UINT32    Pil   : 1;        /* Protection Information Location */
#   UINT32    Ses   : 3;        /* Secure Erase Settings */
#   UINT32    Rsvd1 : 20;
# } NVME_ADMIN_FORMAT_NVM;
class NVME_ADMIN_FORMAT_NVM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Lbaf",    UINT32, 4),
    ("Ms",      UINT32, 1),
    ("Pi",      UINT32, 3),
    ("Pil",     UINT32, 1),
    ("Ses",     UINT32, 3),
    ("Rsvd1",   UINT32, 20)
    ]

# 
# //
# // NvmExpress Admin Security Receive Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Rsvd1 : 8;
#   UINT32    Spsp  : 16;       /* SP Specific */
#   UINT32    Secp  : 8;        /* Security Protocol */
#   //
#   // CDW 11
#   //
#   UINT32    Al;               /* Allocation Length */
# } NVME_ADMIN_SECURITY_RECEIVE;
class NVME_ADMIN_SECURITY_RECEIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1",   UINT32, 8),
    ("Spsp",    UINT32, 16),
    ("Secp",    UINT32, 8)
    ]

# 
# //
# // NvmExpress Admin Security Send Command
# //
# typedef struct {
#   //
#   // CDW 10
#   //
#   UINT32    Rsvd1 : 8;
#   UINT32    Spsp  : 16;       /* SP Specific */
#   UINT32    Secp  : 8;        /* Security Protocol */
#   //
#   // CDW 11
#   //
#   UINT32    Tl;               /* Transfer Length */
# } NVME_ADMIN_SECURITY_SEND;
class NVME_ADMIN_SECURITY_SEND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Rsvd1",   UINT32, 8),
    ("Spsp",    UINT32, 16),
    ("Secp",    UINT32, 8),
    ("Tl",      UINT32)
    ]

# 
# typedef union {
#   NVME_ADMIN_IDENTIFY                   Identify;
#   NVME_ADMIN_CRIOCQ                     CrIoCq;
#   NVME_ADMIN_CRIOSQ                     CrIoSq;
#   NVME_ADMIN_DEIOCQ                     DeIoCq;
#   NVME_ADMIN_DEIOSQ                     DeIoSq;
#   NVME_ADMIN_ABORT                      Abort;
#   NVME_ADMIN_FIRMWARE_ACTIVATE          Activate;
#   NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD    FirmwareImageDownload;
#   NVME_ADMIN_GET_FEATURES               GetFeatures;
#   NVME_ADMIN_GET_LOG_PAGE               GetLogPage;
#   NVME_ADMIN_SET_FEATURES               SetFeatures;
#   NVME_ADMIN_FORMAT_NVM                 FormatNvm;
#   NVME_ADMIN_SECURITY_RECEIVE           SecurityReceive;
#   NVME_ADMIN_SECURITY_SEND              SecuritySend;
# } NVME_ADMIN_CMD;
class NVME_ADMIN_CMD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Identify",              NVME_ADMIN_IDENTIFY               ),
    ("CrIoCq",                NVME_ADMIN_CRIOCQ                 ),
    ("CrIoSq",                NVME_ADMIN_CRIOSQ                 ),
    ("DeIoCq",                NVME_ADMIN_DEIOCQ                 ),
    ("DeIoSq",                NVME_ADMIN_DEIOSQ                 ),
    ("Abort",                 NVME_ADMIN_ABORT                  ),
    ("Activate",              NVME_ADMIN_FIRMWARE_ACTIVATE      ),
    ("FirmwareImageDownload", NVME_ADMIN_FIRMWARE_IMAGE_DOWNLOAD),
    ("GetFeatures",           NVME_ADMIN_GET_FEATURES           ),
    ("GetLogPage",            NVME_ADMIN_GET_LOG_PAGE           ),
    ("SetFeatures",           NVME_ADMIN_SET_FEATURES           ),
    ("FormatNvm",             NVME_ADMIN_FORMAT_NVM             ),
    ("SecurityReceive",       NVME_ADMIN_SECURITY_RECEIVE       ),
    ("SecuritySend",          NVME_ADMIN_SECURITY_SEND          )
    ]

# 
# typedef struct {
#   UINT32    Cdw10;
#   UINT32    Cdw11;
#   UINT32    Cdw12;
#   UINT32    Cdw13;
#   UINT32    Cdw14;
#   UINT32    Cdw15;
# } NVME_RAW;
class NVME_RAW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Cdw10",   UINT32),
    ("Cdw11",   UINT32),
    ("Cdw12",   UINT32),
    ("Cdw13",   UINT32),
    ("Cdw14",   UINT32),
    ("Cdw15",   UINT32),
    ]

# 
# typedef union {
#   NVME_ADMIN_CMD    Admin; // Union of Admin commands
#   NVME_CMD          Nvm;   // Union of Nvm commands
#   NVME_RAW          Raw;
# } NVME_PAYLOAD;
class NVME_PAYLOAD (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Admin",   NVME_ADMIN_CMD),
    ("Nvm",     NVME_CMD      ),
    ("Raw",     NVME_RAW      )
    ]

# 
# //
# // Submission Queue
# //
# typedef struct {
#   //
#   // CDW 0, Common to all commands
#   //
#   UINT8           Opc;       // Opcode
#   UINT8           Fuse  : 2; // Fused Operation
#   UINT8           Rsvd1 : 5;
#   UINT8           Psdt  : 1; // PRP or SGL for Data Transfer
#   UINT16          Cid;       // Command Identifier
# 
#   //
#   // CDW 1
#   //
#   UINT32          Nsid;     // Namespace Identifier
# 
#   //
#   // CDW 2,3
#   //
#   UINT64          Rsvd2;
# 
#   //
#   // CDW 4,5
#   //
#   UINT64          Mptr;     // Metadata Pointer
# 
#   //
#   // CDW 6-9
#   //
#   UINT64          Prp[2];   // First and second PRP entries
# 
#   NVME_PAYLOAD    Payload;
# } NVME_SQ;
class NVME_SQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Opc",     UINT8),
    ("Fuse",    UINT8, 2),
    ("Rsvd1",   UINT8, 5),
    ("Psdt",    UINT8, 1),
    ("Cid",     UINT16),
    ("Nsid",    UINT32),
    ("Rsvd2",   UINT64),
    ("Mptr",    UINT64),
    ("Prp",     UINT64 * 2),
    ("Payload", NVME_PAYLOAD)
    ]

# 
# //
# // Completion Queue
# //
# typedef struct {
#   //
#   // CDW 0
#   //
#   UINT32    Dword0;
#   //
#   // CDW 1
#   //
#   UINT32    Rsvd1;
#   //
#   // CDW 2
#   //
#   UINT16    Sqhd;           // Submission Queue Head Pointer
#   UINT16    Sqid;           // Submission Queue Identifier
#   //
#   // CDW 3
#   //
#   UINT16    Cid;            // Command Identifier
#   UINT16    Pt    : 1;      // Phase Tag
#   UINT16    Sc    : 8;      // Status Code
#   UINT16    Sct   : 3;      // Status Code Type
#   UINT16    Rsvd2 : 2;
#   UINT16    Mo    : 1;      // More
#   UINT16    Dnr   : 1;      // Do Not Retry
# } NVME_CQ;
class NVME_CQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Dword0",  UINT32),
    ("Rsvd1",   UINT32),
    ("Sqhd",    UINT16),
    ("Sqid",    UINT16),
    ("Cid",     UINT16),
    ("Pt",      UINT16, 1),
    ("Sc",      UINT16, 8),
    ("Sct",     UINT16, 3),
    ("Rsvd2",   UINT16, 2),
    ("Mo",      UINT16, 1),
    ("Dnr",     UINT16, 1)
    ]

# 
# //
# // Nvm Express Admin cmd opcodes
# //
# #define NVME_ADMIN_DEIOSQ_CMD               0x00
# #define NVME_ADMIN_CRIOSQ_CMD               0x01
# #define NVME_ADMIN_GET_LOG_PAGE_CMD         0x02
# #define NVME_ADMIN_DEIOCQ_CMD               0x04
# #define NVME_ADMIN_CRIOCQ_CMD               0x05
# #define NVME_ADMIN_IDENTIFY_CMD             0x06
# #define NVME_ADMIN_ABORT_CMD                0x08
# #define NVME_ADMIN_SET_FEATURES_CMD         0x09
# #define NVME_ADMIN_GET_FEATURES_CMD         0x0A
# #define NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD  0x0C
# #define NVME_ADMIN_NAMESACE_MANAGEMENT_CMD  0x0D
# #define NVME_ADMIN_FW_COMMIT_CMD            0x10
# #define NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD    0x11
# #define NVME_ADMIN_NAMESACE_ATTACHMENT_CMD  0x15
# #define NVME_ADMIN_FORMAT_NVM_CMD           0x80
# #define NVME_ADMIN_SECURITY_SEND_CMD        0x81
# #define NVME_ADMIN_SECURITY_RECEIVE_CMD     0x82
NVME_ADMIN_DEIOSQ_CMD               = 0x00
NVME_ADMIN_CRIOSQ_CMD               = 0x01
NVME_ADMIN_GET_LOG_PAGE_CMD         = 0x02
NVME_ADMIN_DEIOCQ_CMD               = 0x04
NVME_ADMIN_CRIOCQ_CMD               = 0x05
NVME_ADMIN_IDENTIFY_CMD             = 0x06
NVME_ADMIN_ABORT_CMD                = 0x08
NVME_ADMIN_SET_FEATURES_CMD         = 0x09
NVME_ADMIN_GET_FEATURES_CMD         = 0x0A
NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD  = 0x0C
NVME_ADMIN_NAMESACE_MANAGEMENT_CMD  = 0x0D
NVME_ADMIN_FW_COMMIT_CMD            = 0x10
NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD    = 0x11
NVME_ADMIN_NAMESACE_ATTACHMENT_CMD  = 0x15
NVME_ADMIN_FORMAT_NVM_CMD           = 0x80
NVME_ADMIN_SECURITY_SEND_CMD        = 0x81
NVME_ADMIN_SECURITY_RECEIVE_CMD     = 0x82

# 
# #define NVME_IO_FLUSH_OPC  0
# #define NVME_IO_WRITE_OPC  1
# #define NVME_IO_READ_OPC   2
NVME_IO_FLUSH_OPC  = 0
NVME_IO_WRITE_OPC  = 1
NVME_IO_READ_OPC   = 2

# 
# typedef enum {
#   DeleteIOSubmissionQueueOpcode = NVME_ADMIN_DEIOSQ_CMD,
#   CreateIOSubmissionQueueOpcode = NVME_ADMIN_CRIOSQ_CMD,
#   GetLogPageOpcode              = NVME_ADMIN_GET_LOG_PAGE_CMD,
#   DeleteIOCompletionQueueOpcode = NVME_ADMIN_DEIOCQ_CMD,
#   CreateIOCompletionQueueOpcode = NVME_ADMIN_CRIOCQ_CMD,
#   IdentifyOpcode                = NVME_ADMIN_IDENTIFY_CMD,
#   AbortOpcode                   = NVME_ADMIN_ABORT_CMD,
#   SetFeaturesOpcode             = NVME_ADMIN_SET_FEATURES_CMD,
#   GetFeaturesOpcode             = NVME_ADMIN_GET_FEATURES_CMD,
#   AsyncEventRequestOpcode       = NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD,
#   NamespaceManagementOpcode     = NVME_ADMIN_NAMESACE_MANAGEMENT_CMD,
#   FirmwareCommitOpcode          = NVME_ADMIN_FW_COMMIT_CMD,
#   FirmwareImageDownloadOpcode   = NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD,
#   NamespaceAttachmentOpcode     = NVME_ADMIN_NAMESACE_ATTACHMENT_CMD,
#   FormatNvmOpcode               = NVME_ADMIN_FORMAT_NVM_CMD,
#   SecuritySendOpcode            = NVME_ADMIN_SECURITY_SEND_CMD,
#   SecurityReceiveOpcode         = NVME_ADMIN_SECURITY_RECEIVE_CMD
# } NVME_ADMIN_COMMAND_OPCODE;
DeleteIOSubmissionQueueOpcode = NVME_ADMIN_DEIOSQ_CMD,
CreateIOSubmissionQueueOpcode = NVME_ADMIN_CRIOSQ_CMD,
GetLogPageOpcode              = NVME_ADMIN_GET_LOG_PAGE_CMD,
DeleteIOCompletionQueueOpcode = NVME_ADMIN_DEIOCQ_CMD,
CreateIOCompletionQueueOpcode = NVME_ADMIN_CRIOCQ_CMD,
IdentifyOpcode                = NVME_ADMIN_IDENTIFY_CMD,
AbortOpcode                   = NVME_ADMIN_ABORT_CMD,
SetFeaturesOpcode             = NVME_ADMIN_SET_FEATURES_CMD,
GetFeaturesOpcode             = NVME_ADMIN_GET_FEATURES_CMD,
AsyncEventRequestOpcode       = NVME_ADMIN_ASYNC_EVENT_REQUEST_CMD,
NamespaceManagementOpcode     = NVME_ADMIN_NAMESACE_MANAGEMENT_CMD,
FirmwareCommitOpcode          = NVME_ADMIN_FW_COMMIT_CMD,
FirmwareImageDownloadOpcode   = NVME_ADMIN_FW_IAMGE_DOWNLOAD_CMD,
NamespaceAttachmentOpcode     = NVME_ADMIN_NAMESACE_ATTACHMENT_CMD,
FormatNvmOpcode               = NVME_ADMIN_FORMAT_NVM_CMD,
SecuritySendOpcode            = NVME_ADMIN_SECURITY_SEND_CMD,
SecurityReceiveOpcode         = NVME_ADMIN_SECURITY_RECEIVE_CMD
NVME_ADMIN_COMMAND_OPCODE     = ENUM

# 
# //
# // Controller or Namespace Structure (CNS) field
# // (ref. spec. v1.1 figure 82).
# //
# typedef enum {
#   IdentifyNamespaceCns    = 0x0,
#   IdentifyControllerCns   = 0x1,
#   IdentifyActiveNsListCns = 0x2
# } NVME_ADMIN_IDENTIFY_CNS;
IdentifyNamespaceCns    = 0x0,
IdentifyControllerCns   = 0x1,
IdentifyActiveNsListCns = 0x2
NVME_ADMIN_IDENTIFY_CNS = ENUM

# 
# //
# // Commit Action
# // (ref. spec. 1.1 figure 60).
# //
# typedef enum {
#   ActivateActionReplace         = 0x0,
#   ActivateActionReplaceActivate = 0x1,
#   ActivateActionActivate        = 0x2
# } NVME_FW_ACTIVATE_ACTION;
ActivateActionReplace         = 0x0,
ActivateActionReplaceActivate = 0x1,
ActivateActionActivate        = 0x2
NVME_FW_ACTIVATE_ACTION       = ENUM

# 
# //
# // Firmware Slot
# // (ref. spec. 1.1 Figure 60).
# //
# typedef enum {
#   FirmwareSlotCtrlChooses = 0x0,
#   FirmwareSlot1           = 0x1,
#   FirmwareSlot2           = 0x2,
#   FirmwareSlot3           = 0x3,
#   FirmwareSlot4           = 0x4,
#   FirmwareSlot5           = 0x5,
#   FirmwareSlot6           = 0x6,
#   FirmwareSlot7           = 0x7
# } NVME_FW_ACTIVATE_SLOT;
FirmwareSlotCtrlChooses = 0x0
FirmwareSlot1           = 0x1
FirmwareSlot2           = 0x2
FirmwareSlot3           = 0x3
FirmwareSlot4           = 0x4
FirmwareSlot5           = 0x5
FirmwareSlot6           = 0x6
FirmwareSlot7           = 0x7
NVME_FW_ACTIVATE_SLOT   = ENUM

# 
# //
# // Get Log Page ? Log Page Identifiers
# // (ref. spec. v1.1 Figure 73).
# //
# typedef enum {
#   ErrorInfoLogID        = LID_ERROR_INFO,
#   SmartHealthInfoLogID  = LID_SMART_INFO,
#   FirmwareSlotInfoLogID = LID_FW_SLOT_INFO
# } NVME_LOG_ID;
ErrorInfoLogID        = LID_ERROR_INFO
SmartHealthInfoLogID  = LID_SMART_INFO
FirmwareSlotInfoLogID = LID_FW_SLOT_INFO
NVME_LOG_ID           = ENUM

# 
# //
# // Get Log Page ? Firmware Slot Information Log
# // (ref. spec. v1.1 Figure 77).
# //
# typedef struct {
#   //
#   // Indicates the firmware slot from which the actively running firmware revision was loaded.
#   //
#   UINT8    ActivelyRunningFwSlot : 3;
#   UINT8                          : 1;
#   //
#   // Indicates the firmware slot that is going to be activated at the next controller reset. If this field is 0h, then the controller does not indicate the firmware slot that is going to be activated at the next controller reset.
#   //
#   UINT8    NextActiveFwSlot      : 3;
#   UINT8                          : 1;
# } NVME_ACTIVE_FW_INFO;
class NVME_ACTIVE_FW_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActivelyRunningFwSlot",   UINT8, 3),
    ("Empty1",                  UINT8, 1),
    ("NextActiveFwSlot",        UINT8, 3),
    ("Empty2",                  UINT8, 1)
    ]

# 
# //
# // Get Log Page ? Firmware Slot Information Log
# // (ref. spec. v1.1 Figure 77).
# //
# typedef struct {
#   //
#   // Specifies information about the active firmware revision.
#   // s
#   NVME_ACTIVE_FW_INFO    ActiveFwInfo;
#   UINT8                  Reserved1[7];
#   //
#   // Contains the revision of the firmware downloaded to firmware slot 1/7. If no valid firmware revision is present or if this slot is unsupported, all zeros shall be returned.
#   //
#   CHAR8                  FwRevisionSlot[7][8];
#   UINT8                  Reserved2[448];
# } NVME_FW_SLOT_INFO_LOG;
class NVME_FW_SLOT_INFO_LOG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ActiveFwInfo",    NVME_ACTIVE_FW_INFO),
    ("Reserved1",       UINT8 * 7),
    ("FwRevisionSlot", (UINT8 * 8) * 7),
    ("Reserved2",       UINT8 * 448),
    ]

# 
# //
# // SMART / Health Information (Log Identifier 02h)
# // (ref. spec. v1.1 5.10.1.2)
# //
# typedef struct {
#   //
#   // This field indicates critical warnings for the state of the controller.
#   //
#   UINT8     CriticalWarningAvailableSpare : 1;
#   UINT8     CriticalWarningTemperature    : 1;
#   UINT8     CriticalWarningReliability    : 1;
#   UINT8     CriticalWarningMediaReadOnly  : 1;
#   UINT8     CriticalWarningVolatileBackup : 1;
#   UINT8     CriticalWarningReserved       : 3;
#   //
#   // Contains a value corresponding to a temperature in degrees Kelvin that represents the current composite temperature of the controller and namespace(s) associated with that controller. The manner in which this value is computed is implementation specific and may not represent the actual temperature of any physical point in the NVM subsystem.
#   //
#   UINT16    CompositeTemp;
#   //
#   // Contains a normalized percentage (0 to 100%) of the remaining spare capacity available.
#   //
#   UINT8     AvailableSpare;
#   //
#   // When the Available Spare falls below the threshold indicated in this field, an asynchronous event completion may occur. The value is indicated as a normalized percentage (0 to 100%).
#   //
#   UINT8     AvailableSpareThreshold;
#   //
#   // Contains a vendor specific estimate of the percentage of NVM subsystem life used based on the actual usage and the manufacturer's prediction of NVM life. A value of 100 indicates that the estimated endurance of the NVM in the NVM subsystem has been consumed, but may not indicate an NVM subsystem failure. The value is allowed to exceed 100. Percentages greater than 254 shall be represented as 255. This value shall be updated once per power-on hour (when the controller is not in a sleep state).
#   //
#   UINT8     PercentageUsed;
#   UINT8     Reserved1[26];
#   //
#   // Contains the number of 512 byte data units the host has read from the controller; this value does not include metadata.
#   //
#   UINT8     DataUnitsRead[16];
#   //
#   // Contains the number of 512 byte data units the host has written to the controller; this value does not include metadata.
#   //
#   UINT8     DataUnitsWritten[16];
#   //
#   // Contains the number of read commands completed by the controller.
#   //
#   UINT8     HostReadCommands[16];
#   //
#   // Contains the number of write commands completed by the controller.
#   //
#   UINT8     HostWriteCommands[16];
#   //
#   // Contains the amount of time the controller is busy with I/O commands. This value is reported in minutes.
#   //
#   UINT8     ControllerBusyTime[16];
#   //
#   // Contains the number of power cycles.
#   //
#   UINT8     PowerCycles[16];
#   //
#   // Contains the number of power-on hours.
#   //
#   UINT8     PowerOnHours[16];
#   //
#   // Contains the number of unsafe shutdowns.
#   //
#   UINT8     UnsafeShutdowns[16];
#   //
#   // Contains the number of occurrences where the controller detected an unrecovered data integrity error.
#   //
#   UINT8     MediaAndDataIntegrityErrors[16];
#   //
#   // Contains the number of Error Information log entries over the life of the controller.
#   //
#   UINT8     NumberErrorInformationLogEntries[16];
#   //
#   // Contains the amount of time in minutes that the controller is operational and the Composite Temperature is greater than or equal to the Warning Composite Temperature Threshold (WCTEMP) field and less than the Critical Composite Temperature Threshold (CCTEMP) field in the Identify Controller data structure in Figure 90.
#   //
#   UINT32    WarningCompositeTemperatureTime;
#   //
#   // Contains the amount of time in minutes that the controller is operational and the Composite Temperature is greater the Critical Composite Temperature Threshold (CCTEMP) field in the Identify Controller data structure in Figure 90.
#   //
#   UINT32    CriticalCompositeTemperatureTime;
#   //
#   // Contains the current temperature in degrees Kelvin reported by the temperature sensor.  An implementation that does not implement the temperature sensor reports a temperature of zero degrees Kelvin.
#   //
#   UINT16    TemperatureSensor[8];
#   UINT8     Reserved2[296];
# } NVME_SMART_HEALTH_INFO_LOG;
class NVME_SMART_HEALTH_INFO_LOG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CriticalWarningAvailableSpare",    UINT8, 1),
    ("CriticalWarningTemperature",       UINT8, 1),
    ("CriticalWarningReliability",       UINT8, 1),
    ("CriticalWarningMediaReadOnly",     UINT8, 1),
    ("CriticalWarningVolatileBackup",    UINT8, 1),
    ("CriticalWarningReserved",          UINT8, 3),
    ("CompositeTemp",                    UINT16),
    ("AvailableSpare",                   UINT8),
    ("AvailableSpareThreshold",          UINT8),
    ("PercentageUsed",                   UINT8),
    ("Reserved1",                        UINT8 * 26),
    ("DataUnitsRead",                    UINT8 * 16),
    ("DataUnitsWritten",                 UINT8 * 16),
    ("HostReadCommands",                 UINT8 * 16),
    ("HostWriteCommands",                UINT8 * 16),
    ("ControllerBusyTime",               UINT8 * 16),
    ("PowerCycles",                      UINT8 * 16),
    ("PowerOnHours",                     UINT8 * 16),
    ("UnsafeShutdowns",                  UINT8 * 16),
    ("MediaAndDataIntegrityErrors",      UINT8 * 16),
    ("NumberErrorInformationLogEntries", UINT8 * 16),
    ("WarningCompositeTemperatureTime",  UINT32),
    ("CriticalCompositeTemperatureTime", UINT32),
    ("TemperatureSensor",                UINT16 * 8),
    ("Reserved2",                        UINT8 * 296)
    ]

# 
# #pragma pack()
# 
# #endif
# 