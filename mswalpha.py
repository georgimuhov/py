"""
function to draw alpha correctly on Microsoft Windows with a shaped frame.
This probably will need be called at the end of your OnPaint event handler method.
"""

import sys

if not sys.platform.startswith('win'):
    print('This script will only run on Microsoft Windows.')
    sys.exit(1)

import ctypes
from ctypes.wintypes import LONG, HWND, INT, HDC, HGDIOBJ, BOOL, DWORD

## import wx

UBYTE = ctypes.c_ubyte
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
ULW_ALPHA = 0x00000002
AC_SRC_OVER = 0x00000000
AC_SRC_ALPHA = 0x00000001


class POINT(ctypes.Structure):
    _fields_ = [
        ('x', LONG),
        ('y', LONG)
    ]


class SIZE(ctypes.Structure):
    _fields_ = [
        ('cx', LONG),
        ('cy', LONG)
    ]


class BLENDFUNCTION(ctypes.Structure):
    _fields_ = [
        ('BlendOp', UBYTE),
        ('BlendFlags', UBYTE),
        ('SourceConstantAlpha', UBYTE),
        ('AlphaFormat', UBYTE)
    ]


user32 = ctypes.windll.User32
gdi32 = ctypes.windll.Gdi32

# LONG GetWindowLongW(
#   HWND hWnd,
#   int  nIndex
# );
GetWindowLongW = user32.GetWindowLongW
GetWindowLongW.restype = LONG

# LONG SetWindowLongW(
#   HWND hWnd,
#   int  nIndex,
#   LONG dwNewLong
# );
SetWindowLongW = user32.SetWindowLongW
SetWindowLongW.restype = LONG

# HDC GetDC(
#   HWND hWnd
# );
GetDC = user32.GetDC
GetDC.restype = HDC

# HWND GetDesktopWindow();
GetDesktopWindow = user32.GetDesktopWindow
GetDesktopWindow.restype = HWND

# HDC CreateCompatibleDC(
#   HDC hdc
# );
CreateCompatibleDC = gdi32.CreateCompatibleDC
CreateCompatibleDC.restype = HDC

# HGDIOBJ SelectObject(
#   HDC     hdc,
#   HGDIOBJ h
# );
SelectObject = gdi32.SelectObject
SelectObject.restype = HGDIOBJ

# BOOL UpdateLayeredWindow(
#   HWND,         hWnd,
#   HDC           hdcDst,
#   POINT         *pptDst,
#   SIZE          *psize,
#   HDC           hdcSrc,
#   POINT         *pptSrc,
#   COLORREF      crKey,
#   BLENDFUNCTION *pblend,
#   DWORD         dwFlags
# );
UpdateLayeredWindow = user32.UpdateLayeredWindow
UpdateLayeredWindow.restype = BOOL

COLORREF = DWORD


def RGB(r, g, b):
    return COLORREF(r | (g << 8) | (b << 16))


def draw_alpha(window, bmp):
    """
    function to draw alpha correctly on Microsoft Windows with a shaped frame.
    This probably will need be called at the end of your Paint event handler method.

    :param bmp: Bitmap with alpha
    :param window: Pointer to a window. Must not be ``None``.
    """
    hndl = window.GetHandle()

    style = GetWindowLongW(HWND(hndl), INT(GWL_EXSTYLE))
    SetWindowLongW(HWND(hndl), INT(GWL_EXSTYLE), LONG(style | WS_EX_LAYERED))

    hdcDst = GetDC(GetDesktopWindow())
    hdcSrc = CreateCompatibleDC(HDC(hdcDst))

    pptDst = POINT(*window.GetPosition())
    psize = SIZE(*window.GetClientSize())
    pptSrc = POINT(0, 0)
    crKey = RGB(0, 0, 0)

    pblend = BLENDFUNCTION(AC_SRC_OVER, 0, 255, AC_SRC_ALPHA)

    SelectObject(HDC(hdcSrc), HGDIOBJ(bmp.GetHandle()))
    UpdateLayeredWindow(
        HWND(hndl),
        HDC(hdcDst),
        ctypes.byref(pptDst),
        ctypes.byref(psize),
        HDC(hdcSrc),
        ctypes.byref(pptSrc),
        crKey,
        ctypes.byref(pblend),
        DWORD(ULW_ALPHA)
    )
