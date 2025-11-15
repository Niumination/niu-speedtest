# Arch Speedtest CLI

[![AUR](https://img.shields.io/badge/AUR-arch--speedtest-blue.svg)](https://aur.archlinux.org/packages/arch-speedtest/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

A simple command-line speedtest utility for Arch Linux that tests your internet connection speed from multiple servers and provides detailed statistics.

## 🚀 Features

- **Multiple Server Testing**: Tests download speed from various reliable servers
- **Detailed Statistics**: Provides average, median, min, and max speeds
- **Lightweight**: No external dependencies beyond Python 3.6+
- **Easy Installation**: Available in AUR for easy installation with yay
- **Clean Output**: Simple and readable command-line interface

## 📦 Installation

### From AUR (Recommended)

Using yay:
```bash
yay -S arch-speedtest
```

Using other AUR helpers:
```bash
# Using paru
paru -S arch-speedtest

# Using pikaur
pikaur -S arch-speedtest
```

### Manual Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/arch-speedtest.git
cd arch-speedtest
```

2. Install using makepkg:
```bash
makepkg -si
```

## 🎯 Usage

### Basic Usage

Run a speedtest:
```bash
arch-speedtest
```

### Help and Version

Show help:
```bash
arch-speedtest --help
# or
arch-speedtest -h
```

Show version:
```bash
arch-speedtest --version
# or
arch-speedtest -v
```

### Example Output

```
🚀 Arch Linux Speedtest CLI
========================================
Started at: 2025-11-15 14:30:25

Testing download speeds...
  Test 1/4: speedtest.tele2.net
    Speed: 45.23 Mbps
  Test 2/4: speedtest.tele2.net
    Speed: 47.89 Mbps
  Test 3/4: proof.ovh.net
    Speed: 43.12 Mbps
  Test 4/4: proof.ovh.net
    Speed: 46.78 Mbps

📊 Results:
  Average: 45.76 Mbps
  Median:  46.01 Mbps
  Min:     43.12 Mbps
  Max:     47.89 Mbps
  Tests:   4 successful
```

## 🔧 Technical Details

### Test Servers

The tool tests against the following reliable servers:
- `speedtest.tele2.net` (1MB and 10MB files)
- `proof.ovh.net` (1Mb and 10Mb files)

### Requirements

- Python 3.6 or higher
- Internet connection
- Standard library modules only (no external dependencies)

### How It Works

1. Downloads test files from multiple servers
2. Measures download time for each file
3. Calculates speed in Mbps
4. Provides statistical analysis of results

## 🛠️ Development

### Building the Package

To build the package locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/arch-speedtest.git
cd arch-speedtest

# Build the package
makepkg

# Install the built package
sudo pacman -U arch-speedtest-*.pkg.tar.zst
```

### Testing the Script

You can test the script without installing:

```bash
python3 speedtest.py
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📋 TODO

- [ ] Add upload speed testing
- [ ] Add ping/latency testing
- [ ] Add server selection options
- [ ] Add configuration file support
- [ ] Add JSON output format
- [ ] Add historical data tracking

## 🐛 Troubleshooting

### Common Issues

1. **Permission Denied**: Make sure the script is executable:
   ```bash
   chmod +x /usr/bin/arch-speedtest
   ```

2. **Python Not Found**: Ensure Python 3.6+ is installed:
   ```bash
   python3 --version
   ```

3. **Network Issues**: Check your internet connection and firewall settings.

### Getting Help

If you encounter any issues:

1. Check the [Issues](https://github.com/yourusername/arch-speedtest/issues) page
2. Create a new issue with details about your problem
3. Include your system information and error messages

## 📊 Performance

The tool is designed to be lightweight and fast:
- Minimal memory usage
- No external dependencies
- Fast execution time
- Accurate speed measurements

## 🙏 Acknowledgments

- Test servers provided by [Tele2](https://speedtest.tele2.net/) and [OVH](https://proof.ovh.net/)
- Inspired by various open-source speedtest tools
- Built for the Arch Linux community

---

**Made with ❤️ for the Arch Linux community**