rm -f /var/lib/dbus/machine-id
apt-get clean
rm -rf /tmp/*
rm /etc/resolv.conf
history -c
umount -lf /proc
umount -lf /sys
umount -lf /dev/pts
exit
