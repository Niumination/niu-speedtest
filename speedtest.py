#!/usr/bin/env python3
"""
Arch Linux Niu-Speedtest CLI Tool
A simple command-line speedtest utility for Arch Linux
*Niumination*
"""

import sys
import time
import statistics
import urllib.request
import urllib.error
from datetime import datetime


class SpeedtestCLI:
    def __init__(self):
        self.test_servers = [
            "http://speedtest.tele2.net/1MB.zip",
            "http://speedtest.tele2.net/10MB.zip",
            "http://proof.ovh.net/files/1Mb.dat",
            "http://proof.ovh.net/files/10Mb.dat",
        ]

    def download_speed(self, url, timeout=10):
        """Test download speed from a given URL"""
        try:
            start_time = time.time()
            with urllib.request.urlopen(url, timeout=timeout) as response:
                data = response.read()
                end_time = time.time()

                file_size = len(data)
                time_taken = end_time - start_time
                speed_bps = file_size / time_taken
                speed_mbps = speed_bps / (1024 * 1024)

                return speed_mbps
        except Exception as e:
            print(f"Error testing {url}: {e}")
            return None

    def run_speedtest(self):
        """Run comprehensive speedtest"""
        print("🚀 Arch Linux Niu-Speedtest CLI")
        print("=" * 40)
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()

        speeds = []

        print("Testing download speeds...")
        for i, server in enumerate(self.test_servers, 1):
            print(f"  Test {i}/{len(self.test_servers)}: {server.split('/')[2]}")
            speed = self.download_speed(server)
            if speed:
                speeds.append(speed)
                print(f"    Speed: {speed:.2f} Mbps")
            else:
                print("    Failed")

        if speeds:
            print()
            print("📊 Results:")
            print(f"  Average: {statistics.mean(speeds):.2f} Mbps")
            print(f"  Median:  {statistics.median(speeds):.2f} Mbps")
            print(f"  Min:     {min(speeds):.2f} Mbps")
            print(f"  Max:     {max(speeds):.2f} Mbps")
            print(f"  Tests:   {len(speeds)} successful")
        else:
            print("❌ All speed tests failed!")
            sys.exit(1)

    def show_version(self):
        """Show version information"""
        print("arch-speedtest version 1.0.0")
        print("A simple CLI speedtest tool for Arch Linux")

    def show_help(self):
        """Show help information"""
        print("Arch Linux Niu-Speedtest CLI")
        print()
        print("Usage:")
        print("  niu-speedtest          Run speedtest")
        print("  niu-speedtest --help   Show this help")
        print("  niu-speedtest --version Show version")
        print()
        print("Description:")
        print("  Tests download speed from multiple servers")
        print("  and provides statistics.")


def main():
    cli = SpeedtestCLI()

    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ["--help", "-h"]:
            cli.show_help()
        elif arg in ["--version", "-v"]:
            cli.show_version()
        else:
            print(f"Unknown argument: {arg}")
            print("Use --help for usage information")
            sys.exit(1)
    else:
        cli.run_speedtest()


if __name__ == "__main__":
    main()
