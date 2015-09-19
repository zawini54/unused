mount none -t proc /proc
mount none -t sysfs /sys
mount none -t devpts /dev/pts
export HOME=/root
export LC_ALL=C
apt-get update
apt-get upgrade --yes
apt-get install sudo nano man-db dialog dbus --yes --force-yes # udev is already installed in debootstrap
dbus-uuidgen > /var/lib/dbus/machine-id
/etc/init.d/udev start
echo "Debwini" > /etc/hostname
apt-get upgrade --yes && apt-get dist-upgrade --yes
apt-get install --no-install-recommends --yes --force-yes linux-image-amd64 live-boot bash-completion
apt-get install mysql-server --yes
apt-get install lighttpd php5-common php5-cgi php5-mysql php5-mcrypt php5-gd php5-curl php5-json php-pear --yes
lighty-enable-mod fastcgi-php
rm /etc/lighttpd/lighttpd.conf
mv /lighttpd.conf /etc/lighttpd/lighttpd.conf
mv /var/www/html/index.lighttpd.html /var/www/
rmdir /var/www/html
/etc/init.d/lighttpd force-reload
apt-get install phpmyadmin --yes
apt-get install --no-install-recommends --yes --force-yes \
net-tools wireless-tools tcpdump wget openssh-client pciutils usbutils \
gparted ntfs-3g hfsprogs dosfstools firmware-linux-free firmware-linux-nonfree flashplugin-nonfree \
g++ python3 iceweasel openjdk-7-jdk git alsa-utils wicd mpv build-essential leafpad xorg feh nautilus \
alsamixergui gnome-icon-theme #tint2
apt-get install openbox menu obmenu fonts-dejavu --yes
#rm /usr/share/applications/exo-mail-reader.desktop
#rm /usr/share/applications/exo-web-browser.desktop
dpkg -i /atom-amd64.deb
apt-get install -f --yes
rm /atom-amd64.deb
alsactl init
passwd root
dpkg-reconfigure tzdata
rm /etc/xdg/openbox/menu.xml
mv /menu.xml /etc/xdg/openbox/menu.xml
rm /var/lib/openbox/debian-menu.xml
mv /debian-menu.xml /var/lib/openbox/debian-menu.xml
mkdir /root/.config/openbox
#echo 'tint2 &' > /root/.config/openbox/autostart.sh
#mkdir /root/.config/tint2
#mv /root/.config/tint2/tint2rc /root/.config/tint2/tint2rc.old
#cp tint2rc /root/.config/tint2/tint2rc
mkdir /etc/systemd/system/getty@tty1.service.d
echo "[Service]" > /etc/systemd/system/getty@tty1.service.d/autologin.conf
echo 'ExecStart=-/sbin/agetty --autologin "user account" %I' >> /etc/systemd/system/getty@tty1.service.d/autologin.conf
cp -r /etc/systemd/system/gety@tty1.service.d /etc/systemd/system/getty@tty2.service.d
cp -r /etc/systemd/system/gety@tty1.service.d /etc/systemd/system/getty@tty3.service.d
cp -r /etc/systemd/system/gety@tty1.service.d /etc/systemd/system/getty@tty4.service.d
cp -r /etc/systemd/system/gety@tty1.service.d /etc/systemd/system/getty@tty5.service.d
cp -r /etc/systemd/system/gety@tty1.service.d /etc/systemd/system/getty@tty6.service.d
