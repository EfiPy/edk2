# /** @file
#   This file defines the encoding for the VFR (Visual Form Representation) language.
#   IFR is primarily consumed by the EFI presentation engine, and produced by EFI
#   internal application and drivers as well as all add-in card option-ROM drivers
# 
# Copyright (c) 2006 - 2018, Intel Corporation. All rights reserved.<BR>
# (C) Copyright 2016 Hewlett Packard Enterprise Development LP<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
#   @par Revision Reference:
#   These definitions are from UEFI 2.1 and 2.2.
# 
# **/
#
# UefiInternalFormRepresentation.py
#
# EfiPy2.MdePkg.Uefi.UefiInternalFormRepresentation
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# 
# #ifndef __UEFI_INTERNAL_FORMREPRESENTATION_H__
# #define __UEFI_INTERNAL_FORMREPRESENTATION_H__
from EfiPy2  import *

# #include <Guid/HiiFormMapMethodGuid.h>
# 
# ///
# /// The following types are currently defined:
# ///
# typedef VOID    *EFI_HII_HANDLE;
# typedef CHAR16  *EFI_STRING;
# typedef UINT16  EFI_IMAGE_ID;
# typedef UINT16  EFI_QUESTION_ID;
# typedef UINT16  EFI_STRING_ID;
# typedef UINT16  EFI_FORM_ID;
# typedef UINT16  EFI_VARSTORE_ID;
# typedef UINT16  EFI_ANIMATION_ID;
# 
# typedef UINT16 EFI_DEFAULT_ID;
# 
# typedef UINT32 EFI_HII_FONT_STYLE;
EFI_HII_HANDLE    = PVOID
EFI_STRING        = PCHAR16
EFI_IMAGE_ID      = UINT16
EFI_QUESTION_ID   = UINT16
EFI_STRING_ID     = UINT16
EFI_FORM_ID       = UINT16
EFI_VARSTORE_ID   = UINT16
EFI_ANIMATION_ID  = UINT16
EFI_DEFAULT_ID    = UINT16
EFI_HII_FONT_STYLE  = UINT32

# 
# #pragma pack(1)
# 
# //
# // Definitions for Package Lists and Package Headers
# // Section 27.3.1
# //
# 
# ///
# /// The header found at the start of each package list.
# ///
# typedef struct {
#   EFI_GUID    PackageListGuid;
#   UINT32      PackageLength;
# } EFI_HII_PACKAGE_LIST_HEADER;
class EFI_HII_PACKAGE_LIST_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("PackageListGuid", EFI_GUID),
    ("PackageLength",   UINT32)
  ]

# 
# ///
# /// The header found at the start of each package.
# ///
# typedef struct {
#   UINT32    Length : 24;
#   UINT32    Type   : 8;
#   // UINT8  Data[...];
# } EFI_HII_PACKAGE_HEADER;
class EFI_HII_PACKAGE_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Length",  UINT32, 24),
    ("Type",    UINT32, 8)
    # ("Data",    UINT8 * N)
  ]

# 
# //
# // Value of HII package type
# //
# #define EFI_HII_PACKAGE_TYPE_ALL           0x00
# #define EFI_HII_PACKAGE_TYPE_GUID          0x01
# #define EFI_HII_PACKAGE_FORMS              0x02
# #define EFI_HII_PACKAGE_STRINGS            0x04
# #define EFI_HII_PACKAGE_FONTS              0x05
# #define EFI_HII_PACKAGE_IMAGES             0x06
# #define EFI_HII_PACKAGE_SIMPLE_FONTS       0x07
# #define EFI_HII_PACKAGE_DEVICE_PATH        0x08
# #define EFI_HII_PACKAGE_KEYBOARD_LAYOUT    0x09
# #define EFI_HII_PACKAGE_ANIMATIONS         0x0A
# #define EFI_HII_PACKAGE_END                0xDF
# #define EFI_HII_PACKAGE_TYPE_SYSTEM_BEGIN  0xE0
# #define EFI_HII_PACKAGE_TYPE_SYSTEM_END    0xFF
EFI_HII_PACKAGE_TYPE_ALL             = 0x00
EFI_HII_PACKAGE_TYPE_GUID            = 0x01
EFI_HII_PACKAGE_FORMS                = 0x02
EFI_HII_PACKAGE_STRINGS              = 0x04
EFI_HII_PACKAGE_FONTS                = 0x05
EFI_HII_PACKAGE_IMAGES               = 0x06
EFI_HII_PACKAGE_SIMPLE_FONTS         = 0x07
EFI_HII_PACKAGE_DEVICE_PATH          = 0x08
EFI_HII_PACKAGE_KEYBOARD_LAYOUT      = 0x09
EFI_HII_PACKAGE_ANIMATIONS           = 0x0A
EFI_HII_PACKAGE_END                  = 0xDF
EFI_HII_PACKAGE_TYPE_SYSTEM_BEGIN    = 0xE0
EFI_HII_PACKAGE_TYPE_SYSTEM_END      = 0xFF

# 
# //
# // Definitions for Simplified Font Package
# //
# 
# ///
# /// Contents of EFI_NARROW_GLYPH.Attributes.
# ///@{
# #define EFI_GLYPH_NON_SPACING  0x01
# #define EFI_GLYPH_WIDE         0x02
# #define EFI_GLYPH_HEIGHT       19
# #define EFI_GLYPH_WIDTH        8
EFI_GLYPH_NON_SPACING                = 0x01
EFI_GLYPH_WIDE                       = 0x02
EFI_GLYPH_HEIGHT                     = 19
EFI_GLYPH_WIDTH                      = 8

# ///@}
# 
# ///
# /// The EFI_NARROW_GLYPH has a preferred dimension (w x h) of 8 x 19 pixels.
# ///
# typedef struct {
#   ///
#   /// The Unicode representation of the glyph. The term weight is the
#   /// technical term for a character code.
#   ///
#   CHAR16    UnicodeWeight;
#   ///
#   /// The data element containing the glyph definitions.
#   ///
#   UINT8     Attributes;
#   ///
#   /// The column major glyph representation of the character. Bits
#   /// with values of one indicate that the corresponding pixel is to be
#   /// on when normally displayed; those with zero are off.
#   ///
#   UINT8     GlyphCol1[EFI_GLYPH_HEIGHT];
# } EFI_NARROW_GLYPH;
class EFI_NARROW_GLYPH (Structure):
  _pack_   = 1
  _fields_ = [
    ("UnicodeWeight", CHAR16),
    ("Attributes",    UINT8),
    ("GlyphCol1",     UINT8 * EFI_GLYPH_HEIGHT)
  ]

# 
# ///
# /// The EFI_WIDE_GLYPH has a preferred dimension (w x h) of 16 x 19 pixels, which is large enough
# /// to accommodate logographic characters.
# ///
# typedef struct {
#   ///
#   /// The Unicode representation of the glyph. The term weight is the
#   /// technical term for a character code.
#   ///
#   CHAR16    UnicodeWeight;
#   ///
#   /// The data element containing the glyph definitions.
#   ///
#   UINT8     Attributes;
#   ///
#   /// The column major glyph representation of the character. Bits
#   /// with values of one indicate that the corresponding pixel is to be
#   /// on when normally displayed; those with zero are off.
#   ///
#   UINT8     GlyphCol1[EFI_GLYPH_HEIGHT];
#   ///
#   /// The column major glyph representation of the character. Bits
#   /// with values of one indicate that the corresponding pixel is to be
#   /// on when normally displayed; those with zero are off.
#   ///
#   UINT8     GlyphCol2[EFI_GLYPH_HEIGHT];
#   ///
#   /// Ensures that sizeof (EFI_WIDE_GLYPH) is twice the
#   /// sizeof (EFI_NARROW_GLYPH). The contents of Pad must
#   /// be zero.
#   ///
#   UINT8     Pad[3];
# } EFI_WIDE_GLYPH;
class EFI_WIDE_GLYPH (Structure):
  _pack_   = 1
  _fields_ = [
    ("UnicodeWeight", CHAR16),
    ("Attributes",    UINT8),
    ("GlyphCol1",     UINT8 * EFI_GLYPH_HEIGHT),
    ("GlyphCol2",     UINT8 * EFI_GLYPH_HEIGHT),
    ("Pad",           UINT8 * 3)
  ]

# 
# ///
# /// A simplified font package consists of a font header
# /// followed by a series of glyph structures.
# ///
# typedef struct _EFI_HII_SIMPLE_FONT_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   UINT16                    NumberOfNarrowGlyphs;
#   UINT16                    NumberOfWideGlyphs;
#   // EFI_NARROW_GLYPH       NarrowGlyphs[];
#   // EFI_WIDE_GLYPH         WideGlyphs[];
# } EFI_HII_SIMPLE_FONT_PACKAGE_HDR;
class EFI_HII_SIMPLE_FONT_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",                EFI_HII_PACKAGE_HEADER),
    ("NumberOfNarrowGlyphs",  UINT16),
    ("NumberOfWideGlyphs",    UINT16)
    # ("NarrowGlyphs",          EFI_NARROW_GLYPH),
    # ("WideGlyphs",            EFI_NARROW_GLYPH)
  ]

# 
# //
# // Definitions for Font Package
# // Section 27.3.3
# //
# 
# //
# // Value for font style
# //
# #define EFI_HII_FONT_STYLE_NORMAL     0x00000000
# #define EFI_HII_FONT_STYLE_BOLD       0x00000001
# #define EFI_HII_FONT_STYLE_ITALIC     0x00000002
# #define EFI_HII_FONT_STYLE_EMBOSS     0x00010000
# #define EFI_HII_FONT_STYLE_OUTLINE    0x00020000
# #define EFI_HII_FONT_STYLE_SHADOW     0x00040000
# #define EFI_HII_FONT_STYLE_UNDERLINE  0x00080000
# #define EFI_HII_FONT_STYLE_DBL_UNDER  0x00100000
EFI_HII_FONT_STYLE_NORMAL            = 0x00000000
EFI_HII_FONT_STYLE_BOLD              = 0x00000001
EFI_HII_FONT_STYLE_ITALIC            = 0x00000002
EFI_HII_FONT_STYLE_EMBOSS            = 0x00010000
EFI_HII_FONT_STYLE_OUTLINE           = 0x00020000
EFI_HII_FONT_STYLE_SHADOW            = 0x00040000
EFI_HII_FONT_STYLE_UNDERLINE         = 0x00080000
EFI_HII_FONT_STYLE_DBL_UNDER         = 0x00100000

# 
# typedef struct _EFI_HII_GLYPH_INFO {
#   UINT16    Width;
#   UINT16    Height;
#   INT16     OffsetX;
#   INT16     OffsetY;
#   INT16     AdvanceX;
# } EFI_HII_GLYPH_INFO;
class EFI_HII_GLYPH_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",     UINT16),
    ("Height",    UINT16),
    ("OffsetX",   INT16),
    ("OffsetY",   INT16),
    ("AdvanceX",  INT16)
  ]

# 
# ///
# /// The fixed header consists of a standard record header,
# /// then the character values in this section, the flags
# /// (including the encoding method) and the offsets of the glyph
# /// information, the glyph bitmaps and the character map.
# ///
# typedef struct _EFI_HII_FONT_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   UINT32                    HdrSize;
#   UINT32                    GlyphBlockOffset;
#   EFI_HII_GLYPH_INFO        Cell;
#   EFI_HII_FONT_STYLE        FontStyle;
#   CHAR16                    FontFamily[1];
# } EFI_HII_FONT_PACKAGE_HDR;
class EFI_HII_FONT_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("HdrSize",           UINT32),
    ("GlyphBlockOffset",  UINT32),
    ("Cell",              EFI_HII_GLYPH_INFO),
    ("FontStyle",         EFI_HII_FONT_STYLE),
    ("FontFamily",        CHAR16 * 1)
  ]

# 
# //
# // Value of different glyph info block types
# //
# #define EFI_HII_GIBT_END                0x00
# #define EFI_HII_GIBT_GLYPH              0x10
# #define EFI_HII_GIBT_GLYPHS             0x11
# #define EFI_HII_GIBT_GLYPH_DEFAULT      0x12
# #define EFI_HII_GIBT_GLYPHS_DEFAULT     0x13
# #define EFI_HII_GIBT_GLYPH_VARIABILITY  0x14
# #define EFI_HII_GIBT_DUPLICATE          0x20
# #define EFI_HII_GIBT_SKIP2              0x21
# #define EFI_HII_GIBT_SKIP1              0x22
# #define EFI_HII_GIBT_DEFAULTS           0x23
# #define EFI_HII_GIBT_EXT1               0x30
# #define EFI_HII_GIBT_EXT2               0x31
# #define EFI_HII_GIBT_EXT4               0x32
EFI_HII_GIBT_END                  = 0x00
EFI_HII_GIBT_GLYPH                = 0x10
EFI_HII_GIBT_GLYPHS               = 0x11
EFI_HII_GIBT_GLYPH_DEFAULT        = 0x12
EFI_HII_GIBT_GLYPHS_DEFAULT       = 0x13
EFI_HII_GIBT_DUPLICATE            = 0x20
EFI_HII_GIBT_SKIP2                = 0x21
EFI_HII_GIBT_SKIP1                = 0x22
EFI_HII_GIBT_DEFAULTS             = 0x23
EFI_HII_GIBT_EXT1                 = 0x30
EFI_HII_GIBT_EXT2                 = 0x31
EFI_HII_GIBT_EXT4                 = 0x32

# 
# typedef struct _EFI_HII_GLYPH_BLOCK {
#   UINT8    BlockType;
# } EFI_HII_GLYPH_BLOCK;
class EFI_HII_GLYPH_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
  ]

# 
# //
# // Definition of different glyph info block types
# //
# 
# typedef struct _EFI_HII_GIBT_DEFAULTS_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   EFI_HII_GLYPH_INFO     Cell;
# } EFI_HII_GIBT_DEFAULTS_BLOCK;
class EFI_HII_GIBT_DEFAULTS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_GLYPH_BLOCK),
    ("Cell",    EFI_HII_GLYPH_INFO)
  ]

# 
# typedef struct _EFI_HII_GIBT_DUPLICATE_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   CHAR16                 CharValue;
# } EFI_HII_GIBT_DUPLICATE_BLOCK;
class EFI_HII_GIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_GLYPH_BLOCK),
    ("TCharValueype", CHAR16)
  ]

# 
# typedef struct _EFI_GLYPH_GIBT_END_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
# } EFI_GLYPH_GIBT_END_BLOCK;
class EFI_GLYPH_GIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_GLYPH_BLOCK)
  ]

# 
# typedef struct _EFI_HII_GIBT_EXT1_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT8                  Length;
# } EFI_HII_GIBT_EXT1_BLOCK;
class EFI_HII_GIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

# 
# typedef struct _EFI_HII_GIBT_EXT2_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT16                 Length;
# } EFI_HII_GIBT_EXT2_BLOCK;
class EFI_HII_GIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

# 
# typedef struct _EFI_HII_GIBT_EXT4_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT32                 Length;
# } EFI_HII_GIBT_EXT4_BLOCK;
class EFI_HII_GIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

# 
# typedef struct _EFI_HII_GIBT_GLYPH_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   EFI_HII_GLYPH_INFO     Cell;
#   UINT8                  BitmapData[1];
# } EFI_HII_GIBT_GLYPH_BLOCK;
class EFI_HII_GIBT_GLYPH_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Cell",        EFI_HII_GLYPH_INFO),
    ("BitmapData",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_GIBT_GLYPHS_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   EFI_HII_GLYPH_INFO     Cell;
#   UINT16                 Count;
#   UINT8                  BitmapData[1];
# } EFI_HII_GIBT_GLYPHS_BLOCK;
class EFI_HII_GIBT_GLYPHS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Cell",        EFI_HII_GLYPH_INFO),
    ("Count",       UINT16),
    ("BitmapData",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_GIBT_GLYPH_DEFAULT_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT8                  BitmapData[1];
# } EFI_HII_GIBT_GLYPH_DEFAULT_BLOCK;
class EFI_HII_GIBT_GLYPH_DEFAULT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("BitmapData",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_GIBT_GLYPHS_DEFAULT_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT16                 Count;
#   UINT8                  BitmapData[1];
# } EFI_HII_GIBT_GLYPHS_DEFAULT_BLOCK;
class EFI_HII_GIBT_GLYPHS_DEFAULT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("Count",       UINT16),
    ("BitmapData",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_GIBT_VARIABILITY_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   EFI_HII_GLYPH_INFO     Cell;
#   UINT8                  GlyphPackInBits;
#   UINT8                  BitmapData[1];
# } EFI_HII_GIBT_VARIABILITY_BLOCK;
class EFI_HII_GIBT_VARIABILITY_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_GLYPH_BLOCK),
    ("Cell",              EFI_HII_GLYPH_INFO),
    ("GlyphPackInBits",   UINT8),
    ("BitmapData",        UINT8 * 1),
  ]

# 
# typedef struct _EFI_HII_GIBT_SKIP1_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT8                  SkipCount;
# } EFI_HII_GIBT_SKIP1_BLOCK;
class EFI_HII_GIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("SkipCount",   UINT8)
  ]

# 
# typedef struct _EFI_HII_GIBT_SKIP2_BLOCK {
#   EFI_HII_GLYPH_BLOCK    Header;
#   UINT16                 SkipCount;
# } EFI_HII_GIBT_SKIP2_BLOCK;
class EFI_HII_GIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_GLYPH_BLOCK),
    ("SkipCount",   UINT16)
  ]

# 
# //
# // Definitions for Device Path Package
# // Section 27.3.4
# //
# 
# ///
# /// The device path package is used to carry a device path
# /// associated with the package list.
# ///
# typedef struct _EFI_HII_DEVICE_PATH_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   // EFI_DEVICE_PATH_PROTOCOL DevicePath[];
# } EFI_HII_DEVICE_PATH_PACKAGE_HDR;
class EFI_HII_DEVICE_PATH_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_PACKAGE_HEADER)
    # ("DevicePath",  EFI_DEVICE_PATH_PROTOCOL * N)
  ]

# 
# //
# // Definitions for GUID Package
# // Section 27.3.5
# //
# 
# ///
# /// The GUID package is used to carry data where the format is defined by a GUID.
# ///
# typedef struct _EFI_HII_GUID_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   EFI_GUID                  Guid;
#   // Data per GUID definition may follow
# } EFI_HII_GUID_PACKAGE_HDR;
class EFI_HII_GUID_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_PACKAGE_HEADER),
    ("Guid",    EFI_GUID)
  ]

# 
# //
# // Definitions for String Package
# // Section 27.3.6
# //
# 
# #define UEFI_CONFIG_LANG    "x-UEFI"
# #define UEFI_CONFIG_LANG_2  "x-i-UEFI"
UEFI_CONFIG_LANG   = b"x-UEFI"
UEFI_CONFIG_LANG_2 = b"x-i-UEFI"

# 
# ///
# /// The fixed header consists of a standard record header and then the string identifiers
# /// contained in this section and the offsets of the string and language information.
# ///
# typedef struct _EFI_HII_STRING_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   UINT32                    HdrSize;
#   UINT32                    StringInfoOffset;
#   CHAR16                    LanguageWindow[16];
#   EFI_STRING_ID             LanguageName;
#   CHAR8                     Language[1];
# } EFI_HII_STRING_PACKAGE_HDR;
class EFI_HII_STRING_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("HdrSize",           UINT32),
    ("StringInfoOffset",  UINT32),
    ("LanguageWindow",    CHAR16 * 16),
    ("LanguageName",      EFI_STRING_ID),
    ("Language",          CHAR8 * 1)
  ]

# 
# typedef struct {
#   UINT8    BlockType;
# } EFI_HII_STRING_BLOCK;
class EFI_HII_STRING_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
  ]

# 
# //
# // Value of different string information block types
# //
# #define EFI_HII_SIBT_END                0x00
# #define EFI_HII_SIBT_STRING_SCSU        0x10
# #define EFI_HII_SIBT_STRING_SCSU_FONT   0x11
# #define EFI_HII_SIBT_STRINGS_SCSU       0x12
# #define EFI_HII_SIBT_STRINGS_SCSU_FONT  0x13
# #define EFI_HII_SIBT_STRING_UCS2        0x14
# #define EFI_HII_SIBT_STRING_UCS2_FONT   0x15
# #define EFI_HII_SIBT_STRINGS_UCS2       0x16
# #define EFI_HII_SIBT_STRINGS_UCS2_FONT  0x17
# #define EFI_HII_SIBT_DUPLICATE          0x20
# #define EFI_HII_SIBT_SKIP2              0x21
# #define EFI_HII_SIBT_SKIP1              0x22
# #define EFI_HII_SIBT_EXT1               0x30
# #define EFI_HII_SIBT_EXT2               0x31
# #define EFI_HII_SIBT_EXT4               0x32
# #define EFI_HII_SIBT_FONT               0x40
EFI_HII_SIBT_END                     = 0x00
EFI_HII_SIBT_STRING_SCSU             = 0x10
EFI_HII_SIBT_STRING_SCSU_FONT        = 0x11
EFI_HII_SIBT_STRINGS_SCSU            = 0x12
EFI_HII_SIBT_STRINGS_SCSU_FONT       = 0x13
EFI_HII_SIBT_STRING_UCS2             = 0x14
EFI_HII_SIBT_STRING_UCS2_FONT        = 0x15
EFI_HII_SIBT_STRINGS_UCS2            = 0x16
EFI_HII_SIBT_STRINGS_UCS2_FONT       = 0x17
EFI_HII_SIBT_DUPLICATE               = 0x20
EFI_HII_SIBT_SKIP2                   = 0x21
EFI_HII_SIBT_SKIP1                   = 0x22
EFI_HII_SIBT_EXT1                    = 0x30
EFI_HII_SIBT_EXT2                    = 0x31
EFI_HII_SIBT_EXT4                    = 0x32
EFI_HII_SIBT_FONT                    = 0x40

# 
# //
# // Definition of different string information block types
# //
# 
# typedef struct _EFI_HII_SIBT_DUPLICATE_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   EFI_STRING_ID           StringId;
# } EFI_HII_SIBT_DUPLICATE_BLOCK;
class EFI_HII_SIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("StringId",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_HII_SIBT_END_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
# } EFI_HII_SIBT_END_BLOCK;
class EFI_HII_SIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK)
  ]

# 
# typedef struct _EFI_HII_SIBT_EXT1_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   BlockType2;
#   UINT8                   Length;
# } EFI_HII_SIBT_EXT1_BLOCK;
class EFI_HII_SIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

# 
# typedef struct _EFI_HII_SIBT_EXT2_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   BlockType2;
#   UINT16                  Length;
# } EFI_HII_SIBT_EXT2_BLOCK;
class EFI_HII_SIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

# 
# typedef struct _EFI_HII_SIBT_EXT4_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   BlockType2;
#   UINT32                  Length;
# } EFI_HII_SIBT_EXT4_BLOCK;
class EFI_HII_SIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

# 
# typedef struct _EFI_HII_SIBT_FONT_BLOCK {
#   EFI_HII_SIBT_EXT2_BLOCK    Header;
#   UINT8                      FontId;
#   UINT16                     FontSize;
#   EFI_HII_FONT_STYLE         FontStyle;
#   CHAR16                     FontName[1];
# } EFI_HII_SIBT_FONT_BLOCK;
class EFI_HII_SIBT_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_SIBT_EXT2_BLOCK),
    ("FontId",    UINT8),
    ("FontSize",  UINT16),
    ("FontStyle", EFI_HII_FONT_STYLE),
    ("FontName",  CHAR16 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_SKIP1_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   SkipCount;
# } EFI_HII_SIBT_SKIP1_BLOCK;
class EFI_HII_SIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("SkipCount", UINT8)
  ]

# 
# typedef struct _EFI_HII_SIBT_SKIP2_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT16                  SkipCount;
# } EFI_HII_SIBT_SKIP2_BLOCK;
class EFI_HII_SIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_STRING_BLOCK),
    ("SkipCount", UINT16)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRING_SCSU_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   StringText[1];
# } EFI_HII_SIBT_STRING_SCSU_BLOCK;
class EFI_HII_SIBT_STRING_SCSU_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringText",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRING_SCSU_FONT_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   FontIdentifier;
#   UINT8                   StringText[1];
# } EFI_HII_SIBT_STRING_SCSU_FONT_BLOCK;
class EFI_HII_SIBT_STRING_SCSU_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringText",      UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRINGS_SCSU_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT16                  StringCount;
#   UINT8                   StringText[1];
# } EFI_HII_SIBT_STRINGS_SCSU_BLOCK;
class EFI_HII_SIBT_STRINGS_SCSU_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringCount", UINT16),
    ("StringText",  UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRINGS_SCSU_FONT_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   FontIdentifier;
#   UINT16                  StringCount;
#   UINT8                   StringText[1];
# } EFI_HII_SIBT_STRINGS_SCSU_FONT_BLOCK;
class EFI_HII_SIBT_STRINGS_SCSU_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringCount",     UINT16),
    ("StringText",      UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRING_UCS2_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   CHAR16                  StringText[1];
# } EFI_HII_SIBT_STRING_UCS2_BLOCK;
class EFI_HII_SIBT_STRING_UCS2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("StringText",      UINT16 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRING_UCS2_FONT_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   FontIdentifier;
#   CHAR16                  StringText[1];
# } EFI_HII_SIBT_STRING_UCS2_FONT_BLOCK;
class EFI_HII_SIBT_STRING_UCS2_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringText",      CHAR16 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRINGS_UCS2_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT16                  StringCount;
#   CHAR16                  StringText[1];
# } EFI_HII_SIBT_STRINGS_UCS2_BLOCK;
class EFI_HII_SIBT_STRINGS_UCS2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_STRING_BLOCK),
    ("StringCount", UINT16),
    ("StringText",  CHAR16 * 1)
  ]

# 
# typedef struct _EFI_HII_SIBT_STRINGS_UCS2_FONT_BLOCK {
#   EFI_HII_STRING_BLOCK    Header;
#   UINT8                   FontIdentifier;
#   UINT16                  StringCount;
#   CHAR16                  StringText[1];
# } EFI_HII_SIBT_STRINGS_UCS2_FONT_BLOCK;
class EFI_HII_SIBT_STRINGS_UCS2_FONT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_HII_STRING_BLOCK),
    ("FontIdentifier",  UINT8),
    ("StringCount",     UINT16),
    ("StringText",      CHAR16 * 1)
  ]

# 
# //
# // Definitions for Image Package
# // Section 27.3.7
# //
# 
# typedef struct _EFI_HII_IMAGE_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   UINT32                    ImageInfoOffset;
#   UINT32                    PaletteInfoOffset;
# } EFI_HII_IMAGE_PACKAGE_HDR;
class EFI_HII_IMAGE_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",            EFI_HII_PACKAGE_HEADER),
    ("ImageInfoOffset",   UINT32),
    ("PaletteInfoOffset", UINT32)
  ]

# 
# typedef struct _EFI_HII_IMAGE_BLOCK {
#   UINT8    BlockType;
# } EFI_HII_IMAGE_BLOCK;
class EFI_HII_IMAGE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType",  UINT8)
  ]

# 
# //
# // Value of different image information block types
# //
# #define EFI_HII_IIBT_END                0x00
# #define EFI_HII_IIBT_IMAGE_1BIT         0x10
# #define EFI_HII_IIBT_IMAGE_1BIT_TRANS   0x11
# #define EFI_HII_IIBT_IMAGE_4BIT         0x12
# #define EFI_HII_IIBT_IMAGE_4BIT_TRANS   0x13
# #define EFI_HII_IIBT_IMAGE_8BIT         0x14
# #define EFI_HII_IIBT_IMAGE_8BIT_TRANS   0x15
# #define EFI_HII_IIBT_IMAGE_24BIT        0x16
# #define EFI_HII_IIBT_IMAGE_24BIT_TRANS  0x17
# #define EFI_HII_IIBT_IMAGE_JPEG         0x18
# #define EFI_HII_IIBT_IMAGE_PNG          0x19
# #define EFI_HII_IIBT_DUPLICATE          0x20
# #define EFI_HII_IIBT_SKIP2              0x21
# #define EFI_HII_IIBT_SKIP1              0x22
# #define EFI_HII_IIBT_EXT1               0x30
# #define EFI_HII_IIBT_EXT2               0x31
# #define EFI_HII_IIBT_EXT4               0x32
EFI_HII_IIBT_END               = 0x00
EFI_HII_IIBT_IMAGE_1BIT        = 0x10
EFI_HII_IIBT_IMAGE_1BIT_TRANS  = 0x11
EFI_HII_IIBT_IMAGE_4BIT        = 0x12
EFI_HII_IIBT_IMAGE_4BIT_TRANS  = 0x13
EFI_HII_IIBT_IMAGE_8BIT        = 0x14
EFI_HII_IIBT_IMAGE_8BIT_TRANS  = 0x15
EFI_HII_IIBT_IMAGE_24BIT       = 0x16
EFI_HII_IIBT_IMAGE_24BIT_TRANS = 0x17
EFI_HII_IIBT_IMAGE_JPEG        = 0x18
EFI_HII_IIBT_DUPLICATE         = 0x20
EFI_HII_IIBT_SKIP2             = 0x21
EFI_HII_IIBT_SKIP1             = 0x22
EFI_HII_IIBT_EXT1              = 0x30
EFI_HII_IIBT_EXT2              = 0x31
EFI_HII_IIBT_EXT4              = 0x32

# 
# //
# // Definition of different image information block types
# //
# 
# typedef struct _EFI_HII_IIBT_END_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
# } EFI_HII_IIBT_END_BLOCK;
class EFI_HII_IIBT_END_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK)
  ]

# 
# typedef struct _EFI_HII_IIBT_EXT1_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT8                  Length;
# } EFI_HII_IIBT_EXT1_BLOCK;
class EFI_HII_IIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

# 
# typedef struct _EFI_HII_IIBT_EXT2_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT16                 Length;
# } EFI_HII_IIBT_EXT2_BLOCK;
class EFI_HII_IIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

# 
# typedef struct _EFI_HII_IIBT_EXT4_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT8                  BlockType2;
#   UINT32                 Length;
# } EFI_HII_IIBT_EXT4_BLOCK;
class EFI_HII_IIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_IMAGE_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_1BIT_BASE {
#   UINT16    Width;
#   UINT16    Height;
#   UINT8     Data[1];
# } EFI_HII_IIBT_IMAGE_1BIT_BASE;
class EFI_HII_IIBT_IMAGE_1BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_1BIT_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_1BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_1BIT_BLOCK;
class EFI_HII_IIBT_IMAGE_1BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_1BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_1BIT_TRANS_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_1BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_1BIT_TRANS_BLOCK;
class EFI_HII_IIBT_IMAGE_1BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_1BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_RGB_PIXEL {
#   UINT8    b;
#   UINT8    g;
#   UINT8    r;
# } EFI_HII_RGB_PIXEL;
class EFI_HII_RGB_PIXEL (Structure):
  _pack_   = 1
  _fields_ = [
    ("b", UINT8),
    ("g", UINT8),
    ("r", UINT8)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_24BIT_BASE {
#   UINT16               Width;
#   UINT16               Height;
#   EFI_HII_RGB_PIXEL    Bitmap[1];
# } EFI_HII_IIBT_IMAGE_24BIT_BASE;
class EFI_HII_IIBT_IMAGE_24BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Bitmap",  EFI_HII_RGB_PIXEL * 1)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_24BIT_BLOCK {
#   EFI_HII_IMAGE_BLOCK              Header;
#   EFI_HII_IIBT_IMAGE_24BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_24BIT_BLOCK;
class EFI_HII_IIBT_IMAGE_24BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Bitmap",  EFI_HII_IIBT_IMAGE_24BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_24BIT_TRANS_BLOCK {
#   EFI_HII_IMAGE_BLOCK              Header;
#   EFI_HII_IIBT_IMAGE_24BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_24BIT_TRANS_BLOCK;
class EFI_HII_IIBT_IMAGE_24BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Bitmap",  EFI_HII_IIBT_IMAGE_24BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_4BIT_BASE {
#   UINT16    Width;
#   UINT16    Height;
#   UINT8     Data[1];
# } EFI_HII_IIBT_IMAGE_4BIT_BASE;
class EFI_HII_IIBT_IMAGE_4BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_4BIT_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_4BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_4BIT_BLOCK;
class EFI_HII_IIBT_IMAGE_4BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_4BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_4BIT_TRANS_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_4BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_4BIT_TRANS_BLOCK;
class EFI_HII_IIBT_IMAGE_4BIT_TRANS_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_4BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_8BIT_BASE {
#   UINT16    Width;
#   UINT16    Height;
#   UINT8     Data[1];
# } EFI_HII_IIBT_IMAGE_8BIT_BASE;
class EFI_HII_IIBT_IMAGE_8BIT_BASE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Width",   UINT16),
    ("Height",  UINT16),
    ("Data",    UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_8BIT_PALETTE_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_8BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_8BIT_BLOCK;
class EFI_HII_IIBT_IMAGE_8BIT_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_8BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_IMAGE_8BIT_TRANS_BLOCK {
#   EFI_HII_IMAGE_BLOCK             Header;
#   UINT8                           PaletteIndex;
#   EFI_HII_IIBT_IMAGE_8BIT_BASE    Bitmap;
# } EFI_HII_IIBT_IMAGE_8BIT_TRAN_BLOCK;
class EFI_HII_IIBT_IMAGE_8BIT_TRAN_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_IMAGE_BLOCK),
    ("PaletteIndex",  UINT8),
    ("Bitmap",        EFI_HII_IIBT_IMAGE_8BIT_BASE)
  ]

# 
# typedef struct _EFI_HII_IIBT_DUPLICATE_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   EFI_IMAGE_ID           ImageId;
# } EFI_HII_IIBT_DUPLICATE_BLOCK;
class EFI_HII_IIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("ImageId", EFI_IMAGE_ID)
  ]

# 
# typedef struct _EFI_HII_IIBT_JPEG_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT32                 Size;
#   UINT8                  Data[1];
# } EFI_HII_IIBT_JPEG_BLOCK;
class EFI_HII_IIBT_JPEG_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_HII_IMAGE_BLOCK),
    ("Size",    UINT32),
    ("Data",    UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_IIBT_PNG_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT32                 Size;
#   UINT8                  Data[1];
# } EFI_HII_IIBT_PNG_BLOCK;
class EFI_HII_IIBT_PNG_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("Size",      UINT32),
    ("Data",      UINT8 * 1)
  ]

# 
# typedef struct _EFI_HII_IIBT_SKIP1_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT8                  SkipCount;
# } EFI_HII_IIBT_SKIP1_BLOCK;
class EFI_HII_IIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("SkipCount", UINT8)
  ]

# 
# typedef struct _EFI_HII_IIBT_SKIP2_BLOCK {
#   EFI_HII_IMAGE_BLOCK    Header;
#   UINT16                 SkipCount;
# } EFI_HII_IIBT_SKIP2_BLOCK;
class EFI_HII_IIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_HII_IMAGE_BLOCK),
    ("SkipCount", UINT16)
  ]

# 
# //
# // Definitions for Palette Information
# //
# 
# typedef struct _EFI_HII_IMAGE_PALETTE_INFO_HEADER {
#   UINT16    PaletteCount;
# } EFI_HII_IMAGE_PALETTE_INFO_HEADER;
class EFI_HII_IMAGE_PALETTE_INFO_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("PaletteCount",  UINT16)
  ]

# 
# typedef struct _EFI_HII_IMAGE_PALETTE_INFO {
#   UINT16               PaletteSize;
#   EFI_HII_RGB_PIXEL    PaletteValue[1];
# } EFI_HII_IMAGE_PALETTE_INFO;
class EFI_HII_IMAGE_PALETTE_INFO (Structure):
  _pack_   = 1
  _fields_ = [
    ("PaletteSize",   UINT16),
    ("PaletteValue",  EFI_HII_RGB_PIXEL * 1)
  ]

# 
# //
# // Definitions for Forms Package
# // Section 27.3.8
# //
# 
# ///
# /// The Form package is used to carry form-based encoding data.
# ///
# typedef struct _EFI_HII_FORM_PACKAGE_HDR {
#   EFI_HII_PACKAGE_HEADER    Header;
#   // EFI_IFR_OP_HEADER         OpCodeHeader;
#   // More op-codes follow
# } EFI_HII_FORM_PACKAGE_HDR;
class EFI_HII_FORM_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_HII_PACKAGE_HEADER)
    # ("OpCodeHeader",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct {
#   UINT8    Hour;
#   UINT8    Minute;
#   UINT8    Second;
# } EFI_HII_TIME;
class EFI_HII_TIME (Structure):
  _pack_   = 1
  _fields_ = [
    ("Hour",    UINT8),
    ("Minute",  UINT8),
    ("Second",  UINT8)
  ]

# 
# typedef struct {
#   UINT16    Year;
#   UINT8     Month;
#   UINT8     Day;
# } EFI_HII_DATE;
class EFI_HII_DATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Year",  UINT16),
    ("Month", UINT8),
    ("Day",   UINT8)
  ]

# 
# typedef struct {
#   EFI_QUESTION_ID    QuestionId;
#   EFI_FORM_ID        FormId;
#   EFI_GUID           FormSetGuid;
#   EFI_STRING_ID      DevicePath;
# } EFI_HII_REF;
class EFI_HII_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormId",      EFI_FORM_ID),
    ("FormSetGuid", EFI_GUID),
    ("DevicePath",  EFI_STRING_ID)
  ]

# 
# typedef union {
#   UINT8            u8;
#   UINT16           u16;
#   UINT32           u32;
#   UINT64           u64;
#   BOOLEAN          b;
#   EFI_HII_TIME     time;
#   EFI_HII_DATE     date;
#   EFI_STRING_ID    string; ///< EFI_IFR_TYPE_STRING, EFI_IFR_TYPE_ACTION
#   EFI_HII_REF      ref;    ///< EFI_IFR_TYPE_REF
#   // UINT8 buffer[];      ///< EFI_IFR_TYPE_BUFFER
# } EFI_IFR_TYPE_VALUE;
class EFI_IFR_TYPE_VALUE (Union):
  _pack_   = 1
  _fields_ = [
    ("u8",      UINT8),
    ("u16",     UINT16),
    ("u32",     UINT32),
    ("u64",     UINT64),
    ("b",       BOOLEAN),
    ("time",    EFI_HII_TIME),
    ("date",    EFI_HII_DATE),
    ("string",  EFI_STRING_ID),
    ("ref",     EFI_HII_REF),
    # ("buffer",  UINT8 * N)
  ]

# 
# //
# // IFR Opcodes
# //
# #define EFI_IFR_FORM_OP                 0x01
# #define EFI_IFR_SUBTITLE_OP             0x02
# #define EFI_IFR_TEXT_OP                 0x03
# #define EFI_IFR_IMAGE_OP                0x04
# #define EFI_IFR_ONE_OF_OP               0x05
# #define EFI_IFR_CHECKBOX_OP             0x06
# #define EFI_IFR_NUMERIC_OP              0x07
# #define EFI_IFR_PASSWORD_OP             0x08
# #define EFI_IFR_ONE_OF_OPTION_OP        0x09
# #define EFI_IFR_SUPPRESS_IF_OP          0x0A
# #define EFI_IFR_LOCKED_OP               0x0B
# #define EFI_IFR_ACTION_OP               0x0C
# #define EFI_IFR_RESET_BUTTON_OP         0x0D
# #define EFI_IFR_FORM_SET_OP             0x0E
# #define EFI_IFR_REF_OP                  0x0F
# #define EFI_IFR_NO_SUBMIT_IF_OP         0x10
# #define EFI_IFR_INCONSISTENT_IF_OP      0x11
# #define EFI_IFR_EQ_ID_VAL_OP            0x12
# #define EFI_IFR_EQ_ID_ID_OP             0x13
# #define EFI_IFR_EQ_ID_VAL_LIST_OP       0x14
# #define EFI_IFR_AND_OP                  0x15
# #define EFI_IFR_OR_OP                   0x16
# #define EFI_IFR_NOT_OP                  0x17
# #define EFI_IFR_RULE_OP                 0x18
# #define EFI_IFR_GRAY_OUT_IF_OP          0x19
# #define EFI_IFR_DATE_OP                 0x1A
# #define EFI_IFR_TIME_OP                 0x1B
# #define EFI_IFR_STRING_OP               0x1C
# #define EFI_IFR_REFRESH_OP              0x1D
# #define EFI_IFR_DISABLE_IF_OP           0x1E
# #define EFI_IFR_ANIMATION_OP            0x1F
# #define EFI_IFR_TO_LOWER_OP             0x20
# #define EFI_IFR_TO_UPPER_OP             0x21
# #define EFI_IFR_MAP_OP                  0x22
# #define EFI_IFR_ORDERED_LIST_OP         0x23
# #define EFI_IFR_VARSTORE_OP             0x24
# #define EFI_IFR_VARSTORE_NAME_VALUE_OP  0x25
# #define EFI_IFR_VARSTORE_EFI_OP         0x26
# #define EFI_IFR_VARSTORE_DEVICE_OP      0x27
# #define EFI_IFR_VERSION_OP              0x28
# #define EFI_IFR_END_OP                  0x29
# #define EFI_IFR_MATCH_OP                0x2A
# #define EFI_IFR_GET_OP                  0x2B
# #define EFI_IFR_SET_OP                  0x2C
# #define EFI_IFR_READ_OP                 0x2D
# #define EFI_IFR_WRITE_OP                0x2E
# #define EFI_IFR_EQUAL_OP                0x2F
# #define EFI_IFR_NOT_EQUAL_OP            0x30
# #define EFI_IFR_GREATER_THAN_OP         0x31
# #define EFI_IFR_GREATER_EQUAL_OP        0x32
# #define EFI_IFR_LESS_THAN_OP            0x33
# #define EFI_IFR_LESS_EQUAL_OP           0x34
# #define EFI_IFR_BITWISE_AND_OP          0x35
# #define EFI_IFR_BITWISE_OR_OP           0x36
# #define EFI_IFR_BITWISE_NOT_OP          0x37
# #define EFI_IFR_SHIFT_LEFT_OP           0x38
# #define EFI_IFR_SHIFT_RIGHT_OP          0x39
# #define EFI_IFR_ADD_OP                  0x3A
# #define EFI_IFR_SUBTRACT_OP             0x3B
# #define EFI_IFR_MULTIPLY_OP             0x3C
# #define EFI_IFR_DIVIDE_OP               0x3D
# #define EFI_IFR_MODULO_OP               0x3E
# #define EFI_IFR_RULE_REF_OP             0x3F
# #define EFI_IFR_QUESTION_REF1_OP        0x40
# #define EFI_IFR_QUESTION_REF2_OP        0x41
# #define EFI_IFR_UINT8_OP                0x42
# #define EFI_IFR_UINT16_OP               0x43
# #define EFI_IFR_UINT32_OP               0x44
# #define EFI_IFR_UINT64_OP               0x45
# #define EFI_IFR_TRUE_OP                 0x46
# #define EFI_IFR_FALSE_OP                0x47
# #define EFI_IFR_TO_UINT_OP              0x48
# #define EFI_IFR_TO_STRING_OP            0x49
# #define EFI_IFR_TO_BOOLEAN_OP           0x4A
# #define EFI_IFR_MID_OP                  0x4B
# #define EFI_IFR_FIND_OP                 0x4C
# #define EFI_IFR_TOKEN_OP                0x4D
# #define EFI_IFR_STRING_REF1_OP          0x4E
# #define EFI_IFR_STRING_REF2_OP          0x4F
# #define EFI_IFR_CONDITIONAL_OP          0x50
# #define EFI_IFR_QUESTION_REF3_OP        0x51
# #define EFI_IFR_ZERO_OP                 0x52
# #define EFI_IFR_ONE_OP                  0x53
# #define EFI_IFR_ONES_OP                 0x54
# #define EFI_IFR_UNDEFINED_OP            0x55
# #define EFI_IFR_LENGTH_OP               0x56
# #define EFI_IFR_DUP_OP                  0x57
# #define EFI_IFR_THIS_OP                 0x58
# #define EFI_IFR_SPAN_OP                 0x59
# #define EFI_IFR_VALUE_OP                0x5A
# #define EFI_IFR_DEFAULT_OP              0x5B
# #define EFI_IFR_DEFAULTSTORE_OP         0x5C
# #define EFI_IFR_FORM_MAP_OP             0x5D
# #define EFI_IFR_CATENATE_OP             0x5E
# #define EFI_IFR_GUID_OP                 0x5F
# #define EFI_IFR_SECURITY_OP             0x60
# #define EFI_IFR_MODAL_TAG_OP            0x61
# #define EFI_IFR_REFRESH_ID_OP           0x62
# #define EFI_IFR_WARNING_IF_OP           0x63
# #define EFI_IFR_MATCH2_OP               0x64
EFI_IFR_FORM_OP                = 0x01
EFI_IFR_SUBTITLE_OP            = 0x02
EFI_IFR_TEXT_OP                = 0x03
EFI_IFR_IMAGE_OP               = 0x04
EFI_IFR_ONE_OF_OP              = 0x05
EFI_IFR_CHECKBOX_OP            = 0x06
EFI_IFR_NUMERIC_OP             = 0x07
EFI_IFR_PASSWORD_OP            = 0x08
EFI_IFR_ONE_OF_OPTION_OP       = 0x09
EFI_IFR_SUPPRESS_IF_OP         = 0x0A
EFI_IFR_LOCKED_OP              = 0x0B
EFI_IFR_ACTION_OP              = 0x0C
EFI_IFR_RESET_BUTTON_OP        = 0x0D
EFI_IFR_FORM_SET_OP            = 0x0E
EFI_IFR_REF_OP                 = 0x0F
EFI_IFR_NO_SUBMIT_IF_OP        = 0x10
EFI_IFR_INCONSISTENT_IF_OP     = 0x11
EFI_IFR_EQ_ID_VAL_OP           = 0x12
EFI_IFR_EQ_ID_ID_OP            = 0x13
EFI_IFR_EQ_ID_VAL_LIST_OP      = 0x14
EFI_IFR_AND_OP                 = 0x15
EFI_IFR_OR_OP                  = 0x16
EFI_IFR_NOT_OP                 = 0x17
EFI_IFR_RULE_OP                = 0x18
EFI_IFR_GRAY_OUT_IF_OP         = 0x19
EFI_IFR_DATE_OP                = 0x1A
EFI_IFR_TIME_OP                = 0x1B
EFI_IFR_STRING_OP              = 0x1C
EFI_IFR_REFRESH_OP             = 0x1D
EFI_IFR_DISABLE_IF_OP          = 0x1E
EFI_IFR_ANIMATION_OP           = 0x1F
EFI_IFR_TO_LOWER_OP            = 0x20
EFI_IFR_TO_UPPER_OP            = 0x21
EFI_IFR_MAP_OP                 = 0x22
EFI_IFR_ORDERED_LIST_OP        = 0x23
EFI_IFR_VARSTORE_OP            = 0x24
EFI_IFR_VARSTORE_NAME_VALUE_OP = 0x25
EFI_IFR_VARSTORE_EFI_OP        = 0x26
EFI_IFR_VARSTORE_DEVICE_OP     = 0x27
EFI_IFR_VERSION_OP             = 0x28
EFI_IFR_END_OP                 = 0x29
EFI_IFR_MATCH_OP               = 0x2A
EFI_IFR_GET_OP                 = 0x2B
EFI_IFR_SET_OP                 = 0x2C
EFI_IFR_READ_OP                = 0x2D
EFI_IFR_WRITE_OP               = 0x2E
EFI_IFR_EQUAL_OP               = 0x2F
EFI_IFR_NOT_EQUAL_OP           = 0x30
EFI_IFR_GREATER_THAN_OP        = 0x31
EFI_IFR_GREATER_EQUAL_OP       = 0x32
EFI_IFR_LESS_THAN_OP           = 0x33
EFI_IFR_LESS_EQUAL_OP          = 0x34
EFI_IFR_BITWISE_AND_OP         = 0x35
EFI_IFR_BITWISE_OR_OP          = 0x36
EFI_IFR_BITWISE_NOT_OP         = 0x37
EFI_IFR_SHIFT_LEFT_OP          = 0x38
EFI_IFR_SHIFT_RIGHT_OP         = 0x39
EFI_IFR_ADD_OP                 = 0x3A
EFI_IFR_SUBTRACT_OP            = 0x3B
EFI_IFR_MULTIPLY_OP            = 0x3C
EFI_IFR_DIVIDE_OP              = 0x3D
EFI_IFR_MODULO_OP              = 0x3E
EFI_IFR_RULE_REF_OP            = 0x3F
EFI_IFR_QUESTION_REF1_OP       = 0x40
EFI_IFR_QUESTION_REF2_OP       = 0x41
EFI_IFR_UINT8_OP               = 0x42
EFI_IFR_UINT16_OP              = 0x43
EFI_IFR_UINT32_OP              = 0x44
EFI_IFR_UINT64_OP              = 0x45
EFI_IFR_TRUE_OP                = 0x46
EFI_IFR_FALSE_OP               = 0x47
EFI_IFR_TO_UINT_OP             = 0x48
EFI_IFR_TO_STRING_OP           = 0x49
EFI_IFR_TO_BOOLEAN_OP          = 0x4A
EFI_IFR_MID_OP                 = 0x4B
EFI_IFR_FIND_OP                = 0x4C
EFI_IFR_TOKEN_OP               = 0x4D
EFI_IFR_STRING_REF1_OP         = 0x4E
EFI_IFR_STRING_REF2_OP         = 0x4F
EFI_IFR_CONDITIONAL_OP         = 0x50
EFI_IFR_QUESTION_REF3_OP       = 0x51
EFI_IFR_ZERO_OP                = 0x52
EFI_IFR_ONE_OP                 = 0x53
EFI_IFR_ONES_OP                = 0x54
EFI_IFR_UNDEFINED_OP           = 0x55
EFI_IFR_LENGTH_OP              = 0x56
EFI_IFR_DUP_OP                 = 0x57
EFI_IFR_THIS_OP                = 0x58
EFI_IFR_SPAN_OP                = 0x59
EFI_IFR_VALUE_OP               = 0x5A
EFI_IFR_DEFAULT_OP             = 0x5B
EFI_IFR_DEFAULTSTORE_OP        = 0x5C
EFI_IFR_FORM_MAP_OP            = 0x5D
EFI_IFR_CATENATE_OP            = 0x5E
EFI_IFR_GUID_OP                = 0x5F
EFI_IFR_SECURITY_OP            = 0x60
EFI_IFR_MODAL_TAG_OP           = 0x61
EFI_IFR_REFRESH_ID_OP          = 0x62
EFI_IFR_WARNING_IF_OP          = 0x63
EFI_IFR_MATCH2_OP              = 0x64

# 
# //
# // Definitions of IFR Standard Headers
# // Section 27.3.8.2
# //
# 
# typedef struct _EFI_IFR_OP_HEADER {
#   UINT8    OpCode;
#   UINT8    Length : 7;
#   UINT8    Scope  : 1;
# } EFI_IFR_OP_HEADER;
class EFI_IFR_OP_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("OpCode",  UINT8),
    ("Length",  UINT8, 7),
    ("Scope",   UINT8, 1)
  ]

# 
# typedef struct _EFI_IFR_STATEMENT_HEADER {
#   EFI_STRING_ID    Prompt;
#   EFI_STRING_ID    Help;
# } EFI_IFR_STATEMENT_HEADER;
class EFI_IFR_STATEMENT_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Prompt",  EFI_STRING_ID),
    ("Help",    EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_QUESTION_HEADER {
#   EFI_IFR_STATEMENT_HEADER    Header;
#   EFI_QUESTION_ID             QuestionId;
#   EFI_VARSTORE_ID             VarStoreId;
#   union {
#     EFI_STRING_ID    VarName;
#     UINT16           VarOffset;
#   }                        VarStoreInfo;
#   UINT8                       Flags;
# } EFI_IFR_QUESTION_HEADER;
class EFI_IFR_QUESTION_HEADER_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_QUESTION_HEADER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_STATEMENT_HEADER),
    ("QuestionId",    EFI_QUESTION_ID),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_QUESTION_HEADER_VarStoreInfo),
    ("Flags",         UINT8)
  ]

# 
# //
# // Flag values of EFI_IFR_QUESTION_HEADER
# //
# #define EFI_IFR_FLAG_READ_ONLY           0x01
# #define EFI_IFR_FLAG_CALLBACK            0x04
# #define EFI_IFR_FLAG_RESET_REQUIRED      0x10
# #define EFI_IFR_FLAG_REST_STYLE          0x20
# #define EFI_IFR_FLAG_RECONNECT_REQUIRED  0x40
# #define EFI_IFR_FLAG_OPTIONS_ONLY        0x80
EFI_IFR_FLAG_READ_ONLY          = 0x01
EFI_IFR_FLAG_CALLBACK           = 0x04
EFI_IFR_FLAG_RESET_REQUIRED     = 0x10
EFI_IFR_FLAG_REST_STYLE         = 0x20
EFI_IFR_FLAG_RECONNECT_REQUIRED = 0x40
EFI_IFR_FLAG_OPTIONS_ONLY       = 0x80

# 
# //
# // Definition for Opcode Reference
# // Section 27.3.8.3
# //
# typedef struct _EFI_IFR_DEFAULTSTORE {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        DefaultName;
#   UINT16               DefaultId;
# } EFI_IFR_DEFAULTSTORE;
class EFI_IFR_DEFAULTSTORE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("DefaultName",   EFI_STRING_ID),
    ("DefaultId",     UINT16)
  ]

# 
# //
# // Default Identifier of default store
# //
# #define EFI_HII_DEFAULT_CLASS_STANDARD        0x0000
# #define EFI_HII_DEFAULT_CLASS_MANUFACTURING   0x0001
# #define EFI_HII_DEFAULT_CLASS_SAFE            0x0002
# #define EFI_HII_DEFAULT_CLASS_PLATFORM_BEGIN  0x4000
# #define EFI_HII_DEFAULT_CLASS_PLATFORM_END    0x7fff
# #define EFI_HII_DEFAULT_CLASS_HARDWARE_BEGIN  0x8000
# #define EFI_HII_DEFAULT_CLASS_HARDWARE_END    0xbfff
# #define EFI_HII_DEFAULT_CLASS_FIRMWARE_BEGIN  0xc000
# #define EFI_HII_DEFAULT_CLASS_FIRMWARE_END    0xffff
EFI_HII_DEFAULT_CLASS_STANDARD       = 0x0000
EFI_HII_DEFAULT_CLASS_MANUFACTURING  = 0x0001
EFI_HII_DEFAULT_CLASS_SAFE           = 0x0002
EFI_HII_DEFAULT_CLASS_PLATFORM_BEGIN = 0x4000
EFI_HII_DEFAULT_CLASS_PLATFORM_END   = 0x7fff
EFI_HII_DEFAULT_CLASS_HARDWARE_BEGIN = 0x8000
EFI_HII_DEFAULT_CLASS_HARDWARE_END   = 0xbfff
EFI_HII_DEFAULT_CLASS_FIRMWARE_BEGIN = 0xc000
EFI_HII_DEFAULT_CLASS_FIRMWARE_END   = 0xffff

# 
# typedef struct _EFI_IFR_VARSTORE {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_GUID             Guid;
#   EFI_VARSTORE_ID      VarStoreId;
#   UINT16               Size;
#   UINT8                Name[1];
# } EFI_IFR_VARSTORE;
class EFI_IFR_VARSTORE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Guid",        EFI_GUID),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Size",        UINT16),
    ("Name",        UINT8 * 1)
  ]

# 
# typedef struct _EFI_IFR_VARSTORE_EFI {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_VARSTORE_ID      VarStoreId;
#   EFI_GUID             Guid;
#   UINT32               Attributes;
#   UINT16               Size;
#   UINT8                Name[1];
# } EFI_IFR_VARSTORE_EFI;
class EFI_IFR_VARSTORE_EFI (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Guid",        EFI_GUID),
    ("Attributes",  UINT32),
    ("Size",        UINT16),
    ("Name",        UINT8 * 1)
  ]

# 
# typedef struct _EFI_IFR_VARSTORE_NAME_VALUE {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_VARSTORE_ID      VarStoreId;
#   EFI_GUID             Guid;
# } EFI_IFR_VARSTORE_NAME_VALUE;
class EFI_IFR_VARSTORE_NAME_VALUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("VarStoreId",  EFI_VARSTORE_ID),
    ("Guid",        EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_FORM_SET {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_GUID             Guid;
#   EFI_STRING_ID        FormSetTitle;
#   EFI_STRING_ID        Help;
#   UINT8                Flags;
#   // EFI_GUID              ClassGuid[];
# } EFI_IFR_FORM_SET;
class EFI_IFR_FORM_SET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("Guid",          EFI_GUID),
    ("FormSetTitle",  EFI_STRING_ID),
    ("Help",          EFI_STRING_ID),
    ("Flags",         UINT8)
    # ("ClassGuid",     EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_END {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_END;
class EFI_IFR_END (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_FORM {
#   EFI_IFR_OP_HEADER    Header;
#   UINT16               FormId;
#   EFI_STRING_ID        FormTitle;
# } EFI_IFR_FORM;
class EFI_IFR_FORM (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("FormId",    UINT16),
    ("FormTitle", EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_IMAGE {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_IMAGE_ID         Id;
# } EFI_IFR_IMAGE;
class EFI_IFR_IMAGE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Id",      EFI_IMAGE_ID)
  ]

# 
# typedef struct _EFI_IFR_MODAL_TAG {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MODAL_TAG;
class EFI_IFR_MODAL_TAG (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_LOCKED {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_LOCKED;
class EFI_IFR_LOCKED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_RULE {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                RuleId;
# } EFI_IFR_RULE;
class EFI_IFR_RULE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("RuleId",  UINT8)
  ]

# 
# typedef struct _EFI_IFR_DEFAULT {
#   EFI_IFR_OP_HEADER     Header;
#   UINT16                DefaultId;
#   UINT8                 Type;
#   EFI_IFR_TYPE_VALUE    Value;
# } EFI_IFR_DEFAULT;
class EFI_IFR_DEFAULT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("DefaultId", UINT16),
    ("Type",      UINT8),
    ("Value",     EFI_IFR_TYPE_VALUE)
  ]

# 
# typedef struct _EFI_IFR_DEFAULT_2 {
#   EFI_IFR_OP_HEADER    Header;
#   UINT16               DefaultId;
#   UINT8                Type;
# } EFI_IFR_DEFAULT_2;
class EFI_IFR_DEFAULT_2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("DefaultId", UINT16),
    ("Type",      UINT8)
  ]

# 
# typedef struct _EFI_IFR_VALUE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_VALUE;
class EFI_IFR_VALUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_SUBTITLE {
#   EFI_IFR_OP_HEADER           Header;
#   EFI_IFR_STATEMENT_HEADER    Statement;
#   UINT8                       Flags;
# } EFI_IFR_SUBTITLE;
class EFI_IFR_SUBTITLE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("Flags",     UINT8)
  ]

# 
# #define EFI_IFR_FLAGS_HORIZONTAL  0x01
EFI_IFR_FLAGS_HORIZONTAL       = 0x01

# 
# typedef struct _EFI_IFR_CHECKBOX {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      Flags;
# } EFI_IFR_CHECKBOX;
class EFI_IFR_CHECKBOX (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

# 
# #define EFI_IFR_CHECKBOX_DEFAULT      0x01
# #define EFI_IFR_CHECKBOX_DEFAULT_MFG  0x02
EFI_IFR_CHECKBOX_DEFAULT       = 0x01
EFI_IFR_CHECKBOX_DEFAULT_MFG   = 0x02

# 
# typedef struct _EFI_IFR_TEXT {
#   EFI_IFR_OP_HEADER           Header;
#   EFI_IFR_STATEMENT_HEADER    Statement;
#   EFI_STRING_ID               TextTwo;
# } EFI_IFR_TEXT;
class EFI_IFR_TEXT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("TextTwo",   EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_REF {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   EFI_FORM_ID                FormId;
# } EFI_IFR_REF;
class EFI_IFR_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("FormId",    EFI_FORM_ID)
  ]

# 
# typedef struct _EFI_IFR_REF2 {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   EFI_FORM_ID                FormId;
#   EFI_QUESTION_ID            QuestionId;
# } EFI_IFR_REF2;
class EFI_IFR_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID)
  ]

# 
# typedef struct _EFI_IFR_REF3 {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   EFI_FORM_ID                FormId;
#   EFI_QUESTION_ID            QuestionId;
#   EFI_GUID                   FormSetId;
# } EFI_IFR_REF3;
class EFI_IFR_REF3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormSetId",   EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_REF4 {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   EFI_FORM_ID                FormId;
#   EFI_QUESTION_ID            QuestionId;
#   EFI_GUID                   FormSetId;
#   EFI_STRING_ID              DevicePath;
# } EFI_IFR_REF4;
class EFI_IFR_REF4 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER),
    ("FormId",      EFI_FORM_ID),
    ("QuestionId",  EFI_QUESTION_ID),
    ("FormSetId",   EFI_GUID),
    ("DevicePath",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_REF5 {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
# } EFI_IFR_REF5;
class EFI_IFR_REF5 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Question",    EFI_IFR_QUESTION_HEADER)
  ]

# 
# typedef struct _EFI_IFR_RESET_BUTTON {
#   EFI_IFR_OP_HEADER           Header;
#   EFI_IFR_STATEMENT_HEADER    Statement;
#   EFI_DEFAULT_ID              DefaultId;
# } EFI_IFR_RESET_BUTTON;
class EFI_IFR_RESET_BUTTON (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Statement", EFI_IFR_STATEMENT_HEADER),
    ("DefaultId", EFI_DEFAULT_ID)
  ]

# 
# typedef struct _EFI_IFR_ACTION {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   EFI_STRING_ID              QuestionConfig;
# } EFI_IFR_ACTION;
class EFI_IFR_ACTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_IFR_OP_HEADER),
    ("Question",        EFI_IFR_QUESTION_HEADER),
    ("QuestionConfig",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_ACTION_1 {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
# } EFI_IFR_ACTION_1;
class EFI_IFR_ACTION_1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER)
  ]

# 
# typedef struct _EFI_IFR_DATE {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      Flags;
# } EFI_IFR_DATE;
class EFI_IFR_DATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

# 
# //
# // Flags that describe the behavior of the question.
# //
# #define EFI_QF_DATE_YEAR_SUPPRESS   0x01
# #define EFI_QF_DATE_MONTH_SUPPRESS  0x02
# #define EFI_QF_DATE_DAY_SUPPRESS    0x04
EFI_QF_DATE_YEAR_SUPPRESS      = 0x01
EFI_QF_DATE_MONTH_SUPPRESS     = 0x02
EFI_QF_DATE_DAY_SUPPRESS       = 0x04

# 
# #define EFI_QF_DATE_STORAGE         0x30
# #define     QF_DATE_STORAGE_NORMAL  0x00
# #define     QF_DATE_STORAGE_TIME    0x10
# #define     QF_DATE_STORAGE_WAKEUP  0x20
EFI_QF_DATE_STORAGE            = 0x30
QF_DATE_STORAGE_NORMAL     = 0x00
QF_DATE_STORAGE_TIME       = 0x10
QF_DATE_STORAGE_WAKEUP     = 0x20
    
# 
# typedef union {
#   struct {
#     UINT8    MinValue;
#     UINT8    MaxValue;
#     UINT8    Step;
#   } u8;
#   struct {
#     UINT16    MinValue;
#     UINT16    MaxValue;
#     UINT16    Step;
#   } u16;
#   struct {
#     UINT32    MinValue;
#     UINT32    MaxValue;
#     UINT32    Step;
#   } u32;
#   struct {
#     UINT64    MinValue;
#     UINT64    MaxValue;
#     UINT64    Step;
#   } u64;
# } MINMAXSTEP_DATA;
class MINMAXSTEP_DATA_u8 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT8),
    ("MaxValue",  UINT8),
    ("Step",      UINT8)
  ]

class MINMAXSTEP_DATA_u16 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT16),
    ("MaxValue",  UINT16),
    ("Step",      UINT16)
  ]

class MINMAXSTEP_DATA_u32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT32),
    ("MaxValue",  UINT32),
    ("Step",      UINT32)
  ]

class MINMAXSTEP_DATA_u64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("MinValue",  UINT64),
    ("MaxValue",  UINT64),
    ("Step",      UINT64)
  ]

class MINMAXSTEP_DATA (Union):
  _pack_   = 1
  _fields_ = [
    ("u8",  MINMAXSTEP_DATA_u8),
    ("u16", MINMAXSTEP_DATA_u16),
    ("u32", MINMAXSTEP_DATA_u32),
    ("u64", MINMAXSTEP_DATA_u64)
  ]

# 
# typedef struct _EFI_IFR_NUMERIC {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      Flags;
#   MINMAXSTEP_DATA            data;
# } EFI_IFR_NUMERIC;
class EFI_IFR_NUMERIC (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8),
    ("data",      MINMAXSTEP_DATA)
  ]

# 
# //
# // Flags related to the numeric question
# //
# #define EFI_IFR_NUMERIC_SIZE      0x03
# #define   EFI_IFR_NUMERIC_SIZE_1  0x00
# #define   EFI_IFR_NUMERIC_SIZE_2  0x01
# #define   EFI_IFR_NUMERIC_SIZE_4  0x02
# #define   EFI_IFR_NUMERIC_SIZE_8  0x03
EFI_IFR_NUMERIC_SIZE           = 0x03
EFI_IFR_NUMERIC_SIZE_1       = 0x00
EFI_IFR_NUMERIC_SIZE_2       = 0x01
EFI_IFR_NUMERIC_SIZE_4       = 0x02
EFI_IFR_NUMERIC_SIZE_8       = 0x03

# 
# #define EFI_IFR_DISPLAY             0x30
# #define   EFI_IFR_DISPLAY_INT_DEC   0x00
# #define   EFI_IFR_DISPLAY_UINT_DEC  0x10
# #define   EFI_IFR_DISPLAY_UINT_HEX  0x20
EFI_IFR_DISPLAY                = 0x30
EFI_IFR_DISPLAY_INT_DEC      = 0x00
EFI_IFR_DISPLAY_UINT_DEC     = 0x10
EFI_IFR_DISPLAY_UINT_HEX     = 0x20

# 
# typedef struct _EFI_IFR_ONE_OF {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      Flags;
#   MINMAXSTEP_DATA            data;
# } EFI_IFR_ONE_OF;
class EFI_IFR_ONE_OF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8),
    ("data",      MINMAXSTEP_DATA)
  ]

# 
# typedef struct _EFI_IFR_STRING {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      MinSize;
#   UINT8                      MaxSize;
#   UINT8                      Flags;
# } EFI_IFR_STRING;
class EFI_IFR_STRING (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("MinSize",   UINT8),
    ("MaxSize",   UINT8),
    ("Flags",     UINT8)
  ]

# 
# #define EFI_IFR_STRING_MULTI_LINE  0x01
EFI_IFR_STRING_MULTI_LINE      = 0x01

# 
# typedef struct _EFI_IFR_PASSWORD {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT16                     MinSize;
#   UINT16                     MaxSize;
# } EFI_IFR_PASSWORD;
class EFI_IFR_PASSWORD (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("MinSize",   UINT8),
    ("MaxSize",   UINT8)
  ]

# 
# typedef struct _EFI_IFR_ORDERED_LIST {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      MaxContainers;
#   UINT8                      Flags;
# } EFI_IFR_ORDERED_LIST;
class EFI_IFR_ORDERED_LIST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("Question",      EFI_IFR_QUESTION_HEADER),
    ("MaxContainers", UINT8),
    ("Flags",         UINT8)
  ]

# 
# #define EFI_IFR_UNIQUE_SET    0x01
# #define EFI_IFR_NO_EMPTY_SET  0x02
EFI_IFR_UNIQUE_SET             = 0x01
EFI_IFR_NO_EMPTY_SET           = 0x02

# 
# typedef struct _EFI_IFR_TIME {
#   EFI_IFR_OP_HEADER          Header;
#   EFI_IFR_QUESTION_HEADER    Question;
#   UINT8                      Flags;
# } EFI_IFR_TIME;
class EFI_IFR_TIME (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Question",  EFI_IFR_QUESTION_HEADER),
    ("Flags",     UINT8)
  ]

# 
# //
# // A bit-mask that determines which unique settings are active for this opcode.
# //
# #define QF_TIME_HOUR_SUPPRESS    0x01
# #define QF_TIME_MINUTE_SUPPRESS  0x02
# #define QF_TIME_SECOND_SUPPRESS  0x04
QF_TIME_HOUR_SUPPRESS          = 0x01
QF_TIME_MINUTE_SUPPRESS        = 0x02
QF_TIME_SECOND_SUPPRESS        = 0x04

# 
# #define QF_TIME_STORAGE           0x30
# #define   QF_TIME_STORAGE_NORMAL  0x00
# #define   QF_TIME_STORAGE_TIME    0x10
# #define   QF_TIME_STORAGE_WAKEUP  0x20
QF_TIME_STORAGE                = 0x30
QF_TIME_STORAGE_NORMAL       = 0x00
QF_TIME_STORAGE_TIME         = 0x10
QF_TIME_STORAGE_WAKEUP       = 0x20

# 
# typedef struct _EFI_IFR_DISABLE_IF {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_DISABLE_IF;
class EFI_IFR_DISABLE_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_SUPPRESS_IF {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_SUPPRESS_IF;
class EFI_IFR_SUPPRESS_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_GRAY_OUT_IF {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_GRAY_OUT_IF;
class EFI_IFR_GRAY_OUT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_INCONSISTENT_IF {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        Error;
# } EFI_IFR_INCONSISTENT_IF;
class EFI_IFR_INCONSISTENT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Error",   EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_NO_SUBMIT_IF {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        Error;
# } EFI_IFR_NO_SUBMIT_IF;
class EFI_IFR_NO_SUBMIT_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Error",   EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_WARNING_IF {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        Warning;
#   UINT8                TimeOut;
# } EFI_IFR_WARNING_IF;
class EFI_IFR_WARNING_IF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Warning", EFI_STRING_ID),
    ("TimeOut", UINT8)
  ]

# 
# typedef struct _EFI_IFR_REFRESH {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                RefreshInterval;
# } EFI_IFR_REFRESH;
class EFI_IFR_REFRESH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",          EFI_IFR_OP_HEADER),
    ("RefreshInterval", UINT8)
  ]

# 
# typedef struct _EFI_IFR_VARSTORE_DEVICE {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        DevicePath;
# } EFI_IFR_VARSTORE_DEVICE;
class EFI_IFR_VARSTORE_DEVICE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_ONE_OF_OPTION {
#   EFI_IFR_OP_HEADER     Header;
#   EFI_STRING_ID         Option;
#   UINT8                 Flags;
#   UINT8                 Type;
#   EFI_IFR_TYPE_VALUE    Value;
# } EFI_IFR_ONE_OF_OPTION;
class EFI_IFR_ONE_OF_OPTION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Option",  EFI_STRING_ID),
    ("Flags",   UINT8),
    ("Type",    UINT8),
    ("Value",   EFI_IFR_TYPE_VALUE)
  ]

# 
# //
# // Types of the option's value.
# //
# #define EFI_IFR_TYPE_NUM_SIZE_8   0x00
# #define EFI_IFR_TYPE_NUM_SIZE_16  0x01
# #define EFI_IFR_TYPE_NUM_SIZE_32  0x02
# #define EFI_IFR_TYPE_NUM_SIZE_64  0x03
# #define EFI_IFR_TYPE_BOOLEAN      0x04
# #define EFI_IFR_TYPE_TIME         0x05
# #define EFI_IFR_TYPE_DATE         0x06
# #define EFI_IFR_TYPE_STRING       0x07
# #define EFI_IFR_TYPE_OTHER        0x08
# #define EFI_IFR_TYPE_UNDEFINED    0x09
# #define EFI_IFR_TYPE_ACTION       0x0A
# #define EFI_IFR_TYPE_BUFFER       0x0B
# #define EFI_IFR_TYPE_REF          0x0C
EFI_IFR_TYPE_NUM_SIZE_8        = 0x00
EFI_IFR_TYPE_NUM_SIZE_16       = 0x01
EFI_IFR_TYPE_NUM_SIZE_32       = 0x02
EFI_IFR_TYPE_NUM_SIZE_64       = 0x03
EFI_IFR_TYPE_BOOLEAN           = 0x04
EFI_IFR_TYPE_TIME              = 0x05
EFI_IFR_TYPE_DATE              = 0x06
EFI_IFR_TYPE_STRING            = 0x07
EFI_IFR_TYPE_OTHER             = 0x08
EFI_IFR_TYPE_UNDEFINED         = 0x09
EFI_IFR_TYPE_ACTION            = 0x0A
EFI_IFR_TYPE_BUFFER            = 0x0B
EFI_IFR_TYPE_REF               = 0x0C

# 
# #define EFI_IFR_OPTION_DEFAULT      0x10
# #define EFI_IFR_OPTION_DEFAULT_MFG  0x20
EFI_IFR_OPTION_DEFAULT         = 0x10
EFI_IFR_OPTION_DEFAULT_MFG     = 0x20

# 
# typedef struct _EFI_IFR_GUID {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_GUID             Guid;
#   // Optional Data Follows
# } EFI_IFR_GUID;
class EFI_IFR_GUID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Guid",    EFI_GUID)
    # Optional Data Follows
  ]

# 
# typedef struct _EFI_IFR_REFRESH_ID {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_GUID             RefreshEventGroupId;
# } EFI_IFR_REFRESH_ID;
class EFI_IFR_REFRESH_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_IFR_OP_HEADER),
    ("RefreshEventGroupId", EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_DUP {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_DUP;
class EFI_IFR_DUP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_EQ_ID_ID {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_QUESTION_ID      QuestionId1;
#   EFI_QUESTION_ID      QuestionId2;
# } EFI_IFR_EQ_ID_ID;
class EFI_IFR_EQ_ID_ID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId1", EFI_QUESTION_ID),
    ("QuestionId2", EFI_QUESTION_ID)
  ]

# 
# typedef struct _EFI_IFR_EQ_ID_VAL {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_QUESTION_ID      QuestionId;
#   UINT16               Value;
# } EFI_IFR_EQ_ID_VAL;
class EFI_IFR_EQ_ID_VAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID),
    ("Value",       UINT16)
  ]

# 
# typedef struct _EFI_IFR_EQ_ID_VAL_LIST {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_QUESTION_ID      QuestionId;
#   UINT16               ListLength;
#   UINT16               ValueList[1];
# } EFI_IFR_EQ_ID_VAL_LIST;
class EFI_IFR_EQ_ID_VAL_LIST (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID),
    ("ListLength",  UINT16),
    ("ValueList",   UINT16 * 1)
  ]

# 
# typedef struct _EFI_IFR_UINT8 {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                Value;
# } EFI_IFR_UINT8;
class EFI_IFR_UINT8 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT8)
  ]

# 
# typedef struct _EFI_IFR_UINT16 {
#   EFI_IFR_OP_HEADER    Header;
#   UINT16               Value;
# } EFI_IFR_UINT16;
class EFI_IFR_UINT16 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT16)
  ]

# 
# typedef struct _EFI_IFR_UINT32 {
#   EFI_IFR_OP_HEADER    Header;
#   UINT32               Value;
# } EFI_IFR_UINT32;
class EFI_IFR_UINT32 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT32)
  ]

# 
# typedef struct _EFI_IFR_UINT64 {
#   EFI_IFR_OP_HEADER    Header;
#   UINT64               Value;
# } EFI_IFR_UINT64;
class EFI_IFR_UINT64 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Value",   UINT64)
  ]

# 
# typedef struct _EFI_IFR_QUESTION_REF1 {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_QUESTION_ID      QuestionId;
# } EFI_IFR_QUESTION_REF1;
class EFI_IFR_QUESTION_REF1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("QuestionId",  EFI_QUESTION_ID)
  ]

# typedef struct _EFI_IFR_QUESTION_REF2 {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_QUESTION_REF2;
class EFI_IFR_QUESTION_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_QUESTION_REF3 {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_QUESTION_REF3;
class EFI_IFR_QUESTION_REF3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_QUESTION_REF3_2 {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        DevicePath;
# } EFI_IFR_QUESTION_REF3_2;
class EFI_IFR_QUESTION_REF3_2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_QUESTION_REF3_3 {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        DevicePath;
#   EFI_GUID             Guid;
# } EFI_IFR_QUESTION_REF3_3;
class EFI_IFR_QUESTION_REF3_3 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("DevicePath",  EFI_STRING_ID),
    ("Guid",        EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_RULE_REF {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                RuleId;
# } EFI_IFR_RULE_REF;
class EFI_IFR_RULE_REF (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("RuleId",  UINT8)
  ]

# 
# typedef struct _EFI_IFR_STRING_REF1 {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_STRING_ID        StringId;
# } EFI_IFR_STRING_REF1;
class EFI_IFR_STRING_REF1 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("StringId",  EFI_STRING_ID)
  ]

# 
# typedef struct _EFI_IFR_STRING_REF2 {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_STRING_REF2;
class EFI_IFR_STRING_REF2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_THIS {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_THIS;
class EFI_IFR_THIS (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_TRUE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TRUE;
class EFI_IFR_TRUE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_FALSE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_FALSE;
class EFI_IFR_FALSE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_ONE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_ONE;
class EFI_IFR_ONE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_ONES {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_ONES;
class EFI_IFR_ONES (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_ZERO {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_ZERO;
class EFI_IFR_ZERO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_UNDEFINED {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_UNDEFINED;
class EFI_IFR_UNDEFINED (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_VERSION {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_VERSION;
class EFI_IFR_VERSION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_LENGTH {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_LENGTH;
class EFI_IFR_LENGTH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_NOT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_NOT;
class EFI_IFR_NOT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_BITWISE_NOT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_BITWISE_NOT;
class EFI_IFR_BITWISE_NOT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_TO_BOOLEAN {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TO_BOOLEAN;
class EFI_IFR_TO_BOOLEAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# ///
# /// For EFI_IFR_TO_STRING, when converting from
# /// unsigned integers, these flags control the format:
# /// 0 = unsigned decimal.
# /// 1 = signed decimal.
# /// 2 = hexadecimal (lower-case alpha).
# /// 3 = hexadecimal (upper-case alpha).
# ///@{
# #define EFI_IFR_STRING_UNSIGNED_DEC   0
# #define EFI_IFR_STRING_SIGNED_DEC     1
# #define EFI_IFR_STRING_LOWERCASE_HEX  2
# #define EFI_IFR_STRING_UPPERCASE_HEX  3
EFI_IFR_STRING_UNSIGNED_DEC      = 0
EFI_IFR_STRING_SIGNED_DEC        = 1
EFI_IFR_STRING_LOWERCASE_HEX     = 2
EFI_IFR_STRING_UPPERCASE_HEX     = 3

# ///@}
# 
# ///
# /// When converting from a buffer, these flags control the format:
# /// 0 = ASCII.
# /// 8 = Unicode.
# ///@{
# #define EFI_IFR_STRING_ASCII    0
# #define EFI_IFR_STRING_UNICODE  8
EFI_IFR_STRING_ASCII             = 0
EFI_IFR_STRING_UNICODE           = 8

# ///@}
# 
# typedef struct _EFI_IFR_TO_STRING {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                Format;
# } EFI_IFR_TO_STRING;
class EFI_IFR_TO_STRING (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Format",    UINT8)
  ]

# 
# typedef struct _EFI_IFR_TO_UINT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TO_UINT;
class EFI_IFR_TO_UINT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_TO_UPPER {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TO_UPPER;
class EFI_IFR_TO_UPPER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_TO_LOWER {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TO_LOWER;
class EFI_IFR_TO_LOWER (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_ADD {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_ADD;
class EFI_IFR_ADD (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_AND {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_AND;
class EFI_IFR_AND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_BITWISE_AND {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_BITWISE_AND;
class EFI_IFR_BITWISE_AND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_BITWISE_OR {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_BITWISE_OR;
class EFI_IFR_BITWISE_OR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_CATENATE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_CATENATE;
class EFI_IFR_CATENATE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_DIVIDE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_DIVIDE;
class EFI_IFR_DIVIDE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_EQUAL {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_EQUAL;
class EFI_IFR_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_GREATER_EQUAL {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_GREATER_EQUAL;
class EFI_IFR_GREATER_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_GREATER_THAN {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_GREATER_THAN;
class EFI_IFR_GREATER_THAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_LESS_EQUAL {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_LESS_EQUAL;
class EFI_IFR_LESS_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_LESS_THAN {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_LESS_THAN;
class EFI_IFR_LESS_THAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_MATCH {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MATCH;
class EFI_IFR_MATCH (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_MATCH2 {
#   EFI_IFR_OP_HEADER    Header;
#   EFI_GUID             SyntaxType;
# } EFI_IFR_MATCH2;
class EFI_IFR_MATCH2 (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("SyntaxType",  EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_MULTIPLY {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MULTIPLY;
class EFI_IFR_MULTIPLY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_MODULO {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MODULO;
class EFI_IFR_MODULO (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_NOT_EQUAL {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_NOT_EQUAL;
class EFI_IFR_NOT_EQUAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_OR {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_OR;
class EFI_IFR_OR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_SHIFT_LEFT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_SHIFT_LEFT;
class EFI_IFR_SHIFT_LEFT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_SHIFT_RIGHT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_SHIFT_RIGHT;
class EFI_IFR_SHIFT_RIGHT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_SUBTRACT {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_SUBTRACT;
class EFI_IFR_SUBTRACT (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_CONDITIONAL {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_CONDITIONAL;
class EFI_IFR_CONDITIONAL (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# //
# // Flags governing the matching criteria of EFI_IFR_FIND
# //
# #define EFI_IFR_FF_CASE_SENSITIVE    0x00
# #define EFI_IFR_FF_CASE_INSENSITIVE  0x01
EFI_IFR_FF_CASE_SENSITIVE    = 0x00
EFI_IFR_FF_CASE_INSENSITIVE  = 0x01

# 
# typedef struct _EFI_IFR_FIND {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                Format;
# } EFI_IFR_FIND;
class EFI_IFR_FIND (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER),
    ("Format",    UINT8)
  ]

# 
# typedef struct _EFI_IFR_MID {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MID;
class EFI_IFR_MID (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_TOKEN {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_TOKEN;
class EFI_IFR_TOKEN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# //
# // Flags specifying whether to find the first matching string
# // or the first non-matching string.
# //
# #define EFI_IFR_FLAGS_FIRST_MATCHING      0x00
# #define EFI_IFR_FLAGS_FIRST_NON_MATCHING  0x01
EFI_IFR_FLAGS_FIRST_MATCHING     = 0x00
EFI_IFR_FLAGS_FIRST_NON_MATCHING = 0x01

# 
# typedef struct _EFI_IFR_SPAN {
#   EFI_IFR_OP_HEADER    Header;
#   UINT8                Flags;
# } EFI_IFR_SPAN;
class EFI_IFR_SPAN (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Flags",   UINT8)
  ]

# 
# typedef struct _EFI_IFR_SECURITY {
#   ///
#   /// Standard opcode header, where Header.Op = EFI_IFR_SECURITY_OP.
#   ///
#   EFI_IFR_OP_HEADER    Header;
#   ///
#   /// Security permission level.
#   ///
#   EFI_GUID             Permissions;
# } EFI_IFR_SECURITY;
class EFI_IFR_SECURITY (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_IFR_OP_HEADER),
    ("Permissions", EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_FORM_MAP_METHOD {
#   ///
#   /// The string identifier which provides the human-readable name of
#   /// the configuration method for this standards map form.
#   ///
#   EFI_STRING_ID    MethodTitle;
#   ///
#   /// Identifier which uniquely specifies the configuration methods
#   /// associated with this standards map form.
#   ///
#   EFI_GUID         MethodIdentifier;
# } EFI_IFR_FORM_MAP_METHOD;
class EFI_IFR_FORM_MAP_METHOD (Structure):
  _pack_   = 1
  _fields_ = [
    ("MethodTitle",       EFI_STRING_ID),
    ("MethodIdentifier",  EFI_GUID)
  ]

# 
# typedef struct _EFI_IFR_FORM_MAP {
#   ///
#   /// The sequence that defines the type of opcode as well as the length
#   /// of the opcode being defined. Header.OpCode = EFI_IFR_FORM_MAP_OP.
#   ///
#   EFI_IFR_OP_HEADER    Header;
#   ///
#   /// The unique identifier for this particular form.
#   ///
#   EFI_FORM_ID          FormId;
#   ///
#   /// One or more configuration method's name and unique identifier.
#   ///
#   // EFI_IFR_FORM_MAP_METHOD  Methods[];
# } EFI_IFR_FORM_MAP;
class EFI_IFR_FORM_MAP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("FormId",  EFI_FORM_ID)
    # ("Methods", EFI_IFR_FORM_MAP_METHOD * N)
  ]

# 
# typedef struct _EFI_IFR_SET {
#   ///
#   /// The sequence that defines the type of opcode as well as the length
#   /// of the opcode being defined. Header.OpCode = EFI_IFR_SET_OP.
#   ///
#   EFI_IFR_OP_HEADER    Header;
#   ///
#   /// Specifies the identifier of a previously declared variable store to
#   /// use when storing the question's value.
#   ///
#   EFI_VARSTORE_ID      VarStoreId;
#   union {
#     ///
#     /// A 16-bit Buffer Storage offset.
#     ///
#     EFI_STRING_ID    VarName;
#     ///
#     /// A Name Value or EFI Variable name (VarName).
#     ///
#     UINT16           VarOffset;
#   }                  VarStoreInfo;
#   ///
#   /// Specifies the type used for storage.
#   ///
#   UINT8    VarStoreType;
# } EFI_IFR_SET;
class EFI_IFR_SET_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_SET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_SET_VarStoreInfo),
    ("VarStoreType",  UINT8)
  ]

# 
# typedef struct _EFI_IFR_GET {
#   ///
#   /// The sequence that defines the type of opcode as well as the length
#   /// of the opcode being defined. Header.OpCode = EFI_IFR_GET_OP.
#   ///
#   EFI_IFR_OP_HEADER    Header;
#   ///
#   /// Specifies the identifier of a previously declared variable store to
#   /// use when retrieving the value.
#   ///
#   EFI_VARSTORE_ID      VarStoreId;
#   union {
#     ///
#     /// A 16-bit Buffer Storage offset.
#     ///
#     EFI_STRING_ID    VarName;
#     ///
#     /// A Name Value or EFI Variable name (VarName).
#     ///
#     UINT16           VarOffset;
#   }                  VarStoreInfo;
#   ///
#   /// Specifies the type used for storage.
#   ///
#   UINT8    VarStoreType;
# } EFI_IFR_GET;
class EFI_IFR_GET_VarStoreInfo (Union):
  _pack_   = 1
  _fields_ = [
    ("VarName",   EFI_STRING_ID),
    ("VarOffset", UINT16)
  ]

class EFI_IFR_GET (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",        EFI_IFR_OP_HEADER),
    ("VarStoreId",    EFI_VARSTORE_ID),
    ("VarStoreInfo",  EFI_IFR_GET_VarStoreInfo),
    ("VarStoreType",  UINT8)
  ]

# 
# typedef struct _EFI_IFR_READ {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_READ;
class EFI_IFR_READ (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_WRITE {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_WRITE;
class EFI_IFR_WRITE (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# 
# typedef struct _EFI_IFR_MAP {
#   EFI_IFR_OP_HEADER    Header;
# } EFI_IFR_MAP;
class EFI_IFR_MAP (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",    EFI_IFR_OP_HEADER)
  ]

# //
# // Definitions for Keyboard Package
# // Releated definitions are in Section of EFI_HII_DATABASE_PROTOCOL
# //
# 
# ///
# /// Each enumeration values maps a physical key on a keyboard.
# ///
# typedef enum {
#   EfiKeyLCtrl,
#   EfiKeyA0,
#   EfiKeyLAlt,
#   EfiKeySpaceBar,
#   EfiKeyA2,
#   EfiKeyA3,
#   EfiKeyA4,
#   EfiKeyRCtrl,
#   EfiKeyLeftArrow,
#   EfiKeyDownArrow,
#   EfiKeyRightArrow,
#   EfiKeyZero,
#   EfiKeyPeriod,
#   EfiKeyEnter,
#   EfiKeyLShift,
#   EfiKeyB0,
#   EfiKeyB1,
#   EfiKeyB2,
#   EfiKeyB3,
#   EfiKeyB4,
#   EfiKeyB5,
#   EfiKeyB6,
#   EfiKeyB7,
#   EfiKeyB8,
#   EfiKeyB9,
#   EfiKeyB10,
#   EfiKeyRShift,
#   EfiKeyUpArrow,
#   EfiKeyOne,
#   EfiKeyTwo,
#   EfiKeyThree,
#   EfiKeyCapsLock,
#   EfiKeyC1,
#   EfiKeyC2,
#   EfiKeyC3,
#   EfiKeyC4,
#   EfiKeyC5,
#   EfiKeyC6,
#   EfiKeyC7,
#   EfiKeyC8,
#   EfiKeyC9,
#   EfiKeyC10,
#   EfiKeyC11,
#   EfiKeyC12,
#   EfiKeyFour,
#   EfiKeyFive,
#   EfiKeySix,
#   EfiKeyPlus,
#   EfiKeyTab,
#   EfiKeyD1,
#   EfiKeyD2,
#   EfiKeyD3,
#   EfiKeyD4,
#   EfiKeyD5,
#   EfiKeyD6,
#   EfiKeyD7,
#   EfiKeyD8,
#   EfiKeyD9,
#   EfiKeyD10,
#   EfiKeyD11,
#   EfiKeyD12,
#   EfiKeyD13,
#   EfiKeyDel,
#   EfiKeyEnd,
#   EfiKeyPgDn,
#   EfiKeySeven,
#   EfiKeyEight,
#   EfiKeyNine,
#   EfiKeyE0,
#   EfiKeyE1,
#   EfiKeyE2,
#   EfiKeyE3,
#   EfiKeyE4,
#   EfiKeyE5,
#   EfiKeyE6,
#   EfiKeyE7,
#   EfiKeyE8,
#   EfiKeyE9,
#   EfiKeyE10,
#   EfiKeyE11,
#   EfiKeyE12,
#   EfiKeyBackSpace,
#   EfiKeyIns,
#   EfiKeyHome,
#   EfiKeyPgUp,
#   EfiKeyNLck,
#   EfiKeySlash,
#   EfiKeyAsterisk,
#   EfiKeyMinus,
#   EfiKeyEsc,
#   EfiKeyF1,
#   EfiKeyF2,
#   EfiKeyF3,
#   EfiKeyF4,
#   EfiKeyF5,
#   EfiKeyF6,
#   EfiKeyF7,
#   EfiKeyF8,
#   EfiKeyF9,
#   EfiKeyF10,
#   EfiKeyF11,
#   EfiKeyF12,
#   EfiKeyPrint,
#   EfiKeySLck,
#   EfiKeyPause
# } EFI_KEY;
EfiKeyLCtrl       =   0
EfiKeyA0          =   1
EfiKeyLAlt        =   2
EfiKeySpaceBar    =   3
EfiKeyA2          =   4
EfiKeyA3          =   5
EfiKeyA4          =   6
EfiKeyRCtrl       =   7
EfiKeyLeftArrow   =   8
EfiKeyDownArrow   =   9
EfiKeyRightArrow  =  10
EfiKeyZero        =  11
EfiKeyPeriod      =  12
EfiKeyEnter       =  13
EfiKeyLShift      =  14
EfiKeyB0          =  15
EfiKeyB1          =  16
EfiKeyB2          =  17
EfiKeyB3          =  18
EfiKeyB4          =  19
EfiKeyB5          =  20
EfiKeyB6          =  21
EfiKeyB7          =  22
EfiKeyB8          =  23
EfiKeyB9          =  24
EfiKeyB10         =  25
EfiKeyRShift      =  26
EfiKeyUpArrow     =  27
EfiKeyOne         =  28
EfiKeyTwo         =  29
EfiKeyThree       =  30
EfiKeyCapsLock    =  31
EfiKeyC1          =  32
EfiKeyC2          =  33
EfiKeyC3          =  34
EfiKeyC4          =  35
EfiKeyC5          =  36
EfiKeyC6          =  37
EfiKeyC7          =  38
EfiKeyC8          =  39
EfiKeyC9          =  40
EfiKeyC10         =  41
EfiKeyC11         =  42
EfiKeyC12         =  43
EfiKeyFour        =  44
EfiKeyFive        =  45
EfiKeySix         =  46
EfiKeyPlus        =  47
EfiKeyTab         =  48
EfiKeyD1          =  49
EfiKeyD2          =  50
EfiKeyD3          =  51
EfiKeyD4          =  52
EfiKeyD5          =  53
EfiKeyD6          =  54
EfiKeyD7          =  55
EfiKeyD8          =  56
EfiKeyD9          =  57
EfiKeyD10         =  58
EfiKeyD11         =  59
EfiKeyD12         =  60
EfiKeyD13         =  61
EfiKeyDel         =  62
EfiKeyEnd         =  63
EfiKeyPgDn        =  64
EfiKeySeven       =  65
EfiKeyEight       =  66
EfiKeyNine        =  67
EfiKeyE0          =  68
EfiKeyE1          =  69
EfiKeyE2          =  70
EfiKeyE3          =  71
EfiKeyE4          =  72
EfiKeyE5          =  73
EfiKeyE6          =  74
EfiKeyE7          =  75
EfiKeyE8          =  76
EfiKeyE9          =  77
EfiKeyE10         =  78
EfiKeyE11         =  79
EfiKeyE12         =  80
EfiKeyBackSpace   =  81
EfiKeyIns         =  82
EfiKeyHome        =  83
EfiKeyPgUp        =  84
EfiKeyNLck        =  85
EfiKeySlash       =  86
EfiKeyAsterisk    =  87
EfiKeyMinus       =  88
EfiKeyEsc         =  89
EfiKeyF1          =  90
EfiKeyF2          =  91
EfiKeyF3          =  92
EfiKeyF4          =  93
EfiKeyF5          =  94
EfiKeyF6          =  95
EfiKeyF7          =  96
EfiKeyF8          =  97
EfiKeyF9          =  98
EfiKeyF10         =  99
EfiKeyF11         = 100
EfiKeyF12         = 101
EfiKeyPrint       = 102
EfiKeySLck        = 103
EfiKeyPause       = 104
EFI_KEY           = ENUM

# 
# typedef struct {
#   ///
#   /// Used to describe a physical key on a keyboard.
#   ///
#   EFI_KEY    Key;
#   ///
#   /// Unicode character code for the Key.
#   ///
#   CHAR16     Unicode;
#   ///
#   /// Unicode character code for the key with the shift key being held down.
#   ///
#   CHAR16     ShiftedUnicode;
#   ///
#   /// Unicode character code for the key with the Alt-GR being held down.
#   ///
#   CHAR16     AltGrUnicode;
#   ///
#   /// Unicode character code for the key with the Alt-GR and shift keys being held down.
#   ///
#   CHAR16     ShiftedAltGrUnicode;
#   ///
#   /// Modifier keys are defined to allow for special functionality that is not necessarily
#   /// accomplished by a printable character. Many of these modifier keys are flags to toggle
#   /// certain state bits on and off inside of a keyboard driver.
#   ///
#   UINT16     Modifier;
#   UINT16     AffectedAttribute;
# } EFI_KEY_DESCRIPTOR;
class EFI_KEY_DESCRIPTOR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Key",                 EFI_KEY),
    ("Unicode",             CHAR16),
    ("ShiftedUnicode",      CHAR16),
    ("AltGrUnicode",        CHAR16),
    ("ShiftedAltGrUnicode", CHAR16),
    ("Modifier",            UINT16),
    ("AffectedAttribute",   UINT16)
  ]

# 
# ///
# /// A key which is affected by all the standard shift modifiers.
# /// Most keys would be expected to have this bit active.
# ///
# #define EFI_AFFECTED_BY_STANDARD_SHIFT  0x0001
EFI_AFFECTED_BY_STANDARD_SHIFT       = 0x0001
# 
# ///
# /// This key is affected by the caps lock so that if a keyboard driver
# /// would need to disambiguate between a key which had a "1" defined
# /// versus an "a" character.  Having this bit turned on would tell
# /// the keyboard driver to use the appropriate shifted state or not.
# ///
# #define EFI_AFFECTED_BY_CAPS_LOCK  0x0002
EFI_AFFECTED_BY_CAPS_LOCK            = 0x0002
# 
# ///
# /// Similar to the case of CAPS lock, if this bit is active, the key
# /// is affected by the num lock being turned on.
# ///
# #define EFI_AFFECTED_BY_NUM_LOCK  0x0004
EFI_AFFECTED_BY_NUM_LOCK             = 0x0004

# 
# typedef struct {
#   UINT16      LayoutLength;
#   EFI_GUID    Guid;
#   UINT32      LayoutDescriptorStringOffset;
#   UINT8       DescriptorCount;
#   // EFI_KEY_DESCRIPTOR    Descriptors[];
# } EFI_HII_KEYBOARD_LAYOUT;
class EFI_HII_KEYBOARD_LAYOUT (Structure):
  _pack_   = 1
  _fields_ = [
    ("LayoutLength",                  UINT16),
    ("Guid",                          EFI_GUID),
    ("LayoutDescriptorStringOffset",  UINT32),
    ("DescriptorCount",               UINT8)
    # ("Descriptors",                   EFI_KEY_DESCRIPTOR * N)
  ]

# 
# typedef struct {
#   EFI_HII_PACKAGE_HEADER    Header;
#   UINT16                    LayoutCount;
#   // EFI_HII_KEYBOARD_LAYOUT Layout[];
# } EFI_HII_KEYBOARD_PACKAGE_HDR;
class EFI_HII_KEYBOARD_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_PACKAGE_HEADER),
    ("LayoutCount", UINT16)
    # ("Layout",      EFI_HII_KEYBOARD_LAYOUT)
  ]

# 
# //
# // Modifier values
# //
# #define EFI_NULL_MODIFIER                 0x0000
# #define EFI_LEFT_CONTROL_MODIFIER         0x0001
# #define EFI_RIGHT_CONTROL_MODIFIER        0x0002
# #define EFI_LEFT_ALT_MODIFIER             0x0003
# #define EFI_RIGHT_ALT_MODIFIER            0x0004
# #define EFI_ALT_GR_MODIFIER               0x0005
# #define EFI_INSERT_MODIFIER               0x0006
# #define EFI_DELETE_MODIFIER               0x0007
# #define EFI_PAGE_DOWN_MODIFIER            0x0008
# #define EFI_PAGE_UP_MODIFIER              0x0009
# #define EFI_HOME_MODIFIER                 0x000A
# #define EFI_END_MODIFIER                  0x000B
# #define EFI_LEFT_SHIFT_MODIFIER           0x000C
# #define EFI_RIGHT_SHIFT_MODIFIER          0x000D
# #define EFI_CAPS_LOCK_MODIFIER            0x000E
# #define EFI_NUM_LOCK_MODIFIER             0x000F
# #define EFI_LEFT_ARROW_MODIFIER           0x0010
# #define EFI_RIGHT_ARROW_MODIFIER          0x0011
# #define EFI_DOWN_ARROW_MODIFIER           0x0012
# #define EFI_UP_ARROW_MODIFIER             0x0013
# #define EFI_NS_KEY_MODIFIER               0x0014
# #define EFI_NS_KEY_DEPENDENCY_MODIFIER    0x0015
# #define EFI_FUNCTION_KEY_ONE_MODIFIER     0x0016
# #define EFI_FUNCTION_KEY_TWO_MODIFIER     0x0017
# #define EFI_FUNCTION_KEY_THREE_MODIFIER   0x0018
# #define EFI_FUNCTION_KEY_FOUR_MODIFIER    0x0019
# #define EFI_FUNCTION_KEY_FIVE_MODIFIER    0x001A
# #define EFI_FUNCTION_KEY_SIX_MODIFIER     0x001B
# #define EFI_FUNCTION_KEY_SEVEN_MODIFIER   0x001C
# #define EFI_FUNCTION_KEY_EIGHT_MODIFIER   0x001D
# #define EFI_FUNCTION_KEY_NINE_MODIFIER    0x001E
# #define EFI_FUNCTION_KEY_TEN_MODIFIER     0x001F
# #define EFI_FUNCTION_KEY_ELEVEN_MODIFIER  0x0020
# #define EFI_FUNCTION_KEY_TWELVE_MODIFIER  0x0021
EFI_NULL_MODIFIER                = 0x0000
EFI_LEFT_CONTROL_MODIFIER        = 0x0001
EFI_RIGHT_CONTROL_MODIFIER       = 0x0002
EFI_LEFT_ALT_MODIFIER            = 0x0003
EFI_RIGHT_ALT_MODIFIER           = 0x0004
EFI_ALT_GR_MODIFIER              = 0x0005
EFI_INSERT_MODIFIER              = 0x0006
EFI_DELETE_MODIFIER              = 0x0007
EFI_PAGE_DOWN_MODIFIER           = 0x0008
EFI_PAGE_UP_MODIFIER             = 0x0009
EFI_HOME_MODIFIER                = 0x000A
EFI_END_MODIFIER                 = 0x000B
EFI_LEFT_SHIFT_MODIFIER          = 0x000C
EFI_RIGHT_SHIFT_MODIFIER         = 0x000D
EFI_CAPS_LOCK_MODIFIER           = 0x000E
EFI_NUM_LOCK_MODIFIER            = 0x000F
EFI_LEFT_ARROW_MODIFIER          = 0x0010
EFI_RIGHT_ARROW_MODIFIER         = 0x0011
EFI_DOWN_ARROW_MODIFIER          = 0x0012
EFI_UP_ARROW_MODIFIER            = 0x0013
EFI_NS_KEY_MODIFIER              = 0x0014
EFI_NS_KEY_DEPENDENCY_MODIFIER   = 0x0015
EFI_FUNCTION_KEY_ONE_MODIFIER    = 0x0016
EFI_FUNCTION_KEY_TWO_MODIFIER    = 0x0017
EFI_FUNCTION_KEY_THREE_MODIFIER  = 0x0018
EFI_FUNCTION_KEY_FOUR_MODIFIER   = 0x0019
EFI_FUNCTION_KEY_FIVE_MODIFIER   = 0x001A
EFI_FUNCTION_KEY_SIX_MODIFIER    = 0x001B
EFI_FUNCTION_KEY_SEVEN_MODIFIER  = 0x001C
EFI_FUNCTION_KEY_EIGHT_MODIFIER  = 0x001D
EFI_FUNCTION_KEY_NINE_MODIFIER   = 0x001E
EFI_FUNCTION_KEY_TEN_MODIFIER    = 0x001F
EFI_FUNCTION_KEY_ELEVEN_MODIFIER = 0x0020
EFI_FUNCTION_KEY_TWELVE_MODIFIER = 0x0021

# 
# //
# // Keys that have multiple control functions based on modifier
# // settings are handled in the keyboard driver implementation.
# // For instance, PRINT_KEY might have a modifier held down and
# // is still a nonprinting character, but might have an alternate
# // control function like SYSREQUEST
# //
# #define EFI_PRINT_MODIFIER        0x0022
# #define EFI_SYS_REQUEST_MODIFIER  0x0023
# #define EFI_SCROLL_LOCK_MODIFIER  0x0024
# #define EFI_PAUSE_MODIFIER        0x0025
# #define EFI_BREAK_MODIFIER        0x0026
EFI_PRINT_MODIFIER               = 0x0022
EFI_SYS_REQUEST_MODIFIER         = 0x0023
EFI_SCROLL_LOCK_MODIFIER         = 0x0024
EFI_PAUSE_MODIFIER               = 0x0025
EFI_BREAK_MODIFIER               = 0x0026

# 
# #define EFI_LEFT_LOGO_MODIFIER   0x0027
# #define EFI_RIGHT_LOGO_MODIFIER  0x0028
# #define EFI_MENU_MODIFIER        0x0029
EFI_LEFT_LOGO_MODIFIER           = 0x0027
EFI_RIGHT_LOGO_MODIFIER          = 0x0028
EFI_MENU_MODIFIER                = 0x0029

# 
# ///
# /// Animation IFR opcode
# ///
# typedef struct _EFI_IFR_ANIMATION {
#   ///
#   /// Standard opcode header, where Header.OpCode is
#   /// EFI_IFR_ANIMATION_OP.
#   ///
#   EFI_IFR_OP_HEADER    Header;
#   ///
#   /// Animation identifier in the HII database.
#   ///
#   EFI_ANIMATION_ID     Id;
# } EFI_IFR_ANIMATION;
class EFI_IFR_ANIMATION (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",  EFI_IFR_OP_HEADER),
    ("Id",      EFI_ANIMATION_ID)
  ]

# 
# ///
# /// HII animation package header.
# ///
# typedef struct _EFI_HII_ANIMATION_PACKAGE_HDR {
#   ///
#   /// Standard package header, where Header.Type = EFI_HII_PACKAGE_ANIMATIONS.
#   ///
#   EFI_HII_PACKAGE_HEADER    Header;
#   ///
#   /// Offset, relative to this header, of the animation information. If
#   /// this is zero, then there are no animation sequences in the package.
#   ///
#   UINT32                    AnimationInfoOffset;
# } EFI_HII_ANIMATION_PACKAGE_HDR;
class EFI_HII_ANIMATION_PACKAGE_HDR (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",              EFI_HII_PACKAGE_HEADER),
    ("AnimationInfoOffset", UINT32)
  ]

# 
# ///
# /// Animation information is encoded as a series of blocks,
# /// with each block prefixed by a single byte header EFI_HII_ANIMATION_BLOCK.
# ///
# typedef struct _EFI_HII_ANIMATION_BLOCK {
#   UINT8    BlockType;
#   // UINT8  BlockBody[];
# } EFI_HII_ANIMATION_BLOCK;
class EFI_HII_ANIMATION_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("BlockType", UINT8)
    # ("BlockBody", UINT8 * N)
  ]

# 
# ///
# /// Animation block types.
# ///
# #define EFI_HII_AIBT_END                  0x00
# #define EFI_HII_AIBT_OVERLAY_IMAGES       0x10
# #define EFI_HII_AIBT_CLEAR_IMAGES         0x11
# #define EFI_HII_AIBT_RESTORE_SCRN         0x12
# #define EFI_HII_AIBT_OVERLAY_IMAGES_LOOP  0x18
# #define EFI_HII_AIBT_CLEAR_IMAGES_LOOP    0x19
# #define EFI_HII_AIBT_RESTORE_SCRN_LOOP    0x1A
# #define EFI_HII_AIBT_DUPLICATE            0x20
# #define EFI_HII_AIBT_SKIP2                0x21
# #define EFI_HII_AIBT_SKIP1                0x22
# #define EFI_HII_AIBT_EXT1                 0x30
# #define EFI_HII_AIBT_EXT2                 0x31
# #define EFI_HII_AIBT_EXT4                 0x32
EFI_HII_AIBT_END                 = 0x00
EFI_HII_AIBT_OVERLAY_IMAGES      = 0x10
EFI_HII_AIBT_CLEAR_IMAGES        = 0x11
EFI_HII_AIBT_RESTORE_SCRN        = 0x12
EFI_HII_AIBT_OVERLAY_IMAGES_LOOP = 0x18
EFI_HII_AIBT_CLEAR_IMAGES_LOOP   = 0x19
EFI_HII_AIBT_RESTORE_SCRN_LOOP   = 0x1A
EFI_HII_AIBT_DUPLICATE           = 0x20
EFI_HII_AIBT_SKIP2               = 0x21
EFI_HII_AIBT_SKIP1               = 0x22
EFI_HII_AIBT_EXT1                = 0x30
EFI_HII_AIBT_EXT2                = 0x31
EFI_HII_AIBT_EXT4                = 0x32

# 
# ///
# /// Extended block headers used for variable sized animation records
# /// which need an explicit length.
# ///
# 
# typedef struct _EFI_HII_AIBT_EXT1_BLOCK  {
#   ///
#   /// Standard animation header, where Header.BlockType = EFI_HII_AIBT_EXT1.
#   ///
#   EFI_HII_ANIMATION_BLOCK    Header;
#   ///
#   /// The block type.
#   ///
#   UINT8                      BlockType2;
#   ///
#   /// Size of the animation block, in bytes, including the animation block header.
#   ///
#   UINT8                      Length;
# } EFI_HII_AIBT_EXT1_BLOCK;
class EFI_HII_AIBT_EXT1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT8)
  ]

# 
# typedef struct _EFI_HII_AIBT_EXT2_BLOCK {
#   ///
#   /// Standard animation header, where Header.BlockType = EFI_HII_AIBT_EXT2.
#   ///
#   EFI_HII_ANIMATION_BLOCK    Header;
#   ///
#   /// The block type
#   ///
#   UINT8                      BlockType2;
#   ///
#   /// Size of the animation block, in bytes, including the animation block header.
#   ///
#   UINT16                     Length;
# } EFI_HII_AIBT_EXT2_BLOCK;
class EFI_HII_AIBT_EXT2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT16)
  ]

# 
# typedef struct _EFI_HII_AIBT_EXT4_BLOCK {
#   ///
#   /// Standard animation header, where Header.BlockType = EFI_HII_AIBT_EXT4.
#   ///
#   EFI_HII_ANIMATION_BLOCK    Header;
#   ///
#   /// The block type
#   ///
#   UINT8                      BlockType2;
#   ///
#   /// Size of the animation block, in bytes, including the animation block header.
#   ///
#   UINT32                     Length;
# } EFI_HII_AIBT_EXT4_BLOCK;
class EFI_HII_AIBT_EXT4_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("Header",      EFI_HII_ANIMATION_BLOCK),
    ("BlockType2",  UINT8),
    ("Length",      UINT32)
  ]

# 
# typedef struct _EFI_HII_ANIMATION_CELL {
#   ///
#   /// The X offset from the upper left hand corner of the logical
#   /// window to position the indexed image.
#   ///
#   UINT16          OffsetX;
#   ///
#   /// The Y offset from the upper left hand corner of the logical
#   /// window to position the indexed image.
#   ///
#   UINT16          OffsetY;
#   ///
#   /// The image to display at the specified offset from the upper left
#   /// hand corner of the logical window.
#   ///
#   EFI_IMAGE_ID    ImageId;
#   ///
#   /// The number of milliseconds to delay after displaying the indexed
#   /// image and before continuing on to the next linked image.  If value
#   /// is zero, no delay.
#   ///
#   UINT16          Delay;
# } EFI_HII_ANIMATION_CELL;
class EFI_HII_ANIMATION_CELL (Structure):
  _pack_   = 1
  _fields_ = [
    ("OffsetX", UINT16),
    ("OffsetY", UINT16),
    ("ImageId", EFI_IMAGE_ID),
    ("Delay",   UINT16)
  ]

# 
# ///
# /// An animation block to describe an animation sequence that does not cycle, and
# /// where one image is simply displayed over the previous image.
# ///
# typedef struct _EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK {
#   ///
#   /// This is image that is to be reference by the image protocols, if the
#   /// animation function is not supported or disabled. This image can
#   /// be one particular image from the animation sequence (if any one
#   /// of the animation frames has a complete image) or an alternate
#   /// image that can be displayed alone. If the value is zero, no image
#   /// is displayed.
#   ///
#   EFI_IMAGE_ID              DftImageId;
#   ///
#   /// The overall width of the set of images (logical window width).
#   ///
#   UINT16                    Width;
#   ///
#   /// The overall height of the set of images (logical window height).
#   ///
#   UINT16                    Height;
#   ///
#   /// The number of EFI_HII_ANIMATION_CELL contained in the
#   /// animation sequence.
#   ///
#   UINT16                    CellCount;
#   ///
#   /// An array of CellCount animation cells.
#   ///
#   EFI_HII_ANIMATION_CELL    AnimationCell[1];
# } EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK;
class EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

# 
# ///
# /// An animation block to describe an animation sequence that does not cycle,
# /// and where the logical window is cleared to the specified color before
# /// the next image is displayed.
# ///
# typedef struct _EFI_HII_AIBT_CLEAR_IMAGES_BLOCK {
#   ///
#   /// This is image that is to be reference by the image protocols, if the
#   /// animation function is not supported or disabled. This image can
#   /// be one particular image from the animation sequence (if any one
#   /// of the animation frames has a complete image) or an alternate
#   /// image that can be displayed alone. If the value is zero, no image
#   /// is displayed.
#   ///
#   EFI_IMAGE_ID              DftImageId;
#   ///
#   /// The overall width of the set of images (logical window width).
#   ///
#   UINT16                    Width;
#   ///
#   /// The overall height of the set of images (logical window height).
#   ///
#   UINT16                    Height;
#   ///
#   /// The number of EFI_HII_ANIMATION_CELL contained in the
#   /// animation sequence.
#   ///
#   UINT16                    CellCount;
#   ///
#   /// The color to clear the logical window to before displaying the
#   /// indexed image.
#   ///
#   EFI_HII_RGB_PIXEL         BackgndColor;
#   ///
#   /// An array of CellCount animation cells.
#   ///
#   EFI_HII_ANIMATION_CELL    AnimationCell[1];
# } EFI_HII_AIBT_CLEAR_IMAGES_BLOCK;
class EFI_HII_AIBT_CLEAR_IMAGES_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("BackgndColor",  EFI_HII_RGB_PIXEL),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

# 
# ///
# /// An animation block to describe an animation sequence that does not cycle,
# /// and where the screen is restored to the original state before the next
# /// image is displayed.
# ///
# typedef struct _EFI_HII_AIBT_RESTORE_SCRN_BLOCK {
#   ///
#   /// This is image that is to be reference by the image protocols, if the
#   /// animation function is not supported or disabled. This image can
#   /// be one particular image from the animation sequence (if any one
#   /// of the animation frames has a complete image) or an alternate
#   /// image that can be displayed alone. If the value is zero, no image
#   /// is displayed.
#   ///
#   EFI_IMAGE_ID              DftImageId;
#   ///
#   /// The overall width of the set of images (logical window width).
#   ///
#   UINT16                    Width;
#   ///
#   /// The overall height of the set of images (logical window height).
#   ///
#   UINT16                    Height;
#   ///
#   /// The number of EFI_HII_ANIMATION_CELL contained in the
#   /// animation sequence.
#   ///
#   UINT16                    CellCount;
#   ///
#   /// An array of CellCount animation cells.
#   ///
#   EFI_HII_ANIMATION_CELL    AnimationCell[1];
# } EFI_HII_AIBT_RESTORE_SCRN_BLOCK;
class EFI_HII_AIBT_RESTORE_SCRN_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("DftImageId",    EFI_IMAGE_ID),
    ("Width",         UINT16),
    ("Height",        UINT16),
    ("CellCount",     UINT16),
    ("AnimationCell", EFI_HII_ANIMATION_CELL * 1)
  ]

# 
# ///
# /// An animation block to describe an animation sequence that continuously cycles,
# /// and where one image is simply displayed over the previous image.
# ///
# typedef EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK EFI_HII_AIBT_OVERLAY_IMAGES_LOOP_BLOCK;
EFI_HII_AIBT_OVERLAY_IMAGES_LOOP_BLOCK  = EFI_HII_AIBT_OVERLAY_IMAGES_BLOCK
# 
# ///
# /// An animation block to describe an animation sequence that continuously cycles,
# /// and where the logical window is cleared to the specified color before
# /// the next image is displayed.
# ///
# typedef EFI_HII_AIBT_CLEAR_IMAGES_BLOCK EFI_HII_AIBT_CLEAR_IMAGES_LOOP_BLOCK;
EFI_HII_AIBT_CLEAR_IMAGES_LOOP_BLOCK    = EFI_HII_AIBT_CLEAR_IMAGES_BLOCK
# 
# ///
# /// An animation block to describe an animation sequence that continuously cycles,
# /// and where the screen is restored to the original state before
# /// the next image is displayed.
# ///
# typedef EFI_HII_AIBT_RESTORE_SCRN_BLOCK EFI_HII_AIBT_RESTORE_SCRN_LOOP_BLOCK;
EFI_HII_AIBT_RESTORE_SCRN_LOOP_BLOCK    = EFI_HII_AIBT_RESTORE_SCRN_BLOCK
# 
# ///
# /// Assigns a new character value to a previously defined animation sequence.
# ///
# typedef struct _EFI_HII_AIBT_DUPLICATE_BLOCK {
#   ///
#   /// The previously defined animation ID with the exact same
#   /// animation information.
#   ///
#   EFI_ANIMATION_ID    AnimationId;
# } EFI_HII_AIBT_DUPLICATE_BLOCK;
class EFI_HII_AIBT_DUPLICATE_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("AnimationId", EFI_ANIMATION_ID)
  ]

# 
# ///
# /// Skips animation IDs.
# ///
# typedef struct _EFI_HII_AIBT_SKIP1_BLOCK {
#   ///
#   /// The unsigned 8-bit value to add to AnimationIdCurrent.
#   ///
#   UINT8    SkipCount;
# } EFI_HII_AIBT_SKIP1_BLOCK;
class EFI_HII_AIBT_SKIP1_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("SkipCount", UINT8)
  ]

# 
# ///
# /// Skips animation IDs.
# ///
# typedef struct _EFI_HII_AIBT_SKIP2_BLOCK {
#   ///
#   /// The unsigned 16-bit value to add to AnimationIdCurrent.
#   ///
#   UINT16    SkipCount;
# } EFI_HII_AIBT_SKIP2_BLOCK;
class EFI_HII_AIBT_SKIP2_BLOCK (Structure):
  _pack_   = 1
  _fields_ = [
    ("SkipCount", UINT16)
  ]

# 
# #pragma pack()
# 
# ///
# /// References to string tokens must use this macro to enable scanning for
# /// token usages.
# ///
# ///
# /// STRING_TOKEN is not defined in UEFI specification. But it is placed
# /// here for the easy access by C files and VFR source files.
# ///
# #define STRING_TOKEN(t)  t
# 
# ///
# /// IMAGE_TOKEN is not defined in UEFI specification. But it is placed
# /// here for the easy access by C files and VFR source files.
# ///
# #define IMAGE_TOKEN(t)  t
# 
# #endif
# 