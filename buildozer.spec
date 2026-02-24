[app]
title = GestionMobile
package.name = gestionmobile
package.domain = org.premices
source.dir = .
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
