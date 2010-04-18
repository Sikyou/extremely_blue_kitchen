#!/sbin/sh
#
# Cleanup .odex files before theme-ing!
#
################################################################################

mount /system;
mount /data;

# Cleanup the dalvik-cache for apps that are themed also.
################################################################################
rm -f /cache/dalvik-cache/*

cd /
/system/bin/fix_permissions

exit 0;

