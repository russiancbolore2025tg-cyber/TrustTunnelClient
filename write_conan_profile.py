#!/usr/bin/env python3
"""
Пишет Conan profile для Android.
Используется из GitHub Action чтобы избежать heredoc в YAML.

Usage:
  python3 write_conan_profile.py <abi> <conan_arch> <build_type> <ndk_path>

Example:
  python3 write_conan_profile.py arm64-v8a armv8 Release /path/to/ndk
"""
import sys, pathlib, os

abi        = sys.argv[1]   # arm64-v8a / armeabi-v7a / x86_64
arch       = sys.argv[2]   # armv8 / armv7 / x86_64
build_type = sys.argv[3]   # Release / Debug
ndk_path   = sys.argv[4]   # /usr/local/lib/android/sdk/ndk/28.x

profile = f"""[settings]
os=Android
os.api_level=26
arch={arch}
compiler=clang
compiler.version=19
compiler.libcxx=c++_shared
compiler.cppstd=20
build_type={build_type}

[conf]
tools.android:ndk_path={ndk_path}
"""

out = pathlib.Path.home() / f".conan2/profiles/android_{abi}"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(profile)
print(f"Written: {out}")
print(profile)
