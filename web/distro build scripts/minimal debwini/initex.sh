mount -o bind /dev ../chroot/dev
mount -o bind /tmp ../chroot/tmp
cp /etc/resolv.conf ../chroot/etc/resolv.conf
chroot ../chroot mount none -t proc /proc
chroot ../chroot mount none -t sysfs /sys
chroot ../chroot mount none -t devpts /dev/pts
chroot ../chroot
