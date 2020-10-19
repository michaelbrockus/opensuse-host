#!/usr/bin/env python3

#
# author: Michael Brockus.
# gmail: mailto:michaelbrockus@gmail.com
#
from shutil import which


def exe_exists(prog_name: str) -> None:
    if not isinstance(prog_name, str):
        raise ValueError
    return False if not which(prog_name) else True


def test_has_python3():
    assert exe_exists('python3') is True
    assert exe_exists('pip3') is True


def test_have_build_systems():
    assert exe_exists('meson') is True
    assert exe_exists('cmake') is True
    assert exe_exists('cargo') is True
    assert exe_exists('ninja') is True


def test_have_ci_tools():
    assert exe_exists('cppcheck') is True
    assert exe_exists('pytest') is True
    assert exe_exists('git') is True


def test_have_gnu_toolchain():
    assert exe_exists('gcc') is True
    assert exe_exists('g++') is True
    assert exe_exists('gdc') is True
    assert exe_exists('gfortran') is True


def test_have_rust_toolchain():
    assert exe_exists('rustc') is True
    assert exe_exists('cargo') is True


def test_has_openjdk_toolchain():
    assert exe_exists('javac') is True
    assert exe_exists('java') is True


def test_has_mono_toolchain():
    assert exe_exists('mono') is True
    assert exe_exists('mcs') is True
