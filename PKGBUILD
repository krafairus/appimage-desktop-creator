pkgname=appimage-desktop-creator
pkgver=1.0
pkgrel=1
pkgdesc="Crea un archivo .desktop con un appimage de forma simple"
arch=('any')
url="https://github.com/krafairus/appimage-desktop-creator"
license=('MIT')
depends=('python' 'python-pyqt5')

source=("appimage-desktop-creator.py"
        "appimage-desktop-creator.desktop"
        "appimage-desktop-creator.png")

sha256sums=('b62b2697ecab45fab9ab55b0281e3c63d499da4ca98b4a6e9fc1587bdb32fcc0'
            '207a9bd28973f0ef95350fb137a9e4d1d793f4cb82f810ccd14b9269b1824d17'
            'df3341183f7b69d0bffb2b9ca2b079aa5588cdad4a97e263222c9030c3a0d708')

package() {
  cd "$srcdir"
  install -Dm755 appimage-desktop-creator.py "$pkgdir/usr/bin/appimage-desktop-creator.py"
  install -Dm644 appimage-desktop-creator.desktop "$pkgdir/usr/share/applications/appimage-desktop-creator.desktop"
  install -Dm644 appimage-desktop-creator.png "$pkgdir/usr/share/icons/hicolor/scalable/apps/appimage-desktop-creator.png"

}
