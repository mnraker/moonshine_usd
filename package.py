# Copyright 2024 DreamWorks Animation LLC
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
import os

name = 'moonshine_usd'

if 'early' not in locals() or not callable(early):
    def early(): return lambda x: x

@early()
def version():
    """
    Increment the build in the version.
    """
    _version = '12.20'
    from rezbuild import earlybind
    return earlybind.version(this, _version)

description = 'USD Shaders for Moonray'

authors = [
    'PSW Rendering and Shading',
    'moonbase-dev@dreamworks.com',
    'Ron.Woods@dreamworks.com'
]

help = ('For assistance, '
        "please contact the folio's owner at: moonbase-dev@dreamworks.com")

variants = [
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.21.8.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.21.8.x.2'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2021.0', 'clang-13', 'usd_core-0.21.8.x.2'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.20.8.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.20.8.x.2'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.20.8.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.20.8.x.2'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.21.5.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.21.5.x.2'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.21.5.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.21.5.x.2'],

    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.21.8.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'usd_core-0.21.8.x.2'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.21.8.x.2'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'usd_core-0.21.8.x.2'],

    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.21.8.x.2'],
    ['os-rocky-9', 'opt_level-debug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.21.8.x.2'],

    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],
    ['os-rocky-9', 'opt_level-debug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],

    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],
    ['os-rocky-9', 'opt_level-debug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'usd_core-0.22.5.x'],

    ['os-rocky-9', 'opt_level-optdebug', 'refplat-vfx2023.0', 'gcc-11.x', 'usd_core-0.22.5.x'],
    ['os-rocky-9', 'opt_level-debug', 'refplat-vfx2023.0', 'gcc-11.x', 'usd_core-0.22.5.x'],
]

conf_rats_variants = variants[0:2]
conf_CI_variants = list(filter(lambda v: 'os-CentOS-7' in v, variants))

requires = [
    'moonray-15.20',
    'moonshine-12.20',
    'scene_rdl2-13.12',
]

private_build_requires = [
    'cmake_modules',
    'usd_imaging',
    'cppunit',
    'ispc-1.20.0.x',
]

commandstr = lambda i: "cd build/"+os.path.join(*variants[i])+"; ctest -j $(nproc)"
testentry = lambda i: ("variant%d" % i,
                       { "command": commandstr(i),
                         "requires": ["cmake-3.23"] + variants[i] } )
testlist = [testentry(i) for i in range(len(variants))]
tests = dict(testlist)

def commands():
    prependenv('CMAKE_PREFIX_PATH', '{root}')
    prependenv('SOFTMAP_PATH', '{root}')
    prependenv('MOONRAY_DSO_PATH', '{root}/rdl2dso')
    prependenv('RDL2_DSO_PATH', '{root}/rdl2dso')
    prependenv('LD_LIBRARY_PATH', '{root}/lib')
    prependenv('PATH', '{root}/bin')
    prependenv('MOONRAY_CLASS_PATH', '{root}/coredata')

uuid = 'bb291e0f-ce27-445d-b280-320a5f23e9b9'

config_version = 0
