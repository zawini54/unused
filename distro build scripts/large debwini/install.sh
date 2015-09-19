mount none -t proc /proc
mount none -t sysfs /sys
mount none -t devpts /dev/pts
export HOME=/root
export LC_ALL=C
apt-get update
apt-get install sudo nano man-db dialog dbus --yes --force-yes # udev is already installed in debootstrap
dbus-uuidgen > /var/lib/dbus/machine-id
/etc/init.d/udev start
echo "Debwini" > /etc/hostname
apt-get upgrade --yes && apt-get dist-upgrade --yes
apt-get install --no-install-recommends --yes --force-yes linux-image-amd64 live-boot \
net-tools wireless-tools tcpdump wget openssh-client pciutils usbutils \
gparted ntfs-3g hfsprogs dosfstools firmware-linux-free firmware-linux-nonfree flashplugin-nonfree banshee \
lightdm g++ python3 iceweasel openjdk-7-jdk transmission-gtk git alsa-utils wicd mirage leafpad build-essential
apt-get install xfce4 --yes
mv /opt/eclipse/icon.xpm /usr/share/pixmaps/eclipse.xpm
ln -s /opt/eclipse/eclipse /usr/bin/eclipse
rm /usr/share/applications/exo-mail-reader.desktop
rm /usr/share/applications/exo-web-browser.desktop
mv /Eclipse.desktop /usr/share/applications/Eclipse.desktop
alsactl init
passwd root
dpkg-reconfigure lightdm
dpkg-reconfigure tzdata
nano /etc/lightdm/lightdm.conf
startx
rmdir /root/Documents
rmdir /root/Music
rmdir /root/Pictures
rmdir /root/Videos
rmdir /root/Public
rmdir /root/Templates

# LAMP
# XFCE panel configuration file
# MIME associations
