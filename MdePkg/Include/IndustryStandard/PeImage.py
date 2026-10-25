# /** @file
#   EFI image format for PE32, PE32+ and TE. Please note some data structures are
#   different for PE32 and PE32+. EFI_IMAGE_NT_HEADERS32 is for PE32 and
#   EFI_IMAGE_NT_HEADERS64 is for PE32+.
# 
#   This file is coded to the Visual Studio, Microsoft Portable Executable and
#   Common Object File Format Specification, Revision 8.3 - February 6, 2013.
#   This file also includes some definitions in PI Specification, Revision 1.0.
# 
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# Portions copyright (c) 2008 - 2009, Apple Inc. All rights reserved.<BR>
# Portions Copyright (c) 2016 - 2020, Hewlett Packard Enterprise Development LP. All rights reserved.<BR>
# Portions Copyright (c) 2022, Loongson Technology Corporation Limited. All rights reserved.<BR>
# 
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
# 
#
# PeImage.py
#
# EfiPy2.MdePkg.IndustryStandard.PeImage
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef __PE_IMAGE_H__
# #define __PE_IMAGE_H__
from EfiPy2.MdePkg.IndustryStandard import *

# 
# //
# // PE32+ Subsystem type for EFI images
# //
# #define EFI_IMAGE_SUBSYSTEM_EFI_APPLICATION          10
# #define EFI_IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER  11
# #define EFI_IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER       12
# #define EFI_IMAGE_SUBSYSTEM_SAL_RUNTIME_DRIVER       13///< defined PI Specification, 1.0
EFI_IMAGE_SUBSYSTEM_EFI_APPLICATION         = 10
EFI_IMAGE_SUBSYSTEM_EFI_BOOT_SERVICE_DRIVER = 11
EFI_IMAGE_SUBSYSTEM_EFI_RUNTIME_DRIVER      = 12
EFI_IMAGE_SUBSYSTEM_SAL_RUNTIME_DRIVER      = 13

# 
# //
# // PE32+ Machine type for EFI images
# //
# #define IMAGE_FILE_MACHINE_I386            0x014c
# #define IMAGE_FILE_MACHINE_IA64            0x0200
# #define IMAGE_FILE_MACHINE_EBC             0x0EBC
# #define IMAGE_FILE_MACHINE_X64             0x8664
# #define IMAGE_FILE_MACHINE_ARMTHUMB_MIXED  0x01c2
# #define IMAGE_FILE_MACHINE_ARM64           0xAA64
# #define IMAGE_FILE_MACHINE_RISCV32         0x5032
# #define IMAGE_FILE_MACHINE_RISCV64         0x5064
# #define IMAGE_FILE_MACHINE_RISCV128        0x5128
# #define IMAGE_FILE_MACHINE_LOONGARCH32     0x6232
# #define IMAGE_FILE_MACHINE_LOONGARCH64     0x6264
IMAGE_FILE_MACHINE_I386            = 0x014c
IMAGE_FILE_MACHINE_IA64            = 0x0200
IMAGE_FILE_MACHINE_EBC             = 0x0EBC
IMAGE_FILE_MACHINE_X64             = 0x8664
IMAGE_FILE_MACHINE_ARMTHUMB_MIXED  = 0x01c2
IMAGE_FILE_MACHINE_ARM64           = 0xAA64
IMAGE_FILE_MACHINE_RISCV32         = 0x5032
IMAGE_FILE_MACHINE_RISCV64         = 0x5064
IMAGE_FILE_MACHINE_RISCV128        = 0x5128
IMAGE_FILE_MACHINE_LOONGARCH32     = 0x6232
IMAGE_FILE_MACHINE_LOONGARCH64     = 0x6264

# 
# //
# // EXE file formats
# //
# #define EFI_IMAGE_DOS_SIGNATURE     SIGNATURE_16('M', 'Z')
# #define EFI_IMAGE_OS2_SIGNATURE     SIGNATURE_16('N', 'E')
# #define EFI_IMAGE_OS2_SIGNATURE_LE  SIGNATURE_16('L', 'E')
# #define EFI_IMAGE_NT_SIGNATURE      SIGNATURE_32('P', 'E', '\0', '\0')
EFI_IMAGE_DOS_SIGNATURE     = SIGNATURE_16('M', 'Z')
EFI_IMAGE_OS2_SIGNATURE     = SIGNATURE_16('N', 'E')
EFI_IMAGE_OS2_SIGNATURE_LE  = SIGNATURE_16('L', 'E')
EFI_IMAGE_NT_SIGNATURE      = SIGNATURE_32('P', 'E', '\0', '\0')

# 
# ///
# /// PE images can start with an optional DOS header, so if an image is run
# /// under DOS it can print an error message.
# ///
# typedef struct {
#   UINT16    e_magic;    ///< Magic number.
#   UINT16    e_cblp;     ///< Bytes on last page of file.
#   UINT16    e_cp;       ///< Pages in file.
#   UINT16    e_crlc;     ///< Relocations.
#   UINT16    e_cparhdr;  ///< Size of header in paragraphs.
#   UINT16    e_minalloc; ///< Minimum extra paragraphs needed.
#   UINT16    e_maxalloc; ///< Maximum extra paragraphs needed.
#   UINT16    e_ss;       ///< Initial (relative) SS value.
#   UINT16    e_sp;       ///< Initial SP value.
#   UINT16    e_csum;     ///< Checksum.
#   UINT16    e_ip;       ///< Initial IP value.
#   UINT16    e_cs;       ///< Initial (relative) CS value.
#   UINT16    e_lfarlc;   ///< File address of relocation table.
#   UINT16    e_ovno;     ///< Overlay number.
#   UINT16    e_res[4];   ///< Reserved words.
#   UINT16    e_oemid;    ///< OEM identifier (for e_oeminfo).
#   UINT16    e_oeminfo;  ///< OEM information; e_oemid specific.
#   UINT16    e_res2[10]; ///< Reserved words.
#   UINT32    e_lfanew;   ///< File address of new exe header.
# } EFI_IMAGE_DOS_HEADER;
class EFI_IMAGE_DOS_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("e_magic",     UINT16),
    ("e_cblp",      UINT16),
    ("e_cp",        UINT16),
    ("e_crlc",      UINT16),
    ("e_cparhdr",   UINT16),
    ("e_minalloc",  UINT16),
    ("e_maxalloc",  UINT16),
    ("e_ss",        UINT16),
    ("e_sp",        UINT16),
    ("e_csum",      UINT16),
    ("e_ip",        UINT16),
    ("e_cs",        UINT16),
    ("e_lfarlc",    UINT16),
    ("e_ovno",      UINT16),
    ("e_res",       UINT16 * 4),
    ("e_oemid",     UINT16),
    ("e_oeminfo",   UINT16),
    ("e_res2",      UINT16 * 10),
    ("e_lfanew",    UINT32)
  ]

# 
# ///
# /// COFF File Header (Object and Image).
# ///
# typedef struct {
#   UINT16    Machine;
#   UINT16    NumberOfSections;
#   UINT32    TimeDateStamp;
#   UINT32    PointerToSymbolTable;
#   UINT32    NumberOfSymbols;
#   UINT16    SizeOfOptionalHeader;
#   UINT16    Characteristics;
# } EFI_IMAGE_FILE_HEADER;
class EFI_IMAGE_FILE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Machine",               UINT16),
    ("NumberOfSections",      UINT16),
    ("TimeDateStamp",         UINT32),
    ("PointerToSymbolTable",  UINT32),
    ("NumberOfSymbols",       UINT32),
    ("SizeOfOptionalHeader",  UINT16),
    ("Characteristics",       UINT16)
  ]

# 
# ///
# /// Size of EFI_IMAGE_FILE_HEADER.
# ///
# #define EFI_IMAGE_SIZEOF_FILE_HEADER  20
EFI_IMAGE_SIZEOF_FILE_HEADER        = 20

# 
# //
# // Characteristics
# //
# #define EFI_IMAGE_FILE_RELOCS_STRIPPED      BIT0     ///< 0x0001  Relocation info stripped from file.
# #define EFI_IMAGE_FILE_EXECUTABLE_IMAGE     BIT1     ///< 0x0002  File is executable  (i.e. no unresolved externel references).
# #define EFI_IMAGE_FILE_LINE_NUMS_STRIPPED   BIT2     ///< 0x0004  Line numbers stripped from file.
# #define EFI_IMAGE_FILE_LOCAL_SYMS_STRIPPED  BIT3     ///< 0x0008  Local symbols stripped from file.
# #define EFI_IMAGE_FILE_BYTES_REVERSED_LO    BIT7     ///< 0x0080  Bytes of machine word are reversed.
# #define EFI_IMAGE_FILE_32BIT_MACHINE        BIT8     ///< 0x0100  32 bit word machine.
# #define EFI_IMAGE_FILE_DEBUG_STRIPPED       BIT9     ///< 0x0200  Debugging info stripped from file in .DBG file.
# #define EFI_IMAGE_FILE_SYSTEM               BIT12    ///< 0x1000  System File.
# #define EFI_IMAGE_FILE_DLL                  BIT13    ///< 0x2000  File is a DLL.
# #define EFI_IMAGE_FILE_BYTES_REVERSED_HI    BIT15    ///< 0x8000  Bytes of machine word are reversed.
EFI_IMAGE_FILE_RELOCS_STRIPPED      = BIT0
EFI_IMAGE_FILE_EXECUTABLE_IMAGE     = BIT1
EFI_IMAGE_FILE_LINE_NUMS_STRIPPED   = BIT2
EFI_IMAGE_FILE_LOCAL_SYMS_STRIPPED  = BIT3
EFI_IMAGE_FILE_BYTES_REVERSED_LO    = BIT7
EFI_IMAGE_FILE_32BIT_MACHINE        = BIT8
EFI_IMAGE_FILE_DEBUG_STRIPPED       = BIT9
EFI_IMAGE_FILE_SYSTEM               = BIT12
EFI_IMAGE_FILE_DLL                  = BIT13
EFI_IMAGE_FILE_BYTES_REVERSED_HI    = BIT15

# 
# ///
# /// Header Data Directories.
# ///
# typedef struct {
#   UINT32    VirtualAddress;
#   UINT32    Size;
# } EFI_IMAGE_DATA_DIRECTORY;
class EFI_IMAGE_DATA_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",  UINT32),
    ("Size",            UINT32)
  ]

# 
# //
# // Directory Entries
# //
EFI_IMAGE_DIRECTORY_ENTRY_EXPORT      = 0
EFI_IMAGE_DIRECTORY_ENTRY_IMPORT      = 1
EFI_IMAGE_DIRECTORY_ENTRY_RESOURCE    = 2
EFI_IMAGE_DIRECTORY_ENTRY_EXCEPTION   = 3
EFI_IMAGE_DIRECTORY_ENTRY_SECURITY    = 4
EFI_IMAGE_DIRECTORY_ENTRY_BASERELOC   = 5
EFI_IMAGE_DIRECTORY_ENTRY_DEBUG       = 6
EFI_IMAGE_DIRECTORY_ENTRY_COPYRIGHT   = 7
EFI_IMAGE_DIRECTORY_ENTRY_GLOBALPTR   = 8
EFI_IMAGE_DIRECTORY_ENTRY_TLS         = 9
EFI_IMAGE_DIRECTORY_ENTRY_LOAD_CONFIG = 10

# #define EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES  16
EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES = 16

# 
# ///
# /// @attention
# /// EFI_IMAGE_NT_OPTIONAL_HDR32_MAGIC means PE32 and
# /// EFI_IMAGE_OPTIONAL_HEADER32 must be used. The data structures only vary
# /// after NT additional fields.
# ///
# #define EFI_IMAGE_NT_OPTIONAL_HDR32_MAGIC  0x10b
EFI_IMAGE_NT_OPTIONAL_HDR32_MAGIC = 0x10b

# 
# ///
# /// Optional Header Standard Fields for PE32.
# ///
# typedef struct {
#   ///
#   /// Standard fields.
#   ///
#   UINT16                      Magic;
#   UINT8                       MajorLinkerVersion;
#   UINT8                       MinorLinkerVersion;
#   UINT32                      SizeOfCode;
#   UINT32                      SizeOfInitializedData;
#   UINT32                      SizeOfUninitializedData;
#   UINT32                      AddressOfEntryPoint;
#   UINT32                      BaseOfCode;
#   UINT32                      BaseOfData; ///< PE32 contains this additional field, which is absent in PE32+.
#   ///
#   /// Optional Header Windows-Specific Fields.
#   ///
#   UINT32                      ImageBase;
#   UINT32                      SectionAlignment;
#   UINT32                      FileAlignment;
#   UINT16                      MajorOperatingSystemVersion;
#   UINT16                      MinorOperatingSystemVersion;
#   UINT16                      MajorImageVersion;
#   UINT16                      MinorImageVersion;
#   UINT16                      MajorSubsystemVersion;
#   UINT16                      MinorSubsystemVersion;
#   UINT32                      Win32VersionValue;
#   UINT32                      SizeOfImage;
#   UINT32                      SizeOfHeaders;
#   UINT32                      CheckSum;
#   UINT16                      Subsystem;
#   UINT16                      DllCharacteristics;
#   UINT32                      SizeOfStackReserve;
#   UINT32                      SizeOfStackCommit;
#   UINT32                      SizeOfHeapReserve;
#   UINT32                      SizeOfHeapCommit;
#   UINT32                      LoaderFlags;
#   UINT32                      NumberOfRvaAndSizes;
#   EFI_IMAGE_DATA_DIRECTORY    DataDirectory[EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES];
# } EFI_IMAGE_OPTIONAL_HEADER32;
class EFI_IMAGE_OPTIONAL_HEADER32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Magic",                         UINT16),
    ("MajorLinkerVersion",            UINT8),
    ("MinorLinkerVersion",            UINT8),
    ("SizeOfCode",                    UINT32),
    ("SizeOfInitializedData",         UINT32),
    ("SizeOfUninitializedData",       UINT32),
    ("AddressOfEntryPoint",           UINT32),
    ("BaseOfCode",                    UINT32),
    ("BaseOfData",                    UINT32),
    ("ImageBase",                     UINT32),
    ("SectionAlignment",              UINT32),
    ("FileAlignment",                 UINT32),
    ("MajorOperatingSystemVersion",   UINT16),
    ("MinorOperatingSystemVersion",   UINT16),
    ("MajorImageVersion",             UINT16),
    ("MinorImageVersion",             UINT16),
    ("MajorSubsystemVersion",         UINT16),
    ("MinorSubsystemVersion",         UINT16),
    ("Win32VersionValue",             UINT32),
    ("SizeOfImage",                   UINT32),
    ("SizeOfHeaders",                 UINT32),
    ("CheckSum",                      UINT32),
    ("Subsystem",                     UINT16),
    ("DllCharacteristics",            UINT16),
    ("SizeOfStackReserve",            UINT32),
    ("SizeOfStackCommit",             UINT32),
    ("SizeOfHeapReserve",             UINT32),
    ("SizeOfHeapCommit",              UINT32),
    ("LoaderFlags",                   UINT32),
    ("NumberOfRvaAndSizes",           UINT32),
    ("DataDirectory",                 EFI_IMAGE_DATA_DIRECTORY * EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES)
  ]

# 
# ///
# /// @attention
# /// EFI_IMAGE_NT_OPTIONAL_HDR64_MAGIC means PE32+ and
# /// EFI_IMAGE_OPTIONAL_HEADER64 must be used. The data structures only vary
# /// after NT additional fields.
# ///
# #define EFI_IMAGE_NT_OPTIONAL_HDR64_MAGIC  0x20b
EFI_IMAGE_NT_OPTIONAL_HDR64_MAGIC = 0x20b

# 
# ///
# /// Optional Header Standard Fields for PE32+.
# ///
# typedef struct {
#   ///
#   /// Standard fields.
#   ///
#   UINT16                      Magic;
#   UINT8                       MajorLinkerVersion;
#   UINT8                       MinorLinkerVersion;
#   UINT32                      SizeOfCode;
#   UINT32                      SizeOfInitializedData;
#   UINT32                      SizeOfUninitializedData;
#   UINT32                      AddressOfEntryPoint;
#   UINT32                      BaseOfCode;
#   ///
#   /// Optional Header Windows-Specific Fields.
#   ///
#   UINT64                      ImageBase;
#   UINT32                      SectionAlignment;
#   UINT32                      FileAlignment;
#   UINT16                      MajorOperatingSystemVersion;
#   UINT16                      MinorOperatingSystemVersion;
#   UINT16                      MajorImageVersion;
#   UINT16                      MinorImageVersion;
#   UINT16                      MajorSubsystemVersion;
#   UINT16                      MinorSubsystemVersion;
#   UINT32                      Win32VersionValue;
#   UINT32                      SizeOfImage;
#   UINT32                      SizeOfHeaders;
#   UINT32                      CheckSum;
#   UINT16                      Subsystem;
#   UINT16                      DllCharacteristics;
#   UINT64                      SizeOfStackReserve;
#   UINT64                      SizeOfStackCommit;
#   UINT64                      SizeOfHeapReserve;
#   UINT64                      SizeOfHeapCommit;
#   UINT32                      LoaderFlags;
#   UINT32                      NumberOfRvaAndSizes;
#   EFI_IMAGE_DATA_DIRECTORY    DataDirectory[EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES];
# } EFI_IMAGE_OPTIONAL_HEADER64;
class EFI_IMAGE_OPTIONAL_HEADER64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Magic",                       UINT16),
    ("MajorLinkerVersion",          UINT8),
    ("MinorLinkerVersion",          UINT8),
    ("SizeOfCode",                  UINT32),
    ("SizeOfInitializedData",       UINT32),
    ("SizeOfUninitializedData",     UINT32),
    ("AddressOfEntryPoint",         UINT32),
    ("BaseOfCode",                  UINT32),
    ("ImageBase",                   UINT64),
    ("SectionAlignment",            UINT32),
    ("FileAlignment",               UINT32),
    ("MajorOperatingSystemVersion", UINT16),
    ("MinorOperatingSystemVersion", UINT16),
    ("MajorImageVersion",           UINT16),
    ("MinorImageVersion",           UINT16),
    ("MajorSubsystemVersion",       UINT16),
    ("MinorSubsystemVersion",       UINT16),
    ("Win32VersionValue",           UINT32),
    ("SizeOfImage",                 UINT32),
    ("SizeOfHeaders",               UINT32),
    ("CheckSum",                    UINT32),
    ("Subsystem",                   UINT16),
    ("DllCharacteristics",          UINT16),
    ("SizeOfStackReserve",          UINT64),
    ("SizeOfStackCommit",           UINT64),
    ("SizeOfHeapReserve",           UINT64),
    ("SizeOfHeapCommit",            UINT64),
    ("LoaderFlags",                 UINT32),
    ("NumberOfRvaAndSizes",         UINT32),
    ("DataDirectory",               EFI_IMAGE_DATA_DIRECTORY * EFI_IMAGE_NUMBER_OF_DIRECTORY_ENTRIES)
  ]

# 
# ///
# /// @attention
# /// EFI_IMAGE_NT_HEADERS32 is for use ONLY by tools.
# ///
# typedef struct {
#   UINT32                         Signature;
#   EFI_IMAGE_FILE_HEADER          FileHeader;
#   EFI_IMAGE_OPTIONAL_HEADER32    OptionalHeader;
# } EFI_IMAGE_NT_HEADERS32;
class EFI_IMAGE_NT_HEADERS32 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("FileHeader",      EFI_IMAGE_FILE_HEADER),
    ("OptionalHeader",  EFI_IMAGE_OPTIONAL_HEADER32)
  ]

# 
# #define EFI_IMAGE_SIZEOF_NT_OPTIONAL32_HEADER  sizeof (EFI_IMAGE_NT_HEADERS32)
EFI_IMAGE_SIZEOF_NT_OPTIONAL32_HEADER = sizeof (EFI_IMAGE_NT_HEADERS32)

# 
# ///
# /// @attention
# /// EFI_IMAGE_HEADERS64 is for use ONLY by tools.
# ///
# typedef struct {
#   UINT32                         Signature;
#   EFI_IMAGE_FILE_HEADER          FileHeader;
#   EFI_IMAGE_OPTIONAL_HEADER64    OptionalHeader;
# } EFI_IMAGE_NT_HEADERS64;
class EFI_IMAGE_NT_HEADERS64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",       UINT32),
    ("FileHeader",      EFI_IMAGE_FILE_HEADER),
    ("OptionalHeader",  EFI_IMAGE_OPTIONAL_HEADER64)
  ]

# 
# #define EFI_IMAGE_SIZEOF_NT_OPTIONAL64_HEADER  sizeof (EFI_IMAGE_NT_HEADERS64)
EFI_IMAGE_SIZEOF_NT_OPTIONAL64_HEADER = sizeof (EFI_IMAGE_NT_HEADERS64)

# 
# //
# // Other Windows Subsystem Values
# //
# #define EFI_IMAGE_SUBSYSTEM_UNKNOWN      0
# #define EFI_IMAGE_SUBSYSTEM_NATIVE       1
# #define EFI_IMAGE_SUBSYSTEM_WINDOWS_GUI  2
# #define EFI_IMAGE_SUBSYSTEM_WINDOWS_CUI  3
# #define EFI_IMAGE_SUBSYSTEM_OS2_CUI      5
# #define EFI_IMAGE_SUBSYSTEM_POSIX_CUI    7
EFI_IMAGE_SUBSYSTEM_UNKNOWN     = 0
EFI_IMAGE_SUBSYSTEM_NATIVE      = 1
EFI_IMAGE_SUBSYSTEM_WINDOWS_GUI = 2
EFI_IMAGE_SUBSYSTEM_WINDOWS_CUI = 3
EFI_IMAGE_SUBSYSTEM_OS2_CUI     = 5
EFI_IMAGE_SUBSYSTEM_POSIX_CUI   = 7

# 
# ///
# /// Length of ShortName.
# ///
# #define EFI_IMAGE_SIZEOF_SHORT_NAME  8
EFI_IMAGE_SIZEOF_SHORT_NAME = 8

# 
# ///
# /// Section Table. This table immediately follows the optional header.
# ///
# typedef struct {
#   UINT8     Name[EFI_IMAGE_SIZEOF_SHORT_NAME];
#   union {
#     UINT32    PhysicalAddress;
#     UINT32    VirtualSize;
#   } Misc;
#   UINT32    VirtualAddress;
#   UINT32    SizeOfRawData;
#   UINT32    PointerToRawData;
#   UINT32    PointerToRelocations;
#   UINT32    PointerToLinenumbers;
#   UINT16    NumberOfRelocations;
#   UINT16    NumberOfLinenumbers;
#   UINT32    Characteristics;
# } EFI_IMAGE_SECTION_HEADER;
class EFI_IMAGE_SECTION_HEADER_Misc (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("PhysicalAddress", UINT32),
    ("VirtualSize",     UINT32)
  ]

class EFI_IMAGE_NT_HEADERS64 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Name",                  UINT8 * EFI_IMAGE_SIZEOF_SHORT_NAME),
    ("Misc",                  EFI_IMAGE_SECTION_HEADER_Misc),
    ("VirtualAddress",        UINT32),
    ("SizeOfRawData",         UINT32),
    ("PointerToRawData",      UINT32),
    ("PointerToRelocations",  UINT32),
    ("PointerToLinenumbers",  UINT32),
    ("NumberOfRelocations",   UINT16),
    ("NumberOfLinenumbers",   UINT16),
    ("Characteristics",       UINT32)
  ]

# 
# ///
# /// Size of EFI_IMAGE_SECTION_HEADER.
# ///
# #define EFI_IMAGE_SIZEOF_SECTION_HEADER  40
EFI_IMAGE_SIZEOF_SECTION_HEADER       = 40

# 
# //
# // Section Flags Values
# //
# #define EFI_IMAGE_SCN_TYPE_NO_PAD             BIT3        ///< 0x00000008  ///< Reserved.
# #define EFI_IMAGE_SCN_CNT_CODE                BIT5        ///< 0x00000020
# #define EFI_IMAGE_SCN_CNT_INITIALIZED_DATA    BIT6        ///< 0x00000040
# #define EFI_IMAGE_SCN_CNT_UNINITIALIZED_DATA  BIT7        ///< 0x00000080
EFI_IMAGE_SCN_TYPE_NO_PAD                  = BIT3
EFI_IMAGE_SCN_CNT_CODE                     = BIT5
EFI_IMAGE_SCN_CNT_INITIALIZED_DATA         = BIT6
EFI_IMAGE_SCN_CNT_UNINITIALIZED_DATA       = BIT7

# 
# #define EFI_IMAGE_SCN_LNK_OTHER   BIT8                    ///< 0x00000100  ///< Reserved.
# #define EFI_IMAGE_SCN_LNK_INFO    BIT9                    ///< 0x00000200  ///< Section contains comments or some other type of information.
# #define EFI_IMAGE_SCN_LNK_REMOVE  BIT11                   ///< 0x00000800  ///< Section contents will not become part of image.
# #define EFI_IMAGE_SCN_LNK_COMDAT  BIT12                   ///< 0x00001000
EFI_IMAGE_SCN_LNK_OTHER                    = BIT8
EFI_IMAGE_SCN_LNK_INFO                     = BIT9
EFI_IMAGE_SCN_LNK_REMOVE                   = BIT11
EFI_IMAGE_SCN_LNK_COMDAT                   = BIT12

# 
# #define EFI_IMAGE_SCN_ALIGN_1BYTES   BIT20                ///< 0x00100000
# #define EFI_IMAGE_SCN_ALIGN_2BYTES   BIT21                ///< 0x00200000
# #define EFI_IMAGE_SCN_ALIGN_4BYTES   (BIT20|BIT21)        ///< 0x00300000
# #define EFI_IMAGE_SCN_ALIGN_8BYTES   BIT22                ///< 0x00400000
# #define EFI_IMAGE_SCN_ALIGN_16BYTES  (BIT20|BIT22)        ///< 0x00500000
# #define EFI_IMAGE_SCN_ALIGN_32BYTES  (BIT21|BIT22)        ///< 0x00600000
# #define EFI_IMAGE_SCN_ALIGN_64BYTES  (BIT20|BIT21|BIT22)  ///< 0x00700000
EFI_IMAGE_SCN_ALIGN_1BYTES    =              BIT20 
EFI_IMAGE_SCN_ALIGN_2BYTES    =              BIT21 
EFI_IMAGE_SCN_ALIGN_4BYTES    =       (BIT20|BIT21)
EFI_IMAGE_SCN_ALIGN_8BYTES    =              BIT22 
EFI_IMAGE_SCN_ALIGN_16BYTES   =       (BIT20|BIT22)
EFI_IMAGE_SCN_ALIGN_32BYTES   =       (BIT21|BIT22)
EFI_IMAGE_SCN_ALIGN_64BYTES   = (BIT20|BIT21|BIT22)

# 
# #define EFI_IMAGE_SCN_MEM_DISCARDABLE  BIT25              ///< 0x02000000
# #define EFI_IMAGE_SCN_MEM_NOT_CACHED   BIT26              ///< 0x04000000
# #define EFI_IMAGE_SCN_MEM_NOT_PAGED    BIT27              ///< 0x08000000
# #define EFI_IMAGE_SCN_MEM_SHARED       BIT28              ///< 0x10000000
# #define EFI_IMAGE_SCN_MEM_EXECUTE      BIT29              ///< 0x20000000
# #define EFI_IMAGE_SCN_MEM_READ         BIT30              ///< 0x40000000
# #define EFI_IMAGE_SCN_MEM_WRITE        BIT31              ///< 0x80000000
EFI_IMAGE_SCN_MEM_DISCARDABLE              = BIT25
EFI_IMAGE_SCN_MEM_NOT_CACHED               = BIT26
EFI_IMAGE_SCN_MEM_NOT_PAGED                = BIT27
EFI_IMAGE_SCN_MEM_SHARED                   = BIT28
EFI_IMAGE_SCN_MEM_EXECUTE                  = BIT29
EFI_IMAGE_SCN_MEM_READ                     = BIT30
EFI_IMAGE_SCN_MEM_WRITE                    = BIT31

# 
# ///
# /// Size of a Symbol Table Record.
# ///
# #define EFI_IMAGE_SIZEOF_SYMBOL  18
EFI_IMAGE_SIZEOF_SYMBOL = 18

# 
# //
# // Symbols have a section number of the section in which they are
# // defined. Otherwise, section numbers have the following meanings:
# //
# #define EFI_IMAGE_SYM_UNDEFINED  (UINT16) 0  ///< Symbol is undefined or is common.
# #define EFI_IMAGE_SYM_ABSOLUTE   (UINT16) -1 ///< Symbol is an absolute value.
# #define EFI_IMAGE_SYM_DEBUG      (UINT16) -2 ///< Symbol is a special debug item.
EFI_IMAGE_SYM_UNDEFINED  =  0
EFI_IMAGE_SYM_ABSOLUTE   = -1
EFI_IMAGE_SYM_DEBUG      = -2

# 
# //
# // Symbol Type (fundamental) values.
# //
# #define EFI_IMAGE_SYM_TYPE_NULL    0  ///< no type.
# #define EFI_IMAGE_SYM_TYPE_VOID    1  ///< no valid type.
# #define EFI_IMAGE_SYM_TYPE_CHAR    2  ///< type character.
# #define EFI_IMAGE_SYM_TYPE_SHORT   3  ///< type short integer.
# #define EFI_IMAGE_SYM_TYPE_INT     4
# #define EFI_IMAGE_SYM_TYPE_LONG    5
# #define EFI_IMAGE_SYM_TYPE_FLOAT   6
# #define EFI_IMAGE_SYM_TYPE_DOUBLE  7
# #define EFI_IMAGE_SYM_TYPE_STRUCT  8
# #define EFI_IMAGE_SYM_TYPE_UNION   9
# #define EFI_IMAGE_SYM_TYPE_ENUM    10 ///< enumeration.
# #define EFI_IMAGE_SYM_TYPE_MOE     11 ///< member of enumeration.
# #define EFI_IMAGE_SYM_TYPE_BYTE    12
# #define EFI_IMAGE_SYM_TYPE_WORD    13
# #define EFI_IMAGE_SYM_TYPE_UINT    14
# #define EFI_IMAGE_SYM_TYPE_DWORD   15
EFI_IMAGE_SYM_TYPE_NULL   = 0
EFI_IMAGE_SYM_TYPE_VOID   = 1
EFI_IMAGE_SYM_TYPE_CHAR   = 2
EFI_IMAGE_SYM_TYPE_SHORT  = 3
EFI_IMAGE_SYM_TYPE_INT    = 4
EFI_IMAGE_SYM_TYPE_LONG   = 5
EFI_IMAGE_SYM_TYPE_FLOAT  = 6
EFI_IMAGE_SYM_TYPE_DOUBLE = 7
EFI_IMAGE_SYM_TYPE_STRUCT = 8
EFI_IMAGE_SYM_TYPE_UNION  = 9
EFI_IMAGE_SYM_TYPE_ENUM   = 10
EFI_IMAGE_SYM_TYPE_MOE    = 11
EFI_IMAGE_SYM_TYPE_BYTE   = 12
EFI_IMAGE_SYM_TYPE_WORD   = 13
EFI_IMAGE_SYM_TYPE_UINT   = 14
EFI_IMAGE_SYM_TYPE_DWORD  = 15

# 
# //
# // Symbol Type (derived) values.
# //
# #define EFI_IMAGE_SYM_DTYPE_NULL      0 ///< no derived type.
# #define EFI_IMAGE_SYM_DTYPE_POINTER   1
# #define EFI_IMAGE_SYM_DTYPE_FUNCTION  2
# #define EFI_IMAGE_SYM_DTYPE_ARRAY     3
EFI_IMAGE_SYM_DTYPE_NULL      = 0
EFI_IMAGE_SYM_DTYPE_POINTER   = 1
EFI_IMAGE_SYM_DTYPE_FUNCTION  = 2
EFI_IMAGE_SYM_DTYPE_ARRAY     = 3

# 
# //
# // Storage classes.
# //
# #define EFI_IMAGE_SYM_CLASS_END_OF_FUNCTION   ((UINT8) -1)
# #define EFI_IMAGE_SYM_CLASS_NULL              0
# #define EFI_IMAGE_SYM_CLASS_AUTOMATIC         1
# #define EFI_IMAGE_SYM_CLASS_EXTERNAL          2
# #define EFI_IMAGE_SYM_CLASS_STATIC            3
# #define EFI_IMAGE_SYM_CLASS_REGISTER          4
# #define EFI_IMAGE_SYM_CLASS_EXTERNAL_DEF      5
# #define EFI_IMAGE_SYM_CLASS_LABEL             6
# #define EFI_IMAGE_SYM_CLASS_UNDEFINED_LABEL   7
# #define EFI_IMAGE_SYM_CLASS_MEMBER_OF_STRUCT  8
# #define EFI_IMAGE_SYM_CLASS_ARGUMENT          9
# #define EFI_IMAGE_SYM_CLASS_STRUCT_TAG        10
# #define EFI_IMAGE_SYM_CLASS_MEMBER_OF_UNION   11
# #define EFI_IMAGE_SYM_CLASS_UNION_TAG         12
# #define EFI_IMAGE_SYM_CLASS_TYPE_DEFINITION   13
# #define EFI_IMAGE_SYM_CLASS_UNDEFINED_STATIC  14
# #define EFI_IMAGE_SYM_CLASS_ENUM_TAG          15
# #define EFI_IMAGE_SYM_CLASS_MEMBER_OF_ENUM    16
# #define EFI_IMAGE_SYM_CLASS_REGISTER_PARAM    17
# #define EFI_IMAGE_SYM_CLASS_BIT_FIELD         18
# #define EFI_IMAGE_SYM_CLASS_BLOCK             100
# #define EFI_IMAGE_SYM_CLASS_FUNCTION          101
# #define EFI_IMAGE_SYM_CLASS_END_OF_STRUCT     102
# #define EFI_IMAGE_SYM_CLASS_FILE              103
# #define EFI_IMAGE_SYM_CLASS_SECTION           104
# #define EFI_IMAGE_SYM_CLASS_WEAK_EXTERNAL     105
EFI_IMAGE_SYM_CLASS_END_OF_FUNCTION   = -1
EFI_IMAGE_SYM_CLASS_NULL              = 0
EFI_IMAGE_SYM_CLASS_AUTOMATIC         = 1
EFI_IMAGE_SYM_CLASS_EXTERNAL          = 2
EFI_IMAGE_SYM_CLASS_STATIC            = 3
EFI_IMAGE_SYM_CLASS_REGISTER          = 4
EFI_IMAGE_SYM_CLASS_EXTERNAL_DEF      = 5
EFI_IMAGE_SYM_CLASS_LABEL             = 6
EFI_IMAGE_SYM_CLASS_UNDEFINED_LABEL   = 7
EFI_IMAGE_SYM_CLASS_MEMBER_OF_STRUCT  = 8
EFI_IMAGE_SYM_CLASS_ARGUMENT          = 9
EFI_IMAGE_SYM_CLASS_STRUCT_TAG        = 10
EFI_IMAGE_SYM_CLASS_MEMBER_OF_UNION   = 11
EFI_IMAGE_SYM_CLASS_UNION_TAG         = 12
EFI_IMAGE_SYM_CLASS_TYPE_DEFINITION   = 13
EFI_IMAGE_SYM_CLASS_UNDEFINED_STATIC  = 14
EFI_IMAGE_SYM_CLASS_ENUM_TAG          = 15
EFI_IMAGE_SYM_CLASS_MEMBER_OF_ENUM    = 16
EFI_IMAGE_SYM_CLASS_REGISTER_PARAM    = 17
EFI_IMAGE_SYM_CLASS_BIT_FIELD         = 18
EFI_IMAGE_SYM_CLASS_BLOCK             = 100
EFI_IMAGE_SYM_CLASS_FUNCTION          = 101
EFI_IMAGE_SYM_CLASS_END_OF_STRUCT     = 102
EFI_IMAGE_SYM_CLASS_FILE              = 103
EFI_IMAGE_SYM_CLASS_SECTION           = 104
EFI_IMAGE_SYM_CLASS_WEAK_EXTERNAL     = 105

# 
# //
# // type packing constants
# //
# #define EFI_IMAGE_N_BTMASK  017
# #define EFI_IMAGE_N_TMASK   060
# #define EFI_IMAGE_N_TMASK1  0300
# #define EFI_IMAGE_N_TMASK2  0360
# #define EFI_IMAGE_N_BTSHFT  4
# #define EFI_IMAGE_N_TSHIFT  2
EFI_IMAGE_N_BTMASK  = 0o17
EFI_IMAGE_N_TMASK   = 0o60
EFI_IMAGE_N_TMASK1  = 0o300
EFI_IMAGE_N_TMASK2  = 0o360
EFI_IMAGE_N_BTSHFT  = 4
EFI_IMAGE_N_TSHIFT  = 2

# 
# //
# // Communal selection types.
# //
# #define EFI_IMAGE_COMDAT_SELECT_NODUPLICATES  1
# #define EFI_IMAGE_COMDAT_SELECT_ANY           2
# #define EFI_IMAGE_COMDAT_SELECT_SAME_SIZE     3
# #define EFI_IMAGE_COMDAT_SELECT_EXACT_MATCH   4
# #define EFI_IMAGE_COMDAT_SELECT_ASSOCIATIVE   5
EFI_IMAGE_COMDAT_SELECT_NODUPLICATES    = 1
EFI_IMAGE_COMDAT_SELECT_ANY             = 2
EFI_IMAGE_COMDAT_SELECT_SAME_SIZE       = 3
EFI_IMAGE_COMDAT_SELECT_EXACT_MATCH     = 4
EFI_IMAGE_COMDAT_SELECT_ASSOCIATIVE     = 5

# 
# //
# // the following values only be referred in PeCoff, not defined in PECOFF.
# //
# #define EFI_IMAGE_WEAK_EXTERN_SEARCH_NOLIBRARY  1
# #define EFI_IMAGE_WEAK_EXTERN_SEARCH_LIBRARY    2
# #define EFI_IMAGE_WEAK_EXTERN_SEARCH_ALIAS      3
EFI_IMAGE_WEAK_EXTERN_SEARCH_NOLIBRARY  = 1
EFI_IMAGE_WEAK_EXTERN_SEARCH_LIBRARY    = 2
EFI_IMAGE_WEAK_EXTERN_SEARCH_ALIAS      = 3

# 
# ///
# /// Relocation format.
# ///
# typedef struct {
#   UINT32    VirtualAddress;
#   UINT32    SymbolTableIndex;
#   UINT16    Type;
# } EFI_IMAGE_RELOCATION;
class EFI_IMAGE_RELOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",    UINT32),
    ("SymbolTableIndex",  UINT32),
    ("Type",              UINT16)
  ]

# 
# ///
# /// Size of EFI_IMAGE_RELOCATION
# ///
# #define EFI_IMAGE_SIZEOF_RELOCATION  10
EFI_IMAGE_SIZEOF_RELOCATION = 10

# 
# //
# // I386 relocation types.
# //
# #define EFI_IMAGE_REL_I386_ABSOLUTE  0x0000 ///< Reference is absolute, no relocation is necessary.
# #define EFI_IMAGE_REL_I386_DIR16     0x0001 ///< Direct 16-bit reference to the symbols virtual address.
# #define EFI_IMAGE_REL_I386_REL16     0x0002 ///< PC-relative 16-bit reference to the symbols virtual address.
# #define EFI_IMAGE_REL_I386_DIR32     0x0006 ///< Direct 32-bit reference to the symbols virtual address.
# #define EFI_IMAGE_REL_I386_DIR32NB   0x0007 ///< Direct 32-bit reference to the symbols virtual address, base not included.
# #define EFI_IMAGE_REL_I386_SEG12     0x0009 ///< Direct 16-bit reference to the segment-selector bits of a 32-bit virtual address.
# #define EFI_IMAGE_REL_I386_SECTION   0x000A
# #define EFI_IMAGE_REL_I386_SECREL    0x000B
# #define EFI_IMAGE_REL_I386_REL32     0x0014 ///< PC-relative 32-bit reference to the symbols virtual address.
EFI_IMAGE_REL_I386_ABSOLUTE = 0x0000
EFI_IMAGE_REL_I386_DIR16    = 0x0001
EFI_IMAGE_REL_I386_REL16    = 0x0002
EFI_IMAGE_REL_I386_DIR32    = 0x0006
EFI_IMAGE_REL_I386_DIR32NB  = 0x0007
EFI_IMAGE_REL_I386_SEG12    = 0x0009
EFI_IMAGE_REL_I386_SECTION  = 0x000A
EFI_IMAGE_REL_I386_SECREL   = 0x000B
EFI_IMAGE_REL_I386_REL32    = 0x0014

# 
# //
# // x64 processor relocation types.
# //
# #define IMAGE_REL_AMD64_ABSOLUTE  0x0000
# #define IMAGE_REL_AMD64_ADDR64    0x0001
# #define IMAGE_REL_AMD64_ADDR32    0x0002
# #define IMAGE_REL_AMD64_ADDR32NB  0x0003
# #define IMAGE_REL_AMD64_REL32     0x0004
# #define IMAGE_REL_AMD64_REL32_1   0x0005
# #define IMAGE_REL_AMD64_REL32_2   0x0006
# #define IMAGE_REL_AMD64_REL32_3   0x0007
# #define IMAGE_REL_AMD64_REL32_4   0x0008
# #define IMAGE_REL_AMD64_REL32_5   0x0009
# #define IMAGE_REL_AMD64_SECTION   0x000A
# #define IMAGE_REL_AMD64_SECREL    0x000B
# #define IMAGE_REL_AMD64_SECREL7   0x000C
# #define IMAGE_REL_AMD64_TOKEN     0x000D
# #define IMAGE_REL_AMD64_SREL32    0x000E
# #define IMAGE_REL_AMD64_PAIR      0x000F
# #define IMAGE_REL_AMD64_SSPAN32   0x0010
IMAGE_REL_AMD64_ABSOLUTE  = 0x0000
IMAGE_REL_AMD64_ADDR64    = 0x0001
IMAGE_REL_AMD64_ADDR32    = 0x0002
IMAGE_REL_AMD64_ADDR32NB  = 0x0003
IMAGE_REL_AMD64_REL32     = 0x0004
IMAGE_REL_AMD64_REL32_1   = 0x0005
IMAGE_REL_AMD64_REL32_2   = 0x0006
IMAGE_REL_AMD64_REL32_3   = 0x0007
IMAGE_REL_AMD64_REL32_4   = 0x0008
IMAGE_REL_AMD64_REL32_5   = 0x0009
IMAGE_REL_AMD64_SECTION   = 0x000A
IMAGE_REL_AMD64_SECREL    = 0x000B
IMAGE_REL_AMD64_SECREL7   = 0x000C
IMAGE_REL_AMD64_TOKEN     = 0x000D
IMAGE_REL_AMD64_SREL32    = 0x000E
IMAGE_REL_AMD64_PAIR      = 0x000F
IMAGE_REL_AMD64_SSPAN32   = 0x0010

# 
# ///
# /// Based relocation format.
# ///
# typedef struct {
#   UINT32    VirtualAddress;
#   UINT32    SizeOfBlock;
# } EFI_IMAGE_BASE_RELOCATION;
class EFI_IMAGE_BASE_RELOCATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("VirtualAddress",  UINT32),
    ("SizeOfBlock",     UINT32)
  ]

# 
# ///
# /// Size of EFI_IMAGE_BASE_RELOCATION.
# ///
# #define EFI_IMAGE_SIZEOF_BASE_RELOCATION  8
EFI_IMAGE_SIZEOF_BASE_RELOCATION  = 8

# 
# //
# // Based relocation types.
# //
# #define EFI_IMAGE_REL_BASED_ABSOLUTE        0
# #define EFI_IMAGE_REL_BASED_HIGH            1
# #define EFI_IMAGE_REL_BASED_LOW             2
# #define EFI_IMAGE_REL_BASED_HIGHLOW         3
# #define EFI_IMAGE_REL_BASED_HIGHADJ         4
# #define EFI_IMAGE_REL_BASED_MIPS_JMPADDR    5
# #define EFI_IMAGE_REL_BASED_ARM_MOV32A      5
# #define EFI_IMAGE_REL_BASED_ARM_MOV32T      7
# #define EFI_IMAGE_REL_BASED_IA64_IMM64      9
# #define EFI_IMAGE_REL_BASED_MIPS_JMPADDR16  9
# #define EFI_IMAGE_REL_BASED_DIR64           10
EFI_IMAGE_REL_BASED_ABSOLUTE        = 0
EFI_IMAGE_REL_BASED_HIGH            = 1
EFI_IMAGE_REL_BASED_LOW             = 2
EFI_IMAGE_REL_BASED_HIGHLOW         = 3
EFI_IMAGE_REL_BASED_HIGHADJ         = 4
EFI_IMAGE_REL_BASED_MIPS_JMPADDR    = 5
EFI_IMAGE_REL_BASED_ARM_MOV32A      = 5
EFI_IMAGE_REL_BASED_ARM_MOV32T      = 7
EFI_IMAGE_REL_BASED_IA64_IMM64      = 9
EFI_IMAGE_REL_BASED_MIPS_JMPADDR16  = 9
EFI_IMAGE_REL_BASED_DIR64           = 10

# 
# ///
# /// Relocation types of RISC-V processor.
# ///
# #define EFI_IMAGE_REL_BASED_RISCV_HI20    5
# #define EFI_IMAGE_REL_BASED_RISCV_LOW12I  7
# #define EFI_IMAGE_REL_BASED_RISCV_LOW12S  8
EFI_IMAGE_REL_BASED_RISCV_HI20    = 5
EFI_IMAGE_REL_BASED_RISCV_LOW12I  = 7
EFI_IMAGE_REL_BASED_RISCV_LOW12S  = 8

# 
# //
# // Relocation types of LoongArch processor.
# //
# #define EFI_IMAGE_REL_BASED_LOONGARCH32_MARK_LA  8
# #define EFI_IMAGE_REL_BASED_LOONGARCH64_MARK_LA  8
EFI_IMAGE_REL_BASED_LOONGARCH32_MARK_LA  = 8
EFI_IMAGE_REL_BASED_LOONGARCH64_MARK_LA  = 8

# 
# ///
# /// Line number format.
# ///
# typedef struct {
#   union {
#     UINT32    SymbolTableIndex; ///< Symbol table index of function name if Linenumber is 0.
#     UINT32    VirtualAddress;   ///< Virtual address of line number.
#   } Type;
#   UINT16    Linenumber;       ///< Line number.
# } EFI_IMAGE_LINENUMBER;
class EFI_IMAGE_LINENUMBER_Type (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("SymbolTableIndex",  UINT32),
    ("VirtualAddress",    UINT32)
  ]

class EFI_IMAGE_LINENUMBER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Type",        EFI_IMAGE_LINENUMBER_Type),
    ("Linenumber",  UINT16)
  ]

# 
# ///
# /// Size of EFI_IMAGE_LINENUMBER.
# ///
# #define EFI_IMAGE_SIZEOF_LINENUMBER  6
EFI_IMAGE_SIZEOF_LINENUMBER = 6

# 
# //
# // Archive format.
# //
# #define EFI_IMAGE_ARCHIVE_START_SIZE        8
# #define EFI_IMAGE_ARCHIVE_START             "!<arch>\n"
# #define EFI_IMAGE_ARCHIVE_END               "`\n"
# #define EFI_IMAGE_ARCHIVE_PAD               "\n"
# #define EFI_IMAGE_ARCHIVE_LINKER_MEMBER     "/               "
# #define EFI_IMAGE_ARCHIVE_LONGNAMES_MEMBER  "//              "
EFI_IMAGE_ARCHIVE_START_SIZE        = 8
EFI_IMAGE_ARCHIVE_START             = b"!<arch>\n"
EFI_IMAGE_ARCHIVE_END               = b"`\n"
EFI_IMAGE_ARCHIVE_PAD               = b"\n"
EFI_IMAGE_ARCHIVE_LINKER_MEMBER     = b"/               " 
EFI_IMAGE_ARCHIVE_LONGNAMES_MEMBER  = b"//              " 

# 
# ///
# /// Archive Member Headers
# ///
# typedef struct {
#   UINT8    Name[16];     ///< File member name - `/' terminated.
#   UINT8    Date[12];     ///< File member date - decimal.
#   UINT8    UserID[6];    ///< File member user id - decimal.
#   UINT8    GroupID[6];   ///< File member group id - decimal.
#   UINT8    Mode[8];      ///< File member mode - octal.
#   UINT8    Size[10];     ///< File member size - decimal.
#   UINT8    EndHeader[2]; ///< String to end header. (0x60 0x0A).
# } EFI_IMAGE_ARCHIVE_MEMBER_HEADER;
class EFI_IMAGE_ARCHIVE_MEMBER_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Name",      UINT8 * 16),
    ("Date",      UINT8 * 12),
    ("UserID",    UINT8 * 6),
    ("GroupID",   UINT8 * 6),
    ("Mode",      UINT8 * 8),
    ("Size",      UINT8 * 10),
    ("EndHeader", UINT8 * 2)
  ]

# 
# ///
# /// Size of EFI_IMAGE_ARCHIVE_MEMBER_HEADER.
# ///
# #define EFI_IMAGE_SIZEOF_ARCHIVE_MEMBER_HDR  60
EFI_IMAGE_SIZEOF_ARCHIVE_MEMBER_HDR = 60

# 
# //
# // DLL Support
# //
# 
# ///
# /// Export Directory Table.
# ///
# typedef struct {
#   UINT32    Characteristics;
#   UINT32    TimeDateStamp;
#   UINT16    MajorVersion;
#   UINT16    MinorVersion;
#   UINT32    Name;
#   UINT32    Base;
#   UINT32    NumberOfFunctions;
#   UINT32    NumberOfNames;
#   UINT32    AddressOfFunctions;
#   UINT32    AddressOfNames;
#   UINT32    AddressOfNameOrdinals;
# } EFI_IMAGE_EXPORT_DIRECTORY;
class EFI_IMAGE_EXPORT_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics",       UINT32),
    ("TimeDateStamp",         UINT32),
    ("MajorVersion",          UINT16),
    ("MinorVersion",          UINT16),
    ("Name",                  UINT32),
    ("Base",                  UINT32),
    ("NumberOfFunctions",     UINT32),
    ("NumberOfNames",         UINT32),
    ("AddressOfFunctions",    UINT32),
    ("AddressOfNames",        UINT32),
    ("AddressOfNameOrdinals", UINT32)
  ]

# 
# ///
# /// Hint/Name Table.
# ///
# typedef struct {
#   UINT16    Hint;
#   UINT8     Name[1];
# } EFI_IMAGE_IMPORT_BY_NAME;
class EFI_IMAGE_IMPORT_BY_NAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Hint",  UINT16),
    ("Name",  UINT8 * 1)
  ]

# 
# ///
# /// Import Address Table RVA (Thunk Table).
# ///
# typedef struct {
#   union {
#     UINT32                      Function;
#     UINT32                      Ordinal;
#     EFI_IMAGE_IMPORT_BY_NAME    *AddressOfData;
#   } u1;
# } EFI_IMAGE_THUNK_DATA;
class EFI_IMAGE_THUNK_DATA_u1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Function",      UINT32),
    ("Ordinal",       UINT32),
    ("AddressOfData", POINTER (EFI_IMAGE_IMPORT_BY_NAME))
  ]

class EFI_IMAGE_THUNK_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("u1",  EFI_IMAGE_THUNK_DATA_u1)
  ]

# 
# #define EFI_IMAGE_ORDINAL_FLAG  BIT31                ///< Flag for PE32.
EFI_IMAGE_ORDINAL_FLAG              = BIT31

# #define EFI_IMAGE_SNAP_BY_ORDINAL(Ordinal)  ((Ordinal & EFI_IMAGE_ORDINAL_FLAG) != 0)
def EFI_IMAGE_SNAP_BY_ORDINAL (Ordinal):

  if (Ordinal & EFI_IMAGE_ORDINAL_FLAG) != 0:
    return True
  else:
    return False

# #define EFI_IMAGE_ORDINAL(Ordinal)          (Ordinal & 0xffff)
def EFI_IMAGE_ORDINAL(Ordinal):
  return Ordinal & 0xffff

# 
# ///
# /// Import Directory Table
# ///
# typedef struct {
#   UINT32                  Characteristics;
#   UINT32                  TimeDateStamp;
#   UINT32                  ForwarderChain;
#   UINT32                  Name;
#   EFI_IMAGE_THUNK_DATA    *FirstThunk;
# } EFI_IMAGE_IMPORT_DESCRIPTOR;
class EFI_IMAGE_IMPORT_DESCRIPTOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics", UINT32),
    ("TimeDateStamp",   UINT32),
    ("ForwarderChain",  UINT32),
    ("Name",            UINT32),
    ("FirstThunk",      POINTER (EFI_IMAGE_THUNK_DATA))
  ]

# 
# ///
# /// Debug Directory Format.
# ///
# typedef struct {
#   UINT32    Characteristics;
#   UINT32    TimeDateStamp;
#   UINT16    MajorVersion;
#   UINT16    MinorVersion;
#   UINT32    Type;
#   UINT32    SizeOfData;
#   UINT32    RVA;         ///< The address of the debug data when loaded, relative to the image base.
#   UINT32    FileOffset;  ///< The file pointer to the debug data.
# } EFI_IMAGE_DEBUG_DIRECTORY_ENTRY;
class EFI_IMAGE_DEBUG_DIRECTORY_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics", UINT32),
    ("TimeDateStamp",   UINT32),
    ("MajorVersion",    UINT16),
    ("MinorVersion",    UINT16),
    ("Type",            UINT32),
    ("SizeOfData",      UINT32),
    ("RVA",             UINT32),
    ("FileOffset",      UINT32)
  ]

# 
# #define EFI_IMAGE_DEBUG_TYPE_CODEVIEW               2    ///< The Visual C++ debug information.
# #define EFI_IMAGE_DEBUG_TYPE_EX_DLLCHARACTERISTICS  20
EFI_IMAGE_DEBUG_TYPE_CODEVIEW               = 2
EFI_IMAGE_DEBUG_TYPE_EX_DLLCHARACTERISTICS  = 20

# 
# ///
# /// Debug Data Structure defined in Microsoft C++.
# ///
# #define CODEVIEW_SIGNATURE_NB10  SIGNATURE_32('N', 'B', '1', '0')
CODEVIEW_SIGNATURE_NB10  = SIGNATURE_32('N', 'B', '1', '0')

# typedef struct {
#   UINT32    Signature;                      ///< "NB10"
#   UINT32    Unknown;
#   UINT32    Unknown2;
#   UINT32    Unknown3;
#   //
#   // Filename of .PDB goes here
#   //
# } EFI_IMAGE_DEBUG_CODEVIEW_NB10_ENTRY;
class EFI_IMAGE_DEBUG_CODEVIEW_NB10_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Unknown",   UINT32),
    ("Unknown2",  UINT32),
    ("Unknown3",  UINT32)
  ]

# 
# ///
# /// Debug Data Structure defined in Microsoft C++.
# ///
# #define CODEVIEW_SIGNATURE_RSDS  SIGNATURE_32('R', 'S', 'D', 'S')
CODEVIEW_SIGNATURE_RSDS  = SIGNATURE_32('R', 'S', 'D', 'S')

# typedef struct {
#   UINT32    Signature;                      ///< "RSDS".
#   UINT32    Unknown;
#   UINT32    Unknown2;
#   UINT32    Unknown3;
#   UINT32    Unknown4;
#   UINT32    Unknown5;
#   //
#   // Filename of .PDB goes here
#   //
# } EFI_IMAGE_DEBUG_CODEVIEW_RSDS_ENTRY;
class EFI_IMAGE_DEBUG_CODEVIEW_RSDS_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("Unknown",   UINT32),
    ("Unknown2",  UINT32),
    ("Unknown3",  UINT32),
    ("Unknown4",  UINT32),
    ("Unknown5",  UINT32)
  ]

# 
# ///
# /// Debug Data Structure defined by Apple Mach-O to Coff utility.
# ///
# #define CODEVIEW_SIGNATURE_MTOC  SIGNATURE_32('M', 'T', 'O', 'C')
CODEVIEW_SIGNATURE_MTOC  = SIGNATURE_32('M', 'T', 'O', 'C')

# typedef struct {
#   UINT32    Signature;                       ///< "MTOC".
#   GUID      MachOUuid;
#   //
#   //  Filename of .DLL (Mach-O with debug info) goes here
#   //
# } EFI_IMAGE_DEBUG_CODEVIEW_MTOC_ENTRY;
class EFI_IMAGE_DEBUG_CODEVIEW_MTOC_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature", UINT32),
    ("MachOUuid", GUID)
  ]

# 
# ///
# /// Extended DLL Characteristics
# ///
# #define EFI_IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT          0x0001
# #define EFI_IMAGE_DLLCHARACTERISTICS_EX_FORWARD_CFI_COMPAT  0x0040
EFI_IMAGE_DLLCHARACTERISTICS_EX_CET_COMPAT          = 0x0001
EFI_IMAGE_DLLCHARACTERISTICS_EX_FORWARD_CFI_COMPAT  = 0x0040

# 
# typedef struct {
#   UINT32    DllCharacteristicsEx;
# } EFI_IMAGE_DEBUG_EX_DLLCHARACTERISTICS_ENTRY;
class EFI_IMAGE_DEBUG_EX_DLLCHARACTERISTICS_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DllCharacteristicsEx", UINT32)
  ]

# 
# ///
# /// Resource format.
# ///
# typedef struct {
#   UINT32    Characteristics;
#   UINT32    TimeDateStamp;
#   UINT16    MajorVersion;
#   UINT16    MinorVersion;
#   UINT16    NumberOfNamedEntries;
#   UINT16    NumberOfIdEntries;
#   //
#   // Array of EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY entries goes here.
#   //
# } EFI_IMAGE_RESOURCE_DIRECTORY;
class EFI_IMAGE_RESOURCE_DIRECTORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Characteristics",       UINT32),
    ("TimeDateStamp",         UINT32),
    ("MajorVersion",          UINT16),
    ("MinorVersion",          UINT16),
    ("NumberOfNamedEntries",  UINT16),
    ("NumberOfIdEntries",     UINT16)
  ]

# 
# ///
# /// Resource directory entry format.
# ///
# typedef struct {
#   union {
#     struct {
#       UINT32    NameOffset   : 31;
#       UINT32    NameIsString : 1;
#     } s;
#     UINT32    Id;
#   } u1;
#   union {
#     UINT32    OffsetToData;
#     struct {
#       UINT32    OffsetToDirectory : 31;
#       UINT32    DataIsDirectory   : 1;
#     } s;
#   } u2;
# } EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY;
class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1_s (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("NameOffset",    UINT32, 31),
    ("NameIsString",  UINT32, 1),
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("s",   EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1_s),
    ("Id",  UINT32)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2_s (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OffsetToDirectory", UINT32, 31),
    ("DataIsDirectory",   UINT32, 1)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2 (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("OffsetToData",  UINT32),
    ("s",             EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2_s)
  ]

class EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("u1",  EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u1),
    ("u2",  EFI_IMAGE_RESOURCE_DIRECTORY_ENTRY_u2)
  ]

# 
# ///
# /// Resource directory entry for string.
# ///
# typedef struct {
#   UINT16    Length;
#   CHAR16    String[1];
# } EFI_IMAGE_RESOURCE_DIRECTORY_STRING;
class EFI_IMAGE_RESOURCE_DIRECTORY_STRING (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Length",  UINT16),
    ("String",  CHAR16 * 1)
  ]

# 
# ///
# /// Resource directory entry for data array.
# ///
# typedef struct {
#   UINT32    OffsetToData;
#   UINT32    Size;
#   UINT32    CodePage;
#   UINT32    Reserved;
# } EFI_IMAGE_RESOURCE_DATA_ENTRY;
class EFI_IMAGE_RESOURCE_DATA_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("OffsetToData",  UINT32),
    ("Size",          UINT32),
    ("CodePage",      UINT32),
    ("Reserved",      UINT32)
  ]

# 
# ///
# /// Header format for TE images, defined in the PI Specification, 1.0.
# ///
# typedef struct {
#   UINT16                      Signature;           ///< The signature for TE format = "VZ".
#   UINT16                      Machine;             ///< From the original file header.
#   UINT8                       NumberOfSections;    ///< From the original file header.
#   UINT8                       Subsystem;           ///< From original optional header.
#   UINT16                      StrippedSize;        ///< Number of bytes we removed from the header.
#   UINT32                      AddressOfEntryPoint; ///< Offset to entry point -- from original optional header.
#   UINT32                      BaseOfCode;          ///< From original image -- required for ITP debug.
#   UINT64                      ImageBase;           ///< From original file header.
#   EFI_IMAGE_DATA_DIRECTORY    DataDirectory[2];    ///< Only base relocation and debug directory.
# } EFI_TE_IMAGE_HEADER;
class EFI_TE_IMAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Signature",           UINT16),
    ("Machine",             UINT16),
    ("NumberOfSections",    UINT8),
    ("Subsystem",           UINT8),
    ("StrippedSize",        UINT16),
    ("AddressOfEntryPoint", UINT32),
    ("BaseOfCode",          UINT32),
    ("ImageBase",           UINT64),
    ("DataDirectory",       EFI_IMAGE_DATA_DIRECTORY * 2)
  ]

# 
# #define EFI_TE_IMAGE_HEADER_SIGNATURE  SIGNATURE_16('V', 'Z')
EFI_TE_IMAGE_HEADER_SIGNATURE  = SIGNATURE_16('V', 'Z')

# 
# //
# // Data directory indexes in our TE image header
# //
# #define EFI_TE_IMAGE_DIRECTORY_ENTRY_BASERELOC  0
# #define EFI_TE_IMAGE_DIRECTORY_ENTRY_DEBUG      1
EFI_TE_IMAGE_DIRECTORY_ENTRY_BASERELOC  = 0
EFI_TE_IMAGE_DIRECTORY_ENTRY_DEBUG      = 1

# 
# ///
# /// Union of PE32, PE32+, and TE headers.
# ///
# typedef union {
#   EFI_IMAGE_NT_HEADERS32    Pe32;
#   EFI_IMAGE_NT_HEADERS64    Pe32Plus;
#   EFI_TE_IMAGE_HEADER       Te;
# } EFI_IMAGE_OPTIONAL_HEADER_UNION;
class EFI_IMAGE_OPTIONAL_HEADER_UNION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Pe32",      EFI_IMAGE_NT_HEADERS32),
    ("Pe32Plus",  EFI_IMAGE_NT_HEADERS64),
    ("Te",        EFI_TE_IMAGE_HEADER)
  ]

# 
# typedef union {
#   EFI_IMAGE_NT_HEADERS32             *Pe32;
#   EFI_IMAGE_NT_HEADERS64             *Pe32Plus;
#   EFI_TE_IMAGE_HEADER                *Te;
#   EFI_IMAGE_OPTIONAL_HEADER_UNION    *Union;
# } EFI_IMAGE_OPTIONAL_HEADER_PTR_UNION;
class EFI_IMAGE_OPTIONAL_HEADER_PTR_UNION (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("Pe32",      POINTER (EFI_IMAGE_NT_HEADERS32)),
    ("Pe32Plus",  POINTER (EFI_IMAGE_NT_HEADERS64)),
    ("Te",        POINTER (EFI_TE_IMAGE_HEADER)),
    ("Union",     POINTER (EFI_IMAGE_OPTIONAL_HEADER_UNION))
  ]

# 
# #endif
# 