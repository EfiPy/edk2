# /** @file
#   This file defines BMP file header data structures.
# 
# Copyright (c) 2006 - 2011, Intel Corporation. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent
# 
# **/
#
# Bmp.py
#
# EfiPy2.MdePkg.IndustryStandard.Bmp
#   part of EfiPy, EfiPy2
#
# Copyright (C) 2015 - 2023 MaxWu efipy.core@gmail.com
#   GPL-2.0
#
# #ifndef _BMP_H_
# #define _BMP_H_
from EfiPy2.MdePkg.IndustryStandard import *

# 
# #pragma pack(1)
# 
# typedef struct {
#   UINT8    Blue;
#   UINT8    Green;
#   UINT8    Red;
#   UINT8    Reserved;
# } BMP_COLOR_MAP;
class BMP_COLOR_MAP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("Blue",      UINT8),
    ("Green",     UINT8),
    ("Red",       UINT8),
    ("Reserved",  UINT8)
  ]

# 
# typedef struct {
#   CHAR8     CharB;
#   CHAR8     CharM;
#   UINT32    Size;
#   UINT16    Reserved[2];
#   UINT32    ImageOffset;
#   UINT32    HeaderSize;
#   UINT32    PixelWidth;
#   UINT32    PixelHeight;
#   UINT16    Planes;              ///< Must be 1
#   UINT16    BitPerPixel;         ///< 1, 4, 8, or 24
#   UINT32    CompressionType;
#   UINT32    ImageSize;           ///< Compressed image size in bytes
#   UINT32    XPixelsPerMeter;
#   UINT32    YPixelsPerMeter;
#   UINT32    NumberOfColors;
#   UINT32    ImportantColors;
# } BMP_IMAGE_HEADER;
class BMP_IMAGE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("CharB",           CHAR8),
    ("CharM",           CHAR8),
    ("Size",            UINT32),
    ("Reserved",        UINT16 * 2),
    ("ImageOffset",     UINT32),
    ("HeaderSize",      UINT32),
    ("PixelWidth",      UINT32),
    ("PixelHeight",     UINT32),
    ("Planes",          UINT16),
    ("BitPerPixel",     UINT16),
    ("CompressionType", UINT32),
    ("ImageSize",       UINT32),
    ("XPixelsPerMeter", UINT32),
    ("YPixelsPerMeter", UINT32),
    ("NumberOfColors",  UINT32),
    ("ImportantColors", UINT32)
  ]

# 
# #pragma pack()
# 
# #endif
# 