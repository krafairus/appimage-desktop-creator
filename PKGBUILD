pkgname=appimage-desktop-creator
pkgver=1.0.2
pkgrel=1
pkgdesc="Crea un archivo .desktop con un appimage de forma simple"
arch=('any')
url="https://github.com/krafairus/appimage-desktop-creator"
license=('MIT')
depends=('python' 'python-pyqt5')

source=("appimage-desktop-creator.py"
        "appimage-desktop-creator.desktop"
        "appimage-desktop-creator.png")

sha256sums=('1d879801b1402c056768f9614b78e3bc3ea0b6590f8ebc25081b610bdb3307a5'
            '1a97c262304029e1bd06938cee02a578e3fabcf0f85368ecb069e4306f37c2ae'
            'df3341183f7b69d0bffb2b9ca2b079aa5588cdad4a97e263222c9030c3a0d708')

package() {
  cd "$srcdir"
  install -Dm755 appimage-desktop-creator.py "$pkgdir/usr/bin/appimage-desktop-creator/appimage-desktop-creator.py"
  install -Dm644 appimage-desktop-creator.desktop "$pkgdir/usr/share/applications/appimage-desktop-creator.desktop"
  install -Dm644 appimage-desktop-creator.png "$pkgdir/usr/share/icons/hicolor/scalable/apps/appimage-desktop-creator.png"

}
