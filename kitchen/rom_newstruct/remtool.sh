#!/sbin/sh
#
# Cleanup .odex files before theme-ing!
#
################################################################################

mount /system;
mount /data;

rm -rf /system/app/*.odex;
rm -rf /system/framework/*.odex;

# Cleanup the dalvik-cache for apps that are themed also.
################################################################################
rm -f /cache/dalvik-cache/system\@app\@AccountAndSyncSettings.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Bluetooth.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Browser.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Calculator.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Calendar.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@CalendarProvider.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Camera.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Contacts.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@ContactsProvider.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@DeskClock.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Development.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Email.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Gallery3D.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@GlobalSearch.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@GoogleSearch.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Launcher2.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@LiveWallpapersPicker.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@MediaProvider.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Mms.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Music.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@PackageInstaller.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Phone.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@Settings.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@SoundRecorder.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@SpareParts.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@TtsService.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@VoiceDialer.apk\@classes.dex
rm -f /cache/dalvik-cache/system\@app\@VpnServices.apk\@classes.dex

rm -f /cache/dalvik-cache/system\@framework\@services.jar\@classes.dex

cd /
/system/bin/fix_permissions

exit 0;

