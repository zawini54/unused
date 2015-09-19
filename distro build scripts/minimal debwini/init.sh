#debootstrap --variant=minbase testing ../chroot http://ftp.th.debian.org/debian
mount -o bind /dev ../chroot/dev
mount -o bind /tmp ../chroot/tmp
cp /etc/resolv.conf ../chroot/etc/resolv.conf
cp install.sh ../chroot/install.sh
cp sources.list ../chroot/etc/apt/sources.list
cp menu.xml ../chroot
cp tint2rc ../chroot
cp atom-amd64.deb ../chroot
cp lighttpd.conf ../chroot
cp debian-menu.xml ../chroot
cp done.sh ../chroot/done.sh
chmod a+x ../chroot/install.sh
chmod a+x ../chroot/done.sh
chroot ../chroot
