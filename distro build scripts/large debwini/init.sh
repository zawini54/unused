#debootstrap --variant=minbase testing ../chroot http://ftp.th.debian.org/debian
mount -o bind /dev ../chroot/dev
cp /etc/resolv.conf ../chroot/etc/resolv.conf
cp install.sh ../chroot/install.sh
cp sources.list ../chroot/etc/apt/sources.list
cp -r eclipse ../chroot/opt/
cp Eclipse.desktop ../chroot/Eclipse.desktop
cp done.sh ../chroot/done.sh
cp 'eclipse installs' '../chroot/eclipse installs'
chmod a+x ../chroot/install.sh
chmod a+x ../chroot/done.sh
chroot ../chroot
