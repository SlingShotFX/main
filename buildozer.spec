[app]
# (str) Title of your application
title = SlingShotFX

# (str) Package name
package.name = slingshotfx

# (str) Package domain (needed for android/ios packaging)
package.domain = org.sfx

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.1.0,kivymd,pillow,MetaTrader5

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 21b

# (list) Android archs to build for
android.archs = armeabi-v7a,arm64-v8a

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
[buildozer]
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
